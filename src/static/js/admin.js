function ShowData() {
    var e = document.getElementById("data");
        if(e.style.display == 'block')
            e.style.display = 'none';
        else
            e.style.display = 'block';
}

function RefreshData() {
    $.post( "/root/refreshdata", function( data ) {
        swal({dangerMode: true, text: "Server Responded With: "+data, title: "Data Refresh Request"}).then((value) => {window.location.reload();});
    });
}

function Show(id) {
    var e = document.getElementById(id);
    if (id == "createuser") {
        var deleteuser = document.getElementById("deleteuser");
        deleteuser.style.display = 'none';
    } else if (id == "deleteuser") {
        var cuser = document.getElementById("createuser");
        cuser.style.display = 'none'; 
    }
    if(e.style.display == 'block')
        e.style.display = 'none';
    else
        e.style.display = 'block';
}

if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)){
    if (window.location.pathname == '/root') {window.location='/mroot';}
}else{
    if (window.location.pathname == '/mroot') {window.location='/root';}
}