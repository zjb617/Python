import dbm
db = dbm.open('definitions', 'c')
db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'
print(len(db))
print(db['pesto'])
db.close()
db = dbm.open('definitions', 'r')
print(db['mustard'])