#scaling: it ensures that all features contribute equally to the model by bringing them to a commom scale, improvong models performance, for distance- based algorithms. z=(x-mean)/ s.d
from sklearn.preprocessing import StandardScaler
import numpy as np

X=np.array([[1,2], [3,4], [5,6]])
scaler= StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)