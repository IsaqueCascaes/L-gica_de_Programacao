# -*- coding: utf-8 -*-
print("Descubra qual número é maior que outro! kk")
num1 = float(input("digite um numero "))
num2 = float(input("digite outro numero "))
num3 = float(input("digite só mais um numero "))


#o numero 1 é maior
if num1 > num2 and num3:

    print ("o numero " + str(num1) + " é maior que " + str(num2) + " e " + str(num3))
    
#igual a num1
elif num1 == num2 and num3:

    print ("o numero " + str(num1) + " é igual a " + str(num2) + " e " + str(num3))

#
elif num2 > num1 and num3:

    print("o numero " + str(num2) + " é maior que " + str(num1) + " e " + str(num3))

#
elif num2 == num1 and num3:

    print ("o numero " + str(num2) + " é igual a " + str(num1) + " e " + str(num3))

#
elif num3 > num2 and num1:
    print("o numero " + str(num3) + " é maior que " + str(num2) + " e " + str(num1))

#
elif num3 == num2 and num1:
    print("o numero " + str(num3) + " é igual a " + str(num2) + " e " + str(num1))
    
#
else:
    print("os numero são iguais")

