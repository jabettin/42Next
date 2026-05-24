#!/usr/bin/env python3

import sys
import typing


def transform_data(content: str) -> str:
    return '\n'.join(line + '#' for line in content.splitlines())


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: ft_stream_management.py <file>')
        return

    filename: str = sys.argv[1]
    f: typing.IO[str] | None = None

    print('=== Cyber Archives Recovery & Preservation ===')
    print(f"Accessing file '{filename}'")
    try:
        f = open(filename)
        content = f.read()
        print('---')
        print(content, end='')
        print('---')
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return
    finally:
        if f is not None:
            f.close()
            print(f"File '{filename}' closed.")
    print()
    transformed = transform_data(content)
    print('Transform data:')
    print('---')
    print(transformed)
    print('---')
    sys.stdout.write('Enter new file name (or empty): ')
    sys.stdout.flush()
    new_file = sys.stdin.readline().rstrip('\n')
    if new_file:
        out_file: typing.IO[str] | None = None
        print(f"Saving data to '{new_file}'")
        try:
            out_file = open(new_file, 'w')
            out_file.write(transformed + '\n')
        except OSError as e:
            sys.stderr.write(f"[STDERR] Error opening file '{new_file}': {e}\n")
        finally:
            if out_file is not None:
                out_file.close()
                print(f"Data saved in file '{new_file}'.")
            else:
                print("Data not saved.")
    else:
        print('Not saving data.')


if __name__ == '__main__':
    main()
