function create(){
    decision = confirm("Are you sure, you want to 'create' this container");
    if(decision == true){
         cname = document.getElementById("container_name").value
         img = document.getElementById("image_name").value
         xhr = new XMLHttpRequest();
         xhr.open('GET','http://13.233.244.12/cgi-bin/create.py?i=' +img+ '&n=' +cname,true);
        
         xhr.send();
         xhr.onload=function (){
             output = xhr.responseText;
             output = output + "\n\n!!! Container Created !!!";
             document.getElementById("output_id").innerHTML = output;
         }
    }
 }
 
function del(){
    decision = confirm("Are you sure, you want to 'Delete' this container");
    if(decision == true){
            cname = document.getElementById("del_name").value
            xhr = new XMLHttpRequest();
            xhr.open('GET','http://13.233.244.12/cgi-bin/del.py?n= '+cname,true);
            // http://15.207.254.199/cgi-bin/del.py?n
            xhr.send();
            xhr.onload=function (){
                output = xhr.responseText;
                    output = "Container " + output + " Deleted";
                document.getElementById("output_id").innerHTML = output;
            }
    }
}

function run(){

i=document.getElementById("command_name").value
var xhr=new XMLHttpRequest();
xhr.open('GET', 'http://13.233.244.12/cgi-bin/run.py?x='+i,true);

xhr.send();
xhr.onload=function(){
        var output=xhr.responseText;

        document.getElementById("output_id1").innerHTML=output;
}
}
