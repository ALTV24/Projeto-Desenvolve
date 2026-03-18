function somar(num1, num2) {
    return num1 + num2;
}

function subtrair(num1, num2) {
    return num1 - num2;
}
function multiplicar(num1, num2) {
    return num1 * num2;
}
function dividir(num1, num2) {
    return num1 / num2;
}

function mostrarResultado (num1, num2) {
    console.log(`Soma entre ${num1} e ${num2}: ${somar(num1, num2)}`);
    console.log(`Subtração entre ${num1} e ${num2}: ${subtrair(num1, num2)}`);
    console.log(`Multiplicação entre ${num1} e ${num2}: ${multiplicar(num1, num2)}`);
    console.log(`Divisão entre ${num1} e ${num2}: ${dividir(num1, num2)}`);
}

mostrarResultado(4,2);