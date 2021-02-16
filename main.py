import math

# String auflösen (in Bestandteile)
def split_str(eingabe:str):
    temp = ''
    zahlen = []
    operatoren = []
    for buchstabe in eingabe:
        if buchstabe in '+-*/()':
            operatoren.append(buchstabe)
            if len(temp) > 0:
                zahlen.append(float(temp))
                temp = ''
        elif buchstabe not in '0123456789.':
            raise(Exception('Ungültige Eingabe!'))
        else: temp += buchstabe
    if eingabe[-1] != ')': zahlen.append(float(temp))
    return zahlen, operatoren

# ['+', '-', '(', '+', ')', '*']
# [1, 2, 3, 4, 5]
# ['+', '-', '*']
# [1, 2, 7, 5]
# ['+', '-']
# [1, 2, 35]
# -32

# Rechnen
# Punkt vor Strich mit Klammern
def calculate(zahlen, operatoren):
    print(f'{zahlen=}')
    print(f'{operatoren=}')
    # KLAMMERN
    klammer_anzahl = 0
    for operator in operatoren: 
        if operator in '()': klammer_anzahl += 1
    klammer_index = None
    offene_klammern = 0
    erste_klammer_offen = False
    x = 0
    while x < len(operatoren):
        if operatoren[x] == "(":
            if not erste_klammer_offen:
                klammer_index = x
                erste_klammer_offen = True
            offene_klammern = offene_klammern + 1
        
        elif operatoren[x] == ")":
            if not erste_klammer_offen:
                raise(Exception('Ungültige Eingabe!'))
            offene_klammern = offene_klammern - 1
            if offene_klammern == 0:
                # ZAHLEN ABGREIFEN
                klammer_zahlen = []
                for n in range(klammer_index, x - klammer_anzahl - 2):
                    klammer_zahlen.append(zahlen[n])

                # OPERATOREN ABGREIFEN
                klammer_operatoren = []
                for n in range(klammer_index + 1, x):
                    klammer_operatoren.append(operatoren[n])

                # ERGEBNIS BERECHNEN (REKURSIV)
                klammer_ergebnis = calculate(klammer_zahlen, klammer_operatoren)
                
                # BEREITS BERECHNETES LÖSCHEN
                del zahlen[klammer_index:x]
                del operatoren[klammer_index:x+1]
                
                # ERGEBNIS IN ZAHLEN EINFÜGEN
                zahlen.insert(klammer_index, klammer_ergebnis)

        x = x + 1

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
            if len(zahlen)-1 == i+1 and operatoren[i] not in '*/':
                neueZahlen.append(zahlen[i+1])
            neueOperatoren.append(operatoren[i])
            last_prio = False
        i = i + 1
    
    # ADDIEREN UND SUBTRAHIEREN
    print(f'{neueOperatoren=}')
    print(f'{neueZahlen=}')
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
    
    if a == 0:
        b = neueZahlen[0]
    
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
        
        ergebnis = calculate(zahlen, operatoren)
        print(f'{ergebnis=}')

        
