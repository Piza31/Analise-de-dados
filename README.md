# 📊 Análise Exploratória de Dados - E-commerce

Este projeto tem como objetivo realizar uma Análise Exploratória de Dados (EDA) com **visualizações interativas** sobre um conjunto de dados de produtos de um e-commerce. Através de diferentes gráficos e técnicas de visualização, buscamos identificar padrões, correlações e tendências relevantes.

---

## 📁 Arquivo utilizado

- `ecommerce_estatistica.csv`: base de dados contendo informações sobre produtos, preços, avaliações, descontos, marca, material, temporada, gênero e outros atributos.

---

## 🧪 Etapas do Projeto

1. **Leitura e padronização dos dados**
   - Remoção de acentos dos nomes das colunas
   - Conversão para letras minúsculas e remoção de espaços extras

2. **Visualizações e Análises com Dash**
   Foram gerados os seguintes gráficos interativos:

   - 📉 **Histograma** da distribuição de preços
   - 🟢 **Gráfico de dispersão** entre preço e nota
   - 🔥 **Mapa de calor** das correlações entre variáveis numéricas (com explicação ao lado)
   - 📊 **Gráfico de barras** da distribuição por gênero
   - 🥧 **Gráfico de pizza** com os 5 materiais mais frequentes + categoria "Outros" com legenda explicativa ao lado
   - 🌄 **Gráfico de densidade** dos preços (com explicação abaixo)
   - 📈 **Gráfico de regressão** entre preço e quantidade vendida codificada (com explicação)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- Pandas
- Seaborn
- Matplotlib
- Plotly
- Dash
- Unicode (para tratamento de acentuação)

---

## 🧠 Insights e Melhorias

- Agrupamento de materiais menos representativos na categoria "Outros"
- Adição de explicações ao lado ou abaixo dos gráficos para facilitar a interpretação
- Possibilidade de expandir o projeto com:
  - Análise de sazonalidade (ex: por temporada)
  - Técnicas de clusterização (agrupamento de produtos)
  - Modelos preditivos de avaliação ou vendas

---

## ▶️ Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/ecommerce-analise.git
   cd ecommerce-analise
   
2. Instale as bibliotecas necessárias:
   pip install -r requirements.txt
   
4. Execute o aplicativo Dash:
   python app.py

5. O aplicativo estará disponível no navegador em:
   http://127.0.0.1:8050

## 📌 Autor
Gabriel Dias Piza

Estudante de Análise de Dados pela EBAC
