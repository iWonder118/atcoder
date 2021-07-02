import time


class Timer:
    start = 0

    def __init__(self):
        self.start = time.perf_counter()

    def get_elapsed_time(self):
        if self.start:
            return time.perf_counter() - self.start
        else:
            raise Exception("Did't initialized!")


def performance_timer(_str):

    def _performance_timer(func):
            
        def wrapper(*args, **kwargs):
            print(_str)
            timer = Timer()
            func(*args, **kwargs)
            print("{}s".format(timer.get_elapsed_time()))
        return wrapper
    return _performance_timer


@performance_timer("Hello?")
def test_method():
    time.sleep(1)
    print("Hello")


def main():
    test_method()


if __name__ == "__main__":
    main()
