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


def calculate(zahlen, operatoren):
    a = 0
    while a < len(operatoren):
        if a == 0:
            if operatoren[a] == '+':
                b = zahlen[0] + zahlen[1]
            elif operatoren[a] == '-':
                b = zahlen[0] - zahlen[1]
            elif operatoren[a] == '*':
                b = zahlen[0] * zahlen[1]
            elif operatoren[a] == '/':
                b = zahlen[0] / zahlen[1]
        else:
            if operatoren[a] == '+':
                b = b + zahlen[a+1]
            elif operatoren[a] == '-':
                b = b - zahlen[a+1]
            elif operatoren[a] == '*':
                b = b * zahlen[a+1]
            elif operatoren[a] == '/':
                b = b / zahlen[a+1]
            
        a = a + 1
    
    return b       



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

        ergebnis = calculate(zahlen, operatoren)

        print(f'{ergebnis=}')
