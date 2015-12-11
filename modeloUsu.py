from google.appengine.ext import ndb
import hashlib


user_key = ndb.Key('User', 'default_user')

class User(ndb.Model):
    nombre = ndb.TextProperty(indexed=True)
    email = ndb.TextProperty(indexed=True)
    password = ndb.TextProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class UsuManager:
    def __init__(self):
        pass

    @staticmethod
    def create(nombre, password, email):
        user = User(parent=user_key)
        user.nombre = nombre
        user.password = hashlib.md5(password).hexdigest()
        user.email = email

        user.put()
        return True;

    @staticmethod
    def cogerUsus():
        users = ndb.gql(
                'SELECT * '
                'FROM User '
                'WHERE ANCESTOR IS :1 '
                'ORDER BY date DESC',
                user_key
        )

        return users

    @staticmethod
    def cogerPorNombre(nombre):
        user = ndb.gql(
                'SELECT * '
                'FROM User '
                'WHERE nombre = :1 '
                'ORDER BY date DESC',
                nombre
        )
        return user.get()

    @staticmethod
    def cogerPorMail(email):
        user = ndb.gql(
                'SELECT * '
                'FROM User '
                'WHERE email = :1 '
                'ORDER BY date DESC',
                 email
        )
        return user.get()