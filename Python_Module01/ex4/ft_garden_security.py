#!/usr/bin/env python3
class Plant:
    name: str
    age: int
    height: float
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age
    def show(self):
        print(f"Plant created: {self.name}: {get_height(self.__height)}cm, {get_age(self.__age)} days old")
    def set_age(self, self.__age) -> int:
        self.__new_age = input()
        self.__age = self.__new_age
    def set_height(self, self.__height) -> float:
        self.__new_height = input()
        self.__height = self.__new_height
    def get_height(self) -> None:
        
    def get_age(self) -> None:



if __name__ == '__main__':
    print("=== Garden Security System ===")
