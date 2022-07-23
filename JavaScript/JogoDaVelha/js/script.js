
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
        locked: false,
        blocked: true
    }
}

// Allowing the x to play first
allow_player(list_x_elements);

// Attribuate to the button function click -> set initial positions
btn.onclick = () => {
    unlock_elements(list_x_elements, list_o_elements);
    unclick_elements(list_x_elements, list_o_elements);
    set_initial_positions(list_x_elements, list_o_elements);  
}

// Attributing a function for each img element when clicked
set_imgs_onclick_function(list_x_elements, list_o_elements);



function set_initial_positions(...list_of_element){
    for(list of list_of_element){
        list.forEach((object) => {
            object.element.style.top = `${object.init_top_pos}px`;
            object.element.style.left = `${object.init_left_pos}px`;
        });
    }      
}

function unlock_elements(...list_of_elements){
    for(lista of list_of_elements){
        lista.forEach((object)=>{
            object.locked = false;
        });
    }
}

function unclick_elements(...list_of_elements){
    for(lista of list_of_elements){
        lista.forEach((object)=>{
            object.clicked = false;
        });
    }
}

function set_imgs_onclick_function(...list_of_elements){
    for(lista of list_of_elements){
        lista.forEach((object)=>{
            object.element.onclick = () => {
                verify_second_click(object);
            }
        });
    }
}

function verify_second_click(object){
    if(object.clicked === true){
        // second click
        object.clicked = false;
        let [locked_top, locked_left] = set_automatic_position(object);

        // denied move an other time the object
        if (locked_left===true && locked_top===true){
            object.locked = true;
            // Verify if x won
            let numbers_x = count_number_objects_moved(list_x_elements);
            if(numbers_x >= 3){  // start to verify if an user win the game
                console.log("verify 'x'");
                let victory_x = verify_victory(list_x_elements);
                if(victory_x === true){
                    console.log("'X' ganhou o jogo");
                }
            }

            // Verify if o won
            let numbers_o = count_number_objects_moved(list_o_elements);
            if(numbers_o >= 3){  // start to verify if an user win the game
                console.log("verify 'o'");
                let victory_o = verify_victory(list_o_elements);
                if(victory_o === true){
                    console.log("'O' ganhou o jogo");
                }
            }

            // if the first is denied, all of them is also denied
            if(list_x_elements[0].blocked === false){
                allow_player(list_o_elements);
                deny_player(list_x_elements);
            }else{
                allow_player(list_x_elements);
                deny_player(list_o_elements);
            }
            
        }

    }else{
        // first click
        if(object.blocked === false){
            object.clicked = true;
        }   
    }
}

function allow_player(list_of_elements){
    list_of_elements.forEach((object)=>{
        object.blocked = false;
    });
}

function deny_player(list_of_elements){
    list_of_elements.forEach((object)=>{
        object.blocked = true;
    });
}

function set_automatic_position(object){
    let confirmed_left, confirmed_top;
    let position_left = object.element.getBoundingClientRect().left;
    let position_top = object.element.getBoundingClientRect().top;
    [object.element.style.left, confirmed_left] = verify_position_left(position_left);
    [object.element.style.top, confirmed_top] = verify_position_top(position_top);
    return [confirmed_top, confirmed_left];

}

function verify_position_left(position_left){
    let pos_left = 0;
    let confirmed = true;
    if(position_left > 375 && position_left < 575){
        pos_left = 475;
    }else if(position_left > 575 && position_left < 775){
        pos_left = 675;
    }else if(position_left > 775 && position_left < 975){
        pos_left = 875;
    }else{
        pos_left = position_left;
        confirmed = false;
    }return [pos_left + "px", confirmed];
}

function verify_position_top(position_top){
    let pos_top = 0;
    let confirmed = true;
    if(position_top > 100 && position_top < 225){
        pos_top = 125;
    }else if(position_top > 225 && position_top < 400){
        pos_top = 325;
    }else if(position_top > 400 && position_top < 550){
        pos_top = 525;
    }else{
        pos_top = position_top;
        confirmed = false;
    }return [pos_top + "px", confirmed];
}

function count_number_objects_moved(list_of_elements){
    let object_moved = 0;
    let list_objects_moved = [];
    list_of_elements.forEach((object, index) => {
        if(object.locked === true){
            list_objects_moved.push(object);
            object_moved += 1;
        }
    }); return object_moved;
}

function verify_victory(list_of_elements){

    // creating a new list to make easier to understand the code
    let left = [];
    let top = [];

    // Get objects positions of the images that were moved
    list_of_elements.forEach((object)=>{
        if(object.locked === true){
            left.push(object.element.getBoundingClientRect().left);
            top.push(object.element.getBoundingClientRect().top);
        }
    });
    let left_sorted = left.sort((a, b) => a - b);
    let top_sorted = top.sort((a, b) => a - b);
     // Verify positions of the images and return if the user won or not
    
    for(let i=0;i<left.length - 2;i++){
        if(left_sorted[i] === left_sorted[i+1] && left_sorted[i+1] === left_sorted[i+2]){
            console.log("win column");
            return true;
        }else if(top_sorted[i] === top_sorted[i+1] && top_sorted[i+1] === top_sorted[i+2]){
            console.log("win row");
            return true;
        }
    }
    // Filtering the positions to get only the validated diagonal positions
    let diagonal = [];
    for(let i=0;i<left.length;i++){
        if((left[i] === 475 && top[i] === 125) ||
           (left[i] === 675 && top[i] === 325) ||
           (left[i] === 875 && top[i] === 525) ||
           (left[i] === 475 && top[i] === 525) ||
           (left[i] === 875 && top[i] === 125)
        ){
            diagonal.push([left[i], top[i]]);
        }
    }
    
    // if we have more or equal then 3 diagonal positions, we can maybe win the game
    if(diagonal.length>=3){
        console.log("diagonal > 3");
        console.log(diagonal);
        for(let i=0; i<diagonal.length - 2; i++){
            // Mathematical validation to certify if 3 points are aligned on the space 
            let a = (Math.abs(diagonal[i][0] - diagonal[i+1][0]))/(Math.abs(diagonal[i][1] - diagonal[i+1][1]));
            let b = (Math.abs(diagonal[i+1][0] - diagonal[i+2][0]))/(Math.abs(diagonal[i+1][1] - diagonal[i+2][1]));
            let c = (Math.abs(diagonal[i][0] - diagonal[i+2][0]))/(Math.abs(diagonal[i][1] - diagonal[i+2][1]));
            console.log(a, b, c);
            if(a === 1 && b === 1 && c === 1){
                console.log("win diagonal");
                return true;
            }
        }
    }
}

// Ading the mousemove action to the page
document.addEventListener("mousemove", (event) => {
    set_new_position(event, list_x_elements, list_o_elements);
});

function set_new_position(event, ...list_of_elements){
    for(lista of list_of_elements){
        lista.forEach((object)=>{
            if(object.locked === false){
                if(object.clicked === true){
                    update_position(event, object);
                }
            }
        });
    }
}

function update_position(event, object){
    object.element.style.top = event.clientY - object.offsetY + "px";
    object.element.style.left = event.clientX - object.offsetX + "px";
    }
