Checklen= lambda Str : len(Str)>5

def main():
	l=["Jay","Ganesh","I","am","Sarthak","Ghodekar"]
	ret=list(filter(Checklen,l))
	print(ret)
if __name__ == "__main__":
	main()