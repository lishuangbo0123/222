# 李双博
# 学习python
# 开发时间 2021/12/26  21:27
import pymysql


#数据库连接   5要素
db = pymysql.connect(user='root',password="Niyingle@54321",host='36.133.5.196',database='pachong_data',port=3306,charset='utf8mb4')
# 创建游标
cursor = db.cursor()
# 执行sql语句   返回受影响行数
cursor.execute()
# 获取全部数据
cursor.fetchall()
#关闭游标
cursor.close()
#关闭数据库
db.close()
#数据库数据增删改时必须提交数据
db.commit()
#当增删改多条数据时
cursor.executemany()
#当表中有自增的主键时，可以使用什么来获取最新的主键id
cursor.lastrowid()
#查询数据库所有数据、一行数据、多行数据，每次获取数据后游标的位置就变了
cursor.fetchone()
cursor.fetchmany()
cursor.fetchall()
#想让查询结果变成字典（每一行都是字典，所有行是列表），默认是元组（每一行是一个小元组，所有行是一个大元组）
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
#相对移动查询的指针
cursor.scroll(1,mode='relative')
#绝对移动查询的指针位置
cursor.scroll(0,mode='absolute')
#上下文管理器
with db.cursor(cursor = pymysql.cursors.DictCursor) as cursor:
    cursor.execute()
    cursor.close()
db.close()




