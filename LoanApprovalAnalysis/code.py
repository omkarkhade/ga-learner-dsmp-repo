# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank  = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = ['object'])
numerical_var = bank.select_dtypes(include = ['number'])

print(categorical_var)
print(numerical_var)

# code starts here






# code ends here


# --------------
# code starts here
import statistics

banks = bank.drop(columns =['Loan_ID'])
#print(banks)
print(banks.isnull().sum())
bank_mode = banks.mode()
#print(bank_mode)
banks.fillna(bank_mode.iloc[0],inplace =True)

#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],
values ='LoanAmount',aggfunc='mean')

#avg_loan_amount =  banks.pivot_table(index=['Gender','Married','Self_Employed'], #values='LoanAmount', aggfunc='mean')

# code ends here



# --------------
# code starts here
m1 = banks['Self_Employed'] == 'Yes'
m2 = banks['Loan_Status'] == 'Y'
loan_approved_se = banks.loc[m1 & m2].shape[0]
m3 = banks['Self_Employed'] == 'No'
loan_approved_nse =  banks.loc[m2 & m3].shape[0]
Loan_Status = 614
percentage_se = loan_approved_se/614 *100
percentage_nse = loan_approved_nse/614 *100
# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
#loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term = banks.loc[ loan_term >= 25 ].shape[0]

# code ends here


# --------------
# code ends here
loan_groupby = banks.groupby(['Loan_Status'],axis=0)['ApplicantIncome','Credit_History']
#loan_groupby = bank.groupby(['Loan_Status'],axis=0)['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.agg([np.mean])
print(mean_values)
# code ends here


