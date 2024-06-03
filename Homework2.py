# homework 2
# ////////////////////////////////////////////////////////////////////////////////////////////
# 1

# answer = input(f"""
# რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?”
# სავარაუდო პასუხები:
# 1. შუმერთა
# 2. სელჩუკთა
# 3. რომის
# 4. მონღოლთა
#
# შეიყვანეთ პასუხის ნომერი ან თავად პასუხი:
# """)
#
# if answer == '3' or answer == 'რომის':
#     print("სწორია")
# else:
#     print('არა, სწორი პასუხია რომის!')

# ////////////////////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////////////////////////
# 2

# categoryChooser = input(f"""
# Choose your deisered category:
# 1. Laptop
# 2. PC
# 3. Mobile
#
# Type category number or name here:
# """).lower()
#
# laptops = ['Lenovo', 'HP', 'Mac']
# laptopPrices = [1000, 2000, 3000]
#
# pcs = ['pc1', 'pc2', 'pc3']
# pcPrices = [1000, 2000, 3000]
#
# mobile = ['iphone11', 'iphone12', 'iphone13']
# mobilePrices = [1000, 2000, 3000]
#
# i=0
# while i<3:
#     if categoryChooser == '1' or categoryChooser == 'laptop':
#         budget = int(input("What's your budget?"))
#
#         if budget >= laptopPrices[0] and budget <= laptopPrices[1]:
#             print(f"Here's what we can offer:{laptops[0]} for {laptopPrices[0]}$")
#             break
#         elif budget >= laptopPrices[1] and budget <= laptopPrices[2]:
#             print(f"Here's what we can offer:{laptops[0]} for {laptopPrices[0]}$ or {laptops[1]} for {laptopPrices[1]}$")
#             break
#         elif budget >= laptopPrices[2]:
#             print(f"Here's what we can offer:{laptops[0]} for {laptopPrices[0]}$, {laptops[1]} for {laptopPrices[1]}$ or {laptops[2]} for {laptopPrices[2]}$")
#             break
#         else:
#             print("We couldn't find product matching your budget")
#             break
#
#
#     elif categoryChooser == '2' or categoryChooser == 'pc':
#         budget = int(input("What's your budget?"))
#
#         if budget >= pcPrices[0] and budget <= pcPrices[1]:
#             print(f"Here's what we can offer:{pcs[0]} for {pcPrices[0]}$")
#             break
#         elif budget >= pcPrices[1] and budget <= pcPrices[2]:
#             print(f"Here's what we can offer:{pcs[0]} for {pcPrices[0]}$ or {pcs[1]} for {pcPrices[1]}$")
#             break
#         elif budget >= pcPrices[2]:
#             print(f"Here's what we can offer:{pcs[0]} for {pcPrices[0]}$, {pcs[1]} for {pcPrices[1]}$ or {pcs[2]} for {pcPrices[2]}$")
#             break
#         else:
#             print("We couldn't find product matching your budget")
#             break
#
#
#     elif categoryChooser == '3' or categoryChooser == 'mobile':
#         budget = int(input("What's your budget?"))
#
#         if budget >= mobilePrices[0] and budget <= mobilePrices[1]:
#             print(f"Here's what we can offer:{mobile[0]} for {mobilePrices[0]}$")
#             break
#         elif budget >= mobilePrices[1] and budget <= mobilePrices[2]:
#             print(f"Here's what we can offer:{mobile[0]} for {mobilePrices[0]}$ or {mobile[1]} for {mobilePrices[1]}$")
#             break
#         elif budget >= mobilePrices[2]:
#             print(f"Here's what we can offer:{mobile[0]} for {mobilePrices[0]}$, {mobile[1]} for {mobilePrices[1]}$ or {mobile[2]} for {mobilePrices[2]}$")
#             break
#         else:
#             print("We couldn't find product matching your budget")
#             break
#
#
#     else:
#         print("Not a category")
#         break

# ////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////////////////////////
# 3

