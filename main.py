import core
import os

def main():
    os.system('cls')
    print(" ############ PASSWORD GENERATOR ############ ")
    menu = ['[1] STRINGS (only)','[2] NUMBERS (only)','[3] SPECIAL CHARS (only)','[4] STRINGS + NUMBERS','[5] STRINGS + SPECIAL CHARS','[6] NUMBERS + SPECIAL CHARS','[7] ALL']

    i=0
    for i in range(len(menu)):
        print(menu[i])

    option = int(input("\nEnter the type of password to Generate: "))

    if option > 7:
        print('Invalid Choice :(')
        ip = input("Continue ? (Y/N) : ")
        if ip.lower() == 'y':
            main()
        else:
            os.system('exit')

    elif option == 0:
        print('Invalid Choice :(')
        ip = input("Continue ? (Y/N) : ")
        if ip.lower() == 'y':
            main()
        else:
            os.system('exit')

    password_length = int(input("\nEnter the length of password to Generate: "))

    if password_length == 0:
        print('Invalid Password Length :(')
        ip = input("Continue ? (Y/N) : ")
        if ip.lower() == 'y':
            main()
        else:
            os.system('exit')
        


    final_password = core.Generate_Password(option, password_length)

    print('\n----------- Generated Password -----------')
    print('\n'+final_password+'\n')
    print('----------- Generated Password -----------')

    option2 = input("\nGenerate More ? (Y/N) : ")

    if option2.lower() == 'y':
        main()

    else:
        os.system('exit')

main()