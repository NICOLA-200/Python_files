

from multiprocessing import Process
import time


def counter(num):
     count = 0
     while count < num:
          count += 1

def main():
     a = Process(target=counter, args=(100000000000,))
     a.start()
     a.join()

     print("finished in:", time.perf_counter(), "seconds")


if __name__ =='__main__':
     main() 