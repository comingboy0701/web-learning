# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


# 1.如何返回一个模板
# 2.如何给模板填充数据
@app.route('/', methods=["get", "post"])
def index():
    url_str = "www.baidu.com"
    my_list = [1,2,3,4,5]
    my_dict = {"name":"coming",
               "year":"1994"}
    return render_template("test01_index.html",
                           url_str=url_str,
                           my_list =my_list,
                           my_dict = my_dict)


if __name__ == '__main__':
    app.run(debug=True)
