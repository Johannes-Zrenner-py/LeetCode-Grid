# Problem: 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/description/
# Schwierigkeit: Easy
# Zeit erledigt in: ca. 20 min 

class Solution (object):
  	def twoSum (self, nums, target):

		# List erstellen der Alten liste bei der Jede Zahl eine Liste mit 	ihrer Koordinate bekommt.
		liste_mit_index = []
		index = 0
		for Zahl in nums:
			liste_mit_index.append([Zahl,index])
			index = index + 1

		# Paar suchen das als Ergebnis die gesuchte Zahl ist:
		for zahl_mit_liste in liste_mit_index:
			for zahl_mit_liste_zum_addieren in liste_mit_index:
				if zahl_mit_liste[1] != zahl_mit_liste_zum_addieren[1]:
					if zahl_mit_liste[0] + zahl_mit_liste_zum_addieren[0] == target:
						Koordinate_in_nums_der_richigen_zahlen = [zahl_mit_liste[1], zahl_mit_liste_zum_addieren[1]]

						# Ergebnis, wenn gefunden zurückgegeben:
						return Koordinate_in_nums_der_richigen_zahlen
