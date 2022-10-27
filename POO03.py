from BDFAKE import BDFAKE

BD = BDFAKE()
BD.criarFuncionarios()
sexo = input("Insira 'M' para Masculino, ou 'F' para Feminino: ")

for item in BD.listFuncionarios:
     if (item.sexo == sexo):
         print(item.nome + " " + item.sobrenome)