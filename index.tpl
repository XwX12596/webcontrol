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
                cmd="{cmd:"+this.id+"}"
                // alert(cmd)
                $.post(this.id);
            });

        });

    </script>
</head>
<body>
        <button id='cam-up' type="button">UP!</button>
        <button id='cam-down' type="button">DOWN!</button>
        <button id='cam-left' type="button">LEFT!</button>
        <button id='cam-right' type="button">RIGHT!</button>
        <button id='fetch' type="button">RIGHT!</button>
        <br>
        <img src="/result.jpg">

</body>
</html>
