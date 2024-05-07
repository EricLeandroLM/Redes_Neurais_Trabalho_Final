# INTRODUÇÃO
Repositório do Projeto Final de Redes Neurais da disciplina de *Redes Neurais e Algoritimos Genéticos*. A disciplina faz parte da grade curricular do 3º semestre da ILUM - Escola de Ciência, sendo administrada pelo Professor Daniel Cassar. 

O repositório está dividido em duas partes:
- A aplicação e otimização da rede neural para previsão da dureza de materiais dado as informações das features junto com explicações detalhadas do códido e do desenvolvimento do raciocínio por trás. Tudo isso dentro de um notebook jupyter com interpolações entre código e texto de forma intuitiva.
  
- A *lore* criada funciona como uma história baseada na cultura geek, em especial, em RPGs de fantasia medieval. Toda a lore foi desenvolvida pensando em inspirar o leitor ou pesquisador a se envolver com o problema, permitindo o fácil entendimento de como funciona o procedimento perdição. [ Esperamos que gostem, fizemos com muito carinho :) ]

## Escopo do projeto
O projeto consiste na aplicação e na otimização de hiperparâmetros de uma rede neural do tipo MLP para prever a dureza, na escala de Mohs, de minerais a partir de 11 features inerentes a cada material, todos os dados utilizados são de datasets públicos de terceiros. 
Vale ressaltar que não faz parte do escopo do projeto se aprofundar nos aspectos técnicos, sendo necessário, para isso, a leitura das referências bibliográficas.

### Objetivo
A partir dos resultados da predição, analisar a eficácia de redes neurais MLP para predição de dureza de minerais com estruturas cristalinas distintas e explorar as variações para cada tipo de estrutura cristalina, considerando as amostragens utilizadas.

## Equipe
*TechTrinity* - Samuel Soares de Araújo, Eric Leandro Lima Mendoça e Daniel Carrasco Vieira 

# Organização
O Repositório está dividido em 4 partes:

- Readme -> Guia do projeto. Incluindo a motivação, origem, fontes e organização do github.
- Datasets -> Pasta com os dois arquivos referentes ao dataset de treino e de validação, os arquivos estão disponibilizados no formato *.csv*
- Notebooks -> Essa pasta consiste em dois arquivos com a extensão *.ipynb*, incluindo o notebook com o desenvolvimento da *lore* e o notebook com a aplicação da rede neural otmizada para predição junto ao detalhamento do processo de raciocínio e explicação dos códigos passo a passo em norma culta científica.
- Imagens -> Pasta com as imagens utilizadas para ilustração da narrativa do notebook referente a lore.

## Lore
O notebook da lore foi desenvolvido com muita atenção para uma imersão semelhante a uma novel de fantasia medieval com dragões e magia. Todas as imagens utilizadas para ilustração foram feitas por IA, permitindo o uso irrestrito das ilustrações, em relação a história, o desenvolvimento por inteiro é original e se encaixa de maneira suave aos tópicos apresentados no notebook do código e das explicações em si. É recomendado que a leitura da lore seja feita antes da leitura do outro notebook, porém a leitura da lore não é obrigatória para o entendimento do desenvolvimento da exploração dos datasets e da predição pela rede neural.

## Código
O notebook com o código possui a estrutura inspirada em publicações científicas, unindo formalidade com uma leitura fluída e de fácil entendimento(assim esperamos). É de suma importância que os textos sejam lidos na ordem e ao decorrer da elaboração dos códigos e dos resultados para que haja um entendimento correto e completo da proposta, do raciocínio e dos resultados. No conteúdo em si, há a introdução aos principais tópicos em relação aos minerais junto as suas features e ao conceito de dureza(alvo principal da predição), além dos códicos com as explicações necessárias, e, por fim, os resultados das predições e as conclusões dos autores. Caso ocorra dúvidas ou haja o desejo de aprofundamento, todas as referências utilizadas estão presentes aqui no Readme e ao fim do notebook.

# Datasets
Os dados extraídos consiste em dois databases de minerais, uma para treino com 622 minerais e outro para validação com 51 minerais. Ambos os dataset possuem um total de 11 descrições atômicas de cada mineral, ou seja, 11 features e a dureza como target.
*Features*
- Número de elétrons
- Número de elétrons de valência
- Número atômico
- Eletronegativa de Pauling
- Eletronegatividade do estado de oxidação mais comum
- Raios atômicos covalentes
- Raio de Vander Waals
- Energia de ionização do neutro
- Média de todos os elétrons
- Densidade média
- Peso atômico
  
Entretanto, o dataset de validação possui duas colunas a mais. A primeira corresponde a fórmula molecular do mineral e a segunda ao tipo de estrutura ceistalina.

## Dataset de Treino
O Dataset de treino é composto por 622 minerais com composições únicas obtidos por permutações composicionais de uma base de dados com 369 minerais únicos retirados do *Physical and Optical Properties of Minerals CRC Handbook of Chemestry and Physics* e da *American Mineralogist Crystal Structure Database* . Os minerais presentes do dataset possuem estruturas critalinas diversas como já foi mencionado, sendo: 

- 210 de estrutura monoclínica;
- 96 de estrutura romboédrica;
- 89 de estrutura hexagonal;
- 80 de estrutura tetragonal;
- 73 de estrutura cúbica;
- 50 de estrutura ortorrômbica;
- 22 de estrutura triclínica;
- 1 de estrutura trigonal;
- 1 de estrutura amorfa.

## Dataset de Validação
O dataset de validação é composto por 51 cristais sintéticos singulares retirados da literatura, sendo a distribuição das estruturas cristalinas:

- 15 de estrutura monoclínica;
- 7 de estrutura tetragonal;
- 7 de estrutura hexagonal;
- 6 de estrutura ortorrômbicas;
- 4 de estrutura cúbica;
- 3 de estrutura romboédrica.

# Tecnologias/Técnicas
## Linguagem
- Python
## Biblitecas
- Pytorch
- Numpy
- Matplotlib
- Pandas
- ScikitLearn
## Plataforma de computação
- Jupyter Notebook
  
# Referências
## Datasets
Dumlao, J. (2024). Prediction of Mohs Hardness with Machine Learning. Kaggle. Retrieved from https://www.kaggle.com/datasets/jocelyndumlao/prediction-of-mohs-hardness-with-machine-learning/data
Garnett, J. C. (2022). Dataset for Mohs Hardness Prediction. Mendeley Data. DOI: 10.17632/jm79zfps6b.1. Retrieved from https://data.mendeley.com/datasets/jm79zfps6b/1

## Literatura 
TABOR, David. Mohs's hardness scale-a physical interpretation. Proceedings of the Physical Society. Section B, v. 67, n. 3, p. 249, 1954.


## Bibliotecas
PyTorch. (2024). PyTorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration. Retrieved from https://pytorch.org/
PyTorch. (2024). torch.nn - PyTorch v1.10.1 documentation. Retrieved from https://pytorch.org/docs/1.10.1/nn.html
PyTorch. (2024). torch.optim - PyTorch v1.10.1 documentation. Retrieved from https://pytorch.org/docs/1.10.1/optim.html
Pandas. (2010). pandas documentation. Retrieved from https://pandas.pydata.org/docs/
Scikit-learn. (2011). scikit-learn preprocessing module documentation. Retrieved from https://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing
Scikit-learn. (2011). scikit-learn metrics module documentation. Retrieved from https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
Matplotlib. (2007). matplotlib.pyplot documentation. Retrieved from https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
NumPy. (2020). NumPy v1.22.0 documentation. Retrieved from https://numpy.org/doc/stable/






