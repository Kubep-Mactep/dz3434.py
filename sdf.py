import colorama

colorama.init()

print("Доступні атрибути та методи в colorama:")
print(dir(colorama))

print("Атрибути та методи Fore:", dir(colorama.Fore))
print("Атрибути та методи Back:", dir(colorama.Back))
print("Атрибути та методи Style:", dir(colorama.Style))

from colorama import Fore, Back, Style

print(Fore.BLACK + 'Цей текст буде чорним')
print(Back.WHITE + 'Цей текст буде з білим фоном')
print(Style.BRIGHT + 'Яскравий текст' + Style.RESET_ALL)