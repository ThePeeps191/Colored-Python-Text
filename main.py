from termcolor import *


def p(text, color):
	print(colored(text, color))


p('Red Text', 'red')
p('Blue Text', 'blue')
p('Green Text', 'green')
p('Cyan Text', 'cyan')
p('White Text', 'white')
p('Yellow Text', 'yellow')

print("\n")

input_text = f'''{colored("What", 'red')} {colored("Is", 'blue')} {colored("Your", 'green')} {colored("Name", 'cyan')}{colored("?", 'white')}\n'''

name = input(input_text)
hello = colored("Hello,", 'red')
n = colored(name, 'blue')
ex = colored("!", 'green')
print(hello, n + ex)

print(colored('\n1 + 1 = 2', 'cyan'))
