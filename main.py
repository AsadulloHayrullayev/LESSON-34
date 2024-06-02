                                       #LESSON 34
#1
# n = str(input('Gimme any number'))
# a = n*2
# b = n + a
# print(a)

#2
# a = 46
# b = 'string'
# print(a*2,b*2)
#
# #3
# a = (5,'F','Privet',90.2)
# b = {67}
# print(a[2])

#4
def fourth():
    user_chislo = input("Gimme 4-znchnoe chislo: ")

    if user_chislo.isdigit() and len(user_chislo) == 4:
        number = [int(number) for number in user_chislo]
        print("Cifri vashego chisla: ", number)
    else:
        print("eto ne 4-znachnoe chislo!")

fourth()

