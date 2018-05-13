print ("************************************************")
print ("*This is a practice list making for dictionaries")
print ("************************************************")

term = {}
while True:
    enter = input("Enter a term or look up one?(1,2)")
    if enter =="1":    
    
    
        short_hand = input("Enter the term:")
        full_pharse = input("Enter the definition:")
        term[short_hand]=full_pharse
        print("ok",short_hand, "saved to term!")

        
    elif enter == "2":
        look_up = input("what term do you want to know?")
        if look_up in term:
            print(look_up, "The term is %s" % term[look_up])
        else:
            print(look_up, " term isn't define yet!")
    yn = input("Do you want to add another item?")
    if yn == "n":
        break