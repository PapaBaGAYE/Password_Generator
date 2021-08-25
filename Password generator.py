import random

def generatePassword():
    """
    Cette fonction generatePassword(),
    permet de générer des mots de passe aléatoires.
    
    Caractères composants le mot de généré : 
            - Majuscules,
            - minicules,
            - chiffres,
            - symboles.

    Exemple :
            print(generatePassword())
            output : _i{g}/W5vSQs
    """

    letters = 'abcdefghijklmnopqrstuvwxyz'
    Maj = letters.upper()
    Min = letters.lower()
    numbers = "0123456789"
    symbols = '-_/[]{()}'

    concat = Maj + Min + numbers + symbols

    password_lenght = 12
    password_generated = "".join(random.sample(concat, password_lenght))

    return password_generated

print('-'*50 ,'\nGENERATION DE 10 MOT DE PASSES',"\n", '-'*49)
for i in range(1, 11):
    if i < 10:
        i = "0" + str(i)
    print(f'Password {i} - {generatePassword()}')
