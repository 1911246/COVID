import pandas as pd
import matplotlib.pyplot as plt
import chardet

#with open('./DATA.csv', 'rb') as f:
 #   result = chardet.detect(f.read())

covid19_data = pd.read_csv('./DATA.csv', encoding=result['encoding'])