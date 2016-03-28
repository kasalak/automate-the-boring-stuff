def spam():
    eggs = 'spam local'
    print(eggs)
def bacon():

    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
