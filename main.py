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
from webapp2_extras import sessions
import SessionModule
import hashlib
import urllib
import json
import datetime
import string
import random


# Import smtplib for the actual sending function
import smtplib
from google.appengine.api import mail
# Import the email modules we'll need
from email.mime.text import MIMEText


from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers


ModificarPass="""\
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/mainCss.css">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<script src="scripts/otros.js"></script>

</head>
<body>
<h1>Modificar password </h1>

<form action="/modi" method="post" >
Introduzca su password vieja:
<INPUT type="password" id="passV" name="passV" autocomplete="off" required>
Introduzca su password nueva:
<INPUT type="password" id="passN" name="passN" autocomplete="off"  required>
<input type="submit" name="submit" value="Submit">
</form>
</form>
  <FORM  action="/" method="get">
    <P>
    <INPUT type="submit" value="Regresar"  >
    </P>
 </FORM>
<script>
    //Si movemos el raton actualizar el tiempo de inactividad
    document.onmousemove = (function() {
    var onmousestop = function() {
    actualizarTiempo();
    }, thread;

  return function() {
    clearTimeout(thread);
    thread = setTimeout(onmousestop, 500);
  };
})();



    //De esta manera veremos si el usuario lleva inactivo un tiempo
var dat;
var v=setInterval(function(){promise = ratificarIdentidad();
	promise.success(function (data) {
		dat=data;
	});
	if (dat == "1") {
	clearInterval(v);
	alert ("Desconectado por periodo largo de inactividad");
	window.location.replace("/");
}
},40000);




</script>
</body>

</html>
"""






MENU_USUARIO="""\
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/mainCss.css">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB_tVbwRzxAWhC43hoJRfkSTaieUs9bAzs"
        async defer></script>
<script src="scripts/otros.js"></script>

</head>
<body>
<h1>Pagina principal</h1>
<div id="divmain"></div>
<img src="images/hello.jpg" >
<form action="/uploadHandler" method="GET" ">
<input type="submit" name="submit" value="Subir fotos">
</form>
<form action="/download" method="GET" ">
<input type="submit" name="submit" value="ver fotos">
</form>
<form action="/modi" method="GET">
<input type="submit" name="submit" value="modificar password">
</form>
<LABEL for="busca">Introduzca el lugar que quiere buscar en el mapa: </LABEL>


<INPUT type="text" id="busca" name="busca" >
<input id="clickMe" type="button" value="buscar" onclick="SacarMapa();" />


<form action="/logout" method="POST" ">
<input type="submit" name="submit" value="Logout">
</form>




<div id="div1"></div>

<script>
    //Si movemos el raton actualizar el tiempo de inactividad
    document.onmousemove = (function() {
    var onmousestop = function() {
    actualizarTiempo();
    }, thread;

  return function() {
    clearTimeout(thread);
    thread = setTimeout(onmousestop, 500);
  };
})();



    //De esta manera veremos si el usuario lleva inactivo un tiempo
var dat;
var v=setInterval(function(){promise = ratificarIdentidad();
	promise.success(function (data) {
		dat=data;
	});
	if (dat == "1") {
	clearInterval(v);
	alert ("Desconectado por periodo largo de inactividad");
	window.location.replace("/");
}
},40000);




</script>
<div id="map"></div>
</body>

</html>
"""





FORM_SUBIR_FOTO="""\
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/mainCss.css">
<script src="scripts/validacion.js"></script>
</head>
<body>
<form action="%(url)s" method="POST" enctype="multipart/form-data">
<input type="file" name="file"><br>
<input type="radio" name="access" value="public" checked="checked" /> Public
<input type="radio" name="access" value="private" /> Private
<input type="submit" name="submit" value="Subir foto">
</form>
  <FORM  action="/" method="get">
    <P>
    <INPUT type="submit" value="Regresar"  >
    </P>
 </FORM>
<script>
    //Si movemos el raton actualizar el tiempo de inactividad
    document.onmousemove = (function() {
    var onmousestop = function() {
    actualizarTiempo();
    }, thread;

  return function() {
    clearTimeout(thread);
    thread = setTimeout(onmousestop, 500);
  };
})();



    //De esta manera veremos si el usuario lleva inactivo un tiempo
var dat;
var v=setInterval(function(){promise = ratificarIdentidad();
	promise.success(function (data) {
		dat=data;
	});
	if (dat == "1") {
	clearInterval(v);
	alert ("Desconectado por periodo largo de inactividad");
	window.location.replace("/");
}
},40000);

</script>
</body>
</html>
"""



