$(document).ready(function() {
  $(".remove").on("click", function(){
    var valor = $(this).text();

    if(confirm('Deseja remover uma unidade de ' + valor + '?')){
      $.ajax({
        type: "POST",
        url: 'index',

        data: {'componente': },
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data){
            $('#changeref').modal('hide');
            alert('Success!');
        },
        failure: function(errMsg) {
            alert('Failure! ' +errMsg);
        }
      });
    }else{
      console.log('no')
    }

  });
});
