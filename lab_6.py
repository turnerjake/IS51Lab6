import random

total_earned = 0

def main():
    results = []
    for i in range(0, 3):
       results.append(spinWheel())
    print(results)

    winner = jackpot(results)
    if winner:
        print("You win!")
    else:
        print("Sorry, please try again")
    
    res = count()
    option = input("Play again? ")

    if option.lower == "y" or option.lower == "yes":
        main()


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
    
    return output

def jackpot(results):
    return results[0] == results[1] == results[2]

def count(results):
    total = 0
    money_dict = {
        "Cherries": 1,
        "Orange": .7,
        "Plum": .6,
        "Bell": .4,
        "Melon": .2,
        "Bar": .1
    }

    for i in results:
        total += money_dict[i]
    print(total)
    return total + total_earned

main(total_earned)