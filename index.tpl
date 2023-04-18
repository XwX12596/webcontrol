<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Remote Raspi</title>
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <!--<meta http-equiv="Expires" content="0"> -->
    <script src="http://code.jquery.com/jquery.js"></script>
    <script>
        $(function(){
            $("button").click(function(){
                // cmd="{cmd:"+this.id+"}"
                // alert(cmd)
                window.history.go(0);
                $.post(this.id);
            });
        });
    </script>
</head>

<body>
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
        <img src="original.jpg">
</body>
</html>
