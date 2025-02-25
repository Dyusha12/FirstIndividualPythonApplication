import random

id_list = 19

begin_range = 5 #Начало диапазона
end_range = id_list * 100 #Конец диапазона
number_elements = id_list + 10 #Количество элементов

#Генерация элементов из диапазона
random_list = [random.randint(begin_range, end_range) for i in range(number_elements)]
print("Generation process...")
print("Randomly generated list: ")
print(random_list)
