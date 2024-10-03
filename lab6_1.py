
import tkinter as tk

def convert_weight():
    try:
        weight_kg = float(entry.get())
        
        weight_g = weight_kg * 1000
        weight_lb = weight_kg * 2.20462
        weight_oz = weight_kg * 35.274
        
        result_g.config(text=f"Грами: {weight_g:.2f} г")
        result_lb.config(text=f"Фунти: {weight_lb:.2f} lb")
        result_oz.config(text=f"Унції: {weight_oz:.2f} oz")
    except ValueError:
        result_g.config(text="Будь ласка, введіть числове значення.")
        result_lb.config(text="")
        result_oz.config(text="")

root = tk.Tk()
root.title("Конвертер ваги")

entry = tk.Entry(root)
entry.pack(pady=10)

convert_button = tk.Button(root, text="Перевести", command=convert_weight)
convert_button.pack(pady=10)

result_g = tk.Label(root, text="")
result_g.pack(pady=5)

result_lb = tk.Label(root, text="")
result_lb.pack(pady=5)

result_oz = tk.Label(root, text="")
result_oz.pack(pady=5)

root.mainloop()
