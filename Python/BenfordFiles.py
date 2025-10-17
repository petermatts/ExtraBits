import argparse
from pathlib import Path
from collections import Counter
import math
import matplotlib.pyplot as plt
import glob

def get_leading_digit(n: int):
    while n >= 10:
        n //= 10
    return int(n)

def benfords_law_distribution():
    return {d: math.log10(1 + 1/d) for d in range(1, 10)}

def collect_file_sizes(directory: Path):
    # todo
    return []

def compute_leading_digit_distribution(sizes):
    leading_digits = [get_leading_digit(size) for size in sizes]
    total = len(leading_digits)
    counts = Counter(leading_digits)
    distribution = {d: counts[d] / total for d in range(1, 10)}
    return distribution

def plot_distribution(observed, expected):
    digits = range(1, 10)
    observed_values = [observed.get(d, 0) for d in digits]
    expected_values = [expected.get(d, 0) for d in digits]

    x = range(1, 10)
    plt.figure(figsize=(10, 6))
    plt.bar(x, observed_values, width=0.4, label='Observed', align='center')
    plt.plot(x, expected_values, color='red', marker='o', label="Benford's Law")

    plt.xticks(x)
    plt.xlabel('Leading Digit')
    plt.ylabel('Frequency')
    plt.title("File Size Leading Digit Distribution vs Benford's Law")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Analyze file sizes in a directory and compare leading digit distribution to Benford's Law.")
    parser.add_argument('directory', nargs='?', default='/', type=str, help='Directory to scan')
    args = parser.parse_args()

    directory = Path(args.directory).resolve()
    if not directory.exists() or not directory.is_dir():
        print(f"Error: '{directory}' is not a valid directory.")
        return

    print(f"Scanning files in: {directory}")
    sizes = collect_file_sizes(directory)

    if not sizes:
        print("No files found or accessible in the specified directory.")
        return

    observed_dist = compute_leading_digit_distribution(sizes)
    expected_dist = benfords_law_distribution()

    plot_distribution(observed_dist, expected_dist)

if __name__ == "__main__":
    main()
