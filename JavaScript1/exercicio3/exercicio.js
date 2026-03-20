function calcularTempoRestante(dataFutura){
    const agora = new Date().getTime();
    const diferenca = dataFutura - agora;
    const dias = Math.floor(diferenca / (1000 * 60 * 60 * 24));
    const horas = Math.floor((diferenca % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutos = Math.floor((diferenca % (1000 * 60 * 60)) / (1000 * 60));
    const segundos = Math.floor((diferenca % (1000 * 60)) / 1000);
    return { dias, horas, minutos, segundos };
}

const dataFutura = new Date("2026-12-31T23:59:59");
function atualizarTemporizador() {
    const tempoRestante = calcularTempoRestante(dataFutura);
    document.getElementById("dias").textContent = `${tempoRestante.dias} dias`;
    document.getElementById("horas").textContent = `${tempoRestante.horas} horas`;
    document.getElementById("minutos").textContent = `${tempoRestante.minutos} minutos`;
    document.getElementById("segundos").textContent = `${tempoRestante.segundos} segundos`;
}

atualizarTemporizador();
setInterval(atualizarTemporizador, 1000);