INTRO_HTML = """\
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/mainCss.css">
<script src="scripts/validacion.js"></script>
</head>
<body>
<div id="divmain"></div>
<br></br>
<h1>Login</h1>

 <FORM  action="/login" method="post" onSubmit="return verificarLogin()">
    <P>
    <LABEL for="user">User(*): </LABEL>
              <INPUT type="text" id="user" name="user"><BR>
    <LABEL for="password">Password(*): </LABEL>
              <INPUT type="password" id="password" name="password" autocomplete="off"><BR>
    <INPUT type="submit" value="Enviar"  > <INPUT type="reset">
    </P>
 </FORM>
 <FORM  action="/registro" method="get">
    <P>
    <INPUT type="submit" value="Registrarse"  >
    </P>
 </FORM>
  <FORM  action="/registro" method="get">

 </FORM>
</body>
</html>
"""



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




 <FORM  action="/validarEs" method="post" onSubmit="return verificarCampos()&& verificarMail() && verificarContras() && verificarTelefono() && verificarNombre()">
    <P>
	<input type="hidden" name="Language" value="Castellano">
    <LABEL for="nombre">Nombre(*): </LABEL>
              <INPUT type="text" id="nombre" name="nombre"><BR>
    <LABEL for="contra1">Contrase&ntilde;a(*): </LABEL>
              <INPUT type="password" id="contra1" name="contra1" autocomplete="off"><BR>
	<LABEL for="contra2">Repetir contrase&ntilde;a(*): </LABEL>
              <INPUT type="password" id="contra2" name="contra2" autocomplete="off"><BR>
    <LABEL for="email">email(*): </LABEL>
              <INPUT type="text" id="email" name="email" onblur="validarMail()"> <div id="divMail"></div><BR>
    <LABEL for="telefono">Numero de telefono: </LABEL>
              <INPUT type="text" id="telefono" name="telefono"><BR>
    <INPUT type="submit" value="Enviar"  > <INPUT type="reset">
    </P>
 </FORM>
  <FORM  action="/" method="get">
    <P>
    <INPUT type="submit" value="Regresar"  >
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
 <FORM  action="/validarEus" method="post" onSubmit="return verificarCampos()&& verificarMail() && verificarContras() && verificarTelefono() && verificarNombre()">
 <input type="hidden" name="Language" value="Euskera">
    <P>
    <LABEL for="nombre">Izena(*): </LABEL>
              <INPUT type="text" id="nombre" name="nombre"><BR>
    <LABEL for="contrasema">Pasahitza(*): </LABEL>
              <INPUT type="password" id="contra1" name="contra1" autocomplete="off"><BR>
	<LABEL for="contrasenia2">Pasahitza berriro(*): </LABEL>
              <INPUT type="password" id="contra2" name="contra2" autocomplete="off"><BR>
    <LABEL for="email">email(*): </LABEL>
              <INPUT type="text" id="email" name="email" onblur="validarMail()"> <div id="divMail"></div><BR>
    <LABEL for="telefono">Telefono zenbakia: </LABEL>
              <INPUT type="text" id="telefono" name="telefono"><BR>
    <INPUT type="submit" value="Enviar"  > <INPUT type="reset">
    </P>
 </FORM>
  <FORM  action="/" method="get">
    <P>
    <INPUT type="submit" value="Regresar"  >
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
 <FORM  action="/validarEn" method="post" onSubmit="return verificarCampos()&& verificarMail() && verificarContras() && verificarTelefono() && verificarNombre()">
    <P>
	<input type="hidden" name="Language" value="English">
    <LABEL for="nombre">Name(*): </LABEL>
              <INPUT type="text" id="nombre" name="nombre"><BR>
    <LABEL for="contrasema">Password(*): </LABEL>
              <INPUT type="password" id="contra1" name="contra1" autocomplete="off"><BR>
	<LABEL for="contrasenia2">Repit password(*): </LABEL>
              <INPUT type="password" id="contra2" name="contra2" autocomplete="off" ><BR>
    <LABEL for="email">email(*): </LABEL>
              <INPUT type="text" id="email" name="email" onblur="validarMail()"> <div id="divMail"></div><BR>
    <LABEL for="telefono">Phone number: </LABEL>
              <INPUT type="text" id="telefono" name="telefono"><BR>
    <INPUT type="submit" value="Enviar"  > <INPUT type="reset">
    </P>
 </FORM>
  <FORM  action="/" method="get">
    <P>
    <INPUT type="submit" value="Regresar"  >
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







