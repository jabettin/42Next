#!/usr/bin/env python3
class Plant:
	def show(self)->None:
		print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")
	def grow(self)->None:
		self.height: float = self.height + 0.8
	def age(self)->None:
		self.days_old: int = self.days_old + 1

if __name__ == '__main__':
	height: float = 10
	age: int = 5
	rose: Plant = None
	rose = Plant()
	rose.name: str = "Rose"
	rose.height: float = height
	rose.days_old: int = age
	print("=== Garden Plant Growth ===")
	rose.show()
	days: int = 1
	while days <= 7:
		rose.grow()
		rose.age()
		print(f"=== Day: {days} ===")
		rose.show()
		days += 1
	print(f"Growth this week: {round(rose.height - height, 1)}cm")