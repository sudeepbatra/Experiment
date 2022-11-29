import functools
import time
from typing import Callable, Any


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args: Any, **kwargs: Any) -> Any:
            print(f"staring {func} with args: {args} {kwargs}")
            start_time = time.time()
            try:
                await func(*args, **kwargs)
            finally:
                end_time = time.time()
                total_time = end_time - start_time
                print(f"finished {func} in {total_time:.4f} seconds(s)")

        return wrapped

    return wrapper
