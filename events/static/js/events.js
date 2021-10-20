/*
 * Author      : Ajith kumar CL
 * Date        : 20 Oct 2021
 * Description : Events behind events.html page
 */

 $(document).ready(function () {

    // Button click event for Create new entity
    $(document).on ("click", "#btn_create_event", function(e){
        e.preventDefault();
        event_form = document.getElementById('event_form_div')
        event_form.removeAttribute('hidden');

        this.setAttribute('hidden',true);
    });
 });