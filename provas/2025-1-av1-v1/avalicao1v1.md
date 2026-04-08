# 1ª Avaliação (v1) - 14/04/2025

## Professores: André Atanasio e Alváro magnum

1. Considerando a expressão a seguir, qual valor seria retornado, caso tivéssemos **a = 2, b = 5, c = 3** e **d = 1**? Deixe escrito na prova a resolução completa da expressão.

    ```Python
    not(a >= c + d) or b - a < c and b**c + d == a
    ```

    - Separar e resolver as expressões dentro dos parênteses

        - primeira operação:

            ```Python
            not(a >= c + d) = not(2 >= 3 + 1) → not(2 >= 4) → not(False)
            ```

        - segunda operação:

            ```Python
            b - a < c → 5 - 2 < 3 → 3 < 3 → False
            ```

        - Terceira operação:

            ```Python
            b ** c + d == a → 5 ** 3 + 1 == 2 → 125 + 1 == 2 → 126 == 2 → False```

    - Substituir operações e aplicar ordem de precedência: **() → not → and → or**

    ```Python
    not(False) or False and False
    ```

    Fica

    ```Python
    True or False and False → True or False → True
    ```

2. Escreva um programa em Python que receba 2 notas, numa escala de 0 a 10.0. As entradas são números reais. Em seguida, calcule e escreva a média ponderada, onde os pesos são 4 e 6. A saída deve ter 1 casa decimal.

    [Resposta](q02-media-ponderada.py)

3. Escreva um programa em Python que leia um valor inteiro, que indica o tempo de duração em segundos de um determinado evento esportivo. Como saída, o programa deve escrever este tempo em horas:minutos:segundos. Por exemplo: Se a entrada for 556, a saída será 0:9:16.

    [resposta](q03-duracao.py)

4. Escreva um programa que leia o salário fixo e o total de vendas efetuadas por um vendedor no mês, ambos valores reais. Sabendo que este vendedor ganha 20% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

    [resposta](q03-salario-bonus.py)

