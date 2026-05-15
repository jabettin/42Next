#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        _ = "str" + 1  # type: ignore
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except Exception as e:
            print(f"Caught {type(e).__name__}: {e}")
    print()
    print("All error types tested successfully!")


if __name__ == '__main__':
    test_error_types()
