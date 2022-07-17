
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
    for(let index in list_x_elements){
        list_x_elements[index].style.top = `${initial_top_position[index]}px`;
        list_x_elements[index].style.left = initial_x_left;
    }
    for(let index in list_o_elements){
        list_o_elements[index].style.top = `${initial_top_position[index]}px`;
        list_o_elements[index].style.left = initial_o_left;  
    }
}

for(let index in list_x_elements){
    // Creating a function for each img_x when clicked
    list_x_elements[index].onclick = function(){

            // second click
            if(list_imgx_clicked[index] === true){
                list_imgx_clicked[index] = false
                let position_left = list_x_elements[index].getBoundingClientRect().left;
                let position_top = list_x_elements[index].getBoundingClientRect().top;
                console.log("left ", position_left);
                console.log("top ", position_top);
                list_x_elements[index].style.left = `${verify_position(position_left, position_top)[0]}px`;
                list_x_elements[index].style.top = `${verify_position(position_left, position_top)[1]}px`;

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

function verify_position(position_left, position_top){
    let pos_left = 0;
    let pos_top = 0;
    if(position_left > 300 && position_top > 100){
        pos_left = 500;
        pos_top = 500;
    }else{
        pos_left = 250;
        pos_top = 250;
    }
    console.log(`pos_left: ${pos_left}, pos_top: ${pos_top}`);
    return [pos_left, pos_top];
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
