class BankAccount:

    ROI=10.5
    
    def __init__ (self,Name,Amount):
        self.Name=Name
        self.Amount=Amount 

    def display(self):
        print("Account Holder : ",self.Name)
        print("Current Balance : ",self.Amount)

    def deposit(self,DAmount):
        if DAmount > 0:
            self.Amount += DAmount
            print("Deposit Successfully : ",DAmount)
    
    def withdraw(self,WAmount):
        if WAmount > self.Amount:
            print("Insufficient balance..")
        elif WAmount <= 0 :
            print("Withdraw Successfully : ",WAmount)
        else :
            self.Amount -= WAmount
            print("Withdraw Successfully : ",WAmount)

    def Cal_interest(self):
        int=(self.Amount*BankAccount.ROI)/100
        return int

#def main():
print("--- Creating Account 1 ---")
account1=BankAccount("Sam",100000.0)
account1.display()

account1.deposit(1500.0)
account1.display()

interest=account1.Cal_interest()
print(f"Calculated Interest is {BankAccount.ROI} : {interest}")

account1.withdraw(2000.0)
account1.display()

account1.withdraw(10000.0)

#if __name__ == "__main__":
#    main()