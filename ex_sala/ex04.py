# Faça um programa que lê uma string e imprime "É um Palíndromo" caso a
# string seja um palíndromo e “Não é um palíndromo” caso não seja.
# E que aceite o palídromo mesmo que as letras correspondentes sejam maiúsculas e minúsculas.

texto = input("Digite um texto: ")

txt_esp = texto.replace(" ","")

texto_inverso = txt_esp[::-1]

if (txt_esp.lower() == texto_inverso.lower()):
    print("É um Palíndromo")
else:
    print("Não é um palíndromo")
