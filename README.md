# INTRODUÇÃO
Repositório do Projeto Final de Redes Neurais da disciplina de *Redes Neurais e Algoritimos Genéticos*. A disciplina faz parte da grade curricular do 3º semestre da ILUM - Escola de Ciência, sendo administrada pelo Professor Daniel Cassar.

## Equipe
*TechTrinity* - Samuel Soares de Araújo, Eric Leandro Lima Mendoça e Daniel Carrasco Vieira 

## Objetivo
O projeto consiste na aplicação e na otimização de hiperparâmetros de uma rede neural do tipo MLP para prever a dureza, na escala de Mohs, de minerais. 

## Datasets
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

### Dataset de Treino
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

### Dataset de Validação
O dataset de validação é composto por 51 cristais sintéticos singulares retirados da literatura, sendo a distribuição das estruturas cristalinas:

- 15 de estrutura monoclínica;
- 7 de estrutura tetragonal;
- 7 de estrutura hexagonal;
- 6 de estrutura ortorrômbicas;
- 4 de estrutura cúbica;
- 3 de estrutura romboédrica.

### Autoria dos Datasets
Os dados utilizados para a rede neural foram retirados de um dataset de domínio público na plataforma Kaggle, o dataset foi disponibilizado por Jocelyn Dumlao(https://www.kaggle.com/datasets/jocelyndumlao/prediction-of-mohs-hardness-with-machine-learning/data). A fonte original dos dados é da doutora Joy Carleen Garnett, cientista de dados na Vanderblit University - Nashville, Tennessee, US.
DOI: 10.17632/jm79zfps6b.1 | link: https://data.mendeley.com/datasets/jm79zfps6b/1

## Organização

### Lore




