import pymysql

#  Connect to a database
db_connection = pymysql.connect(
host = "localhost",
port = 3306,
user = "root",
password = "Mypassword12345",
db = "music_streaming_services"
)


#  Create a cursor to implement SQL queries
my_cursor = db_connection.cursor()

#  Create a table
my_cursor.execute ('create table s (id int not null auto_increment,service varchar (30) not null,'
                   'price int not null,primary key (id));')

#  Fill in the table
sqlQuery = 'insert into s (service,price) values (%s,%s)'
services = [('Spotify',5),
            ('Apple Music',4),
            ('Youtube Music',3)]
my_cursor.executemany(sqlQuery,services)
db_connection.commit()

#  View the table
my_cursor = db_connection.cursor()
my_cursor.execute('select * from s ')
result = my_cursor.fetchall()
for x in result:
    print(x)


