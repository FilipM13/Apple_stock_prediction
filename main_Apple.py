#analysis and prediction with
import pandas as pd 
from tools import get_directions
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
#visualisation with
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



'''
independent variables -> dependent variable
close price, volume, open price, high, low -> open directions
'''

#take data rom csv file
data = pd.read_csv('Apple_modified_5Y.csv')
data = data[::-1]

#take data values (independent variables)
data_v = data.iloc[:-1,1:].values

#create directions (dependent variable)
#each value in indicator of next day's open price (1 - price will be higher, 0 - the same, -1 - lower)
open_price_directions = get_directions(data.iloc[:,3].values)

#split
x_train, x_test, y_train, y_test = train_test_split(data_v, open_price_directions, test_size=0.20, random_state = 0)



#analysis and prediction
#create model
#classifier = DecisionTreeClassifier(random_state=0, criterion='entropy') #accuracy: 62%
#classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2) #accuracy: 60%
#classifier = SVC(kernel='rbf', random_state=0) #accuracy: 55%
#classifier = GaussianNB() #accuracy: 55%
#classifier = SVC(kernel='linear', random_state=0) #accuracy: % #runs for a very long time
#classifier = LogisticRegression(random_state=0) #accuracy: 56.75%
classifier = RandomForestClassifier(n_estimators=5 , criterion='entropy', random_state=0) #accuracy: 66% #most accurate

#fit
classifier.fit(x_train, y_train)

#predict
y_pred = classifier.predict(x_test)

#evaluate
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)
#print results
print(cm)
for n, i in enumerate(cm):
  print(f'Group {n} - correct: {i[n]}, incorrect: {sum(i)-i[n]}.')
print(f'accuracy: {round(ac*100, 2)} %.')



#visualisation
fig, ax = plt.subplots(dpi=200)
x = range(len(data_v))
#plot stock open price
ax.plot(x, data.iloc[:,3].values[:-1], color='black', label='5 years of Apple stock open price', lw=0.5, zorder=2)
#plot stock close price
ax.plot(x, data.iloc[:,1].values[:-1], label='5 years of Apple stock close price', lw=0.3, zorder=1)
#plot stock high
ax.plot(x, data.iloc[:,4].values[:-1], label='5 years of Apple stock high', lw=0.3, zorder=1)
#plot stock low
ax.plot(x, data.iloc[:,5].values[:-1], label='5 years of Apple stock low', lw=0.3, zorder=1)

#plot direction
for n, v in enumerate(open_price_directions[:-1]):
  if v == 1: #green area - opening price going up
    #rgb(161,202,149)
    ax.axvspan(n, n+1, color=[0.631, 0.792, 0.584, 1], lw=0)
  elif v == 0: #blue area - opening price does not change
    ax.axvspan(n, n+1, color=[0.298, 0.345, 0.627, 1], lw=0)
  else: #red area - opening price going down
    ax.axvspan(n, n+1, color=[0.914, 0.4, 0.4, 1], lw=0)

#title
plt.title('Apple stock')
#colors
ax.set_facecolor((0.75, 0.75, 0.85))
fig.set_facecolor((0.97, 0.97, 1))
#adjust X axis
dates = data.iloc[:-1,0].values
plt.xticks(range(len(dates)), dates, size='small', rotation=-45, fontsize=4)
tick_spacing = 20
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.xlabel('date [mm/dd/yyyy]', fontsize=8)
#adjust Y axis
plt.ylabel('price [$]', fontsize=8)
plt.yticks(fontsize=5)
#show legend
plt.legend(fontsize=5)
#execute plot
plt.show()
