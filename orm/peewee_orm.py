from peewee import *

# pip install pymysql


if __name__ == "__main__":
    mysql_db = MySQLDatabase("game", user="root", passwd="admin123", charset="utf8")
    # 连接数据库
    mysql_db.connect()


    class MySQLModel(Model):
        class Meta:
            database = mysql_db


    class User(MySQLModel):  # 类的小写即表名
        username = CharField()  # 字段声明
        email = CharField()


    # User.create_table()
    user = User()
    user.username = "小红"
    user.email = "someuser@github.com"
    user.save()
