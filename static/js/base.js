nav= 1;
$(document).ready(function(){
    $("#menu").toggle();
});
function menu_icon(){
    if(($("#menu").is(":visible"))){
        $("#nav_menu").attr('src', '../static/images/close.svg');
        $("#nav_menu").attr('height', '30px');
    }
    else{
        $("#nav_menu").attr('src', '../static/images/menu.svg');
        $("#nav_menu").attr('height', '35px');
    }
    if($("input").is(":visible")){
        $("input").focus();
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