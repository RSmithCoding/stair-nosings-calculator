import os
import collections
from fpdf import FPDF

sizes = []
takeSize = ""

def clear():
    os.system('clear')

clear()

print("Nosing Size Calculator - Press 'D' when done or 'R' to remove last item")
print()

while takeSize not in ("d","D"):
    takeSize = input("Please enter the Nosing Size, takes any measurements just make sure the units match. Enter ('D' when done) > ")
    if takeSize not in ("d","D","r","R"):
        sizes.append(takeSize)
        clear()
        print(*sizes)
        print("")
    if takeSize in ("R","r"):
        sizes.pop()
        clear()
        print(*sizes)
        print()
        continue    
    else:
        print("Please enter a vaild size or enter 'D' or 'R' > ")
        continue

clear()
print("Order Summary")    
print()
sizes.sort()


total = sum(map(float, sizes))
quantity = collections.Counter(sizes)

print(f"Total Size... {total}")
print()
print("Size        Quantity")
print()
for key, value in quantity.items():
    print(f"{key}\t...\t{value}")


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

    input("Nosing Order Summary.pdf has been saved in the program directory press any key to quit.. ")

    quit()
    
elif choice in ("N","n"):

    quit()
        
  
