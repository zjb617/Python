#SQLAlchemy
#引擎层
import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
conn.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
    count INT,
    damages FLOAT)''')

ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)

rows = conn.execute('SELECT * FROM zoo')
print(rows)
for row in rows:
    print(row)

#SQL表达式语言
meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
    sa.Column('critter', sa.String, primary_key=True),
    sa.Column('count', sa.Integer),
    sa.Column('damages', sa.Float)
    )
meta.create_all(conn)

conn.execute(zoo.insert(('bear', 2, 1000.0)))

result = conn.execute(zoo.select())
rows = result.fetchall()
print(rows)

#对象关系映射
