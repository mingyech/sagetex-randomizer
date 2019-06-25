import subprocess
import os
import csv

#Create array for seeds and names
seed = []
name = []

#Import seeds from csv file
with open('names.csv') as csvDataFile:
        seeds = csv.reader(csvDataFile)
        for row in seeds:
            seed.append(row[0])
            name.append(row[1])

#Compiling latex to pdf
def CompileSageTex(fileName):
    subprocess.call(['pdflatex', fileName+'.tex'])
    subprocess.call(['sage',fileName+'.sagetex.sage'])
    subprocess.call(['pdflatex', fileName+'.tex'])

#Loop through each name and generate pdf
count = 0
for i in seed:
    name = name[count]
    open('num.txt', 'w+').write(i)
    open('name.txt', 'w+').write(name)
    CompileSageTex('random')
    os.rename('random.pdf','Generated_'+name+'.pdf')
    count += 1
