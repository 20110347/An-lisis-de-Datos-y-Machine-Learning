import pandas as pd
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

def exit():
    root.destroy();

def browseFile():
    filetypes = (
        ('Excel files', '*.xlsx'),
    )

    filepath = fd.askopenfilename(
        title='Open a file',
        initialdir='C:/Users/Mariza/Documents/test1',
        filetypes=filetypes)

    if not filepath:
        messagebox.showerror("Error", "No se selecciono un archivo UwU")
        return

    displayExcelFile(filepath)

def displayExcelFile(filepath):
    # Read the Excel file using pandas
    df = pd.read_excel(filepath)
    # Get the columns "edad" and "raza"
    try:
        edad = df["edad"]
        raza = df["raza"]
    except Exception as e:
        # display an error message if an exception is caught
        messagebox.showerror("Error", f"Revisa el nombre de la columna o su tipo de dato")
        print(e)
        return

    try:
        agesFigure = plt.figure(figsize=(5, 8), dpi=70, facecolor="#F0F0F0")
        ax1 = agesFigure.add_subplot(111)
        bar1 = FigureCanvasTkAgg(agesFigure, root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.NONE)
        agesDataFrame = edad.round(
        decimals=0).value_counts().sort_index()
        agesDataFrame.plot(kind='bar', legend=False, ax=ax1, colormap="Spectral")
        ax1.set_title('Perros por Edad')
        ax1.set_xlabel("Edad")
        ax1.set_ylabel("Frecuencia")    

        # Plot the normal distribution of the raza column        
        breedsFigure = plt.figure(figsize=(18, 8), dpi=70, facecolor="#F0F0F0")
        ax2 = breedsFigure.add_subplot(111)
        bar2 = FigureCanvasTkAgg(breedsFigure, root)
        bar2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.NONE)
        breedsDataFrame = raza.value_counts().sort_index()
        breedsDataFrame.plot(kind='bar', legend=False, ax=ax2, colormap="terrain")
        ax2.set_title('Perros por Raza')
        ax2.set_xlabel("Razas")
        ax2.set_ylabel("Frecuencia")

        # Add the navigation toolbar to the plot window
        toolbar1 = NavigationToolbar2Tk(bar1, root)
        toolbar1.update()
        toolbar2 = NavigationToolbar2Tk(bar2, root)
        toolbar2.update()

    except Exception as e:
        # display an error message if an exception is caught
        messagebox.showerror("Error", f"Revisa tu entrada de datos")
        print(e)
        return
   

root = tk.Tk()
root.geometry("1300x625")
root.wm_title("Analisis de Razas de Perros")

# Add a button to select an Excel file
button = tk.Button(root, text='Seleccionar Archivo', command=browseFile)
button.pack(side=tk.TOP, pady=10)
button = tk.Button(root, text='Salir', command=exit)
button.pack(side=tk.BOTTOM, pady=10)

try:
    root.mainloop()    

except Exception as e:
    # display an error message if an exception is caught
    messagebox.showerror("Error", "Estas tontito te chingaste el programa")
    print(e)