a="recognizer/trainingData.yml"
file2=open(a,'r')
line=file2.readline()
while(line!=""):
    print(line)
    line=file2.readline()
file2.close()
'''
import pandas as pd
data = pd.read_csv('recognizer/trainingData.yml', header = None)
print(data)'''
