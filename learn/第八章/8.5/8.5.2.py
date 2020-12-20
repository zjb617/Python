import memcache
db = memcache.Client('127.0.0.1:11211')
db.set('marco', 'polo')
db.get('marco')
db.set('ducks', 0)
db.get('ducks')
db.incr('ducks', 2)
db.get('ducks')