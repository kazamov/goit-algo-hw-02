from queue import Queue
from uuid import uuid4


class Task:
    def __init__(self, description):
        self.id = uuid4()
        self.description = description

    def __str__(self):
        return f"{self.id} - {self.description}"


def generate_request(
    q: Queue,
    description: str,
):
    task = Task(description)
    q.put(task)
    print(f"Task '{task}' is added to queue")


def process_request(q: Queue):
    if q.empty():
        print("Queue is empty")
    else:
        task = q.get()
        print(f"Task '{task}' is processed")


def main():
    queue = Queue()

    try:
        while True:
            print("\n1. Generate request")
            print("2. Process request")
            print("3. Exit\n")

            choice = input("Make a choice: ")

            if choice == "1":
                description = input("Enter description: ")
                generate_request(queue, description)
            elif choice == "2":
                process_request(queue)
            elif choice == "3":
                print("Exiting")
                break
            else:
                print("Invalid choice")
    except KeyboardInterrupt:
        print("Exiting")


if __name__ == "__main__":
    main()
