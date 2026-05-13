#!/usr/bin/env python3

def input_temperature(tempstr: str) -> int:
    result = int(tempstr)
    if 0 <= result <= 40:
        return result
    elif result > 40:
        raise ValueError(f"{result}°C is too hot for plants (max 40°C)")
    else:
        raise ValueError(f"{result}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    try:
        temp = '25'
        print(f"Input data is '{temp}'")
        result = input_temperature(temp)
        print(f"Temperature is now {result}°C")
        print()
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()

    try:
        temp = 'abc'
        print(f"Input data is '{temp}'")
        result = input_temperature(temp)
        print(f"Temperature is now {result}°C")
        print()
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()

    try:
        temp = '100'
        print(f"Input data is '{temp}'")
        result = input_temperature(temp)
        print(f"Temperature is now {result}°C")
        print()
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()

    try:
        temp = '-50'
        print(f"Input data is '{temp}'")
        result = input_temperature(temp)
        print(f"Temperature is now {result}°C")
        print()
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()
