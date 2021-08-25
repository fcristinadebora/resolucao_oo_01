from classes.main import Main

main = Main()

while main.em_execucao == True:
    main.mostrar_menu()
    main.ler_opcao_menu()