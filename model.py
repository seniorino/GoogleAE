from google.appengine.ext import ndb
import hashlib


idenUsu = ndb.Key('User', 'default_user')


class User(ndb.Model):
	nombre = ndb.TextProperty(indexed=True)
	email = ndb.TextProperty(indexed=True)
	password = ndb.TextProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)
	photo = ndb.BlobProperty()


	
def create(username, password, email, photo):

		
		user.name = username
		user.password = hashlib.md5(password).hexdigest()
		user.email = email
		user.photo = photo
		#Necesario para cada usuario tenga su identificador
		user = User(parent=idenUsu)
		
		user.put()
		return True;

		
 def cogerUsus():
		users = ndb.gql(
			'SELECT * '
			'FROM User '
			'WHERE ANCESTOR IS :1 '
			'ORDER BY date DESC',
			idenUsu
			)

		return users
		
