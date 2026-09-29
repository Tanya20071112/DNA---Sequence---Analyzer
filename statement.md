# Project Statement: DNA Sequence Analyzer

## Problem Statement

Students, researchers, and lab technicians frequently need to perform quick, routine checks on short DNA sequences: verifying that a sequence is valid, counting base composition, and calculating GC or AT content before running further analyses. Performing these checks manually is slow and error-prone, and full bioinformatics suites (such as command-line tools or packages like Biopython) are unnecessarily heavy for such small, one-off tasks.

There is no simple, dependency-free tool that anyone with a basic Python installation can run to instantly validate a DNA sequence and report its composition, GC/AT content, complement strand, and reverse sequence in a single step.

This project addresses that gap with a lightweight, interactive command-line tool that performs these fundamental sequence checks in seconds, with no installation overhead and no prior bioinformatics experience required.

## Scope of the Project

### In Scope

- Accepting a DNA sequence as interactive user input from the command line.
- Validating that the input contains only the four canonical DNA bases (A, T, G, C), with automatic case normalization (lowercase input is accepted and converted to uppercase).
- Counting the frequency of each base and reporting the total sequence length.
- Computing GC content and AT content as percentages of the total sequence length, rounded to two decimal places.
- Generating the complement strand of the input sequence (A↔T, G↔C).
- Generating the reverse of the input sequence.
- Displaying all results in a clear, formatted console report.

### Out of Scope

- Support for RNA bases (U), ambiguous/ degenerate IUPAC nucleotide codes (N, R, Y, etc.), or protein sequences.
- Reverse complement generation (the tool produces the complement and the reverse separately, not concatenated).
- Translation of DNA to protein, transcription, restriction-site analysis, or alignment.
- File-based input (FASTA, FASTQ, or plain text files); input is interactive keyboard entry only.
- Graphical user interface or web interface; the tool is command-line only.
- Batch processing of multiple sequences in one run.
- Large-scale or high-throughput sequence processing; the tool targets short, single sequences.

## Target Users

- **Students and learners** in introductory bioinformatics, molecular biology, or programming courses who need a simple tool to understand and verify basic sequence properties.
- **Educators and lab instructors** who want a quick demonstration tool for teaching DNA composition and complementarity concepts.
- **Biology and biotech researchers or lab technicians** who need fast, ad-hoc checks of short sequences (e.g., verifying a primer or oligonucleotide's GC content) without launching a full bioinformatics workflow.
- **Hobbyists and citizen scientists** exploring DNA analysis with minimal technical setup.

## High-Level Features

1. **Input validation** — Checks that the entered sequence contains only valid DNA bases (A, T, G, C) and rejects any input containing other characters with a clear error message, preventing silent garbage-in results.
2. **Base composition analysis** — Reports the total sequence length and the count of each individual base (A, T, G, C).
3. **GC and AT content calculation** — Computes and displays GC content and AT content as percentages of the total sequence length, rounded to two decimal places. These values are widely used in primer design and sequence characterization.
4. **Complement strand generation** — Produces the complementary strand of the input sequence using standard base-pairing rules (A pairs with T, G pairs with C).
5. **Reverse sequence generation** — Produces the input sequence in reverse order.
6. **Formatted console report** — Presents all results together in a labeled, readable report so users get a complete analysis in a single run.
7. **Zero-dependency operation** — Runs on any standard Python 3 installation with no package installation, making setup trivial for non-technical users.
