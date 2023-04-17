import xmlrpc.client
import sys
 
# Calcula total de argumentos
n = len(sys.argv)
 
# Verificação do uso correto/argumentos
if (n!=5):
    print("\nUso correto: rpcCalc_client <server_address> <port_number> <num1> <num2>.\n")
    exit(-1)

rpcServerAddr = "http://" + sys.argv[1] + ":" + sys.argv[2] + "/"
proxy = xmlrpc.client.ServerProxy(rpcServerAddr)

#Remote calls

soma = proxy.add(int(sys.argv[3]), int(sys.argv[4]))
print("%s+%s=%s" % (sys.argv[3], sys.argv[4], soma))

subract = proxy.sub(int(sys.argv[3]), int(sys.argv[4]))
print("%s-%s=%d" % (sys.argv[3], sys.argv[4], subract))

multiply = proxy.mult(int(sys.argv[3]), int(sys.argv[4]))
print("%s*%s=%s" % (sys.argv[3], sys.argv[4], multiply))

divide = proxy.div(int(sys.argv[3]), int(sys.argv[4]))
print("%s/%s=%d" % (sys.argv[3], sys.argv[4], divide))
