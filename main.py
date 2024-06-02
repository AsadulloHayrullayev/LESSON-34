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
# def fourth():
#     user_chislo = input("Gimme 4-znchnoe chislo: ")
#
#     if user_chislo.isdigit() and len(user_chislo) == 4:
#         number = [int(number) for number in user_chislo]
#         print("Cifri vashego chisla: ", number)
#     else:
#         print("eto ne 4-znachnoe chislo!")
#
# fourth()


# #5
# def info():
#     name = input("What is ur name ? ")
#     surname = input("What is ur surname ? ")
#     age = input("how old are u ? ")
#     print('ur name is',name)
#     print('ur surname is ', surname)
#     print('u r ', age ,"years old")
# info()

#6
def math():

    a = float(input("1st number: "))
    b = float(input("2nd number: "))
    c = float(input("3rd number: "))

    plus = a + b + c
    umn = a * b * c
    dele = a/b/c
    min = a-b-c

    print(plus)
    print(min)
    print(umn)
    print(dele)

math()
