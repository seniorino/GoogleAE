#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re 

ESP_HTML = """\
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/mainCss.css">
<script src="scripts/validacion.js"></script>

</head>

<body>
<h1>Registro de usuarios</h1>
 <FORM  action="/validarEs" method="post" onSubmit="return verificarCampos()&& verificarMail() && verificarContras() && verificarTelefono()">
    <P>
	<input type="hidden" name="Language" value="Castellano">
    <LABEL for="nombre">Nombre(*): </LABEL>
              <INPUT type="text" id="nombre" name="nombre"><BR>
    <LABEL for="contra1">Contrase&ntilde;a(*): </LABEL>
              <INPUT type="password" id="contra1" name="contra1"><BR>
	<LABEL for="contra2">Repetir contrase&ntilde;a(*): </LABEL>
              <INPUT type="password" id="contra2" name="contra2"><BR>
    <LABEL for="email">email(*): </LABEL>
              <INPUT type="text" id="email" name="email"><BR>
    <LABEL for="telefono">Numero de telefono: </LABEL>
              <INPUT type="text" id="telefono" name="telefono"><BR>
     Su foto:<INPUT type="file" name="foto"><BR>
    <INPUT type="submit" value="Enviar"  > <INPUT type="reset">
    </P>
 </FORM>
 <br></br>

<div class="button-container">
<form method="get" action="/En">
    <input type="submit" name="English" value="English">
</form>
<form method="get" action="/Eus">
    <input type="submit" name="Euskera" value="Euskera">
</form>
</div>
</body>
</html>
"""

EUS_HTML = """\
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/mainCss.css">
<script src="scripts/validacion.js"></script>
	
</head>
<body>
<h1>Erabiltzaileen erregistroa</h1>
 <FORM  action="/validarEus" method="post" onSubmit="return verificarCampos()&& verificarMail() && verificarContras() && verificarTelefono()">
 <input type="hidden" name="Language" value="Euskera">
    <P>
    <LABEL for="nombre">Izena(*): </LABEL>
              <INPUT type="text" id="nombre" name="nombre"><BR>
    <LABEL for="contrasema">Pasahitza(*): </LABEL>
              <INPUT type="password" id="contra1" name="contra1"><BR>
	<LABEL for="contrasenia2">Pasahitza berriro(*): </LABEL>
              <INPUT type="password" id="contra2" name="contra2"><BR>
    <LABEL for="email">email(*): </LABEL>
              <INPUT type="text" id="email" name="email"><BR>
    <LABEL for="telefono">Telefono zenbakia: </LABEL>
              <INPUT type="text" id="telefono" name="telefono"><BR>
     Zure argazkia:<INPUT type="file" name="foto"><BR>
    <INPUT type="submit" value="Enviar"  > <INPUT type="reset">
    </P>
 </FORM>
 <br></br>

<div class="button-container">
<form method="get" action="/En">
    <input type="submit" name="English" value="English">
</form>
<form method="get" action="/Es">
    <input type="submit" name="Castellano" value="Castellano"">
</form>
</div>
</body>
</html>
"""


