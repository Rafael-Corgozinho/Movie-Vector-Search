# 🎬 Movie Vector Search MVP

## 📌 Sobre o Projeto
Este é um Produto Mínimo Viável (MVP) para um sistema de busca semântica de filmes. Diferente da busca tradicional por palavras-chave (lexical), este sistema utiliza **Inteligência Artificial (Embeddings)** e **Busca Vetorial** para compreender o contexto da pesquisa.

**Exemplo Prático:** Se o usuário buscar *"Quero algo como Se7en"*, o sistema não procurará a palavra "Se7en" no título, mas mapeará o significado da frase e retornará filmes com proximidade semântica (suspense policial, investigação, serial killers). A interface é otimizada para descoberta fluida, com design escuro inspirado em plataformas como Netflix e Letterboxd.



## 🏗️ Arquitetura e Pipeline

O fluxo de funcionamento do sistema é o seguinte:
1. **Ingestão (Seed):** Coleta de dados de filmes (Dataset inicial CSV / TMDB API).
2. **Vetorização:** Textos (Título + Sinopse + Gêneros) são convertidos em vetores numéricos através de um modelo de IA.
3. **Banco Vetorial:** Os vetores são armazenados no banco de dados.
4. **Consulta do Usuário:** O usuário envia uma pesquisa em linguagem natural pelo Front-end.
5. **Busca de Similaridade:** O Back-end vetoriza a pesquisa do usuário e calcula a distância matemática (K-NN/Cosine Similarity) contra os vetores do banco para retornar os filmes mais relevantes.
6. **Renderização:** O Front-end exibe os filmes ordenados pela relevância vetorial, apresentando um *Score de Similaridade*.

## 🛠️ Stack Tecnológica

### Back-End
- **Framework:** FastAPI (Python)
- **Servidor:** Uvicorn
- **Banco de Dados Vetorial:** ChromaDB
- **Modelos de IA:** Sentence Transformers (HuggingFace)

### Front-End
- **Framework:** React (Vite)
- **Estilização:** CSS Customizado (CSS Grid/Flexbox, Variáveis nativas)
- **Ícones:** Lucide React
- **Comunicação de Rede:** Fetch API nativa

## 📂 Estrutura de Diretórios

```text
/
├── BackEnd/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # Ponto de entrada da API
│   │   ├── routes/          # Endpoints (ex: /api/search)
│   │   ├── services/        # Lógica de embeddings e conexão com ChromaDB
│   │   └── models/          # Schemas Pydantic para validação
│   └── requirements.txt
└── FrontEnd/
    ├── public/
    ├── src/
    │   ├── App.jsx          # Lógica principal, estados de busca e renderização
    │   ├── App.css          # Estilização global e dos componentes
    │   └── main.jsx
    └── package.json