class MainHandler(SessionModule.BaseSessionHandler):
    def get(self):
        if self.session.get('log') == 1:

            if self.session.get('Mensaje'):
                self.response.write(self.session.get('Mensaje'))
                del self.session['Mensaje']
                self.response.write(MENU_USUARIO)
            else:
                self.response.write(MENU_USUARIO)

        elif self.session.get('Mensaje'):
            self.response.write(self.session.get('Mensaje'))
            del self.session['Mensaje']
            self.response.write(INTRO_HTML)
        else:

            self.response.write(INTRO_HTML)




class HoraHandler(webapp2.RequestHandler):
    def get(self):
        t =time.localtime()
        if t.tm_hour == 24 or t.tm_hour == 00 :
            self.response.out.write("%s : %s : %s"
                                    %((01),t.tm_min,t.tm_sec))
        elif t.tm_hour == 23 :
            self.response.out.write("%s : %s : %s"
                                    %((00),t.tm_min,t.tm_sec))
        else:
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

class EsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(ESP_HTML)

class EnHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(ENG_HTML)


class EusHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(EUS_HTML)


class validarEs(SessionModule.BaseSessionHandler):
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

        if not re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', email):
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


        if re.match('^[A-Za-z0-9_-]*$', nombre):
            if modeloUsu.UsuManager.create(nombre, contra1, email, telefono):
                self.session['log'] = 1
                self.session['nombre'] = nombre
                self.response.out.write("<h1>Hola " + nombre + "</h1>")
                self.response.out.write(MENU_USUARIO)
                return None
        else:
            self.response.out.write("El nombre de usuario solo puede contener numeros y letras.")

        self.response.out.write(ESP_HTML)


class validarEn(SessionModule.BaseSessionHandler):
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

        if not re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', email):
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

        if re.match('^[A-Za-z0-9_-]*$', nombre):
            if modeloUsu.UsuManager.create(nombre, contra1, email, telefono):
                self.session['log'] = 1
                self.session['nombre'] = nombre
                self.response.out.write("<h1>Hello " + nombre + "</h1>")
                self.response.out.write(MENU_USUARIO)
                return None
        else:
            self.response.out.write("The username can only have letters and numbers.")

        self.response.out.write(ENG_HTML)


class validarEus(SessionModule.BaseSessionHandler):
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

        if not re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', email):
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

        if re.match('^[A-Za-z0-9_-]*$', nombre):
            if modeloUsu.UsuManager.create(nombre, contra1, email, telefono):
                self.session['log'] = 1
                self.session['nombre'] = nombre
                self.response.out.write("<h1>Kaixo " + nombre + "</h1>")
                self.response.out.write(MENU_USUARIO)
                return None
        else:
            self.response.out.write("Erabiltzailearen izena bakarrik letrak eta zenbakiak izan ditzazke.")

        self.response.out.write(EUS_HTML)


