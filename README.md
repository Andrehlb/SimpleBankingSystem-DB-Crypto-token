# Sistema Bancário (Bank System)

## Descrição do Projeto
Este projeto é um sistema bancário simples que permite ao usuário realizar operações básicas como depósitos, saques e visualização de extrato.

## Funcionalidades
1. **Depósito**: O usuário pode depositar qualquer valor positivo na conta. Todos os depósitos são registrados e exibidos no extrato.
2. **Saque**: O usuário pode realizar até 3 saques por dia com um limite máximo de R$ 500,00 por saque. Se o usuário não tiver saldo suficiente, será exibida uma mensagem informando que o saque não é possível. Todos os saques são registrados e exibidos no extrato.
3. **Extrato**: O usuário pode visualizar todas as transações realizadas na conta, incluindo depósitos e saques. O saldo atual da conta também é exibido.
4. **Menu de opções**: o usuário terá um menu com 4 opções:
```
1. Depositar
2. Sacar
3. Ver extrato
4. Sair
```
Acima do menu será exibida a mensagem com o saldo atualizado do usuário. <br>
Caso o usuário digite algo diferente das opções do menu, uma mensagem de alerta para reafzer a operação será exibida.
Será exibido, a partir do primeiro saue, um aviso sobre o número de saques feito pelo usuário.

![Menu de opções do usuário](./images/menuOpcoesUserBank.png)

## Diferenciais

1. **Controle de Saques Diários**: O sistema limita o usuário a realizar apenas 3 saques por dia com um limite máximo de R$ 500,00 por saque, adicionando uma camada extra de segurança à conta do usuário.
2. **Exibição de Saldo Antes das Opções**: Antes de apresentar o menu de opções ao usuário, o sistema exibe o saldo atual da conta, fornecendo ao usuário uma visão clara de seu saldo antes de realizar qualquer operação.
3. **Validação de Entrada Robusta**: O sistema inclui várias verificações para garantir que a entrada do usuário seja válida, melhorando a experiência do usuário.

## Como Usar
Para usar este sistema bancário simples, você precisa seguir estas etapas:
1. Clone o repositório para o seu computador local.
2. Navegue até a pasta do projeto.
3. Execute o arquivo `python .\banco.py`.

## Próximos Passos
Após a implementação inicial do projeto, planejamos adicionar as seguintes melhorias e recursos:

1. **Banco de Dados**: Implementar um banco de dados para armazenar as informações da conta do usuário de forma persistente.
2. **Interface do Usuário**: Desenvolver uma interface gráfica para tornar o sistema mais fácil de usar.
3. **Autenticação e Segurança**: Adicionar autenticação para proteger as informações do usuário e criptografia para garantir a segurança dos dados.
4. **Testes**: Escrever testes unitários para garantir que todas as funcionalidades estejam funcionando corretamente.


## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
SimpleBankingSystem-DB-Crypto-token/
│── backend/                   # Tudo relacionado ao backend (AWS Lambda, API, lógica do servidor)
|   ├── app.py             ← executa o servidor
    ├── config.py          ← configs gerais (como o banco de dados)
    ├── database/
    │   ├── __init__.py    ← inicializa o banco com SQLAlchemy
    │   └── models.py      ← define a tabela Transaction
    ├── routes.py          ← define os endpoints da API
    └── README.md
│   ├── lambda_functions/      # Código das funções Lambda
│   │   ├── process_transaction.py
│   │   ├── function.zip
│   │   └── banco.py
│   ├── tests/                 # Testes unitários e de integração
│   ├── database/              # Scripts de banco de dados (se necessário)
│   ├── serverless.yml         # Configuração do Serverless Framework
│   └── README.md
│
│── frontend/                  # Tudo relacionado ao frontend (HTML, CSS, JS)
│   ├── assets/                # Arquivos estáticos (imagens, ícones, fontes)
│   ├── styles/                # Arquivos CSS
│   ├── scripts/               # Arquivos JavaScript
│   ├── index.html             # Página principal
│   ├── dashboard.html         # Página do dashboard bancário
│   ├── chatbot.html           # Página do assistente bancário com IA
│   └── README.md
│
│── docs/                      # Documentação do projeto
│── .gitignore                 # Arquivos que não devem ser versionados no Git
│── README.md                  # Documentação geral do projeto
│── requirements.txt            # Dependências do projeto (caso use Python)
│── package.json                # Dependências do projeto (caso use Node.js)
│── serverless.yml              # Configuração do Serverless Framework
│── config/                     # Arquivos de configuração geral
```

**📌Descrição das Pastas e Arquivos:**

- **backend/**: Contém todo o código relacionado ao servidor, incluindo funções AWS Lambda, testes e scripts de banco de dados.
  - **lambda_functions/**: Diretório específico para as funções Lambda.
    - `process_transaction.py`: Função Lambda para processar transações.
    - `function.zip`: Arquivo zipado da função para deploy.
    - `banco.py`: Código relacionado às operações bancárias.
  - **tests/**: Testes unitários e de integração para garantir a qualidade do código.
  - **database/**: Scripts para configuração e manutenção do banco de dados, se aplicável.
  - `serverless.yml`: Arquivo de configuração para o Serverless Framework.
  - `README.md`: Documentação específica do backend.

- **frontend/**: Contém a interface do usuário, incluindo arquivos HTML, CSS e JavaScript.
  - **assets/**: Arquivos estáticos como imagens, ícones e fontes.
  - **styles/**: Arquivos CSS para estilização das páginas.
  - **scripts/**: Arquivos JavaScript para interatividade das páginas.
  - `index.html`: Página principal do sistema bancário.
  - `dashboard.html`: Página do dashboard bancário.
  - `chatbot.html`: Página do assistente bancário com IA.
  - `README.md`: Documentação específica do frontend.

- **docs/**: Documentação geral do projeto, incluindo manuais, diagramas e notas técnicas.

- **.gitignore**: Especifica quais arquivos e pastas o Git deve ignorar.

- **README.md**: Documentação geral do projeto, fornecendo uma visão geral e instruções básicas.

- **requirements.txt**: Lista de dependências do projeto para ambientes Python.

- **package.json**: Lista de dependências do projeto para ambientes Node.js.

- **serverless.yml**: Arquivo de configuração para o Serverless Framework, facilitando o deploy de funções Lambda e outros recursos.

- **config/**: Arquivos de configuração geral do projeto.

---

**Nota:** Esta estrutura é projetada para ser escalável e de fácil manutenção, seguindo as melhores práticas adotadas por grandes empresas de tecnologia.

---

Para mais detalhes sobre cada componente, consulte as seções correspondentes neste `README.md`.
