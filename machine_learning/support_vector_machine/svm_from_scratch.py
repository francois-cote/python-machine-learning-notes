import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')


class SupportVectorMachine:
	def __init__(self, visualization=True):
		self.visualization = visualization
		self.colors = {1: 'r', -1: 'b'}
		if self.visualization:
			self.fig = plt.figure()
			self.ax = self.fig.add_subplot(1, 1, 1)

	def fit(self, data):
		pass

	def predict(self, data):
		# sign ( x.w+b )
		classification = 1


data_dict = {-1: np.array([[1, 7], [2, 8], [3, 8]]), 1: np.array([[5, 1], [6, -1], [7, 3]])}
