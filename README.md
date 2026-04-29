## System Calculator
- Calculadora web desenvolvida com Python(Flask) no Back-end e HTML/CSS/JS no Front-end.

## Estrutura
system_calculator/
├── main.py
├── templates/
│   └── index.html
└── static/
├── css/
│   └── style.css
└── js/
└── script.js

## Como Funciona 
1. O usuário clica nos botões → JS monta a expressão
2. o clicar em `=` → JS envia a expressão para o Flask via `fetch`
3. Flask valida e calcula → devolve o resultado em JSON
4. JS exibe o resultado na tela

## Como rodar 
1. pip install flask
2. python main.py

Acesse : 'http://127.0.0.1:5000'

## Tecnologias 

- Back-End | Python + Flask |
- Front-End | HTML + CSS |
- Comunicação | Javascript (fetch) |
