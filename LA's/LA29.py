import tkinter as tk
your_name1 = "Mauring"
your_name2 = "Bsit 2b"
windows_ko = tk.Tk()
windows_ko.title ("OOP La28")
windows_ko.geometry("1000x1000")
windows_ko.configure(bg="black")
text_disp = tk.Label(windows_ko, text=f"OOP la29 {your_name1}, {your_name2}")
text_disp.grid(row=0, column=0, padx = 100, pady=100)

windows_ko.mainloop()