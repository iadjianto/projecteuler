# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 19:08:16 2022

@author: isaia
"""

import numpy as np

number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

window = 13

#print(len(str(number)))
#print(str(number)[0:window])
#print(str(np.roll(letter,1))[0])



def largestproduct(number,window): # Defining a function to find the largest product in a number, with a certain window size
	large = 0 # largest number is initially zero

	for i in range(len(str(number))-window): # Check every number from the start, up to the last minus the last 12 numbers in this case
		if str(number)[window+i-1] == "0": # If the number being searched has 0 for the last digit, skip it
			continue
		else:
			letter = str(number)[i:window+i] # finds the window (13) sized string of numbers
			subset = list(map(float, letter)) # splits it into a list of individual numbers
			product = np.prod(subset) # calculates a product from the list
			#print(product)
			if large < product: # if the product is larger than the currently known largest product, recognize it as the largest..
				large = product
	
			elif product < 0: # troubleshooting
				print(subset)
				print(product)
	
	return large # Prints the largest product

#
if __name__ == "__main__": # main program, will run when python script is loaded
	modified_data = largestproduct(number,window)
	print(modified_data)
