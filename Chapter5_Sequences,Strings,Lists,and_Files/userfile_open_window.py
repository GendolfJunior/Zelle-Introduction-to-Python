# userfile2.py
# Program to create a file of usernames in batch mode.
# it is modified to include open Windows window to specifiy the location of the file to read from
# and windows to specify the location of the file to write into

from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    print(" This program creates a file of usernames from a \nfile of names.")

    # get the file names
    infilename = askopenfilename()
    outfileName = asksaveasfilename()

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
