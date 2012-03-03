#!/usr/bin/env python

'''
Created on Feb 29, 2012

@author: li0nize
'''
import subprocess
import os, sys, string

rangeOfPossible = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+}]{[\|,<.>/?';:"

#file is the encrypted file you are trying to decrypt, later all options for rangeofpossible
#as well as the encryption scheme.
#put a tracker in here and printout everyonce in awhile what its trying maybe at each for loop

filearg = sys.argv[1]
filename = "output.txt"
FILE = open(filename,"w")

currentPassword = ""

for x in range(len(rangeOfPossible)):
	for y in range(len(rangeOfPossible)):
		for z in range(len(rangeOfPossible)):
			for a in range(len(rangeOfPossible)):
				for b in range(len(rangeOfPossible)):
					for c in range(len(rangeOfPossible)):
						if x > 0:
							currentPassword = "" + rangeOfPossible[x] + rangeOfPossible[y] + rangeOfPossible[z] + rangeOfPossible[a] + rangeOfPossible[b] + rangeOfPossible[c]
						elif y > 0:
							currentPassword = "" + rangeOfPossible[y] + rangeOfPossible[z] + rangeOfPossible[a] + rangeOfPossible[b] + rangeOfPossible[c]
						elif z > 0:
							currentPassword = "" + rangeOfPossible[z] + rangeOfPossible[a] + rangeOfPossible[b] + rangeOfPossible[c]
						elif a >0:
							currentPassword = "" + rangeOfPossible[a] + rangeOfPosible[b] + rangeOfPossible[c]
						elif b > 0:
							currentPassword = "" + rangeOfPossible[b] + rangeOfPossible[c]
						else
							currentPassword = "" + rangeOfPossible[c]

				#print currentPassword
				DC = subprocess.Popen(['openssl','aes-256-cbc', '-d', '-in', filearg, '-out', 'output.gz','-pass','pass:' + currentPassword], stderr=subprocess.STDOUT,stdout= subprocess.PIPE)
				out, err = DC.communicate()
				#print out
				if "bad decrypt" not in out:
					FILE.write(currentPassword + '\n')
				#sys.exit("The Password is: " + currentPassword)
FILE.close()
sys.exit("Search Complete")  
