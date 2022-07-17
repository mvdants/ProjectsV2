
// Getting the "mira" element
let mira = document.querySelector(".mira");

// Geting the button element
let btn = document.querySelector(".btn");

// Getting all images elements
const imgs_x = document.querySelectorAll(".x");
const imgs_o = document.querySelectorAll(".o"); 

// Creating a list of elements of images X and O
let list_x_elements = [];
let list_o_elements = [];

// Initializing the list of imgs that was clicked
let list_imgx_clicked = [false, false, false, false, false];
let list_imgo_clicked = [false, false, false, false, false];

// Inserting in the list the elements of x
for(let element of imgs_x){
    list_x_elements.push(element);
}

// Inserting in the list the elements of o
for(let element of imgs_o){
    list_o_elements.push(element);
}

// Getting initial values
const initial_top_position = [50, 175, 300, 425, 550];
const initial_x_left = "10%";
const initial_o_left = "80%";

btn.onclick = function(){  
    for(let element of list_x_elements){
        element.style.top = `${initial_top_position[list_x_elements.indexOf(element)]}px`;
        element.style.left = initial_x_left;
    }
    for(let element of list_o_elements){
        element.style.top = `${initial_top_position[list_o_elements.indexOf(element)]}px`;
        element.style.left = initial_o_left;  
    }
}

for(let index in list_x_elements){
    // Creating a function for each img_x when clicked
    list_x_elements[index].onclick = function(){

            // second click
            if(list_imgx_clicked[index] === true){
                list_imgx_clicked[index] = false
                set_automatic_position(list_x_elements[index]);

            // first click
            }else{
                list_imgx_clicked[index] = true;
            }
        }

    // Creating a function for each img_o when clicked
    list_o_elements[index].onclick = function(){

        // second clicks
        if(list_imgo_clicked[index] === true){
            list_imgo_clicked[index] = false;
            set_automatic_position(list_o_elements[index]);
        
        // first click
        }else{
            list_imgo_clicked[index] = true;
        }
    }
}


// Ading the mousemove action to the page
document.addEventListener("mousemove", function(event){
    for(let index in list_x_elements){

        // Verifing if the img x was clicked before
        if(list_imgx_clicked[index] === true){
            list_x_elements[index].style.top = event.clientY + "px";
            list_x_elements[index].style.left = event.clientX + "px";

        // Verifing if the img o was clicked before
        }else if(list_imgo_clicked[index] === true){
            list_o_elements[index].style.top = event.clientY + "px";
            list_o_elements[index].style.left = event.clientX + "px";
        }
    }
});

function verify_position_left(position_left){
    let pos_left = 0;
    if(position_left > 300 && position_left < 500){
        pos_left = 350;
    }else if(position_left > 500 && position_left < 700){
        pos_left = 550;
    }else if(position_left > 700 && position_left < 900){
        pos_left = 750;
    }else{
        pos_left = position_left;
    }
    console.log(`pos_left: ${pos_left}`);
    return pos_left;
}

function verify_position_top(position_top){
    let pos_top = 0;
    if(position_top > 100 && position_top < 300){
        pos_top = 150;
    }else if(position_top > 300 && position_top < 500){
        pos_top = 350;
    }else if(position_top > 500 && position_top < 700){
        pos_top = 550;
    }else{
        pos_top = position_top;
    }
    console.log(`pos_top: ${pos_top}`);
    return pos_top;
}

function set_automatic_position(element){
    let position_left = element.getBoundingClientRect().left;
    let position_top = element.getBoundingClientRect().top;
    // console.log("left ", position_left);
    // console.log("top ", position_top);
    element.style.left = `${verify_position_left(position_left)}px`;
    element.style.top = `${verify_position_top(position_top)}px`;
}

// use after ...
function make_mira_element(element){
    return {
        element : element,
        init_left_pos: element.getBoundingClientRect().left,
        init_top_pos: element.getBoundingClientRect().top,
        clicked: false,
        blocked: false
    }
}
