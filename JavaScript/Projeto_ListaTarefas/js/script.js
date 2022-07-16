
// Referenciando o input
let inp = document.querySelector("input[name=tarefa]");

// Referenciando o botao
let btn = document.querySelector("#botao");

// Referenciando a lista de itens
let lista = document.querySelector("#lista");

// Pegando a div card
let card = document.querySelector(".card");

let tasks = JSON.parse(localStorage.getItem("tarefas")) || [];

function renderizarTarefas(){

    // Limpar a listagem de itens antes de renderizar novamente a tela
    lista.innerHTML = "";

    for(t of tasks){
        // Criar um elemento da lista
        let itemLista = document.createElement("li");

        // adicionar a classe no item da lista
        itemLista.setAttribute("class", "list-group-item list-group-item-action")

        itemLista.onclick = function(){
            deletarTarefa(this);
        }

        // Criar texto
        let itemTexto = document.createTextNode(t);

        // Adicionar o texto no item da lista
        itemLista.appendChild(itemTexto);

        // Adicionar o item da lista na lista
        lista.appendChild(itemLista);
    }
}

// Executndo a funcao para renderizar as tarefas
renderizarTarefas();


// 1) Precisamos "escutar" o evento do click no botao
btn.onclick = function(){
    // 2) Preciamos capturar o valor digitado pelo usuario no input
    let novaTarefa = inp.value;

    if(novaTarefa !== ""){
        // 3) Precisamos atualizar a nova tarefa na lista ( array ) de tarefas
        tasks.push(novaTarefa);

        // 4) renderizar a tela
        renderizarTarefas();

        // 5) Limpar o input
        inp.value = "";

        // Limpando os spans de erro
        removerSpans();

        // Salva os novos dados no banco de dados
        salvarDadosNoStorage();

    }else{
        // Limpando os spans de erro
        removerSpans();

        // criando elemento span
        let span = document.createElement("span");

        // atribuindo uma classe ao elemento
        span.setAttribute("class", "alert alert-warning");

        // criando uma mensagem de texto
        let msg = document.createTextNode("Voce precisa informar a tarefa!");

        // elemento span adquirindo a mensagem
        span.appendChild(msg);

        // div card adquirindo o elemento span
        card.appendChild(span);
    }
    
}

function removerSpans(){

    // Recuperando os elementos spans
    let spans = document.querySelectorAll("span");

    // removendo os spans da div card
    for(let i=0; i<spans.length; i++){
        card.removeChild(spans[i]);
    }
}

function deletarTarefa(task){
    // Remove a tarefa do array
    tasks.splice(tasks.indexOf(task.textContent), 1);

    // Renderizar novamente a tela
    renderizarTarefas();

    // Salva os novos dados no banco de dados
    salvarDadosNoStorage();
}


function salvarDadosNoStorage(){
    // Todo navegador Web possui essa capacidade
    localStorage.setItem("tarefas", JSON.stringify(tasks));
}
