import numpy as np
import pandas as pd
df=pd.read_csv(r'D:\AI\第3章\data\data\used_cars.csv',sep=',',header=0)
columns=['brand','bodyType','fuelType','gearbox','power','kilometer','notRepairedDamage','days','v_0','v_1','price']
df=df[columns][:]
df=(df-df.min())/(df.max()-df.min())
train_data=df.sample(frac=0.8,replace=False)
test_data=df.drop(train_data.index)
x_train=train_data.iloc[:,0:10].values
y_train=train_data['price'].values
x_test=test_data.iloc[:,0:10].values
y_test=test_data['price'].values
from sklearn.linear_model import SGDRegressor
import joblib
model=SGDRegressor(max_iter=1000,learning_rate='adaptive',eta0=0.01,loss='huber')
model.fit(x_train,y_train)
pre_score=model.score(x_train,y_train)
print('score=',pre_score)
print('coef=',model.coef_,'intercept=',model.intercept_)
joblib.dump(model,'.\\sava_model\SGDRegressor.model')
import joblib
import numpy as np

model = joblib.load('.\\sava_model\\SGDRegressor.model')
y_pred = model.predict(x_test)
print('测试集准确率得分 = %.5f' % model.score(x_test, y_test))
MSE = np.mean((y_test - y_pred) ** 2)
print('损失 MSE = {:.5f}'.format(MSE))
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize = (9,3))
ax1 = plt.subplot(111)
x = range(0,len(y_test))
plt.plot(x,y_test,'g',label = '真实值',marker = '*',linewidth = 0.5)
plt.plot(x,y_pred,'b',label = '预测值',marker = '.',linewidth = 0.5)
ax1.set_xlabel('样本序号')
ax1.set_ylabel('价格')
plt.legend(loc = 'upper right')
plt.show()