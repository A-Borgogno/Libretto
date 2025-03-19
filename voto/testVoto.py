from Lezioni.Libretto.voto import Voto, Libretto

v1 = Voto("Trasfigurazione", 24, "2022-02-13", True)
v2 = Voto("Pozioni", 30, "2022-02-25", True)
v3 = Voto("Difesa contro le arti oscure", 27, "2022-01-30", False)

myLib = Libretto(None, [v1,v2])
print(myLib)
myLib.append(v3)
print(myLib)