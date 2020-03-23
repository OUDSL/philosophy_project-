import PyPDF2
import re
import openpyxl
import pandas as pd

pdfFileObj = open('/Users/ramamohanraoveeramachaneni/Downloads/ga/533Cottrell.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

ls = []
ts = []
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
  
# extracting text from page 
    ls.extend(re.findall(r'\(T.+;\n*\ *SBN.+\)', pageObj.extractText()))
    ts.extend(re.findall(r'\(T .*?\)', pageObj.extractText(),re.S))

# closing the pdf file object 

pdfFileObj.close()

for i in ts:
    if i not in ls:
        if "\n" in i:
            a = i.split("\n")
            #print(a)
            ls.extend(a)
        else:    
            ls.append(i)

#print(ls)

df = pd.DataFrame(ls,columns=["Suffix"])
df["Name_of _Paper"] = pd.Series(["Minds, Composition, and Hume’s Skepticism in the Appendix." for x in range(len(df))])

print(df)

try:
    previous_df = pd.read_excel("/Users/ramamohanraoveeramachaneni/Downloads/Output.xlsx",index_col=0)
except:
    print("No such file exists")

result= pd.concat([previous_df,df])

result.to_excel("Output.xlsx")
