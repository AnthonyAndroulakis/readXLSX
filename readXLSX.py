import pandas as pd
import xlrd

raw = pd.read_excel("lesions/niistat.xlsx", sheet_name="NiiStat")
columns = raw.columns
data = raw.values

print('columns: '+columns[0]+', '+columns[1])
print('1st patient name: '+data[0][0])
print('1st patient data: '+str(data[0][1]))
