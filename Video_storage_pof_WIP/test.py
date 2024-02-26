import codecs, csv

fichier=codecs.open('/home/antonin/code/Coding-projects/Video_storage_pof/encode.csv','r','utf-8')
encode=list(csv.DictReader(fichier,delimiter=','))
fichier.close()

def colour_definer(extracted_octect_from_input_file):
    for i in encode:
        i['extracted_octect_from_input_file']=str(i['MSB'])+str(i['3'])+str(i['2'])+str(i['LSB'])
    for i in encode:
        if i['extracted_octect_from_input_file']==str(extracted_octect_from_input_file):
            return [i['R'],i['G'],i['B']]
        
print(colour_definer(1100))