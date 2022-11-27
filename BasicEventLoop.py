from collections import deque

messages = deque()
while True:
    print("Checking messages.")
    if messages:
        print("Waiting for messages.")
        message = messages.pop()
        print(message)