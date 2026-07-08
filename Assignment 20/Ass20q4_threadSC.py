import threading

def lowercase(input_string):
   
    count = sum(1 for char in input_string if char.islower())
    
   
    current_thread = threading.current_thread()
    
  
    print(f"[{current_thread.name}] (ID: {current_thread.ident})")
    print(f"Result: Lowercase character count = {count}\n")

def uppercase(input_string):
  
    count = sum(1 for char in input_string if char.isupper())
    
  
    current_thread = threading.current_thread()
    
   
    print(f"[{current_thread.name}] (ID: {current_thread.ident})")
    print(f"Result: Uppercase character count = {count}\n")

def digits(input_string):
   
    count = sum(1 for char in input_string if char.isdigit())
    
   
    current_thread = threading.current_thread()
    
   
    print(f"[{current_thread.name}] (ID: {current_thread.ident})")
    print(f"Result: Numeric digit count = {count}\n")

def main():
   
    user_input = input("Enter a string to analyze: ")
    

   
    small = threading.Thread(target=lowercase, args=(user_input,), name="Small")
    capital = threading.Thread(target=uppercase, args=(user_input,), name="Capital")
    digitss = threading.Thread(target=digits, args=(user_input,), name="Digits")

    
    small.start()
    capital.start()
    digitss.start()

   
    small.join()
    capital.join()
    digitss.join()
    
    print("complete.")

if __name__ == "__main__":
    main() 