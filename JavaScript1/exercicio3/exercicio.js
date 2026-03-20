function calcularTempoRestante(dataFutura) {
    const agora = new Date();
    const diferenca = dataFutura - agora;
    const dias = Math.floor(diferenca / (1000 * 60 * 60 * 24));
    const horas = Math.floor((diferenca % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutos = Math.floor((diferenca % (1000 * 60 * 60)) / (1000 * 60));
    const segundos = Math.floor((diferenca % (1000 * 60)) / 1000);
    return { dias, horas, minutos, segundos };
}

const atualizarTemporizador = () => {
    const dataFutura = new Date("2026-12-31T23:59:59");
    const tempoRestante = calcularTempoRestante(dataFutura);
    const elementoTemporizador = document.getElementById("temporizador");
    elementoTemporizador.textContent = (`Tempo restante: ${tempoRestante.dias} dias, ${tempoRestante.horas} horas, ${tempoRestante.minutos} minutos, ${tempoRestante.segundos} segundos`);
}

atualizarTemporizador();
setInterval(atualizarTemporizador, 1000);
