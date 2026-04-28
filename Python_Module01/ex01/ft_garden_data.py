class Plant:
	def show(self)->None:
		print(f"{self.name}: {self.height}cm, {self.age} days old")
if __name__ == '__main__':
	print("=== Garden plant data ===")
	rose = Plant()
	rose.name = "Rose"
	rose.height = 20
	rose.age = 5
	rose.show()

	lilly = Plant()
	lilly.name = "Lilly"
	lilly.height = 15
	lilly.age = 5
	lilly.show()

	sunflower = Plant()
	sunflower.name = "Sunflower"
	sunflower.height = 16
	sunflower.age = 7
	sunflower.show()