
"""
Conftest
"""
from _pytest.fixtures import fixture
from flask.testing import FlaskClient
from main import app
from utils import add_homework_path


add_homework_path(__file__)

@fixture
def client() -> FlaskClient:
    """
    client
    :return:
    """
    app.config.update(SERVER_NAME='myserver.org')
    app.config.update(WTF_CSRF_ENABLED=False)
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client