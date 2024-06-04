# Homework 4

# 1

# wholeList = []
# def customerList():
#     i=1
#     while i<4:
#         if True:
#             name = input(f"Your name {i}: ")
#             lastName = input(f"Your Lastname {i}: ")
#             age = input(f"Your age {i}: ")
#             i+=1
#             wholeList.append(name)
#             wholeList.append(lastName)
#             wholeList.append(age)
#         else:
#             break
#
# customerList()
# print(wholeList)
#
# def getInfo():
#     askForInfo = int(input("Provide the index: "))
#     makeAnIndex = (askForInfo - 1)*3
#     if askForInfo in range(1,4):
#         print(f"""
#         Name: {wholeList[0 + makeAnIndex]}
#         Lastname: {wholeList[1 + makeAnIndex]}
#         Age: {wholeList[2 + makeAnIndex]}
#         """)
#     else:
#         print("Wrong Input")
#         getInfo()
#
# getInfo()

# /////////////////////////////////////////////////////////////

# 2
# შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული
# ცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი.
# თუ სიაში მოიძებნა მსახიობი, დაბეჭდe მის შესახებ
# არსებული ინფორმაცია რეზუმის სახით.

# listOfFame = [['angelina', 'jolie', 48, '1.69 m'],
#               ['brad', 'pitt', 60, '1.8 m'],
#               ['jennifer', 'aniston', 55, '1.64 m'],
#               ['jennifer', 'lawrence', 33, '1.75 m'],
#               ['emma', 'stone', 35, '1.68 m'],
#               ['ryan', 'gosling', 43, '1.84 m'],
#               ['jake', 'gyllenhaal', 43, '1.82 m'],
#               ['maggie', 'gyllenhaal', 46, '1.75 m'],
#               ['zendaya', 'maree stoermer coleman', 27, '1.78 m']
#               ]
#
#
# def findAFamousPerson():
#     inputName = input("""Write the name or the lastname of
#     the famous person you wish to know more about: """).lower()
#
#     for i in listOfFame:
#         if inputName == i[0] or inputName == i[1]:
#             print(f"""
#             Name: {i[0]}
#             Lastname: {i[1]}
#             Age: {i[2]}
#             Height: {i[3]}
#             """)
#             break
#     else:
#         print("Got no info on her/him/them")
#         findAFamousPerson()
#
# findAFamousPerson()


# /////////////////////////////////////////////////////////////

# 3
# შექმენი ფუნქცია რომელიც მიიღებს სიას და
# დააბრუნებს ასევე სიას, თუმცა უნიკალური
# ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
#
# def unique_list():
# ...
# return ...

# def myFunction():
#     a = []
#     while True:
#         answer = input("Type something or type quit to stop: ")
#         if answer == "quit":
#             break
#         else:
#             a.append(answer)
#     a = list(set(a))
#     a.sort()
#     return a
# result = myFunction()
# print(result)


# /////////////////////////////////////////////////////////////


# 4
# შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის
# მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს
# tuple ტიპის მონაცემად და დააბრუნებს შედეგს.
# def set_to_tuple():
# ...
# return ...

# def myFunction():
#     a = set()
#     while True:
#         answer = input("Type something for list 1 or type quit to stop: ")
#         if answer == "quit":
#             print("")
#             break
#         else:
#             a.add(answer)
#
#     b = set()
#     while True:
#         answer = input("Type something for list 2 or type quit to stop: ")
#         if answer == "quit":
#             print("")
#             break
#         else:
#             b.add(answer)
#
#     joinsets = a.union(b)
#     madeTuple = tuple(joinsets)
#     return madeTuple
# result = myFunction()
# print(result)

# /////////////////////////////////////////////////////////////

# 5
# დაწერე პროგრამა, რომელიც შეამოწმებს გადაცემული
# ლექსიკონი არის თუ არა ცარიელი.

# dict = {'a': 1, 'b' : 2}
# # dict = {}
# def checkIfEmpty():
#     if dict == {}:
#         return "empty"
#     else:
#         return "not empty"
#
# print(checkIfEmpty())


# /////////////////////////////////////////////////////////////


# 6
# დაწერე პროგრამა რომელიც სტრიქონისგან ქმნის
# ლექსიკონს.
# დათვალე სტრიქონში კონკრეტული სიმბოლოს
# ოდენობა.

# word = input("Word: ")
# myDict = {}
# for i in word:
#     if i in myDict:
#         myDict[i]+=1
#     else:
#         myDict[i]=1
# print(myDict)


# /////////////////////////////////////////////////////////////

# 7
# შექმენი while ციკლი, რომელიც მომხმარებელს ხუთჯერ
# შემოატანინებს ინფორმაციას და ჩაამატებს ცარიელ
# სიაში. შედეგი დაბეჭდე. (append მეთოდი)

# wholeList = []
# def customerList():
#     i=1
#     while i<6:
#         if True:
#             info = input(f"Info {i}: ")
#             i+=1
#             wholeList.append(info)
#         else:
#             break
#
# customerList()
# print(wholeList)

# /////////////////////////////////////////////////////////////

# 8
# მიღებული სიის პირველ და ბოლო ელემენტებს ადგილი
# შეუცვალე და დაბეჭდე შედეგი.
# წაშალე სიაში მომხმარებლის მიერ მოთხოვნილი
# ელემენტი. (remove მეთოდი)

# a = [1, 2, 3, 4, 5]
# n = len(a)
#
# firstEl = a[0]
# a[0] = a[n-1]
# a[n-1] = firstEl
#
# print(a)
# removeEl = input("Which element do you want to remove: ")
# if removeEl.isdigit():
#     removeEl = int(removeEl)
#     if removeEl in a:
#         a.remove(removeEl)
#         print(a)
#     else:
#         print("No such element here")
# else:
#     print("Please enter a digit")