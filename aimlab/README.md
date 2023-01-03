# Descrição do Projeto

O projeto consiste num programa que captura a tela do computador, que deve estar rodando o AIM LAB (no modo GRIDSHOT) para funcionar, 
e detecta os objetos azuis na tela, movendo o mouse (com Arduino) para o objeto mais próximo do centro da tela.

## O OpenCV

Em resumo, o opencv é utilizado para determinar as posições dos objetos que devem ser quebrados no game. Uma vez tendo ciência
dessa informação, o python calcula os movimentos que devem ser feitos e os informa ao arduino, que move o mouse e atira. Abaixo
segue uma imagem demonstrando como a detecção das bolas funciona

![image](https://user-images.githubusercontent.com/56319681/210400764-ab5cb65e-9242-4e5c-9a65-bfad72feb622.png)

Se você prestar bastante atenção, verá que a detecção falha um pouco nos lados onde existe sombra. Isso ocorre porque o processo
todo é baseado em cor, e pra o computador, uma sombra nada mais é que uma cor mais escura. Assim sendo, é nossa obrigação ajustar
os filtros para que detectem inclusive as sombras. Essa é a parte mais chatinha do processo, principalmente se você fizer
manualmente.

## O Arduino

O Arduino recebe a informação do quanto deve deslocar o mouse, divide isso em alguns movimentos (por conta de uma limitação da
biblioteca usada no processo), e realiza esses movimentos. Quando o OpenCV detecta uma distância específica do centro do objeto, 
ele avisa ao arduino e ele atira, interrompendo o processo. Isso se repete indefinidamente, e é possível parar ou voltar o processo,
clicando em algum botão setado.

## Resultados

Os resultados obtidos no desenvolvimento do programa foram bastante satisfatórios. Primeiro, conseguimos desenvolver um algoritmo que
consistentemente não errava. Ele tinha 100% de precisão. Mas esse resultado não chega a surpreender, já que podemos definir que ele só vai
atirar quando estiver a uma distância específica do centro da imagem. O que há de mais interessante é que conseguimos também fazer ele
funcionar tão bem que ele chegou a pegar o TOP 1 MUNDIAL do game, após apenas algumas horas de trabalho.

![image](https://user-images.githubusercontent.com/56319681/210403009-e5b50dd4-4b8b-449b-a16c-e7cf14a13227.png)

Chamamos a conta criada de "iawithopencv".

Obs.: a conta "Guest" também era nossa, mas esquecemos de dar um nome e o print ia ficar meio zuado, então criamos uma conta e 
fizemos o processo novamente
