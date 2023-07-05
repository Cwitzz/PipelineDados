# ⚔️ Desafios Enfrentados

## Criação dos Dados:
 De início, a ideia era criar uma base de dados super simples em um arquivo txt, imediatamente já percebi que isso dificultaria muito o processo.
 A primeira mudança foi criar dados sobre livros, em formato excel, com poucas colunas como data de publicação, autor, etc...

 Porém, após passar para as outras etapas, encontrei diversos problemas, e o principal seria a falta de complexidade destes dados, basicamente aplicar as coisas que eu gostaria de aplicar futuramente, não seria lógico pois não havia nada para ter tirado dali.
#### 🏁 Finalmente, dedicando mais tempo, criei um banco de dados, nada complexo, porém já em um banco de dados, uma table com colunas, 1000 nomes de clientes utilizando uma bible que cria dados ficticios, essa tabela possuia 1000 linhas com 8 colunas. Imediatamente muitas possibilidades abriram.

## 🧹 Data Cleaning, Pré-Processamento e Transformação
 De início, tudo estava funcionando de maneira tranquila, porém essa etapa, depende muito da próxima, e desenvolvendo os modelos de treinamento, percebi necessidades adicionais de complexidade, por exemplo, na hora de rodar o modelo, os dados do jeito inicial deixavam o processo muito lento, muito lento MESMO!

Depois de algum tempo quebrando a cabeça cheguei a algumas conclusões, modifiquei os valores da coluna `sex` para binário, isto já melhorou a velocidade do treinamento de modelo consideravelmente, além disso, codificar as colunas `customer_name` e `product`, facilitando imensamente a utilização dos métodos de aprendizado de máquina.

Utilizando o método k-means, apliquei uma clusterização nos dados, para facilitar ainda mais os processos futuros. Para saber mais, pesquise sobre o método k-means e clusterização de dados.

Foram muitas outras adaptações, que geraram um aumento superlativo na velocidade de treinamento.
Eu monitorei o aumento de velocidade e os números foram assustadores.
#### Tempo de Execução Inicial: 48 min 50 s
#### Tempo de Execução Final: 22.56 s
#### Diminuição do tempo total de 99,2% e aumento de 128x

## 🤖 Treinamento de Modelo para Recomendação de Produtos
Por incrivel que pareça, esta etapa foi uma das mais tranquilas, no caso, todas as implicações para ela rodar certinho, foram aplicadas na etapa anterior, tive alguns problemas com sintaxe e identação, porém rapidamente resolvidos
, um dos problemas enfrentados foi com uma biblioteca chamada `surprise`, eu não estava conseguindo utilizar ela da melhor maneira, tive alguns problemas com compatibilidade, então voltei para a `skicitlearn` mesmo.
Essa etapa passou por muitas mudanças é claro, porém a mais significativa foi, assim como nas outras, após deixar tudo rodando, tive que quebrar os scripts em microfunções, para facilitar a implementação de `TDD (Test Driven Development)`.

#### Quebrar em microfunções o script, foi um dos maiores desafios.

## ✔️ Avaliar Perfomance do Modelo
Não tive problemas com esse script, gostei muito das aplicações usadas , fica muito facil após rodar o script do modelo. As considerações desta etapa são mais interessantes nos resultados mesmo.

#### Comparando as métricas:

#### Primeira avaliação (Modelo 1):

#### MSE: 103.782312548213  MAE: 27.321351528391  R-squared (R2): -1.2131267381625
#### Para entender melhor, pesquise sobre os 3 métodos: MSE, MAE, R2 para entender, porém, a primeira avaliação demonstrava que o modelo estava HORRÍVEL.
#### Segunda avaliação: 
#### MSE: 23.85376567930002  MAE: 3.605650000000001  R-squared (R2): 0.7809557859075236

##### Na segunda avaliação, tanto o MSE quanto o MAE diminuíram significativamente em relação à primeira avaliação. O MSE é uma métrica que mede o erro médio ao quadrado, portanto, quanto menor o valor, melhor. O MAE é uma métrica que mede o erro médio absoluto, também sendo desejável um valor menor.

##### Além disso, o valor do R-squared (R2) aumentou na segunda avaliação. O R2 é uma métrica que indica a proporção da variância nos dados de destino que é capturada pelo modelo. Um valor mais próximo de 1 é considerado um bom ajuste do modelo aos dados.




