import random, time
##Comment
class Solver:

    def numbertask(self):
        numbers = list(range(1,8))
        for n in numbers:
            print(n)
            if n == 5:
                break
    
    def wordstask(self):
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word)

    def rostics_load(self):
        count = 0
        for i in range(10):
            load = random.randint(0,100)
            print(load)

            if load > 85:
                print(f"Крылышки в опасности! Нагрузка - {load}")
                

practice = Solver()
##practice.numbertask()
##practice.wordstask()
practice.rostics_load()

numbers = [random.randint(1,100) for i in range(9)]

max_num = numbers[0]
for i in numbers:
    if i > max_num:
        max_num = i
print("MAX = " + str(max_num))

while len(numbers) > 1:
    if numbers[0] > numbers[1]:
        numbers.pop(1)
    else:
        numbers.pop(0)
    ##print(numbers)

print("MAX 2 = " + str(numbers[0]))