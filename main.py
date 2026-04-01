import operacoes as ops
import menus

opc=0

while(opc!=5):

    opc=menus.exibir_menu()

    match opc:
        case 1:
            n1=float(input("Digite o primeiro número:"))
            n2=float(input("Digite o segundo número:"))
            resultado=ops.somar(n1,n2)
            print(f"Resultado: {resultado}")

            with open("LogCalculos.txt","a",encoding="utf-8") as arquivo:
                arquivo.write(str(n1)+" + "+str(n2)+" = "+str(resultado)+"\n")
            
        case 2:
            n1=float(input("Digite o primeiro número:"))
            n2=float(input("Digite o segundo número:"))
            resultado=ops.subtrair(n1,n2)
            print(f"Resultado: {resultado}")

            with open("LogCalculos.txt","a",encoding="utf-8") as arquivo:
                arquivo.write(str(n1)+" - "+str(n2)+" = "+str(resultado)+"\n")
            
        case 3:
            n1=float(input("Digite o primeiro número:"))
            n2=float(input("Digite o segundo número:"))
            resultado=ops.dividir(n1,n2)
            print(f"Resultado: {resultado}")

            with open("LogCalculos.txt","a",encoding="utf-8") as arquivo:
                arquivo.write(str(n1)+" x "+str(n2)+" = "+str(resultado)+"\n")
            
        case 4:
            n1=float(input("Digite o primeiro número:"))
            n2=float(input("Digite o segundo número:"))
            resultado=ops.dividir(n1,n2)
            if resultado is None:
                print('Operação inválida! Divisões por zero não são permitidas!')
            else:
                print(f"Resultado: {resultado}")
            
        case 5:
            print("Saindo...")
        case _: #default
            print("Opção Inválida!")

