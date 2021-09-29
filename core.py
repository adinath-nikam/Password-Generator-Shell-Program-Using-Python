import string
import random

def core(password, passwordList, passLength):
    for passChar in range(passLength):
        passRandom = random.choice(password)
        passwordList.append(passRandom)

    finalOutput = "".join(passwordList)
    return finalOutput

def Generate_Password(option, passLength):

    if option == 1:
        password = string.ascii_letters
        passwordList = []
        return core(password, passwordList, passLength)

    elif option == 2:
        password = string.digits
        passwordList = []
        return core(password, passwordList, passLength)

    elif option == 3:
        password = "!@#$%^&*()_+=-./?><|\}{[]"
        passwordList = []
        return core(password, passwordList, passLength)

    elif option == 4:
        password = string.ascii_letters + string.digits
        passwordList = []
        return core(password, passwordList, passLength)

    elif option == 5:
        password = string.ascii_letters + "!@#$%^&*()_+=-./?><|\}{[]"
        passwordList = []
        return core(password, passwordList, passLength)

    elif option == 6:
        password = string.digits + "!@#$%^&*()_+=-./?><|\}{[]"
        passwordList = []
        return core(password, passwordList, passLength)

    elif option == 7:
        password = string.ascii_letters + string.digits + "!@#$%^&*()_+=-./?><|\}{[]"
        passwordList = []
        return core(password, passwordList, passLength)

    else:
        print("Invalid Choice :(")