<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Remote Raspi</title>
    <script src="http://code.jquery.com/jquery.js"></script>
    <script>
        $(function(){
            $("button").click(function(){
                window.history.go(0);
                if (this.id == "updateWait"){
                    text = document.getElementById("wait").value;
                    $.post("updateWait" + text);
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
        <button id='fetch' type="button">FETCH</button>
        <button id='warning' type="button">!WARNING!</button>
        <br>
        <img src="stream.mjpg" width="640" height="480">
</body>
</html>
