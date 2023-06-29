def tratar_dados_ausentes(df):
    # Verificar e tratar dados ausentes
    # Exemplo: preencher valores ausentes com a média da coluna
    df = df.fillna(df.mean())
    return df

