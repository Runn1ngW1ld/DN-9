print "Pozdravljeni v urejevalniku dnevnega menija"

meni = {}

while True:

    jed = raw_input("Vpisi ime jedi: ")
    print "Ime jedi: " + jed

    cena = raw_input("vpisi ceno: ")
    print "Cena jedi: " + cena

    meni[jed] = cena

    konec = raw_input("Ali zelite koncati z urejanjem (da/ne)?: ")
    if konec == "da":
        break

for jed, cena in meni.iteritems():
    print jed, cena, "EUR"

print "Dnevni meni je koncan"

meni_file = open("meni.txt", "w+")
meni_file.write("Dnevni meni\n")

for jed, cena in meni.iteritems():
    if konec == "da":
        meni_file.write("- " + jed + " " + cena + "\n")
        meni_file.write("Dnevni meni je koncan")

meni_file.close()


