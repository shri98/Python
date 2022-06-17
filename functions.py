# def fib(n):
"""
        Function for Fibonacci
"""

#     a, b = 0,1
#     l =[]
#     while a<n:
#         l.append(a)
#         a,b = b, a+b
#
#     return l
# n = int(input("Enter the number upto print the series:\t"))
# print(fib(n))
"""
        default arguments
"""

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)

"""
        Keyword Argument
"""
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

###    Valid Calling of Function
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

###   Invalid Calling of Function
## parrot()                     # required argument missing
## parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
## parrot(110, voltage=220)     # duplicate value for the same argument
## parrot(actor='John Cleese')  # unknown keyword argument

"""
        formal arguments, positional arguments ,fianl formal keyword arguments
"""
# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
#
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")


"""
        Special Parameters
"""

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):      #(positional only, positional or keyword, keyword only)

# def standard_arg(arg):                                #(standard argument)
#     print(arg)

# def pos_only_arg(arg, /):                             #(positional only)
#      print(arg)

# def kwd_only_arg(*, arg):                             #(keyword only)
#     print(arg)

# def combined_example(pos_only, /, standard, *, kwd_only): #combined
#     print(pos_only, standard, kwd_only)


"""
        Lambda Function/Anonymous Function
"""

def inc(n):
    return lambda x: x+n

f = inc(4)
print(f(5))
