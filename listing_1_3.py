import threading


def hello_from_thread():
    print(f'Привет от потока {threading.current_thread()}!\n')


hello_target = threading.Thread(target=hello_from_thread)
hello_target_2 = threading.Thread(target=hello_from_thread)
hello_target_3 = threading.Thread(target=hello_from_thread)
hello_target_4 = threading.Thread(target=hello_from_thread)
hello_target.start()
hello_target_2.start()
hello_target_3.start()
hello_target_4.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'В данный момент Python выполняет {total_threads} поток(ов)')
print(f'Имя текущего потока {thread_name}')
hello_target.join()
hello_target_2.join()
hello_target_3.join()
hello_target_4.join()
