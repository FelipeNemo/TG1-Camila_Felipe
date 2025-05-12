# menu


# Opções menu
# Combate entre dois personagens
# Combate entre múltiplos personagens (FreeFor All)

# O sistema deve carregar todos os personagens
# Habilidades e classes de um arquivo de configuração, que deve estar no formato  markdown . 
# O arquivo de configuração deve conter as informações necessárias para poder instanciar os objetos de personagens. 
# Durante o processo de leitura, deverão ser tratados erros, como por exemplo: 
# quando um personagem carregado do arquivo possui mais habilidades que o permitido pela classe.
# O sistema deve ser capaz de lidar com esses erros e registrar as informações em um arquivo de log.


# teste obj----------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------
import SystemRPG as r

def main():
    personagens, erros = r.carregar_personagens("Entrada/entrada.txt")
    if erros:
        r.salvar_log("erros.log", [["Personagem", "Erro"]] + erros)

    while True:
        print("\n=== MENU RPG ===")
        print("1. Combate entre dois personagens")
        print("2. Combate Free For All")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorio = r.combate_entre_dois(personagens)
            r.salvar_csv("relatorio_entre_dois.txt", relatorio)

        elif opcao == "2":
            relatorio = r.combate_free_for_all(personagens)
            r.salvar_csv("relatorio_free_for_all.txt", relatorio)
        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
