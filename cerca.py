import glob
import os
list=glob.glob('/UtentiProva/*')
file_list=[i.split('\\')[-1] for i in list]
with open("utenze.txt" , 'r' ) as f:	
	listaf=[f.readline(7)]
	for a in f:		
		PrimaRiga=f.readline(7)
		listaf.append(PrimaRiga)
listaf.remove('')

s1=glob.glob('/UtentiProva/S*')
t1=glob.glob('/UtentiProva/T*')
j1=glob.glob('/UtentiProva/J*')

#split liste delle utenze s t j 
s=[i.split('\\')[-1] for i in s1]
t=[i.split('\\')[-1] for i in t1]
j=[i.split('\\')[-1] for i in j1]

for b in listaf:
	if(b not in file_list):
		os.mkdir('/UtentiProva/'+ b) 
#per la rimozione 
for c in t:
	if (c not in listaf) :
		os.rmdir('/UtentiProva/'+ c)
for d in s:
	if (d not in listaf) :
		os.rmdir('/UtentiProva/'+ d)
for e in j:
	if (e not in listaf) :
		os.rmdir('/UtentiProva/'+ e)
	
#impostare i giusti percorsi, crea le cartelle nel percorso dove viene lanciato lo script.
#l' obiettivo e' che sulla /home/ rimangano solo gli utenti con la S/T/J che sono nel file