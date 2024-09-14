import time

p1 = 2
p2 = 3
k1 = 5
k2 = 2
N = p1**k1 * p2 **k2

Namen = [""] * 2
for i in range(2):
    Namen[i] = input(f"Name vom {i+1}. Spieler? ")

Teiler = [N]

def Ziffer(Z, x, y, G):
    """
    Die Ziffer Z wird in die Position (x,y) mit Größe G geschrieben.
    """
    D = [[1,1,1,0,1,1,1], # 0
        [0,0,1,0,0,1,0], # 1
        [1,0,1,1,1,0,1], # 2
        [1,0,1,1,0,1,1], # 3
        [0,1,1,1,0,1,0], # 4
        [1,1,0,1,0,1,1], # 5
        [1,1,0,1,1,1,1], # 6
        [1,0,1,0,0,1,0], # 7
        [1,1,1,1,1,1,1], # 8
        [1,1,1,1,0,1,1]] # 9
    NW = Point(x-G/4, y+G/2)
    NW.is_visible = False
    NO = Point(x+G/4, y+G/2)
    NO.is_visible = False
    W = Point(x-G/4, y)
    W.is_visible = False
    O = Point(x+G/4, y)
    O.is_visible = False
    SW = Point(x-G/4, y-G/2)
    SW.is_visible = False
    SO = Point(x+G/4, y-G/2)
    SO.is_visible = False
    V = [[NW, NO], [NW, W], [NO, O], [W, O], [W, SW], [O, SO], [SW, SO]]
    for i in range(7):
        if D[Z][i] == 1:
            Segment(V[i][0], V[i][1])

def Zahl(Z, x, y, G):
    while Z > 0:
        Ziffer(Z % 10, x, y, G)
        Z = int(Z/10)
        x = x - G

def PfzP(n):
    """
    Berechnet die Primfaktorpotenzen für die Zahl n.
    Falls n=p1^l1*p2^l2, wird [l1,l2] zurückgegeben.
    """
    global p1,p2
    l1 = 0
    l2 = 0
    while n % p1 == 0:
        l1 += 1
        n /= p1
    while n % p2 == 0:
        l2 += 1
        n /= p2
    return [l1,l2]

S = [[None for i in range(k2+1)] for j in range(k1+1)]
for i in range(1, int(N / 2) + 1):
    if N % i == 0:
        Teiler.append(i)

Teiler.sort()
        
for i in Teiler:
    [l1,l2] = PfzP(i)
    P = Point(l1,l2)
    P.is_visible = False
    Q = Point(l1+1,l2)
    Q.is_visible = False
    V = Polygon(P, Q, 4)
    V.opacity = 0.7
    if i == N:
        V.color = "black"
    S[l1][l2] = V
    Zahl(i, l1+0.9, l2+0.5, 0.2)
    time.sleep(0)

def Zug(Spieler):
    richtig = False
    while not richtig:
        Antwort = input("Die erlaubten Züge sind:\n" + str(Teiler) + "\n" +
            "Dein nächster Zug, lieber Spieler " + Spieler + "?")
        richtig = (check_user_input(Antwort) != 0)
    if int(Antwort) == N:
        print("Du hast verloren!")
        quit()
    # Laut Spielregel löschen wir alle Teiler von "Antwort" in "Teiler":
    for i in range(1, int(Antwort)+1):
        if (int(Antwort) % i == 0) and (i in Teiler):
            Teiler.remove(i)
            P = PfzP(i)
            S[P[0]][P[1]].opacity = 0.2
            time.sleep(0.1)

def check_user_input(input):
    # Siehe https://pynative.com/python-check-user-input-is-number-or-string/
    val = 0
    try:
        val = int(input)
        if not (val in Teiler):
            print("Diese Zahl ist nicht erlaubt!")
            val = 0
    except ValueError:
        print("Eine ganze Zahl sollte eingetippt werden!")
    return val

Ende = False
s = 0

while not Ende:
    Zug(Namen[s])
    s = 1 - s
