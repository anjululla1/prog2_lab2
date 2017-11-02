#! /user/bin/env python

class GenBank(object):
    def genbankParser(self):
        file = "/Users/Desktop/prog2/hw2_hla.gb.txt"
        my_file = open(file)
        data = my_file.readlines()
        #print (data)
        return data
    
    def Parsedinfo(info, data):
        #parsed = []
        string = ''
        for i in data:
            string = i.strip()
            #parsed.append(string)

            if string.startswith('ORGANISM'):
                print (string)
            
            if string.startswith('VERSION'):
                print (string)
                
            if string.startswith('ACCESSION'):
                print (string)
        return

obj = GenBank()
file_output = obj.genbankParser()
info_out = obj.Parsedinfo(file_output)




