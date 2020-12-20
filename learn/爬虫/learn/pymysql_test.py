import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306,#unix_socket='/temp/mysql.sock',
                       user='root', password='Taylover6', db='mysql')

'''定位到出错代码为：

unix_socket='/temp/mysql.sock'


查阅资料之后找到了原因，代码中的 unix_socket 是用于连接 socket 的，本示例代码中是使用 IP 连接的，即使用的是端口号（port）。因此，可将上诉代码改为：

port=3306

注意：这里的3306为MySQL的默认端口号。

修改方法：将出错代码换为port=3306'''

cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
