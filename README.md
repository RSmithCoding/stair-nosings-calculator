# Stair Nosings Calculator

Turns a list of stair nosing lengths into an order summary. It groups matching sizes together with a quantity for each, adds up the total length, and can save the summary as a PDF ready to send to the manufacturer.

## Why I built it

I built this while working for a flooring distributor, to make life easier for the sales department. Nosing orders came in as a list of individual lengths, and matching sizes had to be grouped and counted before the order could go to the manufacturer. This program does the grouping and counting automatically, making orders quicker to put together and less prone to mistakes.

## Features

- Enter nosing sizes one at a time, with a running list on screen
- Remove the last size entered if you make a mistake
- Order summary that groups matching sizes and counts how many of each
- Total length of all nosings
- Works with any unit of measurement, as long as one order uses the same unit throughout
- Optional PDF export of the order summary

## Built with

- Python 3
- [fpdf](https://pypi.org/project/fpdf/) for PDF export
- `collections.Counter` for grouping matching sizes
- Tkinter for the desktop version (early start)

## Running it

You need Python 3 and the fpdf package:

```
pip3 install fpdf
python3 Nosings.py
```

Sizes can be in any unit (mm, cm or metres), because customers sent measurements in whatever form suited them, on paper or by email. Just use the same unit for every size in one order.

Type each nosing size and press Enter. Type `R` to remove the last size or `D` when you're done. The summary is then shown on screen, and you can choose to save it as a PDF called `Nosing Order Summary.pdf` in the same folder.

## Example

```
Order Summary

Total Size... 6.45

Size        Quantity

0.9     ...     2
1.05    ...     1
1.2     ...     3
```

## Project status

The command-line version (`Nosings.py`) is the working program. `NosingsGui.py` is an early start on a desktop version: the window layout is there, but the buttons aren't connected to anything yet.

## What I learned

- Collecting input in a loop until the user chooses to stop
- Using `collections.Counter` to group and count matching values
- Creating PDF files from Python with fpdf
- Laying out a window with Tkinter frames and the grid system

## Ideas for improvement

- Build out the desktop version
- Check each entry is a valid number before adding it, so a typo can't crash the program at the total
- Name each PDF after the customer or date, so a new order doesn't overwrite the last one
- Make the screen-clearing work on Windows as well as macOS