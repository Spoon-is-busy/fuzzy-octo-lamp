import tkinter as tk
from tkinter import messagebox

class IncomeTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Income Tracker")
        
        self.monthly_incomes = {}
        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Enter your monthly incomes:").pack()

        for month in self.months:
            tk.Label(self.master, text=month).pack(side=tk.LEFT)
            entry = tk.Entry(self.master)
            entry.pack(side=tk.LEFT)
            self.monthly_incomes[month] = entry

        tk.Button(self.master, text="Calculate", command=self.calculate_incomes).pack(pady=10)
        
    def calculate_incomes(self):
        try:
            incomes = {month: float(entry.get()) for month, entry in self.monthly_incomes.items()}
            max_month = max(incomes, key=incomes.get)
            min_month = min(incomes, key=incomes.get)

            message = f"Month with the highest income: {max_month}\nMonth with the lowest income: {min_month}"
            messagebox.showinfo("Results", message)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for incomes.")

if __name__ == "__main__":
    root = tk.Tk()
    app = IncomeTrackerApp(root)
    root.mainloop()
