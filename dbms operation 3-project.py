import sqlite3

db= sqlite3.connect('school.db')

db.execute('drop table if exists school')

db.execute('create table school(i int, j name, k int)')

db.execute('insert into school(i,j,k) values(?,?,?)',('roll', 'name', 'class'))
db.execute('insert into school(i,j,k) values(?,?,?)',('1', 'sajid',  '10'))
db.execute('insert into school(i,j,k) values(?,?,?)',('2', 'naima',  '5'))
db.execute('insert into school(i,j,k) values(?,?,?)',('3', 'waqar',  '8'))
db.execute('insert into school(i,j,k) values(?,?,?)',('4', 'Preety', '9'))
db.execute('insert into school(i,j,k) values(?,?,?)',('5', 'Rehana', '8'))

result= db.execute('select * from school')
for i in result:
           print(i)
           
db.execute('update school set j=? ,k=? where i=?',('Sanjida',6,2))
db.commit()

print("\nafter update:")
result= db.execute('select * from school')
for i in result:
           print(i)

db.execute('delete from school where i=2')
db.commit()

print("\nafter delete:")
result= db.execute('select * from school')
for i in result:
           print(i)           
