 async function buscarUsuarios() {
      const termo = document.getElementById('busca').value;
      const lista = document.getElementById('lista');
      const mensagem = document.getElementById('mensagem');

      lista.innerHTML = '';
      mensagem.textContent = '';

      if (!termo) return;

      try {
        const resposta = await fetch(`https://api.github.com/search/users?q=${termo}`);
        const dados = await resposta.json();

        if (dados.items.length === 0) {
          mensagem.textContent = 'Não foram encontrados usuários para esta pesquisa';
          return;
        }

        dados.items.forEach(usuario => {
          const li = document.createElement('li');

          li.innerHTML = `
            <img src="${usuario.avatar_url}" alt="avatar">
            <a href="${usuario.html_url}" target="_blank">${usuario.login}</a>
          `;

          lista.appendChild(li);
        });
        } catch (erro) {
          mensagem.textContent = 'Erro ao buscar usuários';
        }
      }