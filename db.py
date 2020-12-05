import sqlite3
conn = sqlite3.connect('contentmodal.db')


cur = conn.cursor()


cur.execute('PRAGMA foreign_keys=on;') ## Enables the foreign key support in Sqlite


## Create  Author table --



sql_query = '''CREATE TABLE modal (
    id_dia INTEGER PRIMARY KEY,
    fecha TEXT(999),
    pregunta TEXT(999),
    respuesta TEXT(999),
    frase TEXT(999),
    link TEXT(999),
    video TEXT(999),
    foto TEXT(999))
    ;'''
 

cur.execute(sql_query)

 

    


##Insert data into Author table
modal_list = [(1, "December 1st 2020", "Which taste better, Oreo or Chocolate Chip Cookies?", "Chocolate Chip Cookies", "frase", " ", " ", " "),
               (2, "December 2nd 2020", "Were Ross and Rachel on a break?", "yes", "frase", " ", " ", " "),
               (3, "December 3rd 2020", "Samantha, Carrie, Miranda or Charlotte?", "Miranda", "frase", " ", " ", " "),
               (4, "December 4th 2020", "French fries better with ketchup or with mayo?", "ketchup", "frase", " ", " ", " "),
               (5, "December 5th 2020", "Is pizza hawai acceptable?", "no", "frase", " ", " ", " "),
               (6, "December 6th 2020", "Who was less of a bitch, Blair or Serena?", "blair", "frase", " ", " ", " "),
               (7, "December 7th 2020", "Cats or Dogs?", "cats", "frase", " ", " ", " "),
               (8, "December 8th 2020", "Brownie or Carrot Cake?", "brownie", "frase", " ", " ", " "),
               (9, "December 9th 2020", "Coca Cola or Pepsi?", "coca cola", "frase", " ", " ", " "),
               (10, "December 10th 2020", "Who makes a better 007, Pierce Brosnan and Daniel Craig", "pierce brosnan", "frase", " ", " ", " "),
               (11, "December 11th 2020", "Team Aniston or Team Jolie?", "aniston", "frase", "aniston", " ", " "),
               (12, "December 12th 2020", "Dark chocolate or white chocolate?", "dark", "frase", " ", " ", " "),
               (13, "December 13th 2020", "Summer or winter?", "summer", "frase", " ", " ", " "),
               (14, "December 14th 2020", "Pokemon or Digimon?", "pokemon", "frase", " ", " ", " "),
               (15, "December 15th 2020", "Madrid or Barcelona?", "madrid", "frase", " ", " ", " "),
               (16, "December 16th 2020", "Who deserved to win, coyote or roadrunner?", "coyote", "frase", " ", " ", " "),
               (17, "December 17th 2020", "Hot chocolate better with whipped cream or with marshmallows?", "marshmallows", "frase", " ", " ", " "),
               (18, "December 18th 2020", "Which animal did McGonagall turn into?", "cat", "frase", " ", " ", " "),
               (19, "December 19th 2020", "Ferrero Rocher and Mon Cheri?", "ferrero rocher", "frase", " ", " ", " "),
               (20, "December 20th 2020", "We'll always have...", "paris", "frase", " ", " ", " "),
               (21, "December 21st 2020", "Which books are more fun: Harry Potter or Lord of the Rings?", "harry potter", "frase", " ", " ", " "),
               (22, "December 22nd 2020", "Name of the cat in Breakfast at Tiffanys?", "cat", "frase", " ", " ", " "),
               (23, "December 23rd 2020", "Gin tonic better with lemon or with cucumber?", "cucumber", "frase", " ", " ", " "),
               (24, "December 24th 2020", "For Christmas: Kevin Home Alone or Love Actually?", "love actually", "frase", " ", " ", " ")
               ]


try:
    sql_query = '''INSERT INTO modal values(:id_dia, :fecha, :pregunta, :respuesta, :frase, :link, :video, :foto );'''
    cur.executemany(sql_query, modal_list)
    conn.commit()
    print ('los valores se han insertado en la tabla')
except:
    print ('no se han podido insertar los valores en la tabla')
    conn.rollback()



'''

## insert data into book table

try:
    sql_query = INSERT INTO book values(?,?,?,?,?);
    cur.executemany(sql_query, book_list)
    conn.commit()
    print ('values inserted successfully')
except:
    print ('insertion operation failed')
    conn.rollback()


## Retrieving data
query_condition = ('USA', )
cur.execute("select * from author where country = ?; ", query_condition)

authors = cur.fetchall()
for author in authors:
    print (author)

cur.execute("select * from book; ")

books = cur.fetchall()
for book in books:
    print (book)


## Update a record
try:
    sql_query = "update book set title=? where title=?;"
    cur.execute(sql_query, ('It rains', 'It'))
    conn.commit()
    print ('value updated successfully')
except:
    print ('updation operation failed')
    conn.rollback()


## Delete a record

try:
    sql_query = "delete from author where name=?;"
    cur.execute(sql_query, ('Stephen King', ))
    conn.commit()
    print ('value deleted successfully')
except:
    print ('deletion operation failed')
    conn.rollback()

cur.close()
conn.close()

'''

