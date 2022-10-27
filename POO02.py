from BDFAKE import BDFAKE

BD = BDFAKE()
BD.criarFuncionarios()
ano = int(input("Insira o ano de Nascimento: "))

for item in BD.listFuncionarios:
     if (item.dataNascimento.year == ano):
         print(item.nome + " " + item.sobrenome)