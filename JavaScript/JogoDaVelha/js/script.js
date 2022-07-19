
// Getting the "mira" element
let mira = document.querySelector(".mira");

// Geting the button element
let btn = document.querySelector(".btn");

// Getting all images elements
const imgs_x = document.querySelectorAll(".x");
const imgs_o = document.querySelectorAll(".o"); 

function create_list_of_elements(list_of_elements){
    let lista = [];
    for(let element of list_of_elements){
        lista.push(make_mira_element(element));
    }
    return lista;
}

// Creating a list of elements of images X and O
let list_x_elements = create_list_of_elements(imgs_x);
let list_o_elements = create_list_of_elements(imgs_o);

// Attribuate to the button function click -> set initial positions
btn.onclick = () => {set_initial_positions(list_x_elements, list_o_elements);}

function set_initial_positions(...list_of_element){
    list_of_element.forEach((element) => {
        element.element.style.top = `${element.init_top_pos}px`;
        element.element.style.left = `${element.init_left_pos}px`;
    });
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
    // console.log(event.clientX, event.clientY);
    for(let index in list_x_elements){

        // Verifing if the img x was clicked before
        if(list_imgx_clicked[index] === true){
            list_x_elements[index].style.top = event.clientY - offsetY + "px";
            list_x_elements[index].style.left = event.clientX - offsetX + "px";

        // Verifing if the img o was clicked before
        }else if(list_imgo_clicked[index] === true){
            list_o_elements[index].style.top = event.clientY - offsetY + "px";
            list_o_elements[index].style.left = event.clientX - offsetX + "px";
        }
    }
});

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
    }
    return pos_left;
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
    }
    
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
        offsetX: element.getBoundingClientRect().width/2,
        offsetY: element.getBoundingClientRect().height/2,
        clicked: false,
        locked: false
    }
}
