<script>
	function classify(){
		// Sending and receiving data in JSON format using Post method
		var tm = parseInt(document.getElementById("tm").value);
		var hm = parseInt(document.getElementById("hm").value);


		var xhr = new XMLHttpRequest();
		var url = "http://127.0.0.1:5000/classify/";
		xhr.open("POST", url, true);
		xhr.setRequestHeader("Content-Type", "application/json");
		xhr.onreadystatechange = function() {
			if (xhr.readyState ==== 4 && xhr.status === 200) {
				var json = JSON.parse(xhr.responseText);
				document.getElementById("category").innerHTML = "Category: " + json.clima;
			}
		};
		var data = JSON.stringify([{"hm":hm, "tm":tm}]);
		xhr.send(data);
	}
</script>

<form method="post">
	<p>Temperatura (°C):
	<br/>
	<input type="text" name="pl" id="pl">
	</p>
	<p>Humedad (°C):
	<br/>
	<input type="text" name="pw" id="pw">
	</p>
	<p><input type="button" value="Classify JSON" onclick="classify()">
</form>
<p id="category"></p>