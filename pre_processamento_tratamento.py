import pandas as pd
import funcoes_pipeline as fp


# Etapa de leitura dos dados
df = pd.read_csv('livros.txt')

# Etapa de tratamento de dados ausentes
df = fp.tratar_dados_ausentes(df)

# Etapa de remoção de dados duplicados
df = df.drop_duplicates()

# Etapa de tratamento de valores discrepantes (outliers)


# Etapa de normalização ou padronização de dados
# ... seu código aqui ...

# Etapa de conversão de tipos de dados
df['coluna_numerica'] = df['coluna_numerica'].astype(float)

# Etapa de tratamento de valores discrepantes e inválidos
# ... seu código aqui ...

# Etapa de criação de novas variáveis ou recursos
df['nova_variavel'] = df['coluna1'] + df['coluna2']

# Finalização do pré-processamento e exportação dos dados processados
df.to_csv('dados_processados.csv', index=False)
