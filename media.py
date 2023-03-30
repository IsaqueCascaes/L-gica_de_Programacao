# -*- coding: utf-8 -*-
aluno = "joao"
nota1 = 10
nota2 = 10
nota3 = input("Digite sua 3 nota: ")
nota4 = input("Digite sua 4 nota: ")

media = (nota1 + nota2 + nota3 + nota4) / 4
print(media)
if media >= 7:
    print("parabéns ," + aluno + " passou")
elif media == 10:
    print("parabéns ," + aluno + " passou com distinção")
else:
    print("o aluno " + aluno + " não passou")

