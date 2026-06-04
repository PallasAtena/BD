# Sistema de Controle de Estoque Interativo

![Python Version](https://shields.io)
![PEP 8](https://shields.io)
![Contributions](https://shields.io)

Um sistema simples, robusto e totalmente interativo via terminal para gerenciamento e controle de estoque de produtos, desenvolvido em **Python**. A aplicação utiliza uma estrutura de dados baseada em uma lista de dicionários, simulando perfeitamente o comportamento de uma API estruturada no formato **JSON**.

O projeto foi revisado, corrigido e estruturado rigorosamente sob as diretrizes de estilo da **PEP 8**.

---

## Funcionalidades

O sistema disponibiliza quatro operações principais através de um menu interativo em laço contínuo:

* **1. Visualizar Estoque Atual:** Exibe todos os itens cadastrados com formatação de preço em duas casas decimais (`R$ 0.00`).
* **2. Registrar Entrada de Produto:** Soma novas unidades a um produto existente (busca case-insensitive) ou realiza o cadastro completo se o item for novo.
* **3. Registrar Saída de Produto:** Subtrai itens do estoque com validação de segurança para impedir que o saldo fique negativo.
* **4. Sair do Sistema:** Interrompe a execução do programa de maneira limpa e segura.

---

## Tecnologias e Boas Práticas (PEP 8)

* **Nativo:** Desenvolvido utilizando apenas recursos padrão do **Python 3**, sem necessidade de instalar bibliotecas externas.
* **Tipagem Correta:** Correção de bugs comuns de terminal, tratando as opções do menu estritamente como strings (`opcao == "1"`).
* **Sintaxe Limpa:** f-strings otimizadas com alternância correta de aspas (`f"Exemplo: {dicionario['chave']}"`).
* **Padrão PEP 8:** Indentação estrita de 4 espaços, espaçamento consistente ao redor de operadores e nomes de variáveis em `snake_case`.

---

## Como Executar o Projeto

### Pré-requisitos
Você precisa apenas do **Python 3** instalado em sua máquina.

### Passo a Passo
1. Clone este repositório para a sua máquina local:
   ```bash
   git clone https://github.com
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd NOME_DO_REPOSITORIO
   ```
3. Execute o script principal:
   ```bash
   python estoque.py
   ```

---

## Estrutura dos Dados (Mock JSON)

Os dados são armazenados na memória de forma estruturada, simulando um banco de dados não relacional ou payload de API:

```json
[
  {"nome": "Notebook ASUS", "quantidade": 10, "preço": 3500.00},
  {"nome": "Mouse Wireless Logitec", "quantidade": 50, "preço": 89.90},
  {"nome": "Teclado Mecânico Adamantium", "quantidade": 25, "preço": 249.90}
]
```

---

## Como Contribuir

Contribuições são sempre bem-vindas! Se você deseja sugerir melhorias (como persistência de dados em arquivos `.json` ou uma interface gráfica), siga os passos:

1. Faça um **Fork** do projeto.
2. Crie uma nova **Branch** com sua funcionalidade: `git checkout -b feature/nova-funcao`.
3. Salve suas alterações e faça o **Commit**: `git commit -m 'Adiciona nova funcao'`.
4. Envie para a Branch original: `git push origin feature/nova-funcao`.
5. Abra um **Pull Request**.

---
Desenvolvido por [PallasAtena](https://github.com/PallasAtena/BD).
