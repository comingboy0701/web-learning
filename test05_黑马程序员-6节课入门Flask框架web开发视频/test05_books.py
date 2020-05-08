# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.secret_key = "coming"

# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1118@localhost/books"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库的操作对象
db = SQLAlchemy(app)
'''
1. 配置数据库
    a. 导入SQLAlchemy
    b. 创建db对象，并配置参数
    c. 终端创建数据库
    
2. 添加书和作者模型
    a. 模型继承db.Model
    b. __tablename__:表名
    c. db.relationship:关系引用
3. 添加数据

4. 使用模板显示数据库查询的数据
    a. 查询所有的作者信息，让信息传递给模板
    b. 模板中按照格式，依次for循环作者和书籍即可（作者获取书籍，用的是关系引用）
5. 使用WTF显示表单
    a. 自定义表单类
    b. 模板中显示
    c. serect_key /编码 / csrf_token
6. 实现相关的增删改逻辑
    a. 增加数据
    b. 删除数据 --> 网页删除 --> 点击需要发送书籍的ID给删除书籍的路由 --> 路由需要接受参数
    c. for else 的使用
'''


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    books = db.relationship('Book', backref="author")

    # 相当于__str__方法。
    def __repr__(self):
        return "Author: %s %s" % (self.id, self.name)


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 创建一个外键，和django不一样。flask需要指定具体的字段创建外键，不能根据类名创建外键
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))

    def __repr__(self):
        return "Book: %s %s" % (self.id, self.name)


class AuthorForm(FlaskForm):
    author = StringField("作者", validators=[DataRequired()])
    book = StringField("书籍", validators=[DataRequired()])
    submit = SubmitField("提交：")


@app.route("/delete_author/<author_id>", methods=["get", "post"])
def delete_author(author_id):
    author = Author.query.get(author_id)
    if author:
        try:
            Book.query.filter_by(author_id=author.id).delete()
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            flash("删除作者出错")
            db.session.rollback
    else:
        flash("作者找不到")
    return redirect(url_for("index"))


@app.route("/delete_book/<book_id>", methods=["get", "post"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            flash("删除书籍出错")
            db.session.rollback
    else:
        flash("书籍找不到")
    return redirect(url_for("index"))


@app.route("/", methods=["get", "post"])
def index():
    # 查询所有的用户
    author_form = AuthorForm()

    '''
    1. 调用WTF的函数实现验证
    2. 验证通过获取数据
    3. 判断作者是否存在
    4. 如果作者存在，判断书籍是否存在，没有重复的书籍添加数据，如果重复就报错
    5. 如果作者不存在，添加作者和书籍
    6. 验证不通过就提示错误
    '''
    print(author_form.validate_on_submit())
    if author_form.validate_on_submit():
        author_name = author_form.author.data
        book_name = author_form.book.data

        author = Author.query.filter_by(name=author_name).first()
        if author:
            book = Book.query.filter_by(name=book_name).first()
            if book:
                flash("已存在同名书籍")
            else:
                try:
                    new_book = Book(name=book_name, author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash("添加书籍失败")
                    db.session.rollback()

        else:
            try:
                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()

                new_book = Book(name=book_name, author_name=new_author.id)
                db.session.add(new_book)
                db.session.commit()

            except Exception as e:
                print(e)
                flash("添加书籍失败")
                db.session.rollback()

    else:
        if request.method == "POST":
            flash("参数不全呀")
    authors = Author.query.all()
    return render_template("test05_books.html", authors=authors, form=author_form)


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # au1 = Author(name="老王")
    # au2 = Author(name="老惠")
    # au3 = Author(name="老刘")
    # db.session.add_all([au1, au2, au3])
    # db.session.commit()
    #
    # bk1 = Book(name="老王回忆录", author_id=au1.id)
    # bk2 = Book(name="我读书少，你别骗我", author_id=au1.id)
    # bk3 = Book(name="如何让自己更帅", author_id=au2.id)
    # bk4 = Book(name="怎么样哄媳妇", author_id=au3.id)
    # bk5 = Book(name="如何学习python", author_id=au3.id)
    #
    # db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # db.session.commit()

    app.run(debug=True)
