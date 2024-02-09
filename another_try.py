from flask import Flask, request, render_template
from models import books, conn, select_all_results
from sqlalchemy import select
another_try = Flask(__name__)
@another_try.route('/')
def DataBasing():
    getting_books = select(books)
    getting_books_call = conn.execute(getting_books)
    return render_template('prize.html')
if __name__ == '__main__':
    another_try.run()