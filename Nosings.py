import os
import collections
from fpdf import FPDF

sizes = []
takeSize = ""

def clear():
    os.system('clear')

clear()

print("Nosing Size Calculator")
print()

while True:

    print("Please enter the Nosing Size, takes any measurements just make sure the units match")
    takeSize = input("Enter ('D' when done, 'R' to remove) > ").strip().lower()

    try:
        size = float(takeSize)
        sizes.append(size)
        clear()
        print(*sizes) 
        print("")   
        continue

    except ValueError:
        clear()
        print(*sizes)
        print("")
        pass

    if takeSize == "d":
        break

    elif takeSize == "r":
        if sizes:
            sizes.pop()
            clear()
            print(*sizes)
            print("")

        else:
            input("No sizes have been entered, press any key to continue.. ")
            clear()




clear()
print("Order Summary")    
print()
sizes.sort()


total = round(sum(map(float, sizes)),3)
quantity = collections.Counter(sizes)

print(f"Total Size... {total}")
print()
print("Size        Quantity")
print()
for key, value in quantity.items():
    print(f"{key:<15}{value}")


print()
choice = input("Enter 'Y' to print summary to a PDF file or 'N' to quit > ")

while choice not in ("y","Y","n","N"):

    choice = input("Enter 'Y' to print summary to a PDF file or 'N' to quit > ")


if choice in ("y","Y"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Order Summary", ln=1, align="C")
    pdf.ln()
    pdf.ln()
    


    for key, value in quantity.items():
 
        pdf.cell(50,5, txt=str(key),ln=0,align="L")
        pdf.cell(50,5, txt=str(value),ln=0,align="L")
        pdf.ln()



    pdf.cell(200, 30, txt=(f"Total... {str(total)}           "), ln=1, align="R")

    pdf.output("Nosing Order Summary.pdf")

    print("")
    input("Nosing Order Summary.pdf has been saved in the program directory press any key to quit.. ")

    quit()
    
elif choice in ("N","n"):

    quit()
        
  
