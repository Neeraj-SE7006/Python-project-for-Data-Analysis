import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('F:\Project_Final\Python_Analysis\Diwali Sales Data.csv', encoding= 'unicode_escape')
print(df.shape)
#print(df.head(10))
#print(df.info())
df.drop(['Status','unnamed1'], axis = 1, inplace = True)
#print(df.info())
#print(pd.isnull(df).sum())
df.dropna(inplace = True)
#print(pd.isnull(df).sum())
df['Amount'] = df['Amount'].astype('int')
#print(df['Amount'].dtypes)
#Data Analysis 
# -----------------> Gender<-------------------------------------------
'''ax = sns.countplot(x = 'Gender', data = df)
for bars in ax.containers:
   ax.bar_label(bars)
   plt.show()

sales_gn = df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
print(sales_gn)
bx = sns.barplot(x = 'Gender', y = 'Amount', data = sales_gn)
for bars in bx.containers:
    bx.bar_label(bars)
    plt.show()'''

#----------------->Age<---------------------------------
'''ax = sns.countplot(x = 'Age Group', hue = 'Gender', data = df)
for bars in ax.containers:
   ax.bar_label(bars)
   plt.show()

sales_age = df.groupby(['Age Group'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
print(sales_age)
bx = sns.barplot(x = 'Age Group', y = 'Amount', data = sales_age)
plt.show()'''

#------------------->State<---------------------------------

'''sales_state = df.groupby(['State'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)
sns.set(rc = {'figure.figsize':(15,5)})
bx = sns.barplot(x = 'State', y = 'Orders', data = sales_state)
plt.show()

sales_state = df.groupby(['State'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)
sns.set(rc = {'figure.figsize':(15,5)})
bx = sns.barplot(x = 'State', y = 'Amount', data = sales_state)
plt.show()'''

#-------------------->marital Status <--------------------------------------

'''ax = sns.countplot(x = 'Marital_Status', hue = 'Gender', data = df)
for bars in ax.containers:
   ax.bar_label(bars)
   plt.show()'''

#--------------------------->Occupation<--------------------------------------

'''ax = sns.countplot(x = 'Occupation', data = df)
sns.set(rc = {'figure.figsize':(30,5)})
for bars in ax.containers:
   ax.bar_label(bars)
   plt.show()

sales_Occupation = df.groupby(['Occupation'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
sns.set(rc = {'figure.figsize':(30,5)})
bx = sns.barplot(x = 'Occupation', y = 'Amount', data = sales_Occupation)
plt.show()'''

#----------------------->Product ID<------------------------------------

'''ax = sns.countplot(x = 'Product_Category', data = df)
sns.set(rc = {'figure.figsize':(30,5)})
for bars in ax.containers:
   ax.bar_label(bars)
   plt.show()

Sale_prdct_category = df.groupby(['Product_Category'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)
sns.set(rc = {'figure.figsize':(40,5)})
bx = sns.barplot(x = 'Product_Category', y = 'Amount', data = Sale_prdct_category)
plt.show()'''


#---------------->ProductID<----------------------------
'''Sale_prdct_Id = df.groupby(['Product_ID'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)
sns.set(rc = {'figure.figsize':(20,5)})
bx = sns.barplot(x = 'Product_ID', y = 'Orders', data = Sale_prdct_Id)
plt.show()'''