class LogHandler(SessionModule.BaseSessionHandler):
        def post(self):
            user = self.request.get('user')
            password = self.request.get('password')

            hashpass = hashlib.md5(password).hexdigest()
            usuario = modeloUsu.UsuManager.cogerPorNombre(user)

            if usuario is not None:
                pass1= modeloUsu.UsuManager.getPassword(usuario)
                nom = modeloUsu.UsuManager.getNombre(usuario)
                bloqueo = modeloUsu.UsuManager.getBloqueo(usuario)
                IdAcceso = "Acceso"+nom;

                if bloqueo == True:
                    self.response.out.write("<h1>Cuenta de usuario "+nom+" bloqueada</h1>")
                    self.response.write(INTRO_HTML)
                    return None;

                if not self.session.get(IdAcceso):
                    self.session[IdAcceso]=1

                else:
                    self.session[IdAcceso] = self.session[IdAcceso]+1



                if (pass1 == hashpass):

                    self.session[IdAcceso]=0
                    self.response.out.write("<h1>Hello " + user + "</h1>")
                    self.session['log'] = 1
                    self.session['nombre'] = user
                    self.session['ultimoAcceso'] = time.time()

                    self.response.write(MENU_USUARIO)
                else:
                    if self.session[IdAcceso] == 3:
                        modeloUsu.UsuManager.bloquearCuenta(usuario)
                        self.response.out.write("<h1>Cuenta de usuario "+nom+" bloqueada</h1>")
                        self.session[IdAcceso]=1
                        self.response.write(INTRO_HTML)

                    else:
                        self.response.out.write("<h1>Password incorrecta</h1>")
                        self.response.out.write("<h1>Lleva "+str(self.session[IdAcceso])+" intentos</h1>")
                        self.response.write(INTRO_HTML)
            else:
                self.response.out.write("<h1>Usuario no existente</h1>")
                self.response.write(INTRO_HTML)


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler, SessionModule.BaseSessionHandler ):
    def get(self):
        if (self.session.get('log'))== 1:
            self.session['ultimoAcceso'] = time.time()
            upload_url = blobstore.create_upload_url('/upload')
            self.response.out.write(FORM_SUBIR_FOTO % {'url':upload_url})
        else:
            self.response.out.write("<h1>Usuario no autenticado, identifiquese</h1>")
            self.response.out.write(INTRO_HTML)




class Upload(blobstore_handlers.BlobstoreUploadHandler, SessionModule.BaseSessionHandler):
    def post(self):
        if (self.session['log'] == 1):
            upload_files = self.get_uploads('file')
            #proceso el fichero que he recibido en el servidor
            try:
                blob_info = upload_files[0] # guardo la imagen en el BlobStore
                img = modeloUsu.Image(user=self.session.get('nombre'),    public=self.request.get("access")=="public", blobkey=blob_info.key())
                img.put() #guardo el objeto Image
                #Dependiendo de la logica de negocio, le permito que suba otra foto o      bien le mando al menu principal
                self.session['Mensaje'] = "<h2><font color='green'>Foto subida correctamente</h2></font>"
                self.redirect('/')
            except:
                self.session['Mensaje'] = "<h2><font color='red'>Error, escoga una foto valida que subir</h2></font>"
                self.redirect('/')

class LogoutHandler(SessionModule.BaseSessionHandler):
    def post(self):
        del self.session['log']
        del self.session['nombre']
        del self.session['ultimoAcceso']

        self.response.out.write("<h1>Sesion terminada</h1>")
        self.response.out.write(INTRO_HTML)


