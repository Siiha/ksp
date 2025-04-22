#r10
from collections import Counter
t = "ksp"
def tarkistus(p,b):
    pk = p['käsi']
    if pk==t[t.index(b)-1]: print("Voitit!"); p['voitot']+=1
    elif pk==b: print("Tasapeli!")
    else: print("Hävisit!")
def datakapistely(p):
	try:
		f = open('data.txt','r+')
		try:
			r = f.read()
		except:
			print("Tiedostoa ei voinut lukea!")
		try:
			f.write(str(t.index(p)))
		except:
			print("Tiedostoon ei voinut kirjoittaa!")
	finally:
		f.close()
	return Counter(r.replace('\n',""))
def tallenna(p,k):
    try:
        f= open('tulokset.txt','a')
    except:
        print("Tiedostoa ei voinut avata.")
    try:
        f.write(f"{p['nimi']} voitot:{p['voitot']}/{k}\n")
    except:
        print("Tiedostoon ei voinut kirjoittaa.")
    finally: f.close()
b_valinta = lambda d: t[int(d.most_common()[0][0])]
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
    p = {'nimi':input('Nimimerkkisi: '),'voitot': 0,'käsi':""};
    j = 1 # jatka
    k = 0 # kierokset
    while j:
        p['käsi']=input("Kätesi k:kivi s:sakset p:paperi: ")
        b = b_valinta(datakapistely(p['käsi']))
        print(h[b])
        tarkistus(p,b)
        j = int(input("Haluatko jatkaa 1: kyllä 0: ei: "))
        k += 1
    if int(input("Haluatko talentaa tuloksen 1: kyllä 0: ei: ")):
        tallenna(p,k)
main()
