const input = document.getElementById("nome");
const resultado = document.getElementById("resultado");
const lista = document.getElementById("listaCurtidas");
const titulo = document.getElementById("titulo");
const limparStorage = document.getElementById("limparStorage");

let listaCurtidas = JSON.parse(localStorage.getItem("curtidas")) || [];

function salvarCurtidas() {
    localStorage.setItem("curtidas", JSON.stringify(listaCurtidas));
}

function curtir() {
    const nome = input.value.trim();

    if (nome === "") return;

    if (listaCurtidas.includes(nome)) {
        alert("Esse nome já curtiu!");
        input.value = "";
        return;
    }

    listaCurtidas.push(nome);
    salvarCurtidas();
    atualizarLista();
    atualizarContador();
    input.value = "";
    console.log("clicou");
}

function atualizarLista() {
    lista.innerHTML = "";

    listaCurtidas.forEach((nome) => {
        const li = document.createElement("li");
        li.textContent = nome;
        lista.appendChild(li);
    });
}

function atualizarContador() {
    if (listaCurtidas.length === 0) {
        resultado.textContent = "Ninguém curtiu";
    } 
    else if (listaCurtidas.length === 1) {
        resultado.textContent = `${listaCurtidas[0]} curtiu`;
    } 
    else if (listaCurtidas.length === 2) {
        resultado.textContent = `${listaCurtidas[0]} e ${listaCurtidas[1]} curtiram`;
    } 
    else {
        resultado.textContent = `${listaCurtidas[0]}, ${listaCurtidas[1]} e mais ${listaCurtidas.length - 2} pessoas curtiram`;
    }
}

limparStorage.addEventListener('click', () => {
  console.log("clicou para limpar");
  listaCurtidas = [];
  localStorage.removeItem('dadosUsuario')
  localStorage.removeItem('curtidas');
  atualizarLista();
  atualizarContador()
})

atualizarLista();
atualizarContador();    

