
# **Catálogo de Filmes e Séries**

![Status](https://img.shields.io/badge/Projeto-Semana%205-blue)
![Python](https://img.shields.io/badge/Python-3.11+-yellow)

Este projeto é um sistema interativo para gerenciamento de filmes e séries! Aqui você encontrará todas as informações sobre o catálogo, suas funcionalidades, as tecnologias utilizadas e como executá-lo em seu ambiente local.

## **Descrição do Projeto**
O catálogo é um sistema desenvolvido para organizar e acompanhar seu consumo de mídia, permitindo cadastrar filmes e séries, registrar avaliações, controlar progresso e gerar relatórios personalizados.

Ele foi construído com foco em Programação Orientada a Objetos, aplicando conceitos como herança, encapsulamento, composição e métodos especiais.

## **Objetivo**

Implementar um sistema completo seguindo todos os requisitos definidos no documento oficial do projeto, utilizando:

* Estruturação POO com classes bem definidas
* Relacionamentos entre entidades
* Configurações e regras acadêmicas
* Persistência em SQLite
* Testes automatizados com pytest
* Interface mínima via CLI

O objetivo central é consolidar o domínio de POO em Python, incluindo uso correto de propriedades, validações, herança e métodos especiais.
Uma etapa do projeto é realizada por semana, com os commits finais de cada semana de desenvolvimento explicitados.

## **Tecnologias Utilizadas**

- **Linguagem:** Python 3.11+
- **Persistência:** SQLite
- **Interface:** CLI (linha de comando)
- **Testes Automatizados:** Pytest
- **Configurações:** JSON

## **Estrutura UML do Projeto**

Abaixo está o diagrama UML que representa a arquitetura do sistema, suas classes e relacionamentos:

<img width="1219" height="1312" alt="Classe UML (1)" src="https://github.com/user-attachments/assets/27f753b8-bb60-4763-a4aa-f7d824a9e518" />

## **Organização das Pastas**

```
catalogo_filmes_e_series/
├── main.py
├── seed.py
├── settings.json
├── banco.db
├── README.md
│
├── models/
│   ├── midia.py
│   ├── filme.py
│   ├── serie.py
│   ├── temporada.py
│   ├── episodio.py
│   ├── usuario.py
│   ├── historico.py
│   ├── relatorio.py
│   └── cli.py
│
├── data/
│   ├── dados.py
│   └── banco.db
│
├── config/
│   └── settings.py
│
└── tests/
    ├── test_midia.py
    ├── test_filme.py
    ├── test_serie.py
    ├── test_temporada.py
    └── test_episodio.py



```

## **Funcionalidades Principais**

- Cadastro de filmes e séries
- Controle de temporadas e episódios
- Progresso de visualização
- Avaliações (0 a 10)
- Histórico automático de mídias assistidas
- Listas personalizadas
- Relatórios (top 10, tempo assistido, notas por gênero etc.)

## **Como Rodar**

Pré-requisitos:

```
Python 3.11+
```

Clone o repositório:

```
git clone https://github.com/mariastrajano/catalogo_filmes_e_series.git
cd catalogo_filmes_e_series
```

Execute o sistema via terminal:

```
python main.py
```

## **Exemplos Visuais da CLI**

Tela Inicial

```
=== CATÁLOGO DE FILMES E SÉRIES ===
[1] Registro de Mídias
[2] Listas Personalizadas
[3] Histórico
[4] Relatórios
[5] Sair
Selecione uma opção (1-5): 
```

Cadastro de Filme

```
=== ADICIONAR MÍDIA ===
Título: Jogos Vorazes
Tipo (Filme ou Série): Filme
Gênero: Ação
Ano de Lançamento: 2012
Classificação Indicativa (L, 10, 12, 14, 16 ou 18): 14
Elenco: Jennifer Lawrence, Josh Hutcherson, Liam Hemsworth       
Status (Não Assistido, Assistindo ou Assistido): Assistido
Duração (em min): 142
Nota (0-10): 10

Mídia adicionada com sucesso!

Deseja adicionar outra mídia? (S/N) 

```

Relatórios

```
=== RELATÓRIOS ===
[1] Média das notas por gênero
[2] Tempo assistido por tipo
[3] Top 10 Filme/Séries
[4] Voltar
Selecione uma opção (1-4): 
```

Exemplo de relatótio

```
=== TEMPO TOTAL ASSISTIDO ===
Filme: 5.08 horas
Serie: 27.00 horas

Pressione Enter para continuar...
```

## **Testes (Opcional)**

Instalar pytest:

```
pip install pytest
```

Executar os testes:

```
pytest -v
```

## **Contribuição**

Se você deseja contribuir com melhorias para o projeto, siga as etapas abaixo:

1. Faça um fork do repositório e clone-o em sua máquina.
2. Crie uma nova branch para suas modificações.
3. Faça as alterações necessárias e adicione-as ao stage.
4. Envie um pull request para que suas modificações sejam revisadas.

Ficarei feliz em receber suas contribuições!

Divirta-se explorando e personalizando o catálogo!
