window.onload = function(){
  data = retrieveData();
}

function retrieveData(componente_id = 0){
  if(componente_id){
      var url = 'http://localhost:8000/api/componentes/' + componente_id + '/';
  }else{
      var url = 'http://localhost:8000/api/componentes';
  }
  var api = new XMLHttpRequest();
  api.open('GET', url, true);
  api.send();

  api.onreadystatechange = function(){
    if(this.status == 200 && this.readyState == 4){
      let data = JSON.parse(this.responseText);

      text = '';

      for(let components of data){
        var tr = document.createElement('tr');
        for(let property of Object.entries(components)){
          text+='\n' + property[0] + ': ' + property[1];
          var td = document.createElement('td');
          td.innerHTML = property[1];
          tr.appendChild(td);
          document.getElementById('t-body').appendChild(tr);
        }
        text+='\n';
      }
      console.log(text);
    }
  }
}

document.querySelector('#download').addEventListener('click', function(){
  var doc = new jsPDF();
  doc.autoTable({html: '#table'});
  doc.save("table.pdf");
});
