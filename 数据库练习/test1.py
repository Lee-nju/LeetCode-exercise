import pandas as pd
from sqlalchemy import create_engine
import pymysql

# 初始化数据库连接
# 按实际情况依次填写MySQL的用户名、密码、IP地址、端口、数据库名
engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', '7948LG2234', 'localhost', '3306', 'testdb'))

# DataFrame写入MySQL
# 新建DataFrame
df_write = pd.DataFrame({'id': [10, 27, 34, 46], 'name': ['张三', '李四', '王五', '赵六'], 'score': [80, 75, 56, 99]})
# 将df储存为MySQL中的表，不储存index列
df_write.to_sql('testdf', engine, index=False)

# MySQL导入DataFrame
# 填写自己所需的SQL语句，可以是复杂的查询语句
sql_query = 'select * from product;'
# 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
df_read = pd.read_sql_query(sql_query, engine)
print(df_read)
