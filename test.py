import datetime
def meow():
    print("Hello motherfuckers.")
    print("Please type motherfucker below to confirm you are one of us.")
    client_input = input(" ").lower()
    if(client_input == "motherfucker"):
        print("Welcome to motherfucker land.")
    else:
        print("You're a fatherfucker.")

# meow()

object_example = {
    "name": "Eric",
    "age": 100
}

print(object_example["age"])

list = [1, 2, 2]

print(list.count(2))

print(datetime.datetime.now().isoweekday())