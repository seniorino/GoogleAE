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
import time
import webapp2
import re
import modeloUsu

ESP_HTML = """\
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/mainCss.css">
<script src="scripts/validacion.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<script src="scripts/otros.js"></script>

</head>

<body>
<br></br>
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
              <INPUT type="text" id="email" name="email" onblur="validarMail()"> <div id="divMail"></div><BR>
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
 <BR>
<h1><div id="div1"></div></h1>

<script>
	var v=setInterval(function(){pedirhora()},1000);
</script>
</body>
</html>
"""

EUS_HTML = """\
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/mainCss.css">
<script src="scripts/validacion.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<script src="scripts/otros.js"></script>
	
</head>
<body>
<br></br>
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
              <INPUT type="text" id="email" name="email" onblur="validarMail()"> <div id="divMail"></div><BR>
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
 <br></br>
<h1><div name =diva id="div1"></div></h1>

<script>
	var v=setInterval(function(){pedirhora()},1000);
</script>
</body>
</html>
"""

ENG_HTML = """\
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/mainCss.css">
<script src="scripts/validacion.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<script src="scripts/otros.js"></script>
	
</head>
<body>
<br></br>
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
              <INPUT type="text" id="email" name="email" onblur="validarMail()"> <div id="divMail"></div><BR>
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
 <br></br>
<h1><div id="div1" ></div></h1>

<script>
	var v=setInterval(function(){pedirhora()},1000);
</script>
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(ESP_HTML)


class HoraHandler(webapp2.RequestHandler):
    def get(self):
        t =time.localtime()
        self.response.out.write("%s : %s : %s"
                        %((t.tm_hour+1),t.tm_min,t.tm_sec))


class EmailHandler(webapp2.RequestHandler):
    def get(self):
        email = self.request.get('email')


        if len(email)> 1:
            mail = modeloUsu.UsuManager.cogerPorMail(email)
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                self.response.out.write("<h2><font color='red'>El formato del email no es correcto</font></h2>")
                return None
            if mail is not None:
                self.response.out.write(
                    "<h2><font color='red'>El email introducido ya ha sido registrado</font></h2>")
                return None
            else:
                self.response.out.write(
                    "<h2><font color='green'>Email correcto</font></h2>")
                return None



class EnHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(ENG_HTML)


class EusHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(EUS_HTML)


class validarEs(webapp2.RequestHandler):
    def post(self):

        nombre = self.request.get('nombre')
        contra1 = self.request.get('contra1')
        contra2 = self.request.get('contra2')
        email = self.request.get('email')
        telefono = self.request.get('telefono')

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
            if not re.match(r"(?<!\d)\d{9}(?!\d)", telefono):
                self.response.out.write("Se requiere un numero de telefono de 9 digitos.")
                self.response.out.write(ESP_HTML)
                return None

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.response.out.write("El formato del email no es correcto")
            self.response.out.write(ESP_HTML)
            return None

                # Todo ha ido ido bien, comprobar si el usuario existe
        user = modeloUsu.UsuManager.cogerPorNombre(nombre)
        if user is not None:
            self.response.out.write(ESP_HTML)
            self.response.out.write("<br></br><h1><font color='red'>Ya existe un usuario con ese nombre</font></h1>")
            return None

        mail = modeloUsu.UsuManager.cogerPorMail(email)
        if mail is not None:
            self.response.out.write(ESP_HTML)
            self.response.out.write(
                    "<br></br><h1><font color='red'>El email introducido ya ha sido registrado</font></h1>")
            return None

        if modeloUsu.UsuManager.create(nombre, contra1, email):
            self.response.out.write("<h1>Hola " + nombre + "</h1>")
            self.response.out.write("<img src='images/homer-hola.gif'>")
            return None

        self.response.out.write(ESP_HTML)


class validarEn(webapp2.RequestHandler):
    def post(self):

        nombre = self.request.get('nombre')
        contra1 = self.request.get('contra1')
        contra2 = self.request.get('contra2')
        email = self.request.get('email')
        telefono = self.request.get('telefono')

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
            if not re.match(r"(?<!\d)\d{9}(?!\d)", telefono):
                self.response.out.write("A 9 digit number is needed.")
                return None

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.response.out.write("The email format is not correct")
            self.response.out.write(ESP_HTML)
            return None

        # Todo ha ido ido bien, comprobar si el usuario existe
        user = modeloUsu.UsuManager.cogerPorNombre(nombre)
        if user is not None:
            self.response.out.write(ENG_HTML)
            self.response.out.write(
                "<br></br><h1><font color='red'>A username with that name already exists</font></h1>")
            return None

        mail = modeloUsu.UsuManager.cogerPorMail(email)
        if mail is not None:
            self.response.out.write(ENG_HTML)
            self.response.out.write(
                    "<br></br><h1><font color='red'>The introduced mail is already registered</font></h1>")
            return None

        if modeloUsu.UsuManager.create(nombre, contra1, email):
            self.response.out.write("<h1>Hello " + nombre + "</h1>")
            self.response.out.write("<img src='images/hello.jpg'>")
            return None

        self.response.out.write(ENG_HTML)


class validarEus(webapp2.RequestHandler):
    def post(self):

        nombre = self.request.get('nombre')
        contra1 = self.request.get('contra1')
        contra2 = self.request.get('contra2')
        email = self.request.get('email')
        telefono = self.request.get('telefono')

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
            if not re.match(r"(?<!\d)\d{9}(?!\d)", telefono):
                self.response.out.write("9 zenbakiko telefonoa behar da")
                return None

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.response.out.write("Emailaren formatua ez da ona")
            self.response.out.write(ESP_HTML)
            return None


                # Todo ha ido ido bien, comprobar si el usuario existe
        user = modeloUsu.UsuManager.cogerPorNombre(nombre)
        if user is not None:
            self.response.out.write(EUS_HTML)
            self.response.out.write(
                "<br></br><h1><font color='red'>Sartutako erabiltzaile izena hartuta dago</font></h1>")
            return None

        mail = modeloUsu.UsuManager.cogerPorMail(email)
        if mail is not None:
            self.response.out.write(EUS_HTML)
            self.response.out.write(
                    "<br></br><h1><font color='red'>Sartutako email-a hartuta dago</font></h1>")
            return None

        if modeloUsu.UsuManager.create(nombre, contra1, email):
            self.response.out.write("<h1>Kaixo " + nombre + "</h1>")
            self.response.out.write("<img src='images/kaixo.jpg'>")
            return None

        self.response.out.write(EUS_HTML)


app = webapp2.WSGIApplication([
    ('/registro', MainHandler),
    ('/Es', MainHandler),
    ('/En', EnHandler),
    ('/Eus', EusHandler),
    ('/validarEs', validarEs),
    ('/validarEn', validarEn),
    ('/validarEus', validarEus),
    ('/hora', HoraHandler),
    ('/mail',EmailHandler),

], debug=True)
