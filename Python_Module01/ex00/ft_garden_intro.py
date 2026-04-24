import os

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age


	# def ft_garden_intro(self):
	# 	print(f"name = {plant.name}")
	# 	print(f"height = {plant.height}")
	# 	print(f"age = {plant.age}")

def ft_garden_intro(plant):
		print(f"name = {plant.name}")
		print(f"height = {plant.height}")
		print(f"age = {plant.age}")




if __name__ == "__main__":
	name = str(input("Enter name: "))
	height = str(input("Enter height: "))
	age = int(input("Enter age: "))
	plant1 = Plant(name, height, age)
	os.system('clear')
	ft_garden_intro(plant1)

