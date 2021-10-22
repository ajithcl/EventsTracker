/*
 * Author      : Ajith kumar CL
 * Date        : 20 Oct 2021
 * Description : Events behind events.html page
 */

 $(document).ready(function () {

    // Load event list
    loadEvents();

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
        event_form_message = document.getElementById('event_input_alert');
        $.ajax({
            url : 'create_event',
            type : 'POST',
            datatype : 'JSON',
            data : new FormData (this),
            processData : false,
            contentType : false,
            success : function(data, status){
                if (data.result == 'success'){
                    event_form_message.removeAttribute('hidden');
                    setTimeout (clearMessage, 4000);
                }
            },
            error : function (xhr, desc, err){
                alert(desc);
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

 // function for loading events list
 function loadEvents(){
    table_body = document.getElementById('table_body');
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    entity_name = urlParams.get('entityname');

    $.ajax({
        url : 'get_events',
        data : {"entity_name" : entity_name},
        type : 'GET',
        datatype : 'JSON',
        success : function (output){
            if (output.result == 'success'){
                event_list = output.data
                event_list = JSON.parse(event_list)
                event_table_html='';
                if (event_list.length > 0){
                    event_list.forEach(function(event_row){
                        event_field = event_row['fields']

                        event_table_html+=`
                                <tr>
                                    <td>${event_field["EventDate"]}</td>
                                    <td>${event_field["EventName"]}</td>
                                    <td>${event_field["Comments"]}</td>
                                    <td>
                                        <img src="../static/images/${event_field['ImageFileName']}" class="img-thumbnail" style="max-width:25%">
                                    </td>
                                </tr>
                        `;
                    })
                    table_body.innerHTML=event_table_html;
                }
            }
            else{
                alert('Error while accessing the events.');
            }
        },
        error : function (xhr, desc, err){
            alert('Error while accessing the events..');
        }
    })
 }

 // Function for clearing the alert message after submitting the input data
 function clearMessage(){
    event_form_message = document.getElementById('event_input_alert');
    event_form_message.setAttribute('hidden', true);
    }