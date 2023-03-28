Laboratório I – Paralelismo de Processos e Threads

Esta pasta contém exemplos do uso de processos e threads para a resolução de um problema.
Existem três arquivos de exemplo. 

O prime.ipynb é um arquivo do tipo notebook jupyter composto por 4 células.<br />
A primeira define uma função de checagem de números primos, que usaremos na resolução do problema de descobrir se um número é primo ou não. Ela deve ser executada primeiro para que todas as outras células possam ser executadas.<br />
A segunda célula tem o código da resolução do problema de maneira sequencial.<br />
As terceira e quarta células tem o código da resolução do problema de maneira paralelizada, usando processos e threads respectivamente. 
Todas essas células testam números indo de um limite inferior até um limite superior. Para mudar os valores dos limites é necessario mudar os valores das variaveis lower_limit e higher_limit. A sequencia de números é limitada [lower_limit,higher_limit[<br />

Os outros dois arquivos, prime_process e prime_threads tem a resolução do mesmo problema, mas em formato de arquivo de programa python normal. Para executa-los é necessario passar ao programa, por linha de comando, os valores das variaveis lower_limit e higher_limit. Sendo o primeiro valor passado o lower_limit e o segundo o higher_limit. Exemplo de uso:

```
$python prime_process 0 10
```
Para compilar a versão em C, faça da seguinte forma:

```
$gcc primes_multi.c -o primes_multi -lpthread
