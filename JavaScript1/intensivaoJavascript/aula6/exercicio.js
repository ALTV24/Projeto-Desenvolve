async function piadaAleatória() {
    const elementoPiada = document.getElementById("piada");
    
    try {
        const resposta = await fetch("https://api.chucknorris.io/jokes/random");
        const dados = await resposta.json();
        elementoPiada.textContent = dados.value;
    } catch (erro) {

        elementoPiada.textContent = "Erro ao carregar a piada, infelizmente não foi dessa vez que você aprenderá sobre a verdadeira essência masculina. 😢";
        console.error(erro);

    }
}