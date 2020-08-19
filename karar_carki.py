import random
import time
while True:
	try:
		veri_sayisi = int(input('Kaç adet veri gireceksin? : '))
		break
	except:
		print('Lütfen Sadece Sayı gir!')
		continue
veri_sayisi2 = veri_sayisi + 1
veriler = []
print('Bilgi!')
print('Girilen veri sayısı fazlaysa büyük harflerle TAMAM yaz.')
while True:
	if veri_sayisi == 0:
		print('Çark Dönüyor')
		time.sleep(1)
		try:
			print('Çark ' + random.choice(veriler) + ' Diyor.')
		except:
			print('Henüz Bir Değer Girmedin!')
		break
	else:
		x = veri_sayisi2 - veri_sayisi
		veri = input(str(x) + '. Veriyi gir: ')
		veri_sayisi = veri_sayisi - 1
		if veri == 'TAMAM':
			veri_sayisi = 0
		else:
			veriler.append(veri)