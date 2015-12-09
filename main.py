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

<<<<<<< HEAD

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
=======
html = """\
<html>
  <head>
  <style>
body {background-color:lightgrey}
h1   {color:blue}
</style>
</head>
  <body>
 
       <img src="http://weknowyourdreams.com/images/arbol/arbol-01.jpg"/>
	   <br></br><h1>Hello world!</h1>
    
  </body>
>>>>>>> dbd6c759a171e39e2c2ac3c142587987b5f37c4e
</html>
"""


<<<<<<< HEAD



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
		self.response.write(ESP_HTML)	

class validarEn(webapp2.RequestHandler):
	def post(self):
		self.response.write(ENG_HTML)	

class validarEus(webapp2.RequestHandler):
	def post(self):
		self.response.write(EUS_HTML)	

		
app = webapp2.WSGIApplication([
    ('/registro', MainHandler),
	('/Es', MainHandler),
	('/En', EnHandler),
	('/Eus', EusHandler),
	('/validarEs', validarEs),
	('/validarEn', validarEn),
	('/validarEus', validarEus)
=======
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html)
 

		

class HolaHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hola mundo!')		

 
 
		
class KaixoHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Kaixo mundua!')
		

	
		
app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/hola', HolaHandler),
	('/kaixo', KaixoHandler),
>>>>>>> dbd6c759a171e39e2c2ac3c142587987b5f37c4e

], debug=True)
