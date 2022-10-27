from BDFAKE import BDFAKE

BD = BDFAKE()
BD.criarFuncionarios ()
buscarnome = input("Insira as 3 primeiras letras do nome: ")
for item in BD.listFuncionarios:
     if (item.nome.lower().startswith(buscarnome)):
        print(item.nome + " " + item.sobrenome)