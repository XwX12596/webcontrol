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
        <button id='15' type="button">15</button>
        <button id='30' type="button">30</button>
        <button id='45' type="button">45</button>
        <button id='60' type="button">60</button>
        <button id='75' type="button">75</button>
        <button id='90' type="button">90</button>
        <br>
        <button id='fetch' type="button">FETCH</button>
        <button id='warning' type="button">!WARNING!</button>
        <br>
        <img src="http://127.0.0.1:25565/stream.mjpg" width="640" height="480">
</body>
</html>
