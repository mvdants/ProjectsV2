
// Getting the "mira" element
let mira = document.querySelector(".mira");

// Geting the button element
let btn = document.querySelector(".btn");

// Getting all images elements
const imgs_x = document.querySelectorAll(".x");
const imgs_o = document.querySelectorAll(".o"); 

// Creating a list of elements of images X and O
let list_x_elements = create_list_of_elements(imgs_x);
let list_o_elements = create_list_of_elements(imgs_o);
function create_list_of_elements(list_of_elements){
    let lista = [];
    for(let element of list_of_elements){
        lista.push(make_mira_element(element));
    }return lista;
}

// Makin the object that we will work with
function make_mira_element(element){
    return {
        element : element,
        init_left_pos: element.getBoundingClientRect().left,
        init_top_pos: element.getBoundingClientRect().top,
        offsetX: element.getBoundingClientRect().width/2,
        offsetY: element.getBoundingClientRect().height/2,
        clicked: false,
        locked: false
    }
}

// Attribuate to the button function click -> set initial positions
btn.onclick = () => {
   set_initial_positions(list_x_elements, list_o_elements);
}

function set_initial_positions(...list_of_element){
    // console.log(list_of_element);
    for(list of list_of_element){
        list.forEach((object) => {
            object.element.style.top = `${object.init_top_pos}px`;
            object.element.style.left = `${object.init_left_pos}px`;
        });
    }      
}

// Attributing a function for each img element when clicked
list_x_elements.forEach((object) => {
    object.element.onclick = () => {
        verify_second_click(object);
    }
});

// Attributing a function for each img element when clicked
list_o_elements.forEach((object) => {
    object.element.onclick = () => {
        verify_second_click(object);
    }
});

function verify_second_click(object){
    if(object.clicked === true){
        // second click
        object.clicked = false;
        set_automatic_position(object);
        
    }else{
        // first click
        object.clicked = true;
    }
}

function set_automatic_position(object){
    let position_left = object.element.getBoundingClientRect().left;
    let position_top = object.element.getBoundingClientRect().top;
    // console.log("left ", position_left);
    // console.log("top ", position_top);
    object.element.style.left = `${verify_position_left(position_left)}px`;
    object.element.style.top = `${verify_position_top(position_top)}px`;
}

function verify_position_left(position_left){
    console.log(`pos_left: ${position_left}`);
    let pos_left = 0;
    if(position_left > 375 && position_left < 575){
        pos_left = 475;
    }else if(position_left > 575 && position_left < 775){
        pos_left = 675;
    }else if(position_left > 775 && position_left < 975){
        pos_left = 875;
    }else{
        pos_left = position_left;
    }return pos_left;
}

function verify_position_top(position_top){
    console.log(`pos_top: ${position_top}`);
    let pos_top = 0;
    if(position_top > 100 && position_top < 225){
        pos_top = 125;
    }else if(position_top > 225 && position_top < 400){
        pos_top = 325;
    }else if(position_top > 400 && position_top < 550){
        pos_top = 525;
    }else{
        pos_top = position_top;
    }return pos_top;
}

// Ading the mousemove action to the page
document.addEventListener("mousemove", function(event){
        list_x_elements.forEach((object) => {
            if(object.clicked === true){
                update_position(event, object);
                object.locked = true;
            }else{
                
            }
        });

        list_o_elements.forEach((object) => {
            if(object.clicked === true){
                update_position(event, object);
                object.locked = true;
            }
        });
    });

function update_position(event, object){
    object.element.style.top = event.clientY - object.offsetY + "px";
    object.element.style.left = event.clientX - object.offsetX + "px";
    }
