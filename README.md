# Meus Projetos de OpenCV com Python

Esse repositório tem o objetivo de ser uma mostra de alguns dos programas que eu fiz/faço enquanto aprendo a utilizar a biblioteca OpenCV. 

## Reconhecendo Inclinação

![image](https://user-images.githubusercontent.com/56319681/130542843-544ee0bf-035b-4855-a7c4-39842492dfbd.png)

Esse programa aplicava um filtro na imagem, procurando objetos azuis. Os pontos que formam o contorno desse objeto eram usados para o cálculo da inclinação. Mais precisamente, o ponto mais abaixo (maior valor em y) e o ponto mais a esquerda (menor valor em x). O resto é matemática: seno, cosseno... bum! chego ao valor do ângulo, em graus.
