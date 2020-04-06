#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
data = pd.read_csv(r"C:\Users\kartik agrawal\Desktop\laptops_prepared_scored.csv")

independent_variables = data.columns 
independent_variables = data.columns 
independent_variables = independent_variables.delete(8) 
X = data[independent_variables] 
Y = data["Price_euros"] 
import sklearn.linear_model as lm 
lr = lm.LinearRegression() 
lr.fit(X,Y) 

user_info = {} 
counter =1 
for features in independent_variables: 
#temp = input("Enter "+features+": ") 
temp=sys.argv[counter] 
counter=counter+1 
user_info[features]= temp user_info_df = pd.DataFrame(data=user_info, index=[0], columns=independent_variables) 
# user_df 
price = lr.predict(user_info_df) 
print(int(round(price[0]))) 
 

