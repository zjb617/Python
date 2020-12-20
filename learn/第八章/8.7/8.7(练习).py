#练习1
test1 = 'This is a test of the emergency text system'
print(len(test1))
outfile = open('test.txt', 'wt')
outfile.write(test1)
outfile.close()
#或者使用with
with open('test.txt', 'wt') as outfile:
    outfile.write(test1)

print('------------------')

#练习2
with open('test.txt', 'rt') as infile:
    test2 = infile.read()

print(len(test2))
print(test1 == test2)

print('------------------')

#练习3
text = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, shoots & Leaves"
'''
with open('test.csv', 'wt') as outfile:
    outfile.write(text)

print('-------------------')

#练习4
import csv
with open('test.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        print(book)

print('--------------------')

#练习5
text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''
with open('books.csv', 'wt') as outfile:
    outfile.write(text)

print('-------------------------')

#练习6
import sqlite3
db = sqlite3.connect('books.db')
curs = db.cursor()
curs.execute('''create table book (title text, author text, year int)''')
db.commit()

print('------------------------')

#练习7
ins_str = 'insert into book values(?, ?, ?)'
with open('books.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], book['year']))

db.commit()



#练习8
#练习9
#练习10
#练习11
#练习12