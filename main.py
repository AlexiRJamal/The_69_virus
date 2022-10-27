# import os
# import threading

# fileSizeInBytes = 1000000000

# def makeFile(name):
#     with open(f'{name}', 'wb') as fout:
#         print(f"Writing file {name}...")
#         fout.write(os.urandom(fileSizeInBytes))
#         print(f"File {name} has been saved.")

# t1 = threading.Thread(target=makeFile, args=('test1',))
# t2 = threading.Thread(target=makeFile, args=('test2',))
# t3 = threading.Thread(target=makeFile, args=('test3',))
# t4 = threading.Thread(target=makeFile, args=('test4',))
# t5 = threading.Thread(target=makeFile, args=('test5',))

# t1.start()
# print("Thread 1 started.")
# t2.start()
# print("Thread 2 started.")
# t3.start()
# print("Thread 3 started.")
# t4.start()
# print("Thread 4 started.")
# t5.start()
# print("Thread 5 started.")

import os

fileSizeInBytes = 2048

def makeFile(name):
    with open(f"{name}.txt", 'wb') as fout:
        print(f"Writing file {name}...")
        fout.write(os.urandom(fileSizeInBytes))
        print(f"File {name}.txt has been saved.")

counter = 0
while counter<=10:
    makeFile(counter)
    counter+=1