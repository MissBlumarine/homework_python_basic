from flask import Blueprint, render_template, request, url_for, redirect, flash


from models import db, Book
from .forms.book import CreateBookForm

books_app = Blueprint("books_app", __name__)


@books_app.route("/", endpoint="list")
def get_books():
    books = Book.query.order_by(Book.id).all()
    return render_template("book/list.html", products=books)


@books_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_book():
    form = CreateBookForm()

    if request.method == "GET":
        return render_template("book/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("book/add.html", form=form), 400

    book_name = form.name.data
    is_new = form.is_new.data

    book = Book(name=book_name, is_new=is_new)
    db.session.add(book)
    db.session.commit()

    flash(f"Successfully added product {book.name}!")
    url = url_for("books_app.list", book_id=book.id)
    return redirect(url)
