const heroi = {
    nome: "Beatryz Pina",
    classe: "Engenheira de Software",
    nivel: 1,
    xp: 0
};

function atualizarInterface() {
    document.getElementById("hero-nome").innerText = heroi.nome;
    document.getElementById("hero-classe").innerText = heroi.classe;
    document.getElementById("hero-nivel").innerText = heroi.nivel;
    document.getElementById("hero-xp").innerText = heroi.xp;
}

document.getElementById("btn-xp").addEventListener("click", () => {
    heroi.xp += 20;
    
    if (heroi.xp >= 100) {
        heroi.nivel += 1;
        heroi.xp = 0;
        alert(`Parabéns! Você evoluiu para o nível ${heroi.nivel}!`);
    }
    
    atualizarInterface();
});

const formulario = document.querySelector("#contato form");
formulario.addEventListener("submit", (event) => {
    event.preventDefault(); 
    
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const mensagemErro = document.createElement("p");
    
    if (nome === "" || email === "") {
        alert("Erro: Nome e Email são obrigatórios!");
    } else {
        alert("Sucesso! Sua mensagem foi enviada.");
        formulario.reset();
    }
});

async function buscarDadosExtras() {
    try {
        const resposta = await fetch('https://jsonplaceholder.typicode.com/users/1');
        const dados = await fetch('https://api.github.com/users/beatryzpina'); // Exemplo 
        console.log("Dados da API carregados com sucesso.");
    } catch (erro) {
        console.error("Erro ao buscar dados da API:", erro);
    }
}

atualizarInterface();
buscarDadosExtras();