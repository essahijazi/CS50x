import csv
import sys


def main():
    # Initialize database and results
    database = []
    results = {}

    # Check for correct command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py DATABASE SEQUENCE")
        return

    # Read database file into a list
    database_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    with open(database_filename) as db_file:
        reader = csv.reader(db_file)
        for row in reader:
            database.append(row)

    # Read DNA sequence file into a string
    with open(sequence_filename) as seq_file:
        sequence = seq_file.read().strip()

    # Find the longest match of each STR in the DNA sequence
    # Extract STRs from the first row of the database (excluding 'name')
    headers = database[0]
    for i in range(1, len(headers)):
        str_name = headers[i]
        results[str_name] = longest_str_run(sequence, str_name)

    # Extract the lengths of STR runs into a list
    sequence_dna = list(results.values())

    # Check database for matching profiles
    for person in database[1:]:
        person_name = person[0]
        person_str_counts = [int(count) for count in person[1:]]

        # Compare STR counts of current person with the sequence's STR counts
        if person_str_counts == sequence_dna:
            print(person_name)
            return

    # If no match found
    print("No match")


def longest_str_run(sequence, subsequence):
    """Returns length of the longest run of 'subsequence' in 'sequence'."""

    sub_len = len(subsequence)
    seq_len = len(sequence)
    longest_run = 0

    # Iterate through the sequence to find the longest run of 'subsequence'
    for i in range(seq_len):
        count = 0
        while True:
            start = i + count * sub_len
            end = start + sub_len
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
