from collections import deque


def is_polindrome(string: str):
    dq = deque(string.lower().replace(" ", "").replace(".", "").replace("?", ""))
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


def main():
    example1 = "Mr. Owl ate my metal worm"
    example2 = "Was it a cat I saw?"
    example3 = "Step on no pets"
    not_polindrome = "This is not a polindrome"

    for example in [example1, example2, example3, not_polindrome]:
        print(f"'{example}' is polindrome: {is_polindrome(example)}")


if __name__ == "__main__":
    main()
