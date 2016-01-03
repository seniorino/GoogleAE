//Para llamarlo sera necesario
//src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"


//Para llamar a la api de google maps
//<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"async defer></script>


function ratificarIdentidad() {
	return $.ajax({
		"type": "get",
		url: "/iden"
	});
}


function actualizarTiempo() {
	return $.ajax({
		"type": "get",
		url: "/acti"
	});
}

//Para poder ver el tiempo actualizado
function actualizarTiempo2(){
	$.ajax("/acti",
		{ "type": "get",
			// usualmente post o get
			"success": function(result) {
				$("#div1").html(result);
			},
			"error": function(result) {
				console.error("Se ha producido un error: ", result);
			},
			"async": true,})};


function ratificarIdentidad2(){

	$.ajax("/iden",
		{ "type": "get",
			// usualmente post o get
			"success": function(result) {
				$("#div1").html(result);
				},
			"error": function(result) {
				console.error("Se ha producido un error: ", result);
				},
			"async": true,})};


function pedirhora(){

		$.ajax("/hora",
		{ "type": "get",
			// usualmente post o ge
		   "success": function(result) {

				$("#div1").html("Hora: "+result);},
		   "error": function(result) {
			console.error("Se ha producido un error: ", result);},
		    "async": true,})};

function validarMail(){
            var mail=document.getElementById("email").value;
		    $.ajax("/mail",
		    { "type": "get",
				"data": {email:mail},
		     // usualmente post o get
		   "success": function(result2) {
				$("#divMail").html(result2);},
		   "error": function(result2) {
			console.error("Se ha producido un error: ", result2);},
		    "async": true,})};



function initMap(latitud, longitud) {
	map = new google.maps.Map(document.getElementById('map'), {
		center: {lat: latitud, lng: longitud},
		zoom: 12
	})}



function SacarMapa()
{
	var lugar=document.getElementById("busca").value;
	debugger;
	$.ajax("/mapa",
		{ "type": "get",
			"data": {busca:lugar},
			"dataType": "json",
			"success": function(datos) {
				if (datos['exito'] == "1")
				{
					initMap(datos['lat'], datos['long']);
				}
			},

			"error": function(datos) {
				debugger;
				console.error("Se ha producido un error: ", datos);},
			"async": true,})};






