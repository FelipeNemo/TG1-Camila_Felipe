import systemRPG as r
#import gameplay as y
#O sistema deve gerar um relatório de combate, que deve conter o nome dos personagens,
# o dano causado por cada ataque e o vencedor do combate.

def main(): 
    with open("reports/erros.log", "w", newline='') as f:  # Limpa o log no início do programa
        pass  

    while True:
        print("\n=== MENU RPG ===")
        print("1. Combate entre dois personagens")
        print("2. Combate Free For All")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            personagens, erros = r.carregar_personagens("Entrada/entrada.txt")
            if erros:
                r.salvar_log("reports/erros.log", [["Personagem", "Erro"]] + erros)
            relatorio1 = r.combate_entre_dois(personagens)
            r.salvar_csv("reports/relatorio_entre_dois.csv", relatorio1) 
            #y.mostrar_batalha(relatorio, sprites)

        elif opcao == "2":
            personagens, erros = r.carregar_personagens("Entrada/entrada.txt")
            if erros:
                r.salvar_log("reports/erros.log", [["Personagem", "Erro"]] + erros)
            relatorio2 = r.combate_free_for_all(personagens)
            r.salvar_csv("reports/relatorio_free_for_all.csv", relatorio2)
        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()