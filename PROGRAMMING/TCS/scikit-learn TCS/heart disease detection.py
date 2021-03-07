from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

dataframe = read_csv("C:\\Users\\nanda gopal\\Desktop\\scikit-learn TCS\\heart.csv")

array = dataframe.values
x = array[:,0:12]
y = array[:,12]
test_size = 0.20
seed = 45

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=test_size,random_state=seed)

model = RandomForestClassifier()
model.fit(x_train,y_train)

result = model.score(x_test,y_test)
print("accuracy :",result*100)