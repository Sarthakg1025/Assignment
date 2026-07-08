import threading
import time

def ascending():
   
    print("Thread1 starting...")
    for i in range(1, 51):
        print(f"Thread1: {i}")
        time.sleep(0.01)  
    print("Thread1 finished.")

def descending():
    
    print("\nThread2 starting...")
    for i in range(50, 0, -1):
        print(f"Thread2: {i}")
        time.sleep(0.01) 
    print("Thread2 finished.")

def main():
   
    t1 = threading.Thread(target=ascending, name="Thread1")
    t2 = threading.Thread(target=descending, name="Thread2")

   
    t2.start()

   
    t2.join()

   
    t1.start()
    
   
    t1.join()

if __name__ == "__main__":
    main()