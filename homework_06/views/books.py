from flask import Blueprint, render_template, request, url_for, redirect, flash


from models import db, Book
from .forms.book import CreateBookForm

books_app = Blueprint("books_app", __name__)


@books_app.route("/", endpoint="list")
def get_books():
    books = Book.query.order_by(Book.id).all()
    return render_template("books/list.html", books=books)


@books_app.route(
    "/<int:book_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm-delete",
)
@books_app.route(
    "/<int:book_id>/",
    methods=["GET", "DELETE"],
    endpoint="details",
)
def get_book_by_id(book_id: int):
    # product = db.session.get(Product, product_id)
    # if product is None:
    #     raise NotFound(f"Product #{product_id} not found!")
    book: Book = Book.query.get_or_404(
        book_id,
        f"Product #{book_id} not found!",
    )

    confirm_delete = request.endpoint == "books_app.confirm-delete"
    if request.method == "GET":
        return render_template(
            "books/confirm-delete.html" if confirm_delete else "books/details.html",
            book=book,
        )


    db.session.delete(book)
    db.session.commit()

    flash(f"Deleted books {book.name}!", "warning")
    url = url_for("books_app.list")
    if confirm_delete:
        return redirect(url)

    return {"ok": True, "url": url}


@books_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_book():
    form = CreateBookForm()

    if request.method == "GET":
        return render_template("books/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("books/add.html", form=form), 400

    book_name = form.name.data
    is_new = form.is_new.data

    book = Book(name=book_name, is_new=is_new)
    db.session.add(book)
    db.session.commit()

    flash(f"Successfully added product {book.name}!")
    url = url_for("books_app.details", book_id=book.id)
    return redirect(url)
