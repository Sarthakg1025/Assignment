import Ass17q1_Mod  
	
def main():
	no1=float(input("Enter the first number : "))
	no2=float(input("Enter the second number : "))
	
	ret1=Ass17q1_Mod.Add(no1,no2)
	print(f"\nAddition is {ret1:.0f}")

	ret2=Ass17q1_Mod.Sub(no1,no2)
	print(f"Subtraction is {ret2:.0f}")

	ret3=Ass17q1_Mod.Mul(no1,no2)
	print(f"Multiplication is {ret3:.0f}")

	ret4=Ass17q1_Mod.Div(no1,no2)
	print(f"Division is {ret4:.4f}")
	
	

if __name__ == "__main__":
	main()