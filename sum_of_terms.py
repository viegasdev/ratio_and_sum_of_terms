#First prints
print('Hello! Choose one of the formulas above!')
print('''Your options are:
[0] Ratio
[1] Sum of terms''')
#Choose the formula 
formula = int(input('Insert the number of the pretended formula: '))
#Ratio input and calculation
if formula == 0:
    up = float(input('Insert the "up" of your succession: '))
    uq = float(input('Insert the "uq" of your succession: '))
    p = float(input('Insert the "p" of your succession: '))
    q = float(input('Insert the "q" of your succession: '))
    ratio = (up-uq)/(p-q)
    #Ratio output
    if ratio > 0:
        print('Your ratio is {} and your succession is a strictly growing one!'. format(ratio))

    elif ratio < 0:
        print('Your ratio is {} and your succession is a strictly decreasing one!'.format(ratio))
    
    elif ratio == 0:
        print('Your ratio is {} and your succession is a constant one!'.format(ratio))
#Sum of terms input and calculation
elif formula == 1:
    u1 = float(input('Insert the "u1" of your succession: '))
    un = float(input('Insert the "un" of the last number that you wanna have on the sum: '))
    n = float(input('Insert the "n" of the last number that you wanna have on the sum: '))
    soma = (u1+un)/2*n
    #Sum of terms output
    print('The value of the sum of n terms is {}!'.format(soma))
#Error message for no correspondent options
else:
    print('WARNING: The selected number is not a valid option, please try again!')
#Final credit print
print('Made by Rodrigo Viegas (viegasdev on github), thanks for using!')
input('Press ENTER to close.')