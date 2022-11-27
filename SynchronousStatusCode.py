import time
import requests

def read_example() -> None:
    response = requests.get("https://www.example.com")
    print(response.status_code)

start = time.time()
read_example()
read_example()
end = time.time()
print(f"Running synchronously took: {end - start:.4f} seconds")