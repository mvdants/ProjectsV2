
let mira = document.querySelector(".mira");
let devmira = document.querySelector(".game");

devmira.mousedown(function(event){
    switch(event.which) {
        case 1:
            $('.game').html('Left Mouse button pressed.');
          break;
        case 2:
            $('.game').html('Middle Mouse button pressed.');
          break;
        case 3:
            $('.game').html('Right Mouse button pressed.');
          break;
        default:
            $('.game').html('You have a strange Mouse!');
      }
});

// console.log(`${event.pageX}, ${event.pageY}`);

// Creating a list of elements of images X
let list_x_elements = [];

// inserting in the list the elements of img
for(let i=0; i<document.querySelectorAll(".x").length; i++){
    list_x_elements.push(document.querySelector(`#x${i+1}`));
}

// 
for(let i=0; i<list_x_elements.length; i++){
    list_x_elements[i].onclick = function(){

    }
}

// Creating a list of elements of images X
let list_o_elements = [];

// inserting in the list the elements of img
for(let i=0; i<document.querySelectorAll(".o").length; i++){
    list_o_elements.push(document.querySelector(`#o${i+1}`));
}
