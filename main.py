#r10
from collections import Counter
t = "ksp";ti = t.index

   
def tarkistus(p,b):
    pk = p['käsi']
    if pk==t[ti(b)-1]: print("Voitit!"); p['voitot']+=1
    elif ti(pk)==ti(b): print("Tasapeli!")
    else: print("Hävisit!")
def datakapistely(p):
	try:
		f = open('data.txt','a+')
		try:
			f.seek(1)
			r = f.read()
		except:
			print("Tiedostoa ei voinut lukea!")
		try:
			f.write(str(ti(p)))
		except:
			print("Tiedostoon ei voinut kirjoittaa!")
	finally:
		f.close()
	return Counter(r)
def tallenna(p,k):
    try:
        f= open('tulokset.txt','a')
    except:
        print("Tiedostoa ei voinut avata.")
    try:
        f.write(f"{p['nimi']} voitot:{p['voitot']}/{k}\n")
    except:
        print("Tiedostoon ei voinut kirjoittaa.")
def b_valinta(d):
    l = tuple
    k,v=l(d.keys()),l(d.values())
    return t[int(k[v.index(max(v))])-1]
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
    j = 1
    k = 0
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
