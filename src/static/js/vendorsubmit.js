window.firstname="none";
window.lastname="none";
window.email="none";
window.phonenumber="none";
window.model="none";
window.size="none";
window.moreinfo="none";

$('#firstName').keyup(function(event) {
    window.firstname=$('#firstName').val()
});
$('#lastName').keyup(function(event) {
    window.lastname=$('#lastName').val()
});
$('#email').keyup(function(event) {
    window.email=$('#email').val()
});
$('#phonenumber').keyup(function(event) {
    window.phonenumber=$('#phonenumber').val()
});
$('#model').keyup(function(event) {
    window.model=$('#model').val()
});
$('#size').keyup(function(event) {
    window.size=$('#size').val()
});
$('#moreinfo').keyup(function(event) {
    window.moreinfo=$('#moreinfo').val()
});

function SubmitInfo() {
    if (window.firstname == "none" || window.lastname == "none" || window.email == "none" || window.phonenumber == "none" || window.model == "none" || window.size == "none") {
        swal({dangerMode: true, text: "Some of input boxes are empty, please try again and fill in all required information.", title: "Error"}).then((value) => {formReset();});
        return;
    }
    $.post("/getcode",
    {
        "FirstName": window.firstname,
        "LastName": window.lastname,
        "Email": window.email,
        "phonenumber": window.phonenumber,
        "model": window.model,
        "size": window.size,
        "moreinfo": window.moreinfo 
    },
    function(data,status){
       window.location="/codeinfo/"+data;
    });
}
