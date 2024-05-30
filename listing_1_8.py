import time
import threading
import requests


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


read_example_thread1 = threading.Thread(target=read_example)
read_example_thread2 = threading.Thread(target=read_example)
read_example_thread3 = threading.Thread(target=read_example)
read_example_thread4 = threading.Thread(target=read_example)
read_example_thread5 = threading.Thread(target=read_example)


start = time.time()

read_example_thread1.start()
read_example_thread2.start()
read_example_thread3.start()
read_example_thread4.start()
read_example_thread5.start()

print('Все потоки работают!')

read_example_thread1.join()
read_example_thread2.join()
read_example_thread3.join()
read_example_thread4.join()
read_example_thread5.join()


end = time.time()

print(f'Многопоточное выполнение заняло {end - start:.4f} с.')
