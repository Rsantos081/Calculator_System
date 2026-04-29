let expressao = '';

// Adiciona número ou operador na expressão
function adicionar(valor) {
    expressao += valor;
    document.getElementById('expressao').textContent = expressao;
}

// Apaga o último caractere
function apagar() {
    expressao = expressao.slice(0, -1);
    document.getElementById('expressao').textContent = expressao;
}

// Limpa tudo
function limpar() {
    expressao = '';
    document.getElementById('expressao').textContent = '';
    document.getElementById('resultado').textContent = '0';
}

// Envia a expressão pro Python e exibe o resultado
async function calcular() {
    if (!expressao) return;

    const resposta = await fetch('/calcular', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ expressao: expressao })
    });

    const dados = await resposta.json();

    if (dados.erro) {
        document.getElementById('resultado').textContent = dados.erro;
    } else {
        document.getElementById('resultado').textContent = dados.resultado;
        expressao = String(dados.resultado);
        document.getElementById('expressao').textContent = '';
    }
}