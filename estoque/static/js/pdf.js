document.querySelector('#download').addEventListener('click', function(){
  var doc = new jsPDF();
  doc.autoTable({html: '#table'});
  doc.save("table.pdf");
});
