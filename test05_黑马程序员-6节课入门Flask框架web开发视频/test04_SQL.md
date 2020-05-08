## 数据库的使用

1. 创建表
db.create_all()

2. 删除表
db.drop_all()

3. 添加数据
role = Role(name="admin")
db.session.add(role)
db.session.commit()

4. 修改数据
user.name = "chengxuyuan"
db.session.commit()

5. 删除数据
db.session.delete(user)
db.session.commit()