class ViewHandler(blobstore_handlers.BlobstoreUploadHandler, SessionModule.BaseSessionHandler):
    def get(self):


        if (self.session.get('log'))== 1:
            #Aqui no tendremos en cuenta la inactividad
            self.session['ultimoAcceso'] = time.time()
            fotos= blobstore.BlobInfo.all()
            for foto in fotos:
                #blobk= str(foto.key())
                #self.response.out.write("<h1>La key de la foto es</h1>"+blobk)
                imagen = modeloUsu.ImageManager.cogerImagen(foto.key())
                if  modeloUsu.getpublicImg(imagen) or (modeloUsu.getUserImg(imagen)== self.session['nombre']):
                    if modeloUsu.getpublicImg(imagen):
                        privaci = 'publica'
                    else:
                        privaci = 'privada'

                    autor= str(modeloUsu.getUserImg(imagen))
                    self.response.out.write('<link rel="stylesheet" type="text/css" href="css/mainCss.css">')
                    self.response.out.write('<div class="img"><img height="300" width="300" src="serve/%s" ><span>Autor: {autor}</span></div></td>'.format(autor=autor) %     foto.key())


            self.response.out.write('<html><body>  <FORM  action="/" method="get"><P><INPUT type="submit" value="Regresar"  ></P></FORM></body></html>')

        else:
            self.response.out.write("<h1>Usuario no autenticado, identifiquese</h1>")
            self.response.out.write(INTRO_HTML)


class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        self.send_blob(blob_info)

class MapHandler(SessionModule.BaseSessionHandler, webapp2.RequestHandler):
    def get(self):
        #Obtencion de datos
        if (self.session['log'] == 1):
            self.session['ultimoAcceso'] = time.time()
            serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
            address=self.request.get('busca')
            url = serviceurl + urllib.urlencode({'address': address})
            uh = urllib.urlopen(url)
            data = uh.read()
            js = json.loads(str(data))
            try:
                location = js['results'][0]['formatted_address']
                latitud = js['results'][0]['geometry']['location']['lat']
                longitud = js['results'][0]['geometry']['location']['lng']
                self.response.headers['Content-Type'] = 'application/json'
                self.response.out.write (json.dumps({"exito": 1, "lat": latitud, "long": longitud}))

            except Exception as e:
                self.response.out.write (json.dumps({"exito":0}))
        else:
            self.response.out.write("<h1>Usuario no autenticado, identifiquese</h1>")
            self.response.out.write(INTRO_HTML)

class IdentityHandler(SessionModule.BaseSessionHandler, webapp2.RequestHandler):
    def get(self):
        if (self.session.get('log'))== 1:
            Now= time.time()
            LastTime = self.session['ultimoAcceso']
            Total= Now-LastTime
            #Si lleva mas de 3 minutos inactivo
            if Total > 180:
                del self.session['log']
                del self.session['nombre']
                del self.session['ultimoAcceso']
                #self.redirect('/')
                #self.response.out.write("<h1>Sesion terminada por inactividad, vuelva a introducir sus datos por favor</h1>")
                self.response.out.write("1")
            #else:
                #self.response.out.write("Total "+str(Total))


class ActualizarActividad(SessionModule.BaseSessionHandler):
    def get(self):
            self.session['ultimoAcceso']=  time.time()





