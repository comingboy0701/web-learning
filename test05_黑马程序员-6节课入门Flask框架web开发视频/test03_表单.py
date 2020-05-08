# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.secret_key = "coming"
'''
目的：实现一个简单的登录的逻辑处理
1.路由需要有get和post两种请求方式 -->> 判断请求方式
2.获取请求的参数
3.判断参数是否填写 & 密码是否相同
4.如果都没有问题，就返回一个success
'''

'''
给模板传递消息
flash --> 需要对内容进行加密，因此需要设置secret_key,做加密消息的混淆
模板中需要遍历消息
'''

'''
使用WTF实现表单类
自定义表单类
'''


class LoginForm(FlaskForm):
    username = StringField("用户名：", validators=[DataRequired()])
    password = PasswordField("密码：", validators=[DataRequired()])
    password2 = PasswordField("确认密码：", validators=[DataRequired(), EqualTo("password", "密码不一致")])
    submit = SubmitField("提交：")


@app.route('/form', methods=["post", "get"])
def login():
    login_form = LoginForm()
    # request: 请求对象  -->> 获取请求方式、数据
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        if login_form.validate_on_submit():
            print(username, password, password2)
            return "success"
        else:
            flash("参数有误")
    return render_template("test02_index.html", form=login_form)


@app.route('/', methods=["post", "get"])
def hello_world():
    # request: 请求对象  -->> 获取请求方式、数据
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        if not all([username, password, password2]):
            flash("参数不完整")
        elif password2 != password:
            flash("密码不一致")
        else:
            return "success"
    return render_template("test02_index.html")


if __name__ == '__main__':
    app.run(debug=True)
