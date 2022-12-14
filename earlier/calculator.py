def calculator():
    while True:
        command = input('введите фунцию (+), (-), (*), (/): ')
        if command == '+':
            qwerty = float(input('Введите число 1: '))
            asd = float(input('Введите число 2: '))
            zxc = qwerty + asd
            print(zxc)
            
            command = input('продолжить y, n: ')
            if command == 'y':
                qwerty1 = float(input('Введите число 3: ')) 
                # данное выражение должно применяться n раз
                zxc1 = zxc + qwerty1
                print(zxc1)
            
                
            command = input('продолжить (y) следующее число (n): ')
            if command == 'y':
                zxc 



        elif command == '-':   
            qwerty = float(input('Введите число 1: '))
            asd = float(input('Введите число 2: '))
            zxc = qwerty - asd
            print(zxc) 	

        elif command == '/':   
            qwerty = float(input('Введите число 1: '))
            asd = float(input('Введите число 2: '))
            zxc = qwerty / asd
            print(zxc) 

        elif command == '*':   
            qwerty = float(input('Введите число 1: '))
            asd = float(input('Введите число 2: '))
            zxc = qwerty * asd
            print(zxc)
        
    
           
calculator()

input('это конец')