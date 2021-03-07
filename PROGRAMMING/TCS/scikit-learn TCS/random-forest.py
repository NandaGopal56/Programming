from pandas import read_csv
#from numpy import set_printoptions
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

file = 'BBC.csv'
dataframe = read_csv(file)

array = dataframe.values
print(array)
x = array[:,0:11]
y = array[:,11]
test_size = 0.20
seed = 45

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=test_size,random_state=seed)

model = RandomForestClassifier(n_estimators=100)
model.fit(x_train,y_train)

result = model.score(x_test,y_test)
print("accuracy :",result*100)