# errorMessage = "Didn't get it, sorry"
#
# voteUnderQuestion = input("Hi there, will you be voting in this election? (yes/no)").lower()
# if voteUnderQuestion == 'no':
#     whyNotVote = input("do you choose not to or just can't get there?(choose / can't)").lower()
#     if whyNotVote == 'choose':
#         print('well, ok, such a shame')
#     elif whyNotVote == "can't":
#         print('too bad')
#     else:
#         print(errorMessage)
# elif voteUnderQuestion == 'yes':
#     yesToVote = input("slay queen/king, wait a sec, did you sell your vote for money? (yes/no)").lower()
#     if yesToVote == 'yes':
#         print(f"""shame on you, your vote and voice is yours and only yours,
#         make a choice for your future, not for todays meal, got nothing else to say to you""")
#     elif yesToVote == 'no':
#         haventSold = input(f"""that's more like it, good to hear.
#         are you going prepared or you need some help?(help/no help)""").lower()
#         if haventSold == "no help":
#             print("great! see you in the bringht future")
#         elif haventSold == "help":
#             needHelp = input("ok sure, how can I help? do you know who are the bad guys? (yes / no)").lower()
#             if needHelp == "yes":
#                 print(f"""ok, in that case just support someone from good guys,
#                 they gotta get at least 5% or so manny votes will be lost""")
#             elif needHelp == "no":
#                 couldIHelp = input(f"""watch out for numbers: (imagine bad guy numbers here),
#                 those are the bad guys, (here please imagine that I've offered you some good numbers too)
#                 these numbers should be fine to vote for, just look them up and make your choise.
#                 btw was I any helpfull?""").lower()
#                 if couldIHelp == "no":
#                     print("oh well, I tried")
#                 elif couldIHelp == "yes":
#                     print("you just made my day, გავიმარჯვებთ სახელოვნად!")
#                 else:
#                     print(errorMessage)
#     else:
#         print(errorMessage)
#
# else:
#     print(errorMessage)

# ////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////////////////////////
# 4

# careerMatching = input("""Hi there, since yuo're here it seems like
# you need some help choosing your future career, I'll be asking some
# questions to help you figure this out. Choose subject you love the most,
# and actually enjoyed (math / physics / chemistry / biology / history / literature / languages )""").lower()
# if careerMatching == "math":
#     mathLover = input("""since you're good at math you can probably do about anything,
#     but on a more serious note, you can think about being one of these things:
#     Math teacher / Architect / Business person / Scientist / Engineer /
#     Do you like to teach? or maybe making sketches? would you imagine yourself doing a science research?
#     or building stuff? or managing a business?
#     (answer range: teach / sketching / science / building / business)""").lower()
#     if mathLover == "teach":
#         print("you could be a Math teacher or a lecturer")
#     elif mathLover == "sketching":
#         print("you could be an Architect")
#     elif mathLover == "science":
#         print("you could be a Scientist")
#     elif mathLover == "building":
#         print("you could be an Engineer")
#     elif mathLover == "business":
#         print("you could be a Business person")
#     else:
#         print("Wrong input")
#
# elif careerMatching == "physics":
#     physicsLover = input("""since you love physics, you will probably do well in:
#     Science / Medicine / Engineering / Architecture / Teaching / or anything else you might wish to become!
#     Do you like to teach? or maybe making sketches? would you imagine yourself doing a science research?
#     or building stuff? ever had a dream of being a doctor?
#     (answer range: teach / sketching / science / building / doctor)""").lower()
#     if physicsLover == "teach":
#         print("you could be a Physics teacher or a lecturer")
#     elif physicsLover == "sketching":
#         print("you could be an Architect")
#     elif physicsLover == "science":
#         print("you could be a Scientist")
#     elif physicsLover == "building":
#         print("you could be an Engineer")
#     elif physicsLover == "doctor":
#         print("you could be a Doctor")
#     else:
#         print("Wrong input")
#
# elif careerMatching == "chemistry":
#     print("""since you love chemistry, you will probably do well in:
#     Physiotherapy / Science / Medicine / Veterinary / Engineering / Pharmacy""")
# elif careerMatching == "biology":
#     print("""since you love biology, you will probably do well in:
#     Physiotherapy / Nursing / Science / Medicine / Dentistry / Pharmacy / Veterinary / Psychology""")
# elif careerMatching == "history":
#     print("since you love history, you will probably do well in: Law / Teaching")
# elif careerMatching == "literature":
#     print("since you love literature, you will probably do well in: Teaching / Acting")
# elif careerMatching == "languages":
#     whichLanguage = input("Which language do you love?")
#     if whichLanguage:
#         print(f"""{whichLanguage} is a great language to learn! it will be very helpful
#         for a career in tourism and also you could teach {whichLanguage}""")
# else:
#     print("sorry, didn't catch that")

# ////////////////////////////////////////////////////////////////////////////////////////////