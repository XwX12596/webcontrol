<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Remote Raspi</title>
    <script src="http://code.jquery.com/jquery.js"></script>
    <script> <!-- javascript 通过button向服务器发送post请求 -->
        $(function(){
            $("button").click(function(){
                window.history.go(0);
                if (this.id == "updateWait"){
                    text = document.getElementById("wait").value;
                    $.post("updateWait" + text);
                }
		else if (this.id == "rotate"){
		    angle = document.getElementById("angle").value;
		    $.post(angle)
		}
                else{
                    $.post(this.id);
                }
            });
        });
    </script>
</head>

<body>
        <input type="text" name="number" id="wait">
        <button type="button" id="updateWait">update</button>
        <br>
	<input type="text" name="number" id="angle"></input>
	<button type="button" id="rotate">update</button>
        <br>
        <button id='fetch' type="button">FETCH</button>
        <button id='warning' type="button">!WARNING!</button>
        <br>
        <img src="result.jpg" width="640" height="480">
</body>
</html>
