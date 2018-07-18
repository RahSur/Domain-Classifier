import docx, re
from docx import Document

file = input("\n Enter your Document name :   ")

target = [['method', 'program', 'feasibility', 'engineering', 'measure', 'function'],
          ['network', 'security', 'cryptography', 'encryption', 'decryption'],
          ['machine learning', 'nlp', 'neural', 'deep learning', 'robotics', 'automation'],
          ['database', 'query', 'records', 'tables', 'sql', 'oracle']]

domain_total = [[0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]

domain = ['Engineering', 'Communication', 'Artificial Intelligence', 'Database']
word_count = 0

fopen = open(file, "rb")
docu = Document(fopen)
pattern = re.compile('[\W_]+')


for para in docu.paragraphs:
    content = para.text
    for word in content.split():
        word = word.lower()
        word = pattern.sub('', word)
        dom_count = 0
        for out_list in target:
            key_count = 0
            for in_list in out_list:
                if in_list == word:
                    domain_total[dom_count][key_count]+=1
                key_count+=1
            dom_count+=1
        word_count+=1


print("\n     Document Domain Classifier")
print('     *****************************\n')
print("  Total Words in Document : ",word_count,' words')


for i in range(4):
          print("\n ",domain[i], " : ", ((sum(domain_total[i] ) / word_count)*100), "%")

print('\n   KeyWords Domain with frequency ')
print('   **********************************\n')

for i in range(4):
    print(" ", domain[i] , "Domain \n")
    for j in range(len(target[i])):
        print( " ",target[i][j], " : ", domain_total[i][j])
        #print( " " ,domain[i], " : ", target[i][j], " : ", domain_total[i][j])
    print('\n')




