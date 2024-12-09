korongok = []
tabla = []

for i in range(8):
    tabla.append([])
    for j in range(8):
        tabla[i].append("⬜")

while True:
    koordinata = ""
    sori = str(input(f"Adja meg a korong sorának számát: "))
    if sori == "":
        break
    else:
        oszlopi = str(input(f"Adja meg a korong oszlopának számát: "))
    koordinata = sori+"K"+oszlopi
    if koordinata in korongok:
        korongok.remove(koordinata)
    elif int(koordinata.split("K")[0])>=1 and int(koordinata.split("K")[0])<=8 and int(koordinata.split("K")[1])>=1 and int(koordinata.split("K")[1])<=8 and koordinata not in korongok:
        korongok.append(koordinata)
    else:
        print(f"Ezt a korongot nem lehet lerakni")
for koordinatak in korongok:
    tabla[int(koordinatak[0])-1][int(koordinatak[2])-1] = "⭕"
for sor in tabla:
    for korong in sor:
        print(korong, end="")
    print("")
