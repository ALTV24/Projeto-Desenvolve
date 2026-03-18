const relatorio = {
    titulo: "Dom Quixote",
    autor: "Miguel de Cervantes",
    anoPublicacao: 1605
};

const {titulo, autor, anoPublicacao} = relatorio;
console.log('Título:', titulo);
console.log('Autor:', autor);

const metadados = {
    status: "Em revisão",
    revisão: 3
};

const relatorioCompleto = {...relatorio,...metadados};
console.log(relatorioCompleto);