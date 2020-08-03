# Description: A program to work out who is identified by a DNA sequence
#
# DECONSTRUCTION:
# Read in DB
# Read in seq file
# using the nucleotide sets we have in the DB header check the seq file for occurrences and add to count for
# that nucleotide
#
# When we have completed the sequence pass our numbers through the match function to see if we have a numbers match
#   if we have a match then print the name of teh match
#   if we have no match then print "No Match"
#   Continue this loop until we have looped over all nucleotide
#

# NOTES:
#  Identifiers for bob and alice in small.csv
# Bob - 1.txt - 4,1,5 - small.csv
# Alice - 4.txt - 2,8,3 - small.csv

import csv
import sys


def main():

    # Check we get enough arguments otherwise print a usage message
    if len(sys.argv) != 3:
        print("Usage: python dna.py database/<filename.csv> sequences/<filename.txt>")
        sys.exit()

    # assign names to command line arguments for readability
    db = sys.argv[1]
    sequence = sys.argv[2]

    # Open the sequence file and read it in
    with open(sequence) as f:
        seq = f.read()

    # open the csv file and read it in
    csv_file = db
    with open(csv_file) as c:
        reader = csv.reader(c)

        # get the headers from the csv entered on the command line
        nu = next(reader)

        # remove the first entry 'name' as its not part of the sequence
        # we are looking for
        nu.pop(0)

        # iterate through the sequence file and count up our occurrences of the headers
        # from nu and append them to searchstr
        searchstr = []
        for i in nu:
            searchstr.append(max([q for q in range(len(seq)) if seq.find(i * q) != -1]))

        # Returns a list of the dna_fingerprint nucleotides
        # for someone e.g Bob = 4,1,5
        dna_fingerprint = searchstr

        # Using the match unction, compare values from CSV reader and the dna_fingerprint
        match(reader, dna_fingerprint)

# Compare values from reader and dna_fingerprint # return a name of entry if the bool is True otherwise print 'No Match'


def match(reader, dna_fingerprint):
    for line in reader:
        # Get name of the dna owner for the sequence
        name = line[0]

        # Get the DNA sequence
        values = [int(val) for val in line[1:]]

        # Iterate through the dna sequences from the csv file
        # until we find a match.
        if values == dna_fingerprint:
            print(name)
            return
    # If we dong get a match print "No match"
    print("No match")


if __name__ == '__main__':
    main()
