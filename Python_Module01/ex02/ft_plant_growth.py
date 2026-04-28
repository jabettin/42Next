class Plant:
	def show(self)->None:
		print(f"{self.name}: {round(self.height,1)}cm, {self.days_old} days old")
	def age(self)->None:
		self.days_old += 1
	def grow(self)->None:
		self.height += 0.8

if __name__ == '__main__':
	initial_height: float = 25.0
	rose: Plant | None = None
	rose = Plant()
	rose.name: str = "Rose"
	rose.height: float = initial_height
	rose.days_old: int = 30
	print("=== Garden Plant Growth ===")
	rose.show()
	days: int = 1
	while days <= 7:
		rose.grow()
		rose.age()
		print(f"=== Day {days} ===")
		rose.show()
		days += 1
	print(f"Growth this week: {round(rose.height - initial_height, 1)}cm")