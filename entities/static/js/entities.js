/*
 * JAVASCRIPT behind entities page
 * Author : Ajith kumar CL
 * 28 Sep 2021
 */

$(document).ready(function () {

    // Load Entity details

    loadEntities()

    // Create new entity form submit
    $(document).on ("submit", "#entity_form", function(e){
        e.preventDefault();
        entity_message = document.getElementById('entity_input_alert');

        // Reference : https://stackoverflow.com/questions/4545081/how-to-do-file-upload-using-jquery-serialization
        $.ajax({
            url : 'create_entity',
            type : 'POST',
            datatype: 'JSON',
            data : new FormData(this),
            processData : false,
            contentType : false,
            success: function (data, status){
                if (data.result == 'success'){
                    entity_message.removeAttribute('hidden');
                    setTimeout (clearMessage, 4000);
                }
            },
            error: function(xhr, desc, err){

            }
        })
    })

    // Button click event for Create new entity
    $(document).on ("click", "#btn_create_entity", function(e){
        e.preventDefault();
        entity_form = document.getElementById('entity_form_div')
        entity_form.removeAttribute('hidden');

        this.setAttribute('hidden',true);
    })

    // Button click for Cancel Event
    $(document).on ("click", "#event_cancel", function (e){
        create_entity_btn = document.getElementById('btn_create_entity');
        entity_form = document.getElementById('entity_form_div')
        entity_form.setAttribute('hidden',true);
        create_entity_btn.removeAttribute('hidden');
    })

 })

// Function for clearing the alert message after submitting the input data
 function clearMessage(){
    entity_message = document.getElementById('entity_input_alert');
    entity_message.setAttribute('hidden', true);
    }

 // Function for loading all entity details
 function loadEntities(){
    entity_cards_span = document.getElementById('entity_cards_span');
    $.ajax({
        url: 'get_entities',
        type: 'GET',
        datatype:'JSON',
        success: function (data){
            if (data.result == 'success'){
                entity_list = data.data;
                entity_list = JSON.parse(entity_list)
                entity_cards_html='';
                if (entity_list.length > 0){
                    entity_list.forEach(function(entity_value){
                        entity_field = entity_value['fields']
                        entity_cards_html+=`
                            <div class="card bg-light mb-2" data-rowid=${entity_field['EntityName']} style="max-width: 18rem;">
                                <img class="card-img-top" src="../static/images/entities/${entity_field['ImageFileName']}" >
                                <div class="card-body">
                                    <h5 class="card-title">${entity_field['EntityName']}</h5>
                                    <p class="card-text">${entity_field['Comments']}</p>
                                </div>
                            </div>
                                            `;
                                        })

                    entity_cards_span.innerHTML = entity_cards_html
                }
            }
        },
        error: function(xhr, desc, err){
        }
    })
 }
