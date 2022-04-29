import math
import pandas

class Investment():
	"""Investment Class is an object for any type of investment charactersized by the principal amount and duration of investment"""
	def __init__(self, name: string,principal: float, duration: int):
		super(Investment, self).__init__()
		self.name = name
		self.principal = principal
		self.duration = duration
		self.risk = 1.0

	def calcFinalAmount(self, rate: float,n=1):
		return self.principal*math.pow(1+rate/n,n*self.duration)

	def calcNetReturn(self, rate: float, n=1):
		finalAmount = self.calcFinalAmount(rate,n)
		return finalAmount-self.principal

	def calcROI(self,rate: float,n=1,cost=0.0,dividend=0.0):
		ROI=(self.calcNetReturn(rate,n)+dividend-cost)/self.principal
		return ROI

	def createReport():
		pass

	def __log():
		pass