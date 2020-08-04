from Models.GreyModels import NGM
import numpy as np
x = [15, 16.1, 17.3, 18.4, 18.7, 19.6, 19.9, 21.3, 22.5]
t = np.arange(len(x))+1
ngm = NGM()
ngm.fit(t, x)
y_predict = ngm.predict(t)
print(x)
print(y_predict)