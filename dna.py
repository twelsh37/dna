# Description: a program to work out who is identified by a DNA sequence
#
# Specification
# In a file called dna.py in ~/pset6/dna/, implement a program that identifies to whom a sequence of DNA belongs.
#
# 1.  The program should require as its first command-line argument the name of a CSV file containing the STR counts for
# a # list of individuals and should require as its second command-line argument the name of a text file containing the
# DNA sequence to identify.
#
# 1.1    If your program is executed with the incorrect number of command-line arguments, your program should print
#     an error message of your choice (with print).# If the correct number of arguments are provided, you may
#     assume that the first argument is indeed the filename of a # valid CSV file, and that the second argument is the
#     filename of a valid text file.
#
# 2. Your program should open the CSV file and read its contents into memory.
#
# 2.2    You may assume that the first row of the CSV file will be the column names.# The first column will be the word
#     'name' and the remaining columns will be the STR sequences themselves.

# 3. Your program should open the DNA sequence and read its contents into memory.
#
# 4. For each of the STRs (from the first line of the CSV file), your program should compute the longest run of
# consecutive repeats of the STR in the DNA sequence to identify.
#
# 5. If the STR counts match exactly with any of the individuals in the CSV file, your program should print out the name
# of the matching individual.
#
# 5.5    You may assume that the STR counts will not match more than one individual.
#     If the STR counts do not match exactly with any of the individuals in the CSV file, your program should print
#     "No match".

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
