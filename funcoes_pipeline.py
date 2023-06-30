def tratar_dados_ausentes(df):
    # Verificar e tratar dados ausentes
    # Exemplo: preencher valores ausentes com a média da coluna
    df = df.fillna(df.mean())
    return df


def remover_duplicatas(df):
    df_sem_duplicatas = df.drop_duplicates(subset=['Título', 'Autor'])
    return df_sem_duplicatas

