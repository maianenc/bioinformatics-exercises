from string import digits
import re

#receive a dna sequence
dnaInput= input("Insira a sequencia do DNA: ")
#transform the dna sequence tu upper case
dnaInput = dnaInput.upper()
#removes spaces from the string of the dna sequence
dnaInput= dnaInput.replace(" ", "")
#removes any number of a dna sequence
remove_digits = str.maketrans('','', digits)
dna = dnaInput.translate(remove_digits)

print(dna) #prints the DNA sequence
len(dna) #the lenght of the DNA sequence
print("tamanho= ", len(dna)) #prints the lenght of the DNA sequence

'A' in dna #test
'B' in dna

print("tem A no dna",'A' in dna) #prints the TEST
print("tem B no dna", 'B' in dna) #prints the TEST

#count the number of nucleotides in a sequence,
a_count=dna.count('A')
c_count=dna.count('C')
g_count=dna.count("G")
t_count=dna.count("T")
#prints the number of nucleotides in a sequence
print("quantidade de A = ", a_count)
print("quantidade de C = ", c_count)
print("quantidade de G = ", g_count)
print("quantidade de T = ", t_count)

#percent of G and C in the DNA
gc=g_count+c_count
length=len(dna)
gc_percent=gc/length * 100
print("GC PERCENT = ", gc_percent)

#PERCENT OF A
length=len(dna)
aPercent = a_count/length * 100
print("Porcentagem de 'A'= ", aPercent)

#PERCENT OF C
length=len(dna)
aPercent = c_count/length * 100
print("Porcentagem de 'C'= ", aPercent)

#PERCENT OF G
length=len(dna)
aPercent = g_count/length * 100
print("Porcentagem de 'G'= ", aPercent)

#PERCENT OF T
length=len(dna)
aPercent = t_count/length * 100
print("Porcentagem de 'T'= ", aPercent)


