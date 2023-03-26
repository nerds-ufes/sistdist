import sys
import time
#biblioteca do python para o uso de multiprocessamento a partir de processos
import multiprocessing

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

#definicao da funcao alvo que sera chamada pelos processos durante sua execucao
def multiprocessing_func(x):
    #fazemos com que o processo que execute esta funcao durma por 2 segundos,
    time.sleep(2)
    #printamos o numero x, passado como argumento da funcao, e se ele eh primo ou nao.
    #Observe que a ordem dos numeros nao eh mantida nos prints.
    #isso acontece pois a ordem de execucao dos processos depende de qual processo eh escolhido pelo scheduler de processos
    # e nao da ordem dos numeros.
    print('{} is {} number'.format(x, is_prime(x)))
    
if __name__ == '__main__':
    #comecamos a contagem do tempo de execucao da celula 
    starttime = time.time()
    #quantidade de numeros que iremos testar, passado pela linha de comando ao programa
    lower_limit = sys.argv[1]
    higher_limit = sys.argv[2]
    #criamos uma lista para abrigar os processos criados[]
    processes = []
    #criamos 10 processos neste loop
    for i in range(int(lower_limit), int(higher_limit)):
        #usamos a funcao Process da biblioteca multiprocessing, 
        #passando para ela o nome da funcao alvo que o processo criado deve executar(target=multiprocessing_func).
        #Como a funcao alvo recebe argumentos de entrada temos que passar para este metodo os argumentos que seram usados
        # como argumentos de entrada para a funcao alvo, o numero i do loop. Para isso que serve o argumento args=(i,),
        # que diz qual sera o argumento passado para a funcao alvo na execucao do processo.
        #o processo criado é armazenado na variavel p
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        #o processo eh inserido no final da lista de processos
        processes.append(p)
        #começamos a execucao do processo p por meio do metodo start(), 
        #a partir deste momento o processo p executa a funcao que passamos como target usando os argumentos passados em args=(i,)
        p.start()
    #Neste loop garantimos que todos os processos terminaram, por meio do metodo join(), antes de continuarmos a execucao da celula.    
    for process in processes:
        process.join()
    #print meramente para pular uma linha    
    print()
    #Ao final printamos a quantidade de tempo decorrida do inicio do processo ate o final.
    #Como cada processo executa em paralelo, as esperas de 2 segundos da funcao sao executadas em paralelo.
    #Por isso o tempo de execucao desta celula deve ser algo em torno de 2 segundos.    
    print('Time taken = {} seconds'.format(time.time() - starttime))