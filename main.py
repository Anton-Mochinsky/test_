# Задание 1.
# Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.

    # def unique_elements(input_list): 
    #     return list(set(input_list))

    # input_list = [1, 2, 2, 3, 4, 4, 5] 
    # print(unique_elements(input_list))


# Задание 2.
# Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.


# def prime_numbers_in_range(minimum, maximum):
#     primes = [] 
#     for num in range(minimum, maximum+1): 
#         if num > 1: 
#             for i in range(2, int(num**0.5)+1): 
#                 if num % i == 0: 
#                     break 
#             else:
#                 primes.append(num) 
#     return primes

# print(prime_numbers_in_range(1, 20))


# Задание 3.
# Создать класс Point, который представляет собой точку в двумерном пространстве. 
# Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки, а также для получения и изменения координат.

# import math

# class Point: 
#     def __init__(self, x=0, y=0): 
#         self.x = x 
#         self.y = y

#     def distance_to(self, other_point):
#         return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

#     def get_coordinates(self):
#         return (self.x, self.y)

#     def set_coordinates(self, x, y):
#         self.x = x
#         self.y = y

# point1 = Point(1, 2) 
# point2 = Point(4, 6) 
# print(point1.distance_to(point2))

# Задание 4.
# Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.

def sort_strings_by_length(strings): 
    return sorted(strings, key=lambda x: (len(x), x))

strings = ["abc", "ab", "abcd", "a"] 
sorted_strings = sort_strings_by_length(strings) 
print(sorted_strings)