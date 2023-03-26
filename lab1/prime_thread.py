import sys
import time
#biblioteca do python para o uso de multiprocessamento a partir de threads
import threading

# função que checa se um numero eh primo ou nao
def is_prime(n):
      #caso o numero seja negativo, 0 ou 1 ele nao eh primo
      if (n <= 1) : 
          return 'not a prime number'
      #caso o numero tenha passado pelo ultimo teste, mas seja menor que 3, ele eh o numero 2 que eh primo
      if (n <= 3) : 
          return 'prime number'
      #se o numero for divisivel por 2 ou 3 ele nao eh primo
      if (n % 2 == 0 or n % 3 == 0) : 
          return 'not a prime number'

      i = 5
      while(i * i <= n) : 
          if (n % i == 0 or n % (i + 2) == 0) : 
              return 'not a prime number'
          i = i + 6

      return 'prime number'

#definicao da funcao alvo que sera chamada pelas threads durante sua execucao
def threading_func(x):
    #Fazemos as threads dormirem por 2 segundos.
    #Como cada thread executa em paralelo essas esperas sao executadas em paralelo.
    #Por isso o tempo de execucao desta celula deve ser algo em torno de 2 segundos. 
    time.sleep(2)
    #printamos o numero x, passado como argumento da funcao, e se ele eh primo ou nao.
    #Observe que a ordem dos numeros nao eh mantida nos prints.
    #isso acontece pois a ordem de execucao das threads nao eh deterministica.
    print('{} is {} number\n'.format(x, is_prime(x)))

if __name__ == "__main__":
    #começa a contagem de tempo da celula
    start = time.time()
    #quantidade de numeros que iremos testar, passado pela linha de comando ao programa
    lower_limit = sys.argv[1]
    higher_limit = sys.argv[2]
    #lista que abriga as threads criadas
    threads = []
    #loop que inicializa as threads, uma para cada numero entre 0 e 9
    for i in range(int(lower_limit), int(higher_limit)):
        #usamos a funcao Thread da biblioteca threading, 
        #passando para ela o nome da funcao alvo que a thread criada deve executar(target=threading_func).
        #Como a funcao alvo recebe argumentos de entrada temos que passar para este metodo os argumentos que seram usados
        # como argumentos de entrada para a funcao alvo, o numero i do loop. Para isso que serve o argumento args=(i,),
        # que diz qual sera o argumento passado para a funcao alvo na execucao da thread.
        #a thread criada é armazenado na lista de threads
        thread = threading.Thread(target=threading_func, args=(i,))
        threads.append(thread)

    # Começa as threads usando o metodo start
    for j in threads:
        j.start()

    # Garantimos que todas as threads terminaram, por meio do metodo join(), antes de continuarmos a execucao da celula. 
    for j in threads:
        j.join()
    #Ao final printamos a quantidade de tempo decorrida do inicio da execucao da celula ate o final.
    #Como cada thread executa em paralelo, as esperas de 2 segundos da funcao sao executadas em paralelo.
    #Por isso o tempo de execucao desta celula deve ser algo em torno de 2 segundos.    
    print('Time taken = {} seconds'.format(time.time() - start))