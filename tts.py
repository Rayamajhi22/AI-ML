from sklearn.model_selection import train_test_split
import numpy as np

x = np.array([[1,2],[3,4],[5,6],[7,8]])
y = np.array([0,1,0,1])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(f"Train: {x_train.shape}, Test: {x_test.shape}")
