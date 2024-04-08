import tkinter as tk
import numpy as np
import time
import random

class SortingVisualizationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorting Algorithm Visualization")
        self.master.configure(bg="#f0f0f0")
        
        self.label_sort = tk.Label(master, text="Sorting algorithm:", pady=5, font=("Arial", 16, "bold"), bg="#f0f0f0")
        self.label_sort.grid(row=0, column=0, columnspan=3)
        
        self.sort_names = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
        self.start_buttons = {}
        self.canvases = {}
        self.text_displays = {}
        self.sort_functions = {
            "Bubble Sort": self.bubble_sort,
            "Selection Sort": self.selection_sort,
            "Insertion Sort": self.insertion_sort
        }
        
        self.create_sort_widgets()
    
    def create_sort_widgets(self):
        for i, sort_name in enumerate(self.sort_names):
            frame = tk.Frame(self.master, bg="#f0f0f0", padx=10, pady=10, borderwidth=2, relief="ridge")
            frame.grid(row=1, column=i)
            
            label = tk.Label(frame, text=f"{sort_name} Visualization", font=("Arial", 12, "bold"), bg="#f0f0f0")
            label.pack()
            
            self.start_buttons[sort_name] = tk.Button(frame, text="Start Visualization", command=lambda s=sort_name: self.start_visualization(s), bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=5, pady=5)
            self.start_buttons[sort_name].pack()
            
            self.canvases[sort_name] = tk.Canvas(frame, width=300, height=200, bg="white", borderwidth=2, relief="ridge")
            self.canvases[sort_name].pack()
            
            self.text_displays[sort_name] = tk.Text(frame, width=30, height=10, bg="#f0f0f0", font=("Arial", 10))
            self.text_displays[sort_name].pack()
    
    def start_visualization(self, sort_algorithm):
        data = [random.randint(10, 100) for _ in range(10)]
        self.draw_data(sort_algorithm, data)
        sorting_function = self.sort_functions[sort_algorithm]
        sorting_function(data, sort_algorithm)
    
    def draw_data(self, sort_algorithm, data, idx1=None, idx2=None):
        canvas = self.canvases[sort_algorithm]
        canvas.delete("all")
        bar_width = 300 / len(data)
        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = 200
            x1 = (i + 1) * bar_width
            y1 = 200 - value * 2
            color = "#2196F3" if i != idx1 and i != idx2 else "#FF5722"  # Highlight swapped elements
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
            canvas.create_text((x0 + x1) / 2, y1 + 10, text=str(value), fill="black", font=("Arial", 8))
            canvas.create_text((x0 + x1) / 2, y0 + 10, text=str(i), fill="black", font=("Arial", 8))

    def update_display(self, sort_algorithm, step):
        text_widget = self.text_displays[sort_algorithm]
        text_widget.insert(tk.END, step + "\n")
        text_widget.see(tk.END)

    def bubble_sort(self, data, sort_algorithm):
        n = len(data)
        for i in range(n):
            for j in range(n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    self.draw_data(sort_algorithm, data, j, j+1)  # Draw only the swapped elements
                    self.update_display(sort_algorithm, f"{data[j]} -> {data[j+1]}")
                    self.master.update()
                    time.sleep(0.5)
                    self.update_display(sort_algorithm, f"{data[j+1]} moved to position {j+1}")
                else:
                    self.update_display(sort_algorithm, f"{data[j+1]} stays at position {j+1}")
    
    def selection_sort(self, data, sort_algorithm):
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            self.draw_data(sort_algorithm, data, i, min_idx)  # Draw only the swapped elements
            self.update_display(sort_algorithm, f"{data[i]} -> {data[min_idx]}")
            self.master.update()
            time.sleep(0.5)
            self.update_display(sort_algorithm, f"{data[min_idx]} moved to position {i}")
    
    def insertion_sort(self, data, sort_algorithm):
        n = len(data)
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
            self.draw_data(sort_algorithm, data)
            self.update_display(sort_algorithm, f"{key} moved to position {j+1}")
            self.master.update()
            time.sleep(0.5)

def main():
    root = tk.Tk()
    root.geometry("900x600")
    app = SortingVisualizationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
