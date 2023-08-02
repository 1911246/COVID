import pandas as pd
import matplotlib.pyplot as plt
import chardet
import csv
'''
count = 0 
Yes_Cnt = 0
No_Cnt = 0
NoData_Cnt = 0

with open('DATA.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        count += 1
        if count>1130:
            break
       # if  (row['Heart_attack'] == ''):
            #NoData_Cnt = 0
       # else:
           # print(row['Heart_attack'])
        
            
        if ((row['sex']) == 'male' and (row['Heart_attack']) == '') :
            Yes_Cnt += 1
        elif((row['sex']) == 'female' and (row['Heart_attack']) == ''):
            No_Cnt +=1
        else:
            NoData_Cnt += 1
print('Number of m:',Yes_Cnt, 'Number of f:', No_Cnt , "No Data Number:", NoData_Cnt)





'''
import pandas as pd
import matplotlib.pyplot as plt
import chardet

with open('./DATA.csv', 'rb') as f:
    result = chardet.detect(f.read())

covid19_data = pd.read_csv('./DATA.csv', encoding=result['encoding'])

# Define the keywords and corresponding values for desired symptoms
keywords = {
    'atigue': 'Fatigue',
    'ypertension': 'Hypertension',
    'ttack': 'Heart Attack'
}

# Create a new column to store the symptom values
covid19_data['symptom_value'] = -1

# Search for the keywords in the columns and assign corresponding values
for col in covid19_data.columns:
    covid19_data[col] = covid19_data[col].astype(str)
    covid19_data.loc[covid19_data[col].str.lower().str.contains('|'.join(keywords.keys())), 'symptom_value'] = covid19_data[col].map(keywords)

# Analyze the impact of long COVID on symptoms
long_covid_symptoms = covid19_data[covid19_data['symptom_value'] != -1]

# Count the occurrences of each symptom value for long COVID
symptom_counts = long_covid_symptoms['symptom_value'].value_counts()

# Create a bar plot of symptom value counts
plt.figure(figsize=(8, 6))
symptom_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Symptom')
plt.ylabel('Count')
plt.title('Impact of Long COVID on Symptoms')
plt.xticks(rotation=0)
plt.show()