ENG_HTML = """\
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/mainCss.css">
<script src="scripts/validacion.js"></script>
	
</head>
<body>
<h1>User registry</h1>
 <FORM  action="/validarEn" method="post" onSubmit="return verificarCampos()&& verificarMail() && verificarContras() && verificarTelefono()">
    <P>
	<input type="hidden" name="Language" value="English">
    <LABEL for="nombre">Name(*): </LABEL>
              <INPUT type="text" id="nombre" name="nombre"><BR>
    <LABEL for="contrasema">Password(*): </LABEL>
              <INPUT type="password" id="contra1" name="contra1"><BR>
	<LABEL for="contrasenia2">Repit password(*): </LABEL>
              <INPUT type="password" id="contra2" name="contra2"><BR>
    <LABEL for="email">email(*): </LABEL>
              <INPUT type="text" id="email" name="email"><BR>
    <LABEL for="telefono">Phone number: </LABEL>
              <INPUT type="text" id="telefono" name="telefono"><BR>
     Photo:<INPUT type="file" name="foto"><BR>
    <INPUT type="submit" value="Enviar"  > <INPUT type="reset">
    </P>
 </FORM>
 <br></br>

<div class="button-container">
<form method="get" action="/Eus">
    <input type="submit" name="Euskera" value="Euskera">
</form>
<form method="get" action="/Es">
    <input type="submit" name="Castellano"" value="Castellano"">
</form>
</div>
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(ESP_HTML)

class EnHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(ENG_HTML)
		
class EusHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(EUS_HTML)
			
		
class validarEs(webapp2.RequestHandler):
	def post(self):
		
		nombre=self.request.get('nombre')
		contra1=self.request.get('contra1')
		contra2=self.request.get('contra2')
		email=self.request.get('email')
		telefono=self.request.get('telefono')


		if len(nombre) < 1:
			self.response.out.write("Nombre de usuario vacio.")
			self.response.out.write(ESP_HTML)
			return None
		
		if len(contra1) < 6:
			self.response.out.write("Minimo numero de caracteres necesarios para la password es 6.")
			self.response.out.write(ESP_HTML)
			return None
		
		if contra1 != contra2:
			self.response.out.write("Las password no coinciden.")
			self.response.out.write(ESP_HTML)
			return None
			
		if len(telefono) > 1:
			if not re.match(r"\D(\d{9})\D", telefono):
				self.response.out.write("Se requiere un numero de telefono de 9 digitos.")
				return None
			self.response.out.write(ESP_HTML)
			return None
			
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			self.response.out.write("El formato del email no es correcto")
			self.response.out.write(ESP_HTML)
			return None

		
		self.response.out.write("<h1>Bienvenido "+nombre+"</h1>")
		self.response.out.write(ESP_HTML)
		
		
class validarEn(webapp2.RequestHandler):
	def post(self):
	
		nombre=self.request.get('nombre')
		contra1=self.request.get('contra1')
		contra2=self.request.get('contra2')
		email=self.request.get('email')
		telefono=self.request.get('telefono')


		if len(nombre) < 1:
			self.response.out.write("Username empty.")
			self.response.out.write(ENG_HTML)
			return None
		
		if len(contra1) < 6:
			self.response.out.write("The minimum ammount of characters needed for the password are 6.")
			self.response.out.write(ENG_HTML)
			return None
		
		if contra1 != contra2:
			self.response.out.write("Password do not match.")
			self.response.out.write(ENG_HTML)
			return None
			
		if len(telefono) > 1:
			if not re.match(r"\D(\d{9})\D", telefono):
				self.response.out.write("A 9 digit number is needed.")
				return None
			self.response.out.write(ENG_HTML)
			return None
			
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			self.response.out.write("Email format is not correct")
			self.response.out.write(ENG_HTML)
			return None

		self.response.out.write("<h1>Hello "+nombre+"</h1>")
		self.response.out.write(ENG_HTML)
		
class validarEus(webapp2.RequestHandler):
	def post(self):
		
		nombre=self.request.get('nombre')
		contra1=self.request.get('contra1')
		contra2=self.request.get('contra2')
		email=self.request.get('email')
		telefono=self.request.get('telefono')


		if len(nombre) < 1:
			self.response.out.write("Erabiltzailearen izena huts.")
			self.response.out.write(EUS_HTML)
			return None
		
		if len(contra1) < 6:
			self.response.out.write("Pasahitza gutxienez 6 digito behar ditu.")
			self.response.out.write(EUS_HTML)
			return None
		
		if contra1 != contra2:
			self.response.out.write("Pasahitzak ez dira berdinak.")
			self.response.out.write(EUS_HTML)
			return None
			
		if len(telefono) > 1:
			if not re.match(r"\D(\d{9})\D", telefono):
				self.response.out.write("9 zenbakiko telefonoa behar da")
				return None
			self.response.out.write(EUS_HTML)
			return None
			
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			self.response.out.write("Email-a ez da ona")
			self.response.out.write(EUS_HTML)
			return None
	
		self.response.out.write("<h1>Kaixo"+nombre+"</h1>")
		self.response.out.write(EUS_HTML)

		
app = webapp2.WSGIApplication([
    ('/registro', MainHandler),
	('/Es', MainHandler),
	('/En', EnHandler),
	('/Eus', EusHandler),
	('/validarEs', validarEs),
	('/validarEn', validarEn),
	('/validarEus', validarEus),

], debug=True)
