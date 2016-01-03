from google.appengine.ext import ndb
import hashlib
import time
import string
import random


user_key = ndb.Key('User', 'default_user')

class User(ndb.Model):
    nombre = ndb.TextProperty(indexed=True)
    email = ndb.TextProperty(indexed=True)
    password = ndb.TextProperty(indexed=True)
    telefono = ndb.TextProperty(indexed=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
    bloqueada = ndb.BooleanProperty()
    Confirmation = ndb.TextProperty(indexed=True)
    ConfirmationTime = ndb.IntegerProperty(indexed=True)
    OptionalPassword = ndb.TextProperty(indexed=True)


class Image(ndb.Model):
    user = ndb.StringProperty()
    public = ndb.BooleanProperty()
    blobkey = ndb.BlobKeyProperty()










def getpublicImg(image):
    return image.public

def getUserImg(image):
    return image.user



class ImageManager:
    def __init__(self):
        pass

    @staticmethod
    def cogerImagen(blobkey):
        img = ndb.gql(
                'SELECT * '
                'FROM Image '
                'WHERE blobkey = :1 ',
                 blobkey
        )
        return img.get()






class UsuManager:
    def __init__(self):
        pass

    @staticmethod
    def create(nombre, password, email, telefono):
        user = User(parent=user_key)
        user.nombre = nombre
        user.password = hashlib.md5(password).hexdigest()
        user.email = email
        user.telefono = telefono
        user.bloqueada = False
        user.Confirmation = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(15))
        user.ConfirmationTime = 1
        user.OptionalPassword = 'None'


        user.put()
        return True;

    @staticmethod
    def getBloqueo(user):
        return user.bloqueada

    @staticmethod
    def guardarCodigo(user,codigo):
        user.Confirmation = codigo
        user.put()
        return True;

    @staticmethod
    def guardarTimeCodigo(user):
        user.ConfirmationTime = int(time.time())
        user.put()
        return True;


    @staticmethod
    def guardarOpcionalPass(user,Opass):
        user.OptionalPassword = Opass
        user.put()
        return True;



    @staticmethod
    def cambiarPass(user,passw):
        user.password = passw
        user.put()
        return True;


    @staticmethod
    def getOptionalPassword (user):
        return user.OptionalPassword


    @staticmethod
    def getPassword (user):
        return user.password

    @staticmethod
    def getNombre (user):
        return user.nombre

    @staticmethod
    def bloquearCuenta(user):
        user.bloqueada = True
        user.put()
        return True;


    @staticmethod
    def getConfirmationTime (user):
        return user.ConfirmationTime

    @staticmethod
    def getConfirmation (user):
        return user.Confirmation


    @staticmethod
    def getUserConfirmation(Confirmation):
        user = ndb.gql(
                'SELECT * '
                'FROM User '
                'WHERE Confirmation = :1 '
                'ORDER BY date DESC',
                 Confirmation
        )
        return user.get()




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

    @staticmethod
    def cogerPorPassYUser(nombre, password):
         user = ndb.gql(
                'SELECT * '
                'FROM User '
                'WHERE nombre = :1 AND password = :2',
                 nombre,password
         )

         return user.get()


