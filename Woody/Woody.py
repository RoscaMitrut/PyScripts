from tkinter import Tk,Label,Entry,Button,messagebox,Toplevel
from random import randrange

window = Tk()
window.title("Woody")
marja = 5/100

top = Toplevel(window)
top.title("Results")

def formula_calcul(diametru,lungime):
	#diamentru = cm   lungime = cm    return = sqm
	rezultat = diametru/200*diametru/200*3.1416*lungime/100
	return round(rezultat,3)

def delete_function():
	l_min.delete(0,'end')
	l_max.delete(0,'end')
	d_min.delete(0,'end')
	d_max.delete(0,'end')
	vol.delete(0,'end')
	nr_buc.delete(0,'end')
	l_min.focus_set()

def afisare(volum,lungimi,diametre):
	for widget in top.winfo_children():
		widget.destroy()
	Label(top, text='Volum:').grid(column=0,row=0)
	Label(top, text=round(volum,3)).grid(column=1,row=0)
	Label(top, text='NR. CRT.:').grid(column=0,row=1)
	Label(top, text='Lungime').grid(column=1,row=1)
	Label(top, text='Diametru').grid(column=2,row=1) 
	for i in range(len(lungimi)):
		Label(top,text=i).grid(column=0,row=2+i)
		Label(top,text=lungimi[i]).grid(column=1,row=2+i)
		Label(top,text=diametre[i]).grid(column=2,row=2+i)

def validate_volum():
	volum = vol.get()
	if volum:
		try:
			float(volum)
			return True
		except:
			return False
	else:
		return False

def validate_nr_buc():
	numar_bucati = nr_buc.get()
	if numar_bucati:
		try:
			int(numar_bucati)
			return True
		except:
			return False
	else:
		return False

def test_data(min_len,max_len,min_dia,max_dia,volume,amount=0):
	vol_min = formula_calcul(min_dia,min_len)
	vol_max = formula_calcul(max_dia,max_len)
	match amount:
		case 0:
			return vol_min<volume
		case _:
			return (vol_min*amount < volume) and (vol_max*amount > volume)


def generate_v(min_len,max_len,min_dia,max_dia,volume=0):
	suma_volum_calculat = 0
	lungimi = []
	diametre = []
	for i in range(10000000):
		lungime = randrange(min_len, max_len+1, 10)
		diam = randrange(min_dia, max_dia+1, 2)
		suma_volum_calculat += formula_calcul(diam, lungime)
		lungimi.append(lungime)
		diametre.append(diam)
		if suma_volum_calculat>volume-volume*marja and suma_volum_calculat<volume+volume*marja:
			return suma_volum_calculat,lungimi,diametre
		elif suma_volum_calculat > volume+volume*marja:
			lungimi.clear()
			diametre.clear()
			suma_volum_calculat = 0
	return None,None,None
  
def generate_a(min_len,max_len,min_dia,max_dia,amount=0):
	suma_volum_calculat = 0
	lungimi = []
	diametre = []
	for _ in range(amount):
		lungime = randrange(min_len, max_len+1, 10)
		diam = randrange(min_dia, max_dia+1, 2)
		suma_volum_calculat += formula_calcul(diam, lungime)
		lungimi.append(lungime)
		diametre.append(diam)
	return suma_volum_calculat,lungimi,diametre

def generate_va(min_len,max_len,min_dia,max_dia,volume=0,amount=0):
	suma_volum_calculat = 0
	lungimi = []
	diametre = []
	while True:
		for _ in range(amount):
			lungime = randrange(min_len, max_len+1, 10)
			diam = randrange(min_dia, max_dia+1, 2)
			suma_volum_calculat += formula_calcul(diam, lungime)
			lungimi.append(lungime)
			diametre.append(diam)
		if suma_volum_calculat>volume-volume*marja and suma_volum_calculat<volume+volume*marja:
			return suma_volum_calculat,lungimi,diametre
		else:
			lungimi.clear()
			diametre.clear()
			suma_volum_calculat = 0

