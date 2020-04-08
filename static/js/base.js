nav= 1;
$(document).ready(function(){
    $("#menu").toggle();
    // $('#academics_innermenu').removeClass('d-none');
    // $('#people_innermenu').removeClass('d-none');
    // $('#research_innermenu').removeClass('d-none');
});
function handleinnermenu(head, id){
    head= head.toString().toLowerCase();
    let selector2= $('#'+id.toString());
    let selector3= $('#'+head+'_svg');
    if(!($('#'+head+'_innermenu').hasClass('d-none'))){
        $('#'+head+'_innermenu').addClass('d-none');
        if(selector2.hasClass('bg-green')){
            selector2.removeClass('bg-green text-white');
            selector3.attr('src', '../static/images/arrow.svg');
        }
    }
    else{
        $('#'+head+'_innermenu').removeClass('d-none');
        if(!(selector2.hasClass('bg-green'))){
            selector2.addClass('bg-green text-white');
            selector3.attr('src', '../static/images/whitearrow.svg');
        }
    }
}
function menu_icon(){
    if(($("#menu").is(":visible"))){
        $("#nav_menu").attr('src', '../static/images/close.svg');
        $("#nav_menu").attr('height', '25px');
    }
    else{
        $("#nav_menu").attr('src', '../static/images/menu.svg');
        $("#nav_menu").attr('height', '35px');
    }
}
function openmenu(option_value){
    $("#menu").show();
    for(let i_menu=1; i_menu<=6; i_menu++){
        if(i_menu.toString()===option_value.toString()){
            $(".menu-option-" + i_menu.toString()).attr('class', "menu-option-" +  i_menu.toString() +  " btn btn-block btn-lg bg-green text-white");
        }
        else{
            $(".menu-option-" + i_menu.toString()).attr('class', "menu-option-" +  i_menu.toString() +  " btn btn-block btn-lg text-dark");
        }
    }
    menu_icon();
}
check_menu_id= "";
function togglemenu(param_id){
    if(param_id === 'null'){
        $("#menu").toggle();
        menu_icon();
    }
    else{
        if(param_id.toString()!==check_menu_id.toString()){
            openmenu(param_id);
            check_menu_id= param_id.toString();
        }
        else{
            $("#menu").hide();
            check_menu_id="";
        }
    }
}