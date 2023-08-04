inflacja = [1.592824484, -0.4535091012, 2.324671717, 1.261254407, 1.782526286, 2.329384541, 1.502229842, 1.782526286, 2.328848994, 0.6169213482, 2.352295886, 0.3377795452, 1.577035247, -0.2927814426, 2.48619659, 0.2671103178, 1.417952672, 1.054243267, 1.480520104, 1.577035247, -0.07742069031, 1.165733399, -0.4041867176, 1.499708521]
kwota_kredytu = input("Podaj kwote kredytu: ")
oprocentowanie = input("Podaj oprocentowanie kredytu: ")
rata = input("Podaj rate kredytu: ")
kwota_kredytu = float(kwota_kredytu)
oprocentowanie = float(oprocentowanie)
rata = float(rata)
print(kwota_kredytu)
x = 0
while x < len(inflacja):
    nowa_kwota =  (1.0 + ((inflacja[x] + oprocentowanie)/1200.0)) * kwota_kredytu - rata
    nowa_kwota = round(nowa_kwota, 2)
    roznica = kwota_kredytu - nowa_kwota
    roznica = round(roznica, 2)
    print (f"Twoja pozostała kwota kredytu w miesiącu {x+1} to {nowa_kwota}zł to {roznica} mniej niz w poprzednim miesiącu" )
    kwota_kredytu = nowa_kwota
    x = x+1
