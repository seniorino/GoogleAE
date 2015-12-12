//Para llamarlo sera necesario
//src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"

function pedirhora(){

		$.ajax("/hora",
		{ "type": "get",
			// usualmente post o get

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
