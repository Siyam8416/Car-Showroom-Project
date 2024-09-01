import tkinter as tk
from tkinter import messagebox

class CarShowroom:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Showroom")
        self.root.geometry("500x500")
        
        # Available cars for sale and rent (in PKR)
        self.cars = {
            "Civic": {"price": 4000000, "rent_per_hour": 500},
            "Grande": {"price": 4500000, "rent_per_hour": 600},
            "City": {"price": 3000000, "rent_per_hour": 400},
            "Suzuki Every": {"price": 1500000, "rent_per_hour": 200},
            "Alto": {"price": 1300000, "rent_per_hour": 150},
            "Swift": {"price": 2200000, "rent_per_hour": 350},
            "Fortuner": {"price": 7500000, "rent_per_hour": 800}
        }
        
        self.sold_cars = []
        self.rented_cars = []

        # UI Elements
        self.label = tk.Label(root, text="Pakistani Car Showroom", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        self.label_select = tk.Label(root, text="Select a Car:")
        self.label_select.pack(pady=5)
        
        self.car_var = tk.StringVar(root)
        self.car_var.set("Select a car")
        
        self.car_menu = tk.OptionMenu(root, self.car_var, *self.cars.keys())
        self.car_menu.pack(pady=5)
        
        self.buy_button = tk.Button(root, text="Buy Car", command=self.buy_car)
        self.buy_button.pack(pady=10)
        
        self.rent_button = tk.Button(root, text="Rent Car", command=self.rent_car)
        self.rent_button.pack(pady=10)
        
        self.summary_button = tk.Button(root, text="Show Summary", command=self.show_summary)
        self.summary_button.pack(pady=20)

    def buy_car(self):
        car = self.car_var.get()
        if car != "Select a car":
            price = self.cars[car]["price"]
            self.sold_cars.append(car)
            messagebox.showinfo("Purchase", f"You bought a {car} for Rs. {price:,}")
        else:
            messagebox.showwarning("Warning", "Please select a car to buy")
    
    def rent_car(self):
        car = self.car_var.get()
        if car != "Select a car":
            rent_window = tk.Toplevel(self.root)
            rent_window.title("Rent a Car")
            rent_window.geometry("300x250")
            
            hours_label = tk.Label(rent_window, text="Enter number of hours:")
            hours_label.pack(pady=10)
            
            self.hours_entry = tk.Entry(rent_window)
            self.hours_entry.pack(pady=5)
            
            minutes_label = tk.Label(rent_window, text="Enter number of minutes:")
            minutes_label.pack(pady=10)
            
            self.minutes_entry = tk.Entry(rent_window)
            self.minutes_entry.pack(pady=5)
            
            rent_confirm_button = tk.Button(rent_window, text="Confirm Rent", command=lambda: self.confirm_rent(car))
            rent_confirm_button.pack(pady=20)
        else:
            messagebox.showwarning("Warning", "Please select a car to rent")
    
    def confirm_rent(self, car):
        try:
            hours = int(self.hours_entry.get())
            minutes = int(self.minutes_entry.get())
            rent_rate_per_minute = self.cars[car]["rent_per_hour"] / 60
            total_rent = (hours * self.cars[car]["rent_per_hour"]) + (minutes * rent_rate_per_minute)
            self.rented_cars.append((car, hours, minutes, total_rent))
            messagebox.showinfo("Rent", f"You rented a {car} for {hours} hours and {minutes} minutes. Total cost: Rs. {total_rent:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for hours and minutes")

    def show_summary(self):
        total_sales = sum(self.cars[car]["price"] for car in self.sold_cars)
        total_rent_income = sum(rent[3] for rent in self.rented_cars)
        
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Summary")
        summary_window.geometry("400x500")
        
        sold_label = tk.Label(summary_window, text="Sold Cars:", font=("Helvetica", 12))
        sold_label.pack(pady=10)
        
        if self.sold_cars:
            for car in self.sold_cars:
                tk.Label(summary_window, text=f"{car} - Rs. {self.cars[car]['price']:,}").pack()
            tk.Label(summary_window, text=f"Total Sales: Rs. {total_sales:,}", font=("Helvetica", 12, "bold")).pack(pady=10)
        else:
            tk.Label(summary_window, text="No cars sold yet.").pack()

        rented_label = tk.Label(summary_window, text="Rented Cars:", font=("Helvetica", 12))
        rented_label.pack(pady=20)
        
        if self.rented_cars:
            for car, hours, minutes, total_rent in self.rented_cars:
                tk.Label(summary_window, text=f"{car} - {hours}h {minutes}m - Rs. {total_rent:.2f}").pack()
            tk.Label(summary_window, text=f"Total Rental Income: Rs. {total_rent_income:.2f}", font=("Helvetica", 12, "bold")).pack(pady=10)
        else:
            tk.Label(summary_window, text="No cars rented yet.").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CarShowroom(root)
    root.mainloop()
