/* JAVASCRIPT behind login page
 * Author : Ajith kumar CL
 * Date   : 27 Sep 2021   
 */


$(document).ready (function(){

    /* Login form submit event activates below trigger */
    $(document).on('submit', '#login_form', function(e){
        e.preventDefault();

        alert("Hello world");

    });


})