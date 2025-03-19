from Lezione01 import Student
from voto.voto import Libretto, Voto

Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
myLib = Libretto(Harry, [])

v1 = Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)
v2 = Voto("Babbanologia", 21, "2022-02-12", False)
myLib.append(v1)
myLib.append(v2)
myLib.append(Voto("Pozioni", 21, "2022-06-14", False))

myLib.calcolaMedia()

votiFiltrati = myLib.getVotiByPunti(21)
print(votiFiltrati)

votoPozioni = myLib.getVotoByName("Pozioni")
if votoPozioni is None:
    print("Voto non trovato")
else:
    print(votoPozioni.materia)

print("Test metodo hasVoto")
print(myLib.hasVoto(v1))
print(myLib.hasVoto(Voto("Aritmanzia", 30, "2023-07-10", False)))
print(myLib.hasVoto(Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)))
print("Test metodo hasConflitto")
print(myLib.hasConflitto(Voto("Difesa contro le arti oscure", 21, "2022-01-30", False)))

print("Test append modificata")
myLib.append(Voto("Aritmanzia", 30, "2023-07-10", False))
# myLib.append(Voto("Difesa contro le arti oscure", 21, "2022-01-30", False))


myLib.append(Voto("Divinazione", 27, "2021-02-08", False))
myLib.append(Voto("Cura delle creature magiche", 26, "2021-06-14", False))
print("--------------------------------")
print("Libretto originario")
print(myLib)

nuovoLib = myLib.creaMigliorato()
print("--------------------------------")
print("Libretto migliorato")
print(nuovoLib)

print("--------------------------------")
print("Libretto originario")
print(myLib)

print("--------------------------------")
ordinato = myLib.creaLibOrdinatoPerMateria()
print("libretto ordinato per materia")
print(ordinato)

print("--------------------------------")
ordinato2 = myLib.creaLibOrdinatoPerVoto()
print("libretto ordinato per voto")
print(ordinato2)

print("-------------------------------")
print("Libretto a cui ho eliminato i voti inferiori a 24")
ordinato2.cancellaInferiori(24)
print(ordinato2)