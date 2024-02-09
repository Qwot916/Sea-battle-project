from flask import Flask, request, render_template
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Boolean, select, String, update
engine = create_engine('sqlite:///myDatabase')
conn = engine.connect()
metadata = MetaData()
accounts = Table("accounts", metadata,
                 Column("account_id", Integer, primary_key=True),
                 Column("Login", String),
                 Column("Password", String))
metadata.create_all(engine)
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def tries():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        insertion_account = accounts.insert().values([
            {"Login": username, "Password": password}
        ])
        conn.execute(insertion_account)
        login_and_password_get = select(accounts)
        select_login_and_password = conn.execute(login_and_password_get)
        print(select_login_and_password.fetchall())
        final = select_login_and_password.fetchall()
        return render_template('admin.html')
    else:
        return render_template('login.html')
if __name__ == '__main__':
    app.run()