def main_function():
	try:
		lungime_minima = int(float(l_min.get())*100)
		lungime_maxima = int(float(l_max.get())*100)
		diametru_minim = int(d_min.get())
		diametru_maxim = int(d_max.get())
	except:
		messagebox.showinfo("Eroare date", "Date invalide")
		return

	switch=0
	if(validate_volum()):
		switch+=1
	if(validate_nr_buc()):
		switch+=2
  
	match switch:
		case 0:
			messagebox.showinfo("Eroare volum / nr bucati", "Volum/nr bucati invalide")
			return

		case 1:
			volum = float(vol.get())
			if(test_data(lungime_minima,lungime_maxima,diametru_minim,diametru_maxim,volum)):
				v,l,d = generate_v(lungime_minima,lungime_maxima,diametru_minim,diametru_maxim,volum)
				if (v,l,d == None,None,None):
					messagebox.showinfo("S-a depasit limita de 10M de iteratii", "Considerati schimbarea valorilor")	
					return
				afisare(v,l,d)
			else:
				messagebox.showinfo("Eroare calcul", f"Volum imposibil de calculat\nVolum minim: {formula_calcul(diametru_minim,lungime_minima)}\nVolum maxim: {formula_calcul(diametru_maxim,lungime_maxima)}")
    
		case 2:
			numar_bucati = nr_buc.get()
			numar_bucati = int(numar_bucati)
			v,l,d = generate_a(lungime_minima,lungime_maxima,diametru_minim,diametru_maxim,numar_bucati)
			afisare(v,l,d)
   
		case 3:
			volum = vol.get()
			volum = float(volum)
			numar_bucati = nr_buc.get()
			numar_bucati = int(numar_bucati)
			if(test_data(lungime_minima,lungime_maxima,diametru_minim,diametru_maxim,volum,numar_bucati)):
				v,l,d = generate_va(lungime_minima,lungime_maxima,diametru_minim,diametru_maxim,volum,numar_bucati)
				afisare(v,l,d)
			else:
				messagebox.showinfo("Eroare calcul", f"Volum imposibil de calculat\nVolum minim: {formula_calcul(diametru_minim,lungime_minima)*numar_bucati}\nVolum maxim: {formula_calcul(diametru_maxim,lungime_maxima)*numar_bucati}")


Label(window, text="Lungime minima [m]").grid(column=0,row=0)
l_min = Entry(window, width=20)
l_min.grid(column=1, row=0)

Label(window, text="Lungime maxima [m]").grid(column=0,row=1)
l_max = Entry(window, width=20)
l_max.grid(column=1, row=1)

Label(window, text="Diametru minim [cm]").grid(column=0,row=2)
d_min = Entry(window, width=20)
d_min.grid(column=1, row=2)

Label(window, text="Diametru maxim [cm]").grid(column=0,row=3)
d_max = Entry(window, width=20)
d_max.grid(column=1, row=3)

Label(window, text="Volum [m^3]").grid(column=0,row=4)
vol = Entry(window, width=20)
vol.grid(column=1, row=4)

Label(window, text="Nr. Bucati").grid(column=0,row=5)
nr_buc = Entry(window, width=20)
nr_buc.grid(column=1, row=5)


Button(window, text="Start",command=lambda: main_function()).grid(column=1,row=7)
Button(window, text="Reset",command=lambda: delete_function()).grid(column=0, row=7)

l_min.bind('<Return>', lambda ceva: l_max.focus_set())

l_max.bind('<Return>', lambda ceva: d_min.focus_set())

d_min.bind('<Return>', lambda ceva: d_max.focus_set())

d_max.bind('<Return>', lambda ceva: vol.focus_set())

vol.bind('<Return>', lambda ceva: nr_buc.focus_set())

nr_buc.bind('<Return>', lambda ceva: main_function())


window.mainloop()
