import math

# String auflösen (in Bestandteile)
def split_str(eingabe:str):
    temp = ''
    zahlen = []
    operatoren = []
    for buchstabe in eingabe:
        if buchstabe in '+-*/':
            operatoren.append(buchstabe)
            zahlen.append(float(temp))
            temp = ''
        elif buchstabe not in '0123456789.':
            raise(Exception('Ungültige Eingabe!'))
        else: temp += buchstabe
    zahlen.append(float(temp))
    return zahlen, operatoren

if __name__ == '__main__':
    variablen = {
        'pi': math.pi,
        'e': math.e
    }
    while(True):
        eingabe = input('>>> ')
        eingabe = eingabe.replace(' ', '')
        if eingabe == 'exit' or eingabe == 'stop':
            break
        try:
            zahlen, operatoren = split_str(eingabe)
        except Exception as error:
            print(error)
            continue
        
        print(f'{zahlen=}')
        print(f'{operatoren=}')

