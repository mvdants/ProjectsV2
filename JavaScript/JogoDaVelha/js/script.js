
// Getting the "mira" element
let mira = document.querySelector(".mira");

// Getting the position of the "mira" img
let mira_width = mira.getBoundingClientRect().width;
let mira_height = mira.getBoundingClientRect().height;

// Creating a list of elements of images X and O
let list_x_elements = [];
let list_o_elements = [];

// Inserting in the list the elements of img
for(let i=0; i<document.querySelectorAll(".x").length; i++){
    // As both have the same number of elements
    list_x_elements.push(document.querySelector(`#x${i+1}`));
    list_o_elements.push(document.querySelector(`#o${i+1}`));
}

// Initializing the list of imgs that was clicked
let list_imgx_clicked = [false, false, false, false, false]
let list_imgo_clicked = [false, false, false, false, false]

// Creating a function for each img_x when clicked
for(let i=0; i<list_x_elements.length; i++){
    list_x_elements[i].onclick = function(event){
            if(list_imgx_clicked[i] === true){
                list_imgx_clicked[i] = false
            }else{
                list_imgx_clicked[i] = true
            }
        }
}

// Creating a function for each img_o when clicked
for(let i=0; i<list_o_elements.length; i++){
    list_o_elements[i].onclick = function(event){
            if(list_imgo_clicked[i] === true){
                list_imgo_clicked[i] = false
            }else{
                list_imgo_clicked[i] = true
            }
        }
}

// Ading the mousemove action to the page
document.addEventListener("mousemove", function(event){
    for(let i=0; i<list_x_elements.length;i++){

        // Verifing if the img x was clicked before
        if(list_imgx_clicked[i] === true){
            list_x_elements[i].style.top = event.clientY + "px";
            list_x_elements[i].style.left = event.clientX + "px";

        // Verifing if the img o was clicked before
        }else if(list_imgo_clicked[i] === true){
            list_o_elements[i].style.top = event.clientY + "px";
            list_o_elements[i].style.left = event.clientX + "px";
        }
    }
});
