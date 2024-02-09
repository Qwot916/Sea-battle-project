from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Boolean, select, String, update
engine = create_engine('sqlite:///myDatabase')
conn = engine.connect()
metadata = MetaData()
books = Table("books", metadata,
              Column("book_id", Integer, primary_key=True),
              Column("book_name", String),
              Column("book_author", String),
              Column("book_is_taken", Boolean, default=False))
metadata.create_all(engine)
insertion_query = books.insert().values([
    {"book_name": "rep", "book_author": "me"},
    {"book_name": "SOUP", "book_author": "vlad"},
    {"book_name": "rep", "book_author": "cooler me"},
    {"book_name": "pill", "book_author": "me"},
    {"book_name": "figure", "book_author": "not me"}
])
conn.execute(insertion_query)
select_all_query = select(books).where(books.columns.book_author == "me")
select_all_results = conn.execute(select_all_query)
print(select_all_results.fetchall())
update_query = update(books).where(books.columns.book_name == "SOUP").values(book_author="me")
conn.execute(update_query)
select_all_query = select(books).where(books.columns.book_author == "me")
select_all_results = conn.execute(select_all_query)
print(select_all_results.fetchall())
