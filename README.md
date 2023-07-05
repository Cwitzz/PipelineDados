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

Esta pipeline é uma solução robusta para a construção de um sistema de recomendação de produtos. Ela engloba desde a criação da base de dados até a avaliação de desempenho do modelo, assegurando qualidade, testabilidade e escalabilidade.

## 👨‍💻 Como executar

Instruções sobre como executar os scripts e configurar o ambiente.

## 📝 Licença

Informações sobre a licença do projeto (se aplicável).

