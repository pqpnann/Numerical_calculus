# O Problema dos Três Corpos
O problema dos três corpos é um clássico da mecânica celeste que busca descrever o movimento de três corpos que interagem gravitacionalmente. A complexidade surge porque, diferentemente do problema de dois corpos (cuja solução é exata e bem compreendida), o acréscimo de um terceiro corpo cria interações que tornam o sistema não resolvível por métodos analíticos gerais, sendo necessário o uso de métodos numéricos.

# O Problema Restrito dos Três Corpos
O problema restrito dos três corpos é uma simplificação do problema geral que considera um dos corpos como sendo de massa desprezível (ou seja, não influencia os outros dois corpos significativamente). Os dois corpos principais seguem órbitas influenciadas mutuamente (como no problema de dois corpos), enquanto o terceiro corpo é influenciado pelo campo gravitacional resultante, mas não interfere nele.

# Paper
Este trabalho teve como objetivo simular a órbita de Plutão no sistema Sol-Netuno-Plutão, que forma um caso real do Problema Restrito dos Três Corpos, sendo Plutão o corpo celeste de massa desprezível no sistema. Como pôde ser visto, a órbita de Plutão forma um desenho único e bem diferente.
A resolução matemática utilizou o conhecido método de Runge-Kutta para resolução de EDOs.
Para fazer os cálculos matemáticos e a representação gráfica da órbita, foi usada a linguagem Python e sua biblioteca _Matplotlib_. O paper foi feito em LaTeX, como um verdadeiro paper científico.

# Arquivos
O código presente em _Runge-Kutta_EDOs.py_ implementa o algoritmo de Runge-Kutta para as Equações Diferenciais Ordinárias deduzidas no paper e com as condições iniciais tiradas do [artigo](https://www.scielo.br/j/rbef/a/ngrxHPwZ6bDbbhvPnnLQ8LL/?format=pdf&lan) que está nas referências bibliográficas. 
O código em _Plot.py_ plota a órbita de Plutão no sistema Sol-Netuno-Plutão utilizando a biblioteca _Matplotlib_.
