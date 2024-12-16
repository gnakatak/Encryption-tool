A cifra usada neste programa é baseada em uma substituição 
simples de caracteres.

Para cada letra ou número, existe correspondentes em uma 
tabela que define quais símbolos ou caracteres irão 
substituí-los. Existem dois tipos de cifras:

1. Cifra Simples: utiliza uma tabela de substituição fixa, 
onde cada letra ou número é substituído por outro símbolo 
específico de forma direta e imutável. Por exemplo, a 
letra 'a' sempre será substituída por '1', 'b' por '2', 
e assim por diante, sem qualquer variação. A substituição 
segue um padrão fixo, e, portanto, é mais fácil de ser 
quebrada sem o uso de uma chave secreta. A simplicidade 
desse método torna-o vulnerável a ataques de análise de 
frequência.

2. Cifra Complexa: é mais dinâmica, e a substituição de 
caracteres pode variar dependendo de certos critérios, 
como a ordem das letras ou uma chave secreta. Assim, a 
letra 'a' pode ser substituída por '1' em uma parte do 
texto e por 'r' em outra, ou até mesmo por diferentes 
símbolos conforme a regra definida. Isso torna o processo
de cifragem mais difícil de ser decifrado, pois a 
substituição não segue um padrão fixo. A Cifra Complexa
oferece maior segurança ao introduzir variabilidade, 
dificultando ataques sem o conhecimento da chave ou da 
lógica usada na cifra.

O programa utiliza duas tabelas: uma para letras e outra 
para números, onde cada caractere possui múltiplas 
possibilidades de substituição.

Tabela de Letras:
--------------------------------------------
| Letra | Substituições  |  Alternativas  |
--------------------------------------------
|   a   |       1        |       r        |
|   b   |       2        |       s        |
|   c   |       3        |       t        |
|   d   |       4        |       u        |
|   e   |       5        |       v        |
|   f   |       6        |       w        |
|   g   |       7        |       x        |
|   h   |       8        |       y        |
|   i   |       9        |       z        |
|   j   |       a        |       !        |
|   k   |       b        |       @        |
|   l   |       c        |       #        |
|   m   |       d        |       $        |
|   n   |       e        |       %        |
|   o   |       f        |       ^        |
|   p   |       g        |       &        |
|   q   |       h        |       *        |
|   r   |       i        |       (        |
|   s   |       j        |       )        |
|   t   |       k        |       -        |
|   u   |       l        |       _        |
|   v   |       m        |       =        |
|   w   |       n        |       +        |
|   x   |       o        |       <        |
|   y   |       p        |       >        |
|   z   |       q        |       ~        |
|   ' ' |       ' '      |       ' '      |
--------------------------------------------
Tabela de Números:
--------------------------------------------
| Número | Substituições  |  Alternativas  |
--------------------------------------------
|   1   |       a        |       t        |
|   2   |       b        |       s        |
|   3   |       c        |       r        |
|   4   |       d        |       q        |
|   5   |       e        |       p        |
|   6   |       f        |       o        |
|   7   |       g        |       n        |
|   8   |       h        |       m        |
|   9   |       i        |       l        |
|   0   |       j        |       k        |
|   ' ' |       ' '      |       ' '      |
|    ,  |        ,       |        ,       |
|    .  |        .       |        .       |
--------------------------------------------
Cada caractere do texto é substituído com base 
nessas tabelas, criando uma cifra complexa ou 
simples, dependendo da escolha do usuário.