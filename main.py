from Investment import Investment

if __name__ == '__main__':

	while True:
		
		name = input("Enter Investment Name: ")
		
		if name =="exit":
			break

		principal = float(input("Enter Principal Amount: Rs."))

		duration = int(input("Enter Duration: "))

		new_investment = Investment(name,principal,duration)

		rate = float(input("Enter Interest Rate: "))

		ROI = new_investment.calcROI(rate)*100
		netReturn = new_investment.calcNetReturn(rate)
		finalAmount = new_investment.calcFinalAmount(rate)

		print(f"ROI:\t{ROI}%")
		print(f"Net Returns:\t Rs. {netReturn}")
		print(f"Final Amount:\t Rs. {finalAmount}")
