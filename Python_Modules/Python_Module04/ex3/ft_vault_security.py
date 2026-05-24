#!/usr/bin/env python3


def secure_archive(filename: str, action: str = 'r', content: str = '') -> tuple[bool, str]:
    try:
        with open(filename, action) as f:
            if action == 'r':
                return (True, f.read())
            elif action == 'w':
                f.write(content)
                return (True, 'Content successfully written to file')
            return (False, 'Invalid action')
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print('=== Cyber Archives Security ===')
    print("Using 'secure_archive' to read from a nonexistent file:")
    result1 = secure_archive("non/existent/file")
    print(result1)
    print("Using 'secure_archive' to read from an inaccessible file:")
    result2 = secure_archive("/etc/shadow")
    print(result2)
    print("Using 'secure_archive' to read from a regular file:")
    result3 = secure_archive("ancient_fragment.txt")
    print(result3)
    print("Using 'secure_archive' to write previous content to a new file:")
    result4 = secure_archive("newfile.txt", 'w', result3[1])
    print(result4)


if __name__ == '__main__':
    main()
