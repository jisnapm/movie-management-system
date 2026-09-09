import mysql.connector

class MovieManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user= 'root',
            password= 'Jis12#na',
            database= 'movie_db'
        )
        print("Connected Successfully!")

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            q = 'insert into movies(title, genre, language, rating, release_year) values(%s, %s, %s, %s, %s)'
            values = [v for v in kwargs.values()]
            self.cursor.execute(q, values)
            self.connection.commit()
            print("Movie Added Successfully!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()
            q = 'select * from movies'
            self.cursor.execute(q)
            records = self.cursor.fetchall()
            print('- - - - MOVIE DETAILS - - - -')
            for data in records:
                print(data)
        except Exception as e:
            print(e)

    def get_object(self, id= None):
        try:
            self.c = self.connection.cursor()
            q = 'select * from movies where movie_id = %s'
            v = (id, )
            self.c.execute(q, v)
            record = self.c.fetchone()
            return record
        except Exception as e:
            print(e)

    def retrieve(self, id= None):
        try:
            record = self.get_object(id)
            if record != None:
                print("- - - DETAILS - - -")
                print(record)
            else:
                print("Movie Not Found")
        except Exception as e:
            print(e)

    def delete(self, id= None):
        try:
            record = self.get_object(id)
            if record != None:
                self.c = self.connection.cursor()
                q = 'delete from movies where movie_id = %s'
                v = (id, )
                self.c.execute(q, v)
                self.connection.commit()
                print("Movie Deleted!")
            else:
                print("Movie Not Found!")
        except Exception as e:
            print(e)

    def put(self, id= None, **kwargs):
        try:
            record = self.get_object(id)
            if record != None:
                self.c = self.connection.cursor()
                placeholder = ''
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")
                q = f"update movies set {placeholder} where movie_id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.c.execute(q, values)
                self.connection.commit()
                print("Movie Details Updated")
            else:
                print("Movie Not Found!")
        except Exception as e:
            print(e)



movie_instance = MovieManager()
# movie_instance.post(title= "Obsession", genre= "Horror", language= "English", rating= 4.1, release_year= 2026)
movie_instance.get()

# movie_instance.post(
#     title="Parasite",
#     genre="Thriller",
#     language="Korean",
#     rating=8.5,
#     release_year=2019
# )
#
# movie_instance.post(
#     title="3 Idiots",
#     genre="Comedy",
#     language="Hindi",
#     rating=8.4,
#     release_year=2009
# )
# print(movie_instance.get_object(1))
movie_instance.retrieve(1)
movie_instance.delete(2)
movie_instance.put(1, rating= 9.2)
movie_instance.get()