$(document).ready( function() {

    $("#about-btn").click( function(event) {
          $("#msg").html('alloha!')
        msgstr = msgstr + "o"
        $("#msg").html(msgstr) 
});
});
//$(document).ready( function() {
//  $("#date").click( function(event) {
//      $( "#date" ).datepicker();
//      });
//});

  //$( "#date" ).datepicker();


//$(function myFunction() {
//    alert("Hello\nHow are you?");
//});
$(':input').blur(function() {
	  if($(this).val().length == 0) {
	    $(this)
	      .addClass('error')
	      .after('<span class="error">This field must be filled in!</span>');
	  }
	});
	$(':input').focus(function() {
	  $(this)
	    .removeClass('error')
	    .next('span')
	    .remove();
	  });
	  
$('#myform').bind('submit', function(event) {
	  $('[type=text]').each(function() {
	    if(!$(this).val().length) {
	      event.preventDefault();
	      $(this).css('border', '2px solid red');
	    }
	  });
	});
	

$('#del').click(function myFunction() {
    confirm("Press a button!");
});

$('#del').click(function() {
    confirm("Press a button!");
});

$(function () {
    $('#container1').highcharts({
        title: {
            text: 'Step line types, with null values in the series'
        },
        xAxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        },
        series: [{
            data: [1, 2, 3, 12, 9, 6, 7, 11, 9],
            name: 'Right'
        }, {
            data: [5, 6, 7, 8, 10, 11,  13],
            name: 'Center'
        }, {
            data: [9, 10, 11, 12, null, 14, 15, null, 17],
            step: 'left',
            name: 'Left'
        }]

    });
});

$(function() {
            $( "#dialog-1" ).dialog({
               autoOpen: false,  
               width: 500,
               height: 'auto',
                buttons: [
        {
            text: "Сохранить",
            //type: "submit",
            //form: "dateform",
            click: function() {
                $( "form#dateform" ).submit();
            }
        },
        {
            text: "Отмена",
            click: function() {
                $( this ).dialog( "close" );
            }
        }
    ]
,
            });
            $( "#opener" ).click(function() {
               $( "#dialog-1" ).dialog( "open" );
            });
         });



$(document).ready( function() { 
    for(var i = 0; i < 24; i++){
        $( "#date4" ).append($('<option>', {value: i, text: i} ));
        $( "#date3" ).append($('<option>', {value: i, text: i} ));
        $( "#date22" ).append($('<option>', {value: i, text: i} ));
        $( "#date11" ).append($('<option>', {value: i, text: i} ));
        }
    for(i = 0; i < 60; i += 30){
       $( "#datem4" ).append($('<option>', {value: i, text: i} ));
       $( "#datem3" ).append($('<option>', {value: i, text: i} ));
       $( "#datem2" ).append($('<option>', {value: i, text: i} ));
       $( "#datem1" ).append($('<option>', {value: i, text: i} ));  
        }
    });

$(document).ready( function() {
$('form #datedorm').submit(function(){

$.ajax({
            type: "POST",
            url: "graph_data/",
            data: $("#dateform").serialize(),
            dataType : "json"
          })
            .done(function(data){
               var trHTML = '';
               for (var i in data.zn1) {
               trHTML += '<tr class="success" style="font-size:75%"><td>' + data.ftime[i]+' '+'('+data.cur_day+')' + '</td>' + '<td>' + data.zn1[i]*2 + '</td>' + '<td>' + data.zn2[i]*2 + '</td>' + '<td>' + data.zn3[i]*2 + '</td>' + '<td>' + data.zn4[i]*2 + '</td>' + '<td>' + data.zn1[i] + '</td>' + '<td>' + data.zn2[i] + '</td>' + '<td>' + data.zn3[i] + '</td>' + '<td>' + data.zn4[i] + '</td></tr>';
               }
               $('#data_time').html(trHTML);
           
       });
    });
});
