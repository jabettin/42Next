#!/usr/bin/env python


def secure_archive(filename: str, action: str = 'r', content: str = '') -> tuple[bool, str]:
    try:
        with open(filename, action) as f:
            if action == 'r':
                return (True, f.read())
            elif action == 'w':
                f.write(content)
                return (True, 'Content successfully written to file')
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print('=== Cyber Archives Security ===')
    secure_archive("ancient_fragments.txt", "r",)
    secure_archive("ancient_fragments.txt", "w", "hello")


if __name__ == '__main__':
    main()
