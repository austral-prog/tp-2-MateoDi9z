def change():
    expense = 23.75
    money = 100
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido\n100\n\nVuelto\n")

    total = money - expense
    
    print(f"Pesos:\n{int(total)}")
    print(f"Centavos:\n{int((total - int(total)) * 100)}")