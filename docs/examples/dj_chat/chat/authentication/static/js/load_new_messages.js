window.onload = function(){
    //document.getElementById("message_list").innerHTML+= "added by js";




    var i = 10;
    while (i > 0)
    {
        var x = new XMLHttpRequest();
        x.open("GET", "{% url 'get_messages' %}", true);
        x.send();
        x.onload = function (){
            document.getElementById("message_list").innerHTML += x.responseText;
            document.getElementById("message_list").innerHTML += '</br>'
            /*JSON.parce(x.responseText, function(k, v){
                document.getElementById("message_list").innerHTML += k;
                document.getElementById("message_list").innerHTML += v;
            });*/
        }

        var now = new Date().getTime();
        while(new Date().getTime() < now + 500){ /* Do nothing */ }

        i = i - 1;
    }

}