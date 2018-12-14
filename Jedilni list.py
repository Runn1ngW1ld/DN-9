from datetime import datetime

now = datetime.now()

print "Pozdravljeni v urejevalniku dnevnega menija"

#day = ["Ponedeljek", "Torek", "Sreda", "Cetrtek", "Petek", "Sobota", "Nedelja"]
meni = {}

while True:

    dan = raw_input("Vpisite danasnki dan: ")
    print dan

    jed = raw_input("Vpisi ime jedi: ")
    print "Ime jedi: " + jed

    cena = raw_input("vpisi ceno: ")
    print "Cena jedi: " + cena

    meni[jed] = cena

    konec = raw_input("Ali zelite koncati z urejanjem (da/ne)?: ")
    if konec == "da":
        break

for jed, cena in meni.iteritems():
    print dan
    print '%02d - %02d - %04d' % (now.day, now.month, now.year)
    print jed, cena, "EUR"

print "Dnevni meni je koncan"

meni_file = open("meni " + '%02d-%02d-%04d' % (now.day, now.month, now.year) + ".txt", "w+")
meni_file.write("Dnevni meni za dan\n" + dan + "\n" + '%02d-%02d-%04d' % (now.day, now.month, now.year) + "\n")

for jed, cena in meni.iteritems():
    if konec == "da":
        meni_file.write("- " + jed + " " + cena + "\n")
        meni_file.write("Dnevni meni je koncan")

meni_file.close()