class ModificarDatos(SessionModule.BaseSessionHandler, webapp2.RequestHandler):
    def get(self):
        if (self.session.get('log'))== 1:
            self.response.out.write(ModificarPass)
        else:
            self.response.out.write("<h1>Usuario no autenticado, identifiquese</h1>")
            self.response.write(ModificarPass)

    def post(self):
        if (self.session.get('log'))== 1:
            nombre = self.session['nombre']
            user = modeloUsu.UsuManager.cogerPorNombre(nombre)
            passV = self.request.get('passV')
            passN = self.request.get('passN')
            hashpassV = hashlib.md5(passV).hexdigest()
            hashpassN = hashlib.md5(passN).hexdigest()

            if len(passN) < 6:
                self.response.out.write("Minimo numero de caracteres necesarios para la nueva password es 6.")
                self.response.write(ModificarPass)
                return None

            if user is not None:
                pass1= modeloUsu.UsuManager.getPassword(user)
                if (pass1== hashpassV):
                    if (pass1 == hashpassN):
                        self.response.out.write("<h1>No puede introducir su ultima password, introduzca otra por favor</h1>")
                        self.response.write(ModificarPass)
                    else:
                        randomCode= ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
                        urlConfirm= "http://5.prime-service-114619.appspot.com/confirm/"+str(randomCode)
                        #Creamos un codigo aleatorio con caracteres y marcamos cuando se envia
                        modeloUsu.UsuManager.guardarCodigo(user,str(randomCode))
                        modeloUsu.UsuManager.guardarTimeCodigo(user)
                        modeloUsu.UsuManager.guardarOpcionalPass(user,str(hashpassN))
                        email = str(user.email)
                        user_address = email
                        sender_address = "onega47@hotmail.com"
                        subject = "Confirmacion de cambio de password"
                        body = """
                            Su actual password va a ser cambiada por la siguiente:
                            {passi}
                            Si esta de acuerdo, vaya al siguiente enlace:
                            {confirmationURL}
                            """.format(passi = passN, confirmationURL = urlConfirm)
                        mail.send_mail(sender_address, user_address, subject, body)
                        self.response.write("<h2>Un correo le ha sido enviado a "+str(email)+" para confirmar el cambio, el correo le sera enviado desde la direccion 'onega47@hotmail.com' </h2>")
                        self.response.write(MENU_USUARIO)


                else:
                    self.response.out.write("<h1>La password que ha introducido no es correcta</h1>")
                    self.response.write(ModificarPass)
        else:
            self.response.out.write("<h1>Usuario no autenticado, identifiquese</h1>")
            self.response.write(ModificarPass)


class ConfirmationHandler(SessionModule.BaseSessionHandler, webapp2.RequestHandler):
    def get(self,Paramsurl):
        #Con esto sabremos el codigo que viene en la URL
        #Paramsurl= self.request.path
        #codeRegIni = re.search(r"/confirm/(.*)",Paramsurl)
        #codeReg=codeRegIni.group(1)
        codeReg=str(Paramsurl)
        #self.response.out.write("Code reg es "+codeReg)
        ####
        #Ahora buscamos en nuestra base de datos un codigo cuyas primeras cifras se parezcan a este
        usuario = modeloUsu.UsuManager.getUserConfirmation(codeReg)

        if usuario is not None:
            tiempoActual = time.time()
            tiempoEnvio = modeloUsu.UsuManager.getConfirmationTime(usuario)

            if ((int(tiempoActual)-int(tiempoEnvio))>180):
                self.session['Mensaje'] = "<h1><font color='red'>Su mensaje de confirmacion ha expirado, pruebe otra vez</h1></font>"
                modeloUsu.UsuManager.guardarCodigo(usuario,''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(15)))
                modeloUsu.UsuManager.guardarOpcionalPass(usuario,'None')
            else:
                opPass= modeloUsu.UsuManager.getOptionalPassword(usuario)
                modeloUsu.UsuManager.cambiarPass(usuario,opPass)
                modeloUsu.UsuManager.guardarOpcionalPass(usuario,'None')
                self.session['Mensaje'] = "<h1><font color='green'>Su password ha sido cambiada correctamente</h1></font>"

            self.redirect("/")

        else:
            self.session['Mensaje'] ="<h1><font color='red'>Detectado intento de acceso no permitido</h1></font>"
            self.redirect("/")






app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/registro', EsHandler),
    ('/Es', EsHandler),
    ('/En', EnHandler),
    ('/Eus', EusHandler),
    ('/validarEs', validarEs),
    ('/validarEn', validarEn),
    ('/validarEus', validarEus),
    ('/hora', HoraHandler),
    ('/mail',EmailHandler),
    ('/login',LogHandler),
    ('/logout',LogoutHandler),
    ('/uploadHandler',UploadHandler),
    ('/upload',Upload),
    ('/download', ViewHandler),
    ('/serve/([^/]+)?', ServeHandler),
    ('/mapa', MapHandler),
    ('/iden',IdentityHandler),
    ('/acti',ActualizarActividad),
    ('/modi',ModificarDatos),
    (r'/confirm/(.*)', ConfirmationHandler)

], config = SessionModule.myconfig_dict, debug=True)
