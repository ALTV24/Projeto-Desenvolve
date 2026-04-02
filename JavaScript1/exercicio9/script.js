async function fetchCat() {
        const response = await fetch('https://api.thecatapi.com/v1/images/search');
        const data = await response.json();
        document.getElementById('cat-image').src = data[0].url;
    }
    fetchCat();

    function curtirPost() {
        alert('Você curtiu este gatinho!');
    }

let posts = [];

async function criarPost() {
    const texto = document.getElementById("Postagens").value;
    const response = await fetch('https://api.thecatapi.com/v1/images/search');
    const data = await response.json();
    const novoPost = {
    data: new Date(),
    usuario: "@cat_lover_br",
    avatar: `https://i.pravatar.cc/150?img=${Math.floor(Math.random() * 70)}`,
    texto: texto,
    imagem: data[0].url,
    likes: 0
};
    posts.unshift(novoPost); // mais recente primeiro
    renderPosts();
}

function renderPosts() {
    const container = document.getElementById("feed");
    container.innerHTML = "";
    posts.forEach((post, index) => {
        container.innerHTML += `
            <div class="post-container">
                <div class="user-info">
                    <img src="${post.avatar}" class="avatar">
                    <span class="username">${post.usuario}</span>
                </div>
                <p>${post.texto}</p>
                <img src="${post.imagem}" class="post-image">
                <button onclick="curtir(${index})">
                    Curtir (${post.likes})
                </button>
            </div>
        `;
    });
}

function curtir(index) {
    posts[index].likes++;
    renderPosts();
}
document.getElementById("Postagens").value = "";