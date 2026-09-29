def dna_analyzer(sequence):
    sequence = sequence.upper()
    if not all(base in "ATGC" for base in sequence):
        print("Invalid DNA sequence!")
        return

    A = sequence.count("A")
    T = sequence.count("T")
    G = sequence.count("G")
    C = sequence.count("C")
    length = len(sequence)

    GC_content = ((G + C) / length) * 100
    AT_content = ((A + T) / length) * 100

    complement = ""

    for base in sequence:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"

    reverse = sequence[::-1]

    print("--- DNA Sequence Analyzer ---")
    print("DNA Sequence:", sequence)
    print("Length:", length)
    print("A:", A)
    print("T:", T)
    print("G:", G)
    print("C:", C)
    print("GC Content:", round(GC_content, 2), "%")
    print("AT Content:", round(AT_content, 2), "%")
    print("Complement:", complement)
    print("Reverse:", reverse)
Sequence = input("Enter DNA sequence:")
dna_analyzer(Sequence)