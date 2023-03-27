
Belgium = "Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German"
Belgium_pop = int(Belgium[8:16])
Brussels_pop = int(Belgium[26:32])
print(len(Belgium))
for characters in range(len(Belgium)):
    characters = "-"
    print(characters, end="")
print("")
print(Belgium.replace(",", ":"))
print(Brussels_pop + Belgium_pop)