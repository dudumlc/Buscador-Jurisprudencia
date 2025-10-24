# JurisAI - Inteligência Jurídica Aplicada à Jurisprudência

Bem-vindo ao repositório do JurisAI, um projeto desenvolvido para automatizar a leitura, estruturação e compreensão de informativos de jurisprudência por meio de Inteligência Artificial e processamento de texto.

## Sobre o Projeto
O JurisAI nasceu da necessidade de facilitar o acesso e o entendimento de informativos de jurisprudência que, embora riquíssimos em conteúdo, costumam estar dispersos em inúmeros arquivos e formatos pouco estruturados.
.
O projeto automatiza o processo de coleta, organização e busca dessas informações, tornando a pesquisa jurídica rápida, estruturada e inteligente.
.
Com ele, advogados, pesquisadores e estudantes podem consultar jurisprudências por tema, termo ou área do direito, sem precisar decorar referências nem navegar manualmente por diversos documentos.

## Sobre a Solução

O JurisAI realiza três etapas principais:

### 1. Leitura e extração automática de informações:
O sistema percorre diversos informativos de jurisprudência e utiliza expressões regulares (Regex) para capturar dados relevantes, como:

PROCESSO
TEMA
DESTAQUE
ARQUIVO
LINK
INTEIRO_TEOR
RAMO_DO_DIREITO

### 2. Estruturação dos dados:
Após a extração, as informações são tabuladas em um formato estruturado (DataFrame) para facilitar consultas e análises posteriores.

### 3. Busca inteligente e resumo automatizado:
O usuário pode buscar jurisprudências com base em termos específicos ou temas jurídicos.
Além disso, um modelo de IA integrada gera resumos automáticos do conteúdo completo, tornando a leitura e compreensão dos casos muito mais ágil.
.

Essa abordagem permite transformar grandes volumes de texto jurídico em conhecimento acessível e inteligível — uma verdadeira IA assistente jurídica.

## Estrutura do Repositório

A estrutura de pastas deste repositório foi organizada para manter o projeto limpo e modular. Cada diretório principal contém um arquivo `README.md` que detalha seu propósito específico.

- `data/`: Contém os datasets brutos, processados e externos.
- `docs/`: Documentação do projeto, relatórios e apresentações.
- `notebooks/`: Notebooks Jupyter para exploração de dados, modelagem e análise.
- `src/`: Código fonte, scripts e módulos reutilizáveis.
- `results/`: Resultados finais, como submissões, visualizações e modelos treinados.

## Como Começar

1.  **Clone o repositório:**
    ```bash
    git clone git@github.com:dudumlc/JurisAI.git
    
    ```

2.  **Restaure as dependências:**
    Por exemplo:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Execute o projeto:**
    Por exemplo:
    ```bash
    python main.py
    ```

