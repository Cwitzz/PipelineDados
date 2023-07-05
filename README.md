# Pipeline de Dados para Sistema de Recomendação de Produtos

Este projeto representa uma pipeline de dados sofisticada que objetiva construir um sistema de recomendação de produtos com foco em práticas de engenharia de dados, aprendizado de máquina, e testes automatizados.

## 🧱 Componentes da Pipeline

### 1. Criação da Base de Dados

O script `criação_base_dados.py` cria um banco de dados SQLite chamado `DBFIC.db`. O banco contém uma coleção de transações de produtos de jardinagem com dados fictícios, gerados através da biblioteca Faker, incluindo nomes, endereços, preços, quantidades e outros.

### 2. Limpeza e Transformação dos Dados

O script `data_cleaning_transform.py` realiza várias operações de limpeza e transformação de dados, incluindo tratamento de valores faltantes, conversão de formatos e normalização de características numéricas utilizando pandas, scikit-learn e NumPy.

### 3. Treinamento do Modelo de Recomendação

`model_training_product_recomm.py` é responsável pelo treinamento de um modelo de aprendizado de máquina para recomendação de produtos. O modelo e os encoders são serializados em arquivos `.pkl` para reutilização.

### 4. Inserção de Recomendações no Banco de Dados

O script `insert_recommendations.py` aplica o modelo treinado para gerar recomendações personalizadas que são inseridas no banco de dados `DBFIC.db`.

### 5. Avaliação de Desempenho

O script `evaluate_perfomance_model.py` calcula métricas de desempenho relevantes para sistemas de recomendação, como precisão, recall, pontuação F1, entre outros.

### 6. Testes Automatizados

O projeto inclui testes automatizados nos scripts `Test_model_training_product_recomm.py` e `test_data_cleaning_transform.py` para verificar a integridade das funções e resultados.

### 7. Documentação

O arquivo `README.md` fornece informações sobre a configuração, objetivos do projeto, instruções para execução, e explicações sobre os componentes da pipeline.

## ⚙️ Escalabilidade e Desempenho

O projeto é projetado com foco na escalabilidade e desempenho, com possibilidade de extensão para conjuntos de dados maiores e integração com plataformas de dados em nuvem.

## 🚀 Conclusão

Esta pipeline é uma solução robusta para a construção de um sistema de recomendação de produtos. Ela engloba desde a criação da base de dados até a avaliação de desempenho do modelo, assegurando qualidade, testabilidade e escalabilidade. Não foi desenvolvida por enquanto etapas de análise dos dados pois o foco do projeto não era esse.


## 👨‍💻 Como executar

### Pré-requisitos
Certifique-se de ter Python 3.11 instalado em sua máquina. Além disso, você precisará de algumas bibliotecas Python. Você pode instalá-las usando pip:
`pip install pandas scikit-learn sqlite3 joblib faker numpy random`

Existe a possibilidade de nem todas as bibles entrarem, por isso aconselho a utilização de uma IDE para abrir o projeto.
### Passo 1: Configurando o Banco de Dados
Primeiro, você precisa criar e popular o banco de dados com dados fictícios. Use o script criação_base_dados.py para isso.
`python criação_base_dados`
### Passo 2: Limpeza, Pré-processamento e Transformação de Dados
Após configurar o banco de dados, execute o script data_cleaning_transform.py para limpar e transformar os dados.
`python data_cleaning_transform.py`
### Passo 3: Treinando o Modelo de Recomendação
Agora que os dados estão prontos, você pode treinar o modelo de recomendação. Execute o script model_training_product_recomm.py.
`python model_training_product_recomm.py`
### Passo 4: Avaliando a Performance do Modelo
Avalie a performance do modelo usando o script evaluate_perfomance_model.py. Isso fornecerá métricas úteis para entender o valor real do modelo.
`python evaluate_perfomance_model.py`
### Passo 5: Inserindo Recomendações no Banco de Dados
Finalmente, use o script insert_recommendations.py para inserir as recomendações geradas no banco de dados.
`python insert_recommendations.py`

Este passo é talvez irrelevante, pois com atualizações inseri esta função no próprio script de treinamento de modelo.
### Conclusão execução
Após executar esses scripts na ordem especificada, você terá um modelo de recomendação de produtos treinado e pronto para uso. As recomendações serão armazenadas no banco de dados SQLite e poderão ser acessadas conforme necessário.

## Considerações
Quero deixar claro que o usuário que quiser utilizar a pipeline para estudos, deve adaptar todos os aspectos do código para as suas condições, por exemplo, nome do banco de dados, caminhos, até mesmo o SGDB utilizado para banco de dados, ou até mesmo não utilizar, alterando para dados em excel por exemplo.

Além disto, os scripts foram escritos específicamente para a table criada pelo script inicial, caso você deseje utilizar tables diferentes, com aspectos diferentes, deve fazer a adaptação de todo o resto da cadeia de scripts.

## 📝 Licença

Informações sobre a licença do projeto (se aplicável).

