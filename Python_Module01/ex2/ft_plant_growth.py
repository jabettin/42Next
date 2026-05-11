#!/usr/bin/env python3
class Plant:
    name: str
    height: float
    d_old: int

    def show(self) -> None:
        info = f"{self.name}: {round(self.height, 1)}cm, {self.d_old} days old"
        print(info)

    def age(self) -> None:
        self.d_old += 1

    def grow(self) -> None:
        self.height += 0.8


if __name__ == '__main__':
    initial_height: float = 25.0
    rose: Plant | None = None
    rose = Plant()
    rose.name = "Rose"
    rose.height = initial_height
    rose.d_old = 30
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
