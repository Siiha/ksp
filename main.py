#r10
from collections import Counter
t = "ksp"
def tarkistus(pelaajan_valinta,koneen_valinta):
    if pelaajan_valinta==t[t.index(koneen_valinta)-1]: print("Voitit!"); return 1
    elif pelaajan_valinta==koneen_valinta: print("Tasapeli!"); return 0
    else: print("Hävisit!"); return 0
def historian_kapistely(pelaajan_valinta):
	try:
		f = open('historia.txt','r+')
		try:
			r = f.read()
		except:
			print("Tiedostoa ei voinut lukea!")
		try:
			f.write(str(t.index(pelaajan_valinta)))
		except:
			print("Tiedostoon ei voinut kirjoittaa!")
	finally:
		f.close()
	return Counter(r.replace('\n',""))
def tallenna(pelaaja,kierokset):
    try:
        f= open('tulokset.txt','a')
    except:
        print("Tiedostoa ei voinut avata.")
    try:
        f.write(f"{pelaaja['nimi']} voitot:{pelaaja['voitot']}/{kierokset}\n")
    except:
        print("Tiedostoon ei voinut kirjoittaa.")
    finally: f.close()
botin_valinta = lambda d: t[int(d.most_common()[0][0])-1]
def main():
    h = {"k":"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""","s":"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""","p":"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""} 
    pelaaja = {'nimi':input('Nimimerkkisi: '),'voitot': 0,'käsi':""};
    jatka = 1 
    kierokset = 0 
    while jatka:
        pelaaja['käsi']=input("Kätesi k:kivi s:sakset p:paperi: ")
        bot = botin_valinta(historian_kapistely(pelaaja['käsi']))
        print(h[bot])
        pelaaja['voitot']+=tarkistus(pelaaja['käsi'],bot)
        jatka = int(input("Haluatko jatkaa 1: kyllä 0: ei: "))
        kierokset += 1
    if int(input("Haluatko talentaa tuloksen 1: kyllä 0: ei: ")):
        tallenna(pelaaja,kierokset)
main()
