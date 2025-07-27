import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import unicodedata


# Função para remover acentos
def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')


# === 1. Ler o arquivo CSV ===
df = pd.read_csv(r"C:\Users\Gabriel Estudo\Downloads\ecommerce_estatistica.csv")

# === 2. Padronizar os nomes das colunas ===
df.columns = [remover_acentos(col).strip().lower() for col in df.columns]

# Exemplo de colunas após padronização:
# ['titulo', 'nota', 'n_avaliacoes', 'desconto', ..., 'preco', ...]

# === 3. Gráfico de Histograma ===
plt.figure(figsize=(8, 5))
sns.histplot(df['preco'], bins=30, kde=True, color='skyblue')
plt.title('Distribuição de Preços')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# === 4. Gráfico de Dispersão ===
plt.figure(figsize=(8, 5))
sns.scatterplot(x='preco', y='nota', data=df)
plt.title('Dispersão entre Preço e Nota')
plt.xlabel('Preço')
plt.ylabel('Nota')
plt.tight_layout()
plt.show()

# === 5. Mapa de Calor ===
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlação entre Variáveis Numéricas')
plt.tight_layout()
plt.show()

# === 6. Gráfico de Barras (Distribuição por Gênero - ajustado) ===
plt.figure(figsize=(10, 6))
sns.countplot(x='genero', data=df, order=df['genero'].value_counts().index)
plt.title('Distribuição por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos
plt.tight_layout()
plt.show()

# === 7. Gráfico de Pizza (Materiais - TOP 10 + Outros) ===
top_materiais = df['material'].value_counts()
top_10 = top_materiais[:10]
outros = top_materiais[10:].sum()

# Junta os 10 primeiros com a soma dos demais como "Outros"
materiais_ajustados = top_10.copy()
materiais_ajustados['Outros'] = outros

plt.figure(figsize=(7, 7))
plt.pie(
    materiais_ajustados,
    labels=materiais_ajustados.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Distribuição dos Materiais (Top 10 + Outros)')
plt.tight_layout()
plt.show()

# === 8. Gráfico de Densidade (preço) ===
plt.figure(figsize=(8, 5))
sns.kdeplot(df['preco'], fill=True, color='green')
plt.title('Densidade de Preços')
plt.xlabel('Preço')
plt.ylabel('Densidade')
plt.tight_layout()
plt.show()

# === 9. Gráfico de Regressão (preço vs qtd_vendidos_cod) ===
plt.figure(figsize=(8, 5))
sns.regplot(x='preco', y='qtd_vendidos_cod', data=df, scatter_kws={'alpha': 0.5})
plt.title('Regressão: Preço vs Qtd Vendidos Codificados')
plt.xlabel('Preço')
plt.ylabel('Qtd Vendidos (Cod)')
plt.tight_layout()
plt.show()

