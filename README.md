# 📊 Análise Exploratória de Dados - E-commerce

Este projeto tem como objetivo realizar uma análise exploratória de dados (EDA) com visualizações gráficas sobre um conjunto de dados de produtos de um e-commerce. Através de diferentes gráficos e técnicas de visualização, buscamos identificar padrões, correlações e tendências relevantes.

---

## 📁 Arquivo utilizado

- **ecommerce_estatistica.csv**: base de dados contendo informações sobre produtos, notas, avaliações, preços, descontos, marca, material, temporada, entre outros.

---

## 🧪 Etapas do Projeto

1. **Leitura e padronização dos dados**
   - Remoção de acentos dos nomes das colunas
   - Conversão para letras minúsculas e remoção de espaços

2. **Análise Estatística e Visualizações**
   Foram gerados os seguintes gráficos com título e rótulos explicativos:

   - 📉 **Histograma** da distribuição de preços
   - 🟢 **Gráfico de dispersão** entre preço e nota
   - 🔥 **Mapa de calor** de correlação entre variáveis numéricas
   - 📊 **Gráfico de barras** da distribuição por gênero (com ajuste de rotação para evitar sobreposição)
   - 🥧 **Gráfico de pizza** da distribuição dos 10 principais materiais (os demais foram agrupados como "Outros" para maior legibilidade)
   - 🌄 **Gráfico de densidade** dos preços
   - 📈 **Gráfico de regressão** entre preço e quantidade vendida (codificada)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- Pandas
- Seaborn
- Matplotlib
- Unicode (para tratamento de acentuação)

---

## 🧠 Insights e Melhorias

- Materiais com pouca frequência foram agrupados em "Outros" no gráfico de pizza para melhorar a clareza.
- Rótulos de categorias sobrepostos foram ajustados com rotação e redimensionamento dos gráficos.
- O projeto pode ser expandido com técnicas de clusterização, análise de variáveis categóricas ou modelagem preditiva.

---

## 📎 Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/ecommerce-analise.git

2. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas matplotlib seaborn

3. Execute o arquivo Python:
   ```bash
   python AnaliseDados.py

## 📌  Autor
Gabriel Dias Piza

Estudante de Análise de Dados pela EBAC
