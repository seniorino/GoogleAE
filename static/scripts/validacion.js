
function verificarCampos()
{ 
/*verifica que el nombre, apellidos y email no sean nulos*/
var nombre=document.getElementById("nombre").value;
var contra1=document.getElementById("contra1").value;
var contra2=document.getElementById("contra2").value;
var email=document.getElementById("email").value;
var idioma=document.getElementsByName("Language");

var ido= (idioma[0].value);

//alert (idioma[0].value);


if(nombre==''|| contra1 ==''|| email == '' || contra2 =='')
{

if( ido == 'Castellano')
{
alert('Error, rellene todos los campos obligatorios (*)');
return false;
}

if( ido == 'English')
{
alert('Error, fill all the requiered information(*)');
return false;
}

else
{
alert('Errorea, sartu beharrezko informazio guztia(*)');
return false;
}

}

 
return true;
}


function verificarLogin()
{
	var usuario=document.getElementById("user").value;
	var contra=document.getElementById("password").value;
	if (usuario==' ' || contra== '')
	{
		alert('Introduzca toda la informacion necesaria(*)');
		return false;
	}
	return true;

}


function verificarContras()
{
var contra1=document.getElementById("contra1").value;
var contra2=document.getElementById("contra2").value;
var idioma=document.getElementsByName("Language");

var ido= (idioma[0].value);

debugger;

if(   (contra1.length)<6  && ido == 'Castellano')
{

alert('La contraseña tiene que tener un minimo de 6 caracteres(*)');
return false;
}

else if(   (contra1.length)< 6  && ido == 'English')
{

alert('The password must have at least 6 characters(*)');
return false;
}

else if(   (contra1.length)< 6  && ido == 'Euskera')
{

alert('Pasahitza gutxienez 6 karaktere behar ditu(*)');
return false;
}
	debugger;

if(contra1 != contra2)
{
if( ido == 'Castellano')
{

alert('Error, las contrasenas tienen que ser iguales(*)');
return false;
}

else if( ido == 'English')
{

alert('Error, passwords must match(*)');
return false;
}

else
{

alert('Errorea, pasahitzak berdinak izan behar dira(*)');
return false;
}
} 
return true;
}

function verificarMail()
{
//Verifica que el mail que se inserta es correcto
var email=document.getElementById("email").value;
var idioma=document.getElementsByName("Language");

var ido= (idioma[0].value);
   expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ( !expr.test(email) )
	{
	
	if( ido == 'Castellano')
{
alert('Error: La direccion de correo electronico es incorrecta.');
return false;
}

if( ido == 'English')
{
alert('Error, the email format it not correct(*)');
return false;
}

else
{
alert('Errorea, email-aren formatua ez da ona(*)');
return false;
}
	
		}
return true;
}


function verificarNombre()
{
//Verifica que el mail que se inserta es correcto
	var nombre=document.getElementById("nombre").value;
	var idioma=document.getElementsByName("Language");

	var ido= (idioma[0].value);
	expr = /^[A-Za-z0-9_-]*$/;
	if ( !expr.test(nombre) )
	{

		if( ido == 'Castellano')
		{
			alert('Error: El nombre solo puede contener numeros y letras(*).');
			return false;
		}

		if( ido == 'English')
		{
			alert('Error, the name can only contain numbers and letters(*)');
			return false;
		}

		else
		{
			alert('Errorea, izenak bakarrik letrak eta zenbakiak izan ditzazke(*)');
			return false;
		}

	}
	return true;
}


function verificarTelefono()
{
//Verificamos que el telefono esta compuesto por 9 cifras numericas

var telf=document.getElementById("telefono").value;
var idioma=document.getElementsByName("Language");
	
var ido= (idioma[0].value);
if (telf!='')
{	

    expr= /^\d{9}$/;
	if ( !expr.test(telf) )
	{
	
	if( ido == 'Castellano')
{
alert('Error: Introduzca un telefono valido con 9 cifras.');
return false;
}

if( ido == 'English')
{
alert('Error, introduce a 9 digit telephone number');
return false;
}

else
{
alert('Errorea, sartutako telefono zenbakia ez ditu 9 zenbaki');
return false;
}
	
	}
}
return true;
}

function ValidarTodo()
{
	return verificarCampos()&&verificarMail()&&verificarContras()&&verificarTelefono()
}