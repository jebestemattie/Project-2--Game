import random

def GetNumbers():
	#Maak variabele om later te returnen
	result = []
	
	#Maak variabele om alle nummers die we nodig hebben in te bewaren
	allnumbers = []
	
	#Stop de nummers 1 t/m 5 er 6 keer in
	for i in range(6):
		allnumbers.extend(range(1, 6))
	
	#Shuffle 'em around
	random.shuffle(allnumbers)

	#Doe 5 keer...
	for i in range(0, 30, 6):
		#Maak een tijdelijke variabele waar 1 blok met getallen in gaat
		part = []

		#Stop de volgende 6 getallen van 'allnumbers' in 'part'
		#
		#(De eerste keer dat dit runt, wordt 'i' dus [0,1,2,3,4,5], dus de eerste 6 getallen
		# uit 'allnumbers' worden in een array/blok gestopt en dat wordt aan 'result' toegevoegd.
		# De 2e keer worden de getallen met de index [6,7,8,9,10,11] uit 'allnumbers' als blok toegevoegd aan 'result', enz.)
		for j in range(i, i+6):
			part.append(allnumbers[j])

		#Voeg dit blok toe aan het resultaat
		result.append(part)

	#Return het resultaat.
	return result
