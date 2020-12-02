import random

def main():
    for i in range(0, 3):
        spinWheel()

def spinWheel():
    rand_num = random.randint(1, 20)
    output = ""

    if rand_num > 15:
        output = "Cherries"
    elif rand_num > 10:
        output = "Orange"
    elif rand_num > 5:
        output = "Plum"
    elif rand_num > 2:
        output = "Melon"
    elif rand_num > 1:
        output = "Bell"
    else:
        output = "Bar"
    
    print(output)

main()