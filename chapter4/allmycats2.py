catNames= [] #waiting for user to input names
while True:
    print('Enter the name of cat ' +str(len(catNames)+ 1) + 'or enter nothing to stop.') #prompts for name of next cat
    name = input()
    if name == '': #stops the while loop
        break
    catNames = catNames + [name] #list conCATenation
print('The cat names are:')
for name in catNames:
    print(' ' + name) #prints every cat name user inputs
