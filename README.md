
# **Catálogo de Filmes e Séries**

![Status](https://img.shields.io/badge/Projeto-Semana%204-blue)
![Python](https://img.shields.io/badge/Python-3.11+-yellow)

Este projeto é um sistema interativo para gerenciamento de filmes e séries! Aqui você encontrará todas as informações sobre o catálogo, suas funcionalidades, as tecnologias utilizadas e como executá-lo em seu ambiente local.

## **Descrição do Projeto**
O catálogo é um sistema desenvolvido para organizar e acompanhar seu consumo de mídia, permitindo cadastrar filmes e séries, registrar avaliações, controlar progresso de episódios e gerar relatórios personalizados.

Ele foi construído com foco em Programação Orientada a Objetos, aplicando conceitos como herança, encapsulamento, composição e métodos especiais.

## **Objetivo**

Implementar um sistema completo seguindo todos os requisitos definidos no documento oficial do projeto, aplicando:

* Estruturação POO com classes bem definidas
* Relacionamentos entre entidades
* Configurações e regras acadêmicas
* Persistência em JSON ou SQLite
* Testes automatizados com pytest
* Interface mínima via CLI

O objetivo central é consolidar o domínio de POO em Python, incluindo uso correto de propriedades, validações, herança e métodos especiais.
Uma etapa do projeto é realizada por semana, com os commits finais de cada semana de desenvolvimento explicitados.

## **Tecnologias Utilizadas**

- Linguagem: Python
- Persistência: JSON
- Interface: CLI (linha de comando)

## **Estrutura UML do Projeto**

Abaixo está o diagrama UML que representa a arquitetura do sistema, suas classes e relacionamentos:

<img width="1760" height="1360" alt="Classe UML (1)" src="https://github.com/user-attachments/assets/bae2e6eb-6b98-405b-bd4f-966bf4423572" />


## **Organização das Pastas**

```
catalogo_filmes_series/
├── README.md
│
├── catalogo/
|   ├── classes
|   │   ├── midia.py
|   │   ├── filme.py
|   │   ├── serie.py
|   │   ├── temporada.py
|   │   ├── episodio.py
|   │   ├── usuario.py
|   │   ├── lista_personalizada.py
|   │   ├── historico.py
|   │   ├── registro_consumo.py
|   │   ├── relatorio.py
|   │   └── dados.py
│   └── main.py
|

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

Rodar via CLI:

```
python main.py
```

## **Contribuição**

Se você deseja contribuir com melhorias para o projeto, siga as etapas abaixo:

1. Faça um fork do repositório e clone-o em sua máquina.
2. Crie uma nova branch para suas modificações.
3. Faça as alterações necessárias e adicione-as ao stage.
4. Envie um pull request para que suas modificações sejam revisadas.

Ficarei feliz em receber suas contribuições!

✨ Divirta-se explorando e personalizando o catálogo! ✨
