#!/usr/bin/env python3
class Plant:
    name: str
    height: float
    age: int
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age
    def show(self):
        print(f"Plant created: {self.name}: {self.__height}cm, {self.__age} days old")
    def set_age(self) -> int:
        self.__new_age = input()
        if self.__new_age > 0:
            self.__age = self.__new_age
        else:
            print("Age has to be a positive int")
    def set_height(self, __height) -> float:
        self.__new_height = input()
        self.__height = self.__new_height




if __name__ == '__main__':
    print("=== Garden Security System ===")
    rose = Plant("rose", 25.5, 20)
    rose.show()
    rose.set_age()
    rose.show()
