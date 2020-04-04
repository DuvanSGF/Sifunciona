<!DOCTYPE html>
<html>
<style>
table,th,td {
  border : 1px solid black;
  border-collapse: collapse;
}
th,td {
  padding: 5px;
}
</style>
<body>

<button type="button" onclick="loadXMLDoc()">Get my Sensor Data classification from Python Flask</button>
<br><br>
<table id="demo"></table>

<script>
function loadXMLDoc() {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      myFunction(this);
    }
  };
  xmlhttp.open("GET", "http://127.0.0.1:5000/list", true);
  xmlhttp.send();
}
function myFunction(data) {	
  var str = data.responseText;
  
  var x = JSON.parse(str);
  x = x.Tiempo;
  var table = "<tr><th>#</th><th>Temperatura</th><th>Humedad</th>"
  table = table + "<th>Clima</th></tr>";
  for(var i=0; i<x.length; i=i+1){
  	 table += "<tr>";
  	 table += "<td>" + (i+1) + "</td>";
  	 table += "<td>" + x[i].tm + "</td>";
  	 table += "<td>" + x[i].hm + "</td>";
  	 table += "<td>" + x[i].clima + "</td>"
  	 table += "</tr>";	
  }
  document.getElementById("demo").innerHTML = table;
}
</script>

</body>
</html>