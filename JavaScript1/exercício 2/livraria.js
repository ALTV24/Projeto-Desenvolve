const estoque = [
    {id: 1234, titulo: "A Menina que Roubava Livros", autor: "Markus Zusak", quantidade: 3},
    {id: 5678, titulo: "Como Eu Era Antes de Você", autor: "Jojo Moyes", quantidade: 5},
    {id: 9012, titulo: "O Pequeno Príncipe", autor: "Antoine de Saint-Exupéry", quantidade: 25}
];

const  adicionarLivro = (id, titulo, autor, quantidade) => {
    const existe = estoque.find(livro => livro.id === id);
    if (existe) {
        console.log('Livro com ID já adicionado no estoque')
    } else {
        estoque.push({id, titulo, autor, quantidade});
    }
};

const removerLivro = (id) => {
    const index = estoque.findIndex(livro => livro.id === id);
    if (index !== -1) {
        estoque.splice(index, 1);
    }
}

const atualizarQuantidade = (id, novaQuantidade) => {
    const livro = estoque.find(livro => livro.id === id);
    if (livro) {
        livro.quantidade = novaQuantidade;
    }
}

const listarLivros = () => {
    estoque.forEach(livros => {
        console.log('ID:', livros.id, 'Título:', livros.titulo, 'Autor:', livros.autor, 'Quantidade:', livros.quantidade);
    })
}

listarLivros();