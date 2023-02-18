#!/usr/bin/env python
# coding: utf-8

# In[ ]:


mongodb = {
    'host': 'localhost',
    'port': 27017
}

serial = {
    'port': '/dev/ttyUSB0',
    'baud_rate': 9600    
}

model = {
    'model_file_name': 'sample_data/PrenatalTracker.h5',
    'sklearn_scaler_file_name': 'sample_data/scaler.save',
    'test_data_file': 'sample_data/test_data.csv'
}

