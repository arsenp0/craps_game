import random

def main():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    summ = x + y
    
    return x, y, summ

x, y, summ = main()

print(f"the summ of dice is: {x} + {y}: ", summ)

if (summ == 7 or summ == 11):
    print("You won!")
elif(summ == 2 or summ == 3 or summ == 12):
    print("Craps the casino wins!!!")
else:
    target = summ
    print(f"Now your goal is {target}")
    
    while True:
        x, y, summ = main()
        print(f"The sum of dice is: {x} + {y} = {summ}")

        if summ == target:
            print("You won!")
            break
        elif summ == 7:
            print("You lose!")
            break
