import Vehicle
import argparse
import sys
import time
import datetime
current_date_time= datetime.datetime.now()

if sys.version_info[0] == 2:
	input = raw_input

class ParkingLot:
	def __init__(self):
		self.capacity = 0
		self.slotid = 0
		self.numOfOccupiedSlots = 0

	def createParkingLot(self,capacity):
		self.slots = [-1] * capacity
		self.capacity = capacity
		return self.capacity

	def getEmptySlot(self):
		for i in range(len(self.slots)):
			if self.slots[i] == -1:
				return i

	def park(self,regno,color):
		if self.numOfOccupiedSlots < self.capacity: 
			slotid = self.getEmptySlot()
			self.slots[slotid] = Vehicle.Car(regno,color)
			self.slotid = self.slotid+1
			self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
			return slotid+1
		else:
			return -1

	def leave(self,slotid):

		if self.numOfOccupiedSlots > 0 and self.slots[slotid-1] != -1:
			self.slots[slotid-1] = -1
			self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
			return True
		else:
			return False

	def status(self):
		print("Slot No.\tRegistration No.\tColour")
		for i in range(len(self.slots)):
			if self.slots[i] != -1:
				print(str(i+1) + "\t\t" +str(self.slots[i].regno) + "\t\t" + str(self.slots[i].color))
			else:
				continue

	def getRegNoFromColor(self,color):

		regnos = []
		for i in self.slots:

			if i == -1:
				continue
			if i.color == color:
				regnos.append(i.regno)
		return regnos
			
	def getSlotNoFromRegNo(self,regno):
		
		for i in range(len(self.slots)):
			if self.slots[i].regno == regno:
				return i+1
			else:
				continue
		return -1
			

	def getSlotNoFromColor(self,color):
		
		slotnos = []

		for i in range(len(self.slots)):

			if self.slots[i] == -1:
				continue
			if self.slots[i].color == color:
				slotnos.append(str(i+1))
		return slotnos

	def show_line(self,user_input):
        
		user_input = user_input.split()
		if user_input == 'create_parking_lot':
			n = int(line.split(' ')[1])
			res = self.createParkingLot(n)
			print('Created a parking lot with '+str(res)+' slots')

		elif user_input =='park':
			regno = line.split(' ')[1]
			color = line.split(' ')[2]
			res = self.park(regno,color)
			if res == -1:
				print("Sorry, parking lot is full")
			else:
				print('Allocated slot number: '+str(res))

		elif user_input =='leave':
			leave_slotid = int(line.split(' ')[1])
			status = self.leave(leave_slotid)
			if status:
				print('Slot number '+str(leave_slotid)+' is free')

		elif user_input == 'status':
			self.status()

		elif user_input == 'registration_numbers_for_cars_with_colour':
			color = line.split(' ')[1]
			regnos = self.getRegNoFromColor(color)
			print(', '.join(regnos))

		elif user_input == 'slot_numbers_for_cars_with_colour':
			color = line.split(' ')[1]
			slotnos = self.getSlotNoFromColor(color)
			print(', '.join(slotnos))

		elif user_input == 'slot_number_for_registration_number':
			regno = line.split(' ')[1]
			slotno = self.getSlotNoFromRegNo(regno)
			if slotno == -1:
				print("Not found")
			else:
				print(slotno)
		elif user_input == 'exit':
			exit(0)

        
        
        
def main():

	parkinglot = ParkingLot()
	   
    
	print("---- Welcome to the automated parking lot system ----")

	print("\n")
	time.sleep(2)
	print("System Initializing...")
	time.sleep(1)
	print("\n")
	user_input=input("Enter your choice - interactive or file ?: ")

	print("\n")
	if "interactive" in user_input.lower():
		
		while True:
			print("----------------------------")
			user_input=input("Enter your requirement: ")
			if user_input=="exit":
				print("Thank you for mingling with Me!")
				print("\n")
				breakleave
			parkinglot.show_line(user_input)

	if "file" in user_input.lower():

		with open("E:\parking lot project\input.txt","r") as f:
			for command in f:
				user_input=command
				parking.show_line(user_input)
			print("Thank you for mingling with Me!")
if __name__ == '__main__':
	main()