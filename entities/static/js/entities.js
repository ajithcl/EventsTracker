/*
 * JAVASCRIPT behind entities page
 * Author : Ajith kumar CL
 * 28 Sep 2021
 */

$(document).ready(function () {

    // Create new entity form submit
    $(document).on ("submit", "#entity_form", function(e){
        e.preventDefault();

        var form_input = $(this).serialize();


    })

    // Button click event for Create new entity
    $(document).on ("click", "#btn_create_entity", function(e){
        e.preventDefault();


    })

 })