"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask, request, render_template

app = Flask(__name__)

app.config.update(
    ENV="development",
    SECRET_KEY="sdkjnslkdfgnajrsgoiqejrogj3qo4itgj",
)


@app.route("/", endpoint="index_page")
def hello_world():
    print_request()
    return render_template("index.html")


@app.route("/about/", endpoint="about_book")
def hello_world():
    print_request()
    return render_template("books.html")


def print_request():
    print("request:", request)
    print("request.method", request.method)
    print("request.path", request.path)


if __name__ == "__main__":
    app.run(debug=True)
