import tkinter as tk
from tkinter import messagebox


def analyze_dna():
    dna = sequence_box.get().upper().replace(" ", "")

    if dna == "":
        messagebox.showwarning("Warning", "Please enter a DNA sequence.")
        return

    if any(base not in "ATGC" for base in dna):
        messagebox.showerror(
            "Invalid DNA",
            "Please enter only A, T, G and C."
        )
        return

    length = len(dna)

    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    a_percent = (a / length) * 100
    t_percent = (t / length) * 100
    g_percent = (g / length) * 100
    c_percent = (c / length) * 100

    gc_content = ((g + c) / length) * 100
    at_content = ((a + t) / length) * 100

    # DNA to RNA
    rna = dna.replace("T", "U")

    # Complement
    complement = ""

    for base in dna:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"

    # Reverse Complement
    reverse_complement = complement[::-1]

    result.delete("1.0", tk.END)

    result.insert(tk.END, "DNA SEQUENCE ANALYSIS\n")
    result.insert(tk.END, "============================\n\n")

    result.insert(tk.END, f"DNA Sequence       : {dna}\n")
    result.insert(tk.END, f"Sequence Length    : {length}\n\n")

    result.insert(tk.END, "NUCLEOTIDE COUNT\n")
    result.insert(tk.END, "----------------------------\n")
    result.insert(tk.END, f"Adenine (A)        : {a}\n")
    result.insert(tk.END, f"Thymine (T)        : {t}\n")
    result.insert(tk.END, f"Guanine (G)        : {g}\n")
    result.insert(tk.END, f"Cytosine (C)       : {c}\n\n")

    result.insert(tk.END, "NUCLEOTIDE PERCENTAGE\n")
    result.insert(tk.END, "----------------------------\n")
    result.insert(tk.END, f"A percentage       : {a_percent:.2f}%\n")
    result.insert(tk.END, f"T percentage       : {t_percent:.2f}%\n")
    result.insert(tk.END, f"G percentage       : {g_percent:.2f}%\n")
    result.insert(tk.END, f"C percentage       : {c_percent:.2f}%\n\n")

    result.insert(tk.END, f"GC Content         : {gc_content:.2f}%\n")
    result.insert(tk.END, f"AT Content         : {at_content:.2f}%\n\n")

    result.insert(tk.END, "SEQUENCE CONVERSION\n")
    result.insert(tk.END, "----------------------------\n")
    result.insert(tk.END, f"RNA Sequence       : {rna}\n")
    result.insert(tk.END, f"Complement         : {complement}\n")
    result.insert(tk.END, f"Reverse Complement : {reverse_complement}\n")


def clear_all():
    sequence_box.delete(0, tk.END)
    result.delete("1.0", tk.END)


# Main window
window = tk.Tk()
window.title("DNA Sequence Analyzer")
window.geometry("650x650")
window.resizable(False, False)

heading = tk.Label(
    window,
    text="DNA Sequence Analyzer",
    font=("Arial", 21, "bold")
)
heading.pack(pady=18)

instruction = tk.Label(
    window,
    text="Enter DNA sequence (A, T, G, C):",
    font=("Arial", 12)
)
instruction.pack()

sequence_box = tk.Entry(
    window,
    width=55,
    font=("Arial", 13)
)
sequence_box.pack(pady=12)

button_frame = tk.Frame(window)
button_frame.pack(pady=5)

analyze_button = tk.Button(
    button_frame,
    text="Analyze",
    command=analyze_dna,
    width=14
)
analyze_button.grid(row=0, column=0, padx=8)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_all,
    width=14
)
clear_button.grid(row=0, column=1, padx=8)

result_heading = tk.Label(
    window,
    text="Analysis Result",
    font=("Arial", 14, "bold")
)
result_heading.pack(pady=12)

result = tk.Text(
    window,
    width=65,
    height=27,
    font=("Courier New", 10)
)
result.pack()

window.mainloop()