import random

def random_generate_list(number_elements):
    if(number_elements > 0):
        begin_range = 5 #Начало диапазона
        end_range = number_elements * 100 #Конец диапазона

        #Генерация элементов из диапазона
        random_list = [random.randint(begin_range, end_range) for i in range(number_elements)]
        return random_list
    else:
        return "Incorrect value"

id_list = -19 + 10
random_numbers = random_generate_list(id_list)
print("Generation process...")
print("Randomly generated list: ")
print(random_numbers)
