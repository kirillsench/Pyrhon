import colorama



#це початок роботи з colorama , тобто ініціалізація

'''
from colorama import init
init()
'''



#атрибут Style
'''
from colorama import init, Style
init()
print(Style.BRIGHT + 'colorama') #робить текст жирним
'''


#атрибут Курсора , його налаштування
'''
from colorama import init
init()
from colorama import Cursor
print('I love python')
print(Cursor.FORWARD(7) + Cursor.UP(4) + Cursor.DOWN(2) + 'Курсор перейшов праворуч на 10 символів , у верх на 4, та вниз на 2')
'''


#атрибути Fore та Backround , налаштування тексту в плані кольору на фону
'''
from colorama import  Fore, Back, init
init()
print(Fore.BLUE + 'Text have blue color')
print(Back.YELLOW + 'Text have yellow background')
'''



