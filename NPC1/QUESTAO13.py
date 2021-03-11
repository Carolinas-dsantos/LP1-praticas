#Faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
#O programa deve imprimir 10, 9, 8..., 1, 0 e "Fogo!". Detalhe, o cronômetro está quebrado e pula os números pares..

from  time import sleep 
import os
x = 10-1
while x > 0:
    for contagem in range(2):
        sleep(1)
        print(x)
        x = x-2
        
os.system('clear')  
print('Fogo')