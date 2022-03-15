import os
os.system('')  # this will change the font colors in windows CMD.


def intro():
    print('''

\u001b[33m*\u001b[0m                                          \u001b[33m*\u001b[0m        
                                   \u001b[33m*\u001b[0m
\u001b[31m
                                                           888          
                                                           888          
                                                           888          
 .d88b.   .d8888b  .d88b.  88888b.   .d8888b  .d88b.   .d88888  .d88b.  
d8P  Y8b d88P"    d88""88b 888 "88b d88P"    d88""88b d88" 888 d8P  Y8b 
88888888 888      888  888 888  888 888      888  888 888  888 88888888 
Y8b.     Y88b.    Y88..88P 888  888 Y88b.    Y88..88P Y88b 888 Y8b.     
 "Y8888   "Y8888P  "Y88P"  888  888  "Y8888P  "Y88P"   "Y88888  "Y8888  
\u001b[0m
                                    \u001b[33m*\u001b[0m 
\u001b[33m*\u001b[0m                  
                                                                      \u001b[33m*\u001b[0m 
\n\n''')

    print('''
\u001b[33m
Calculate Options: 

+---------------------------------------+
+                                       +
+   Price elasticity of demand   -  1   +
+   Cross elasticity of demand   -  2   +
+   Income elasticity of demand  -  3   +
+   Price elasticity of Supply   -  4   +
+                                       +
+---------------------------------------+

Input Format:

Use persentage% value or before_value <space> after_value. (e.g. 100 200)
(persentage values must have % symbol at the end of the value. e.g. 20%)
\u001b[0m''')


def getElasticity(numerator, denominator, is_abs=False):
    persentage_numerator = 0
    persentage_denominator = 1  # avoiding zero devided by zero error.

    if not numerator.endswith('%'):
        b, a = [float(x) for x in numerator.split(' ')]
        persentage_numerator = (a - b) * 100 / b
    else:
        persentage_numerator = float(numerator[:-1])

    if not denominator.endswith('%'):
        b, a = [float(x) for x in denominator.split(' ')]
        persentage_denominator = (a - b) * 100 / b
    else:
        persentage_denominator = float(denominator[:-1])

    if not persentage_denominator:
        return 'infinity'

    elasticity = round(persentage_numerator / persentage_denominator, 3)
    if is_abs:
        elasticity = abs(elasticity)
    return elasticity


def getNature(elasticity, option):
    nature = ''

    if option == '1' or option == '4':
        if elasticity == 'infinity':
            nature = 'Perfectly Elastic'
        elif elasticity == 0:
            nature = 'Parfectly Inelastic'
        elif elasticity == 1:
            nature = 'Unitary elastic'
        elif elasticity > 1:
            nature = 'Elastic'
        elif elasticity < 1:
            nature = 'Inelastic'
    elif option == '2':
        if elasticity > 0:
            nature = 'Substitutable goods'
        elif elasticity < 0:
            nature = 'Complementary goods'
        elif elasticity == 0:
            nature = 'No relationship between goods'
    elif option == '3':
        if elasticity > 1:
            nature = 'Normal and Luxuries'
        elif elasticity > 0:
            nature = 'Normal and Necessities'
        elif elasticity < 0:
            nature = 'Inferior goods'

    return nature


def init():
    is_abs = False
    while(True):
        option = input("\nwhat do you want to calculate: ")

        if option == '1':
            numerator_input_string = 'Enter demand change: '
            denominator_input_string = 'Enter price change: '
            output_string = 'Price elasticity of demand (PED) is '
            is_abs = True
        elif option == '2':
            numerator_input_string = 'Enter demand change of good X: '
            denominator_input_string = 'Enter price change of good Y: '
            output_string = 'Cross elasticity of demand (XED) is '
            is_abs = False
        elif option == '3':
            numerator_input_string = 'Enter demand change: '
            denominator_input_string = 'Enter income change: '
            output_string = 'Income elasticity of demand (YED) is '
            is_abs = False
        elif option == '4':
            numerator_input_string = 'Enter quantity supplied change: '
            denominator_input_string = 'Enter price change: '
            output_string = 'Price elasticity of Supply (PES) is '
            is_abs = True
        else:
            print("Invalid option!")
            continue

        denominator = input(denominator_input_string).strip()
        numerator = input(numerator_input_string).strip()

        elasticity = getElasticity(numerator, denominator, is_abs)

        print(output_string, '\u001b[33m', elasticity, '\u001b[0m')
        print(
            'Nature of the Elasticity is ',
            '\u001b[33m',
            getNature(elasticity, option),
            '\u001b[0m')

        is_exit = input('\nDo you want to exit (y or n): ')
        if is_exit == 'Y' or is_exit == 'y':
            break


if __name__ == '__main__':
    intro()
    init()
