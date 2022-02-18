import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.linspace(10,50,10)
print(x)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y)
plt.show()
plt.plot(x,z)
plt.show()
df=pd.read_csv('diabetes.csv')
df.head()