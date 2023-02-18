#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from sklearn.externals import joblib

import config


# In[ ]:


scaler = joblib.load(config.model['sklearn_scaler_file_name'])
regressor = joblib.load(config.model['model_file_name'])


# In[ ]:


df = pd.read_csv(config.model['test_data_file']).set_index('_id')
output = ['sys_val','dias_val']
y = df[output]
X = df.drop(columns=output)


# In[ ]:


y_pred = regressor.predict(scaler.transform(np.array([X])))
print(regressor.evaluate(X,y))

