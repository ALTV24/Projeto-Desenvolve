function processarNomes(lista) {
    const semDuplicatas = [...new Set(lista)];
    const filtrados = semDuplicatas.filter(nome => nome.length >= 10);
    const ordenados = filtrados.sort((a, b) => a.localeCompare(b));
    return ordenados;
}
const nomes = [ '"Ana Silva", "João Pereira", "Maria Souza", "João Pereira", "Pedro Oliveira", "José Santos", "Ana Silva", "Gabriela Rodrigues"'

];

const resultados = processarNomes(nomes);
console.log(resultados);