#!/usr/bin/env python3
def input_temperature(tempstr: str) -> int:
    return int(tempstr)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    try:
        print("Input data is '25'")
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C")
        print()
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()

    try:
        print("Input data is 'abc'")
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
        print()
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()
