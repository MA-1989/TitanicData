import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%pylab

titanicdata = pd.read_csv('titanic_data.csv')

titanicdata.info()
titanicdata.describe()

#The total number of the survivors
survived_num = titanicdata['Survived'].sum()
dead_num = titanicdata['Survived'].count() - titanicdata['Survived'].sum()
print "%d people survived, while %d people were dead." %(survived_num, dead_num)

survived_rate = float(survived_num)/titanicdata['Survived'].count()

labels = ['Survived', 'Dead']
X = [survived_num, dead_num]
fig = plt.figure()
plt.pie(X, labels=labels, autopct='%1.2f%%')
plt.title('Survival rate')
plt.show()

#The number of the survivors of three different Pclasses
Pclass_total = titanicdata[['Pclass', 'Survived']].groupby(['Pclass']).count()
print Pclass_total
plt.figure()
plt.subplot()
sns.countplot(x='Pclass', data=titanicdata)
plt.title('Pclass Count')

Pclass_survivors = titanicdata[titanicdata['Survived'] == 1]
Pclass_survivors[['Pclass', 'Survived']].groupby(['Pclass']).sum()
plt.figure()
plt.subplot()
sns.countplot(x='Pclass', data=Pclass_survivors)
plt.title('Pclass Count')

Pclass_survivedrate = titanicdata.groupby('Pclass')['Survived'].mean()
Pclass_survivedrate.plot(kind='bar')

#The number of the survivors between two genders
male_total = titanicdata['Sex'][titanicdata['Sex'] == 'male'].count()
female_total = titanicdata['Sex'][titanicdata['Sex'] == 'female'].count()

survivor_gender = titanicdata.groupby(['Sex']).Survived.sum()
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Sex')
ax1.set_ylabel('Number')
ax1.set_title('The survivors of two genders')
survivor_gender.plot(kind='bar')
plt.show()

gender_rate = (titanicdata.groupby(['Sex']).sum()/titanicdata.groupby(['Sex']).count())['Survived']
gender_rate.plot(kind='bar')
