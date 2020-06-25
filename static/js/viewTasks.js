$('#stopped').click(function(){
   $('tr td').css({ 'background-color' : 'green'});
   $('td', this).css({ 'background-color' : 'red' });
});