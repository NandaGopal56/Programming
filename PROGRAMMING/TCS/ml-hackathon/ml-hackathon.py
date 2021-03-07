from pandas import read_csv
from sklearn.ensemble import RandomForestClassifier
import numpy as np

file = 'C:\\Users\\nanda gopal\\Desktop\\May 26 - Hands on\\churn.csv'
dataframe = read_csv(file)
#dataframe = dataframe.sample(frac=1)


#replacing true false values with 1 and 0
def replace_churn(val):
    if val == "False.":
        return 0
    else:
        return 1
dataframe['Churn?'] = dataframe['Churn?'].apply(replace_churn,1)

#replacing true false values with 1 and 0
def replace_intl_plan(val):
    if val == 'no':
        return 0
    else:
        return 1
dataframe["Int'l Plan"] = dataframe["Int'l Plan"].apply(replace_intl_plan,1)

#replacing true false values with 1 and 0 using map function
dataframe["VMail Plan"] = dataframe["VMail Plan"].map({"no":0,"yes":1}.get)

#dropping the columns State and phone
dataframe =  dataframe.drop(columns = "State")
dataframe =  dataframe.drop(columns = "Phone")


print(dataframe.info())
print(dataframe.shape)
print(dataframe.head(30))

x = dataframe[["Account Length","Area Code","Int'l Plan","VMail Plan","VMail Message","Day Mins","Day Calls","Day Charge",
               "Eve Mins","Eve Calls","Eve Charge","Night Mins","Night Calls","Night Charge","Intl Mins","Intl Calls",
                "Intl Charge","CustServ Calls"]]
y = dataframe["Churn?"]
test_size = 0.30
seed = 45

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=test_size,random_state=seed)

model = RandomForestClassifier(n_estimators=10)
model.fit(x_train,y_train)

result = model.score(x_test,y_test)
print("accuracy :",result*100)

#print(x_test["Churn?"])
print(y_test[100:200])