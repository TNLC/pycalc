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


# Rechnen
# Punkt vor Strich
def calculate(zahlen, operatoren):
    # MULTIPLIZIEREN UND DIVIDIEREN
    neueZahlen = []
    neueOperatoren = []
    last_prio = False
    i = 0
    while i < len(operatoren):
        if operatoren[i] == '*':
            if last_prio:
                a = neueZahlen[-1] * zahlen[i+1]
                neueZahlen[-1] = a
            else:
                a = zahlen[i] * zahlen[i+1]
                neueZahlen.append(a)
            last_prio = True
        elif operatoren[i] == '/':
            if last_prio:
                a = neueZahlen[-1] / zahlen[i+1]
                neueZahlen[-1] = a
            else:
                a = zahlen[i] / zahlen[i+1]
                neueZahlen.append(a)
            last_prio = True
        else:
            if not last_prio:
                neueZahlen.append(zahlen[i])
            neueOperatoren.append(operatoren[i])
            last_prio = False
        i = i + 1
    
    # ADDIEREN UND SUBTRAHIEREN
    a = 0
    b = None
    while a < len(neueOperatoren):
        if a == 0:
            if neueOperatoren[a] == '+':
                b = neueZahlen[0] + neueZahlen[1]
            elif neueOperatoren[a] == '-':
                b = neueZahlen[0] - neueZahlen[1]
        else:
            if neueOperatoren[a] == '+':
                b = b + neueZahlen[a+1]
            elif neueOperatoren[a] == '-':
                b = b - neueZahlen[a+1]
            
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

        
