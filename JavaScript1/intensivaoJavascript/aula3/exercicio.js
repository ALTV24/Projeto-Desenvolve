function classificarIdade(anoNascimento) {
    const anoAtual = new Date().getFullYear();
    const idade = anoAtual - anoNascimento;
    if (idade >=18) {
        return 'Maior de idade';
    } else {
        return 'Menor de idade';
    }
}

const anos = [1995, 2008, 2001, 2010];

for (let i=0; i < anos.length; i++){
    const resultado = classificarIdade(anos[i]);
    console.log(`Ano: ${anos[i]} - ${resultado}`);
}