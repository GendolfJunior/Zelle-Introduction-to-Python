# userfile.py
# Program to create a file of usernames in batch mode.

def main():
    print(" This program creates a f ile of usernames from a \nfile of names.")

    # get the file names
    infilename = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # open the files
    infile = open(infilename, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create the username
        uname = (first[0] + last[:7]).lower()
        # write it to the output file
        print(uname, file=outfile)
    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to ", outfileName)


main()
