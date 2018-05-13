phone_number = {
    "james": "945-394-2356",
    "miranda": "648-384-2345",
    "gandalf": "800-124-3165",
    "frodo": "678-121-1212",
    "aragon": "123-456-7890",
    "legolas": "098-765-4321"
    }
while True:
    
    name = input("What is the name of the phone number?")
    number = input("What is the phone number?")
    phone_number[name]=number
    yn= input("Do you want to add another?")
    if yn == "n":
        break
look_up = input("Who's number are you looking for?")
if look_up in phone_number:
    print(look_up,"phone number is: %s" % phone_number[look_up])
else:
    print (look_up, "phone number not found.")
result = phone_number["james"]
print ("This is James phone number",result)
result = phone_number["miranda"]
print ("This is Miranda's phone number",result)