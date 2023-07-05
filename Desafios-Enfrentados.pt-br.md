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
#### Diminuição do tempo total de 99,2% 
#### Aumento de 128x

Isso acaba por 




