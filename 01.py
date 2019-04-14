# def find():
#     with open('numbers.txt') as f:
#         datafile = f.readlines()
    
#     for line in datafile:
#         if zvire in line:
#             position = (line.find(':'))
#             return ("Cislo na " + zvire + " je: " + line[(position+1):])
#     return "neni v seznamu"  

# zvire = input("Koho chces volat?: ")
# print(find())

def dict_from_txt():
    number_dict = {}
    with open('numbers.txt') as f:
        datafile = f.readlines()

    for line in datafile:
        (key, val) = line.split(":")
        number_dict[key] = int(val)
    return number_dict

def find_in_dict(number_dict):
    zvire = input("Koho chces volat?: ")
    if zvire in number_dict:
        print("Cislo na " + zvire + " je " + str(number_dict[zvire]))
    else:
        print("Nemam cislo na " + zvire)

number_dict = dict_from_txt()
find_in_dict(number_dict)
