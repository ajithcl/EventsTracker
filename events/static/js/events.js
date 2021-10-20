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

    // Input event form submit event
    $(document).on ("submit", "#event_form", function (e){
        e.preventDefault();
        console.log('submitted');
        $.ajax({
            url : 'create_event',
            type : 'POST',
            datatype : 'JSON',
            data : new FormData (this),
            processData : false,
            contentType : false,
            success : function(data, status){
                if (data.result == 'success'){
                    console.log(data); //TODO
                }
            },
            error : function (xhr, desc, err){
                console.error(desc); //TODO
            }
        })
    });


    // Button click for Cancel button Event
    $(document).on ("click", "#event_cancel", function (e){
        create_event_btn = document.getElementById('btn_create_event');
        event_form = document.getElementById('event_form_div')
        event_form.setAttribute('hidden',true);
        create_event_btn.removeAttribute('hidden');
    })
 });