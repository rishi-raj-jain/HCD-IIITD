nav= 1;
$(document).ready(function(){
    $(".searchenabled").toggle();
    $("#menu").toggle();
    $("#search").click(function(){
        nav= (nav+1)%2;
        $("#menu").hide();
        if(nav==0){
            $(".searchenabled").toggle();
            $("#searchdisabled").toggle();
            $(".searchdisabled").removeClass("d-md-block");
            $("input").focus();
        }
        else if(nav==1){
            $(".searchenabled").toggle();
            $("#searchdisabled").toggle();
            $(".searchdisabled").addClass("d-md-block");
        }
    });
});
function menu_icon(){
    if(($("#menu").is(":visible"))){
        $("#nav_menu").attr('src', '../static/images/close.jpg');
    }
    else{
        $("#nav_menu").attr('src', '../static/images/menu.svg');
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
    console.log(param_id + ' ' + check_menu_id);
}