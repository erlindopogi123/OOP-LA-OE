import tkinter as tk
your_name1 = "Mauring"
your_name2 = "Bsit 2b"

windows_ko = tk.Tk()
windows_ko.title ("OOP La28")
windows_ko.geometry("1000x1000")
windows_ko.configure(bg="black")

text_disp = tk.Label(windows_ko, text=f"OOP la29 {your_name1}, {your_name2}")
text_disp.grid(row=0, column=0, padx = 100, pady=100)

counter = 0
def gawin_mo_to():
    global counter
    print(f"My favorite anime is naruto {counter}")
    counter +=1

button_ito = tk.Button(windows_ko, text="run", command=gawin_mo_to)
button_ito.grid(row=10, column=10) 

windows_ko.mainloop()