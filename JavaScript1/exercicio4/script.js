const input = document.getElementById("descricaoTarefa");
const button = document.getElementById("adicionarTarefa");
const lista = document.getElementById("listaTarefas");

let taskList = JSON.parse(localStorage.getItem("tasks")) || [];

button.addEventListener("click", () => {
    const descricao = input.value.trim();

    if (descricao === "") return;

    const task = {
        description: descricao,
        status: false
    };

    taskList.push(task);
    salvar();
    input.value = "";
    renderTasks();
});

function salvar() {
    localStorage.setItem("tasks", JSON.stringify(taskList));
}

function renderTasks() {
    lista.innerHTML = "";

    taskList.forEach((task, index) => {
        const li = document.createElement("li");
        li.classList.add("task-item");

        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.checked = task.status;
        checkbox.classList.add("task-checkbox");

        checkbox.addEventListener("change", () => {
            task.status = checkbox.checked;
            salvar();
            atualizarContador();
        });

        const label = document.createElement("label");
        label.textContent = task.description;
        label.classList.add("task-description");

        // botão de excluir
        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "🗑";
        deleteBtn.classList.add("delete-btn");

        deleteBtn.addEventListener("click", () => {
            taskList.splice(index, 1);
            salvar();
            renderTasks();
            atualizarContador();
        });

        // animação
        li.style.opacity = "0";
        li.style.transform = "translateY(10px)";

        setTimeout(() => {
            li.style.transition = "0.6s";
            li.style.opacity = "1";
            li.style.transform = "translateY(0)";
        }, 50);

        li.appendChild(checkbox);
        li.appendChild(label);
        li.appendChild(deleteBtn);

        lista.appendChild(li);
    });
}

function atualizarContador() {
    const total = taskList.length;
    const concluidas = taskList.filter(task => task.status).length;
    document.getElementById("contador").textContent = `Total: ${total} | Concluídas: ${concluidas}`;
}
