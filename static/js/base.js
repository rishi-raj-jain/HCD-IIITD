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
    // console.log(option_value.toString()+"HI");
    for(let i_menu=1; i_menu<=6; i_menu++){
        if(i_menu.toString()===option_value.toString()){
            // console.log(i_menu.toString()+"HI");
            $(".menu-option-" + i_menu.toString()).attr('class', "menu-option-" +  i_menu.toString() +  " btn btn-block btn-lg bg-green text-white");
        }
        else{
            $(".menu-option-" + i_menu.toString()).attr('class', "menu-option-" +  i_menu.toString() +  " btn btn-block btn-lg text-dark");
        }
    }
    menu_icon();
}
function togglemenu(){
    $("#menu").toggle();
    if(($("#menu").is(":visible"))){
        openmenu('4');
    }
    menu_icon();
}