print('Start')
print('Enter password')

passwordCorrect=False

while not passwordCorrect:
    password=input()    
    if password=='PonyParty':
        print('Correct')
        passwordCorrect=True
    else:
        print('Incorrect try again')

print(' What color is your favorite pony? ')
pony=input()
print ('What is your ponys favorite food?')
food=input()
print('Based on your anwsers your favorite pony is '+pony+' '+food)
