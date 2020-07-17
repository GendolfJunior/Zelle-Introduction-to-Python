#  3. Write a program that computes the molecular weight of a carbohydrate (in grams per mole) based on the number of hydrogen, carbon, and
#     oxygen atoms in the molecule. The program should prompt the user to enter the number of hydrogen atomes, the number of carbon atoms,
#     and the number of oxygen atoms. The program then prints the total combined molecular weight of all the atoms based on these individual
#     atom weights:
#                  Atom      Weight
#                            (grams/mole)
#                  ______________________
#                  H         1.00894
#                  C         12.0107
#                  O         15.9994
#     For example, the molecular weight of water (H20) is 2(1.00794) + 15.9994 = 18.01528.

# prompt a user to input hydrogen atoms
# prompt a user to input carbon atoms
# prompt a user to input oxygen atoms
# calculate with formula weight of inputed data
# print out the results

def main():
    hydrogen = int(input("Enter quantity of hydrogen atoms: "))
    carbon = int(input("Enter quantity of carbon atoms: "))
    oxygen = int(input("Enter quantity of carbon atoms: "))
    weight = 1.00794 * hydrogen + 12.0107 * carbon + 15.9994 * oxygen
    print("The total weight is: ", weight)


main()
