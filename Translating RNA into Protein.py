# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:54:52 2020

@author: Shujaat
"""

#Merage differnt line Strings to one String from File
def MerageFileLines2String(FileName):
              
    string=""  
    lineList = list()
#Get all strings to one strings
    with open(FileName,'r') as f:
        for line in f:
            lineList.append(line)
        for x in range (len(lineList)):
            string+=(lineList[x])
    return string
string1="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
#Create Directories First
str="rosalind_prot (4).txt"
string=MerageFileLines2String(str)
def TranscribingDNA2RNA(string):
    string=string.replace('T', 'U')
    return (string)
string=TranscribingDNA2RNA(string)
DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "_", "UAG": "_", "UGA": "_"
}
RNA_Codons = {
    # 'M' - START, '_' - STOP
    "UUU": "F", "UUC": "F",
    "UUA":"L","UUG":"L",
    "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
    "UAU":"Y","UAC":"Y",
    "UAA":"STOP","UAG":"STOP",
    "UGU":"C","UGC":"C",
    "UGA":"STOP",
    "UGG":"W",
    "CUU":"L","CUC":"L","CUA":"L","CUG":"L",
    "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
    "CAU":"H","CAC":"H",
    "CAA":"Q","CAG":"Q",
    "CGU":"R","CGC":"R","CGA":"R","CGG":"R",
    "AUU":"I","AUC":"I","AUA":"I",
    "AUG":"M",
    "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
    "AAU":"N","AAC":"N",
    "AAA":"K","AAG":"K",
    "AGU":"S","AGC":"S",
    "AGA":"R","AGG":"R",
    "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
    "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
    "GAU":"D","GAC":"D",
    "GAA":"E","GAG":"E",
    "GGU":"G","GGC":"G","GGA":"G","GGG":"G"
    }
#Split String into Codon and Find the Start and End Index
lists=list()
NotMatch=list()
NotMatchIndex=list()
StopIndex=0
StartIndex=string.find("AUG")
Si=string.find("UGA")
for i in range(StartIndex,len(string)-2,3):
    #print(string[i])
    codon=string[i]+string[i+1]+string[i+2]
    if(codon=="UGA"):
        StopIndex=i
    else:
        lists.append(codon) 
OutPutString=""        
for i in range(0,len(lists)):
    if lists[i] in RNA_Codons:
        OutPutString+=(RNA_Codons[lists[i]])
    else:
        NotMatch.append(lists[i])
        NotMatchIndex.append(i)
print(OutPutString)