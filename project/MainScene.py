from godot import exposed, export
from godot import *

import numpy as np
import sklearn
import pandas as pd
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])

print(df.head())
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
#plt.show()


@exposed
class MainScene(Node2D):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		print(np.array([1,3,4]))
		print("Godot on Steam")
