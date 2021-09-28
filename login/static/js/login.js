/* JAVASCRIPT behind login page
 * Author : Ajith kumar CL
 * Date   : 27 Sep 2021   
 */


$(document).ready (function(){

    /* Login form submit event activates below trigger */
    $(document).on('submit', '#login_form', function(e){
        e.preventDefault();

        var form_input = $(this).serialize();

        $.ajax({
            url: 'login/verify_login',
            type: 'GET',
            data : form_input,
            success : function (output){
                if (output['result'] == 'error'){
                    alert('Login failed');
                }
                else{
                    window.location.href="/entities";
                }
            }
        })
    });


})