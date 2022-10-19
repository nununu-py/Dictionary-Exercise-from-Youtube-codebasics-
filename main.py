# Question 1

data = {
    "China": 143,
    "India": 136,
    "USA": 32,
    "Pakistan": 21
}

ask_user = input("what do you want to do : ")

if ask_user.lower() == "print":

    for key in data:
        print(key, "-->>", data[key])
elif ask_user.lower() == "add":
    temp = {}
    country_name = input("enter a country name : ")
    population = int(input("enter a population : "))
    temp[country_name] = population

    for key1 in temp:
        list_key2 = []
        for key2 in data:
            list_key2.append(key2)
        if key1 in list_key2:
            print("Country Name is Already Exist")
        else:
            data[country_name] = population
            print("Your Data is Update\n", data)
elif ask_user.lower() == "remove":
    country_name = input("enter a country name : ")
    list_key = []

    for key in data:
        list_key.append(key)
    if key not in list_key:
        print("Input Country doesn't Exist")
    else:
        del data[country_name]
        print(f"Success Remove '{country_name}'\n", data)
elif ask_user.lower() == "query":
    country_name = input('enter a country name : ')
    list_key = list(data.keys())[0:]

    if country_name in list_key:
        print(f"{country_name} -->> {data[country_name]}")
else:
    print("Invalid Input")


# Question 2

global stock_price

stock_price = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}


def print_data():

    for key, value in stock_price.items():
        total = 0
        for i in value:
            total += i
        print(f"{key} ==>> {value} ==>> avg: {round(total/len(value), 2)}")


def add_data():

    key_input = input("what key do you want to insert : ")
    adding_value = int(input("what value do you want to insert : "))

    if key_input in stock_price:
        stock_price[key_input].append(adding_value)
    else:
        stock_price[key_input] = [adding_value]

    print(f"Your Data is Updated\n{stock_price}" )


command = input("what do you want to do (print or add) : ")

if command.lower() == "print":
    print_data()
elif command.lower() == "add":
    add_data()
else:
    print("Your Input Command is NOT Available")


# Question 3

PI = 22/7

def circle_calc(radius:int):
    
    area = PI * radius * radius
    circumference = 2 * PI * radius
    diameter = 2 * radius

    result = "circle area ==>> {}, circumference ==>> {}, diamter  ==>> {}"
    print(result.format(round(area, 3), round(circumference, 3) , \
        round(diameter, 3)))


radius = 5
call_funct = circle_calc(radius)
call_funct
