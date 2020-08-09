$(document).ready(function(){
    $("#search_result").on('change', function getinput(event){
    	var query_string = event.target.value

		 $.ajax({ 
            url: 'http://127.0.0.1:8000/iflame/search/?q=n',
            // dataType: 'JSON',
            
            // data: { matchvalue: matchvalue },
            type: 'get'
        }).done(function(responseData) {
            console.log('Done: ', responseData);
        }).fail(function() {
            console.log('Failed');
        });


    // 	$.get("demo_test.asp", function(data, status){
    // 		alert("Data: " + query_string + "\nStatus: " + status);
  		// });

    });
}); 