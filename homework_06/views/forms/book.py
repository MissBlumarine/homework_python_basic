from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class CreateBookForm(FlaskForm):
    name = StringField(
        label="Book name",
        name="book-name",
        validators=[
            DataRequired(),
            Length(min=3, max=100),
        ],
    )
    is_new = BooleanField(
        label="Is new book?",
        default=False,
    )
