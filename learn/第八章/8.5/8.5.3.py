#字符串
import redis
conn = redis.Redis()
conn.keys('*')
conn.set('secret', 'ni!')
conn.set('carats', 24)
conn.set('fever', '101.5')
conn.get('secret')
conn.get('carats')
conn.get('fever')
conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!')
conn.get('secret')
conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!')
conn.get('secret')
conn.getrange('secret', -6, -1)
conn.setrange('secret', 0, 'ICKY')
conn.get('secret')
conn.mset({'pie': 'cherry', 'corrdial': 'sherry'})
conn.mget(['fever', 'carats'])
conn.delete('fever')
conn.incr('carats')
conn.incr('carats', 10)
conn.decr('carats')
conn.decr('carats', 15)
conn.set('fever', '101.5')
conn.incrbyfloat('fever')
conn.incrbyfloat('fever', 0.5)


conn.incrbyfloat('fever', -2.0)

#列表
conn.lpush('zoo', 'bear')
conn.lpush('zoo', 'alligator', 'duck')
conn.linsert('zoo', 'before','bear','beaver')
conn.linsert('zoo', 'after','bear','cassowary')
conn.lset('zoo', 2, 'marmoset')
conn.rpush('zoo', 'yak')
conn.lindex('zoo',3)
conn.lrange('zoo', 0, 2)
conn.ltrim('zoo', 1, 4)
conn.lrange('zoo', 0, -1)

# 哈希表
# 集合
# 有序集合
# 位图
