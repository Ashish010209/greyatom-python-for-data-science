# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)
categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var.shape)
numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var.shape)

print('=' * 50)

banks = bank.drop('Loan_ID', axis=1)
print(banks.isnull().sum())
bank_mode=dict(banks.mode())
bank_mode={'Gender':'Male', 'Married':'Yes', 'Dependents': 0, 'Education':'Graduate', 'Self_Employed':'No', 'ApplicantIncome': 2500, 'CoapplicantIncome': 0.0, 'LoanAmount': 120.0, 'Loan_Amount_Term': 360.0, 'Credit_History': 1.0, 'Property_Area':'Semiurban', 'Loan_Status':'Y'}
banks=banks.fillna(bank_mode)
print(banks.shape)
print(banks.isnull().sum().values.sum())

print('=' * 50)

avg_loan_amount=banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc='mean')
print(avg_loan_amount['LoanAmount'][1],2)

print('=' * 50)

loan_approved_se=(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')
loan_approved_nse=loan_approved_se
loan_approved_se=[i for i in loan_approved_se if i==True]
loan_approved_se=len(loan_approved_se)
percentage_se=(loan_approved_se / 614) * 100
print(percentage_se)
loan_approved_nse=(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y') 
loan_approved_nse=[i for i in loan_approved_nse if i==True]
loan_approved_nse=len(loan_approved_nse)
percentage_nse=(loan_approved_nse / 614) * 100
print(percentage_nse) 

print('=' * 50)

loan_term=banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term=[i for i in loan_term if i >= 25]
print(len(big_loan_term))

print('=' * 50)

loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.mean()
print(mean_values.iloc[1,0], 2)
#Code starts here




