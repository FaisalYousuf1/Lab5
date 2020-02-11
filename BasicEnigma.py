#BasicEnigma.py
#Name:
#Date:
#Assignment:

#This is a simplified version of the German Enigma used during WWII.

def main():
    alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    reflectorA = "EJMZALYXVBWFCRQUONTSPIKHGD"

    # get a message from the user


    letter = 'A'
    pos = alpha.find(letter)    # Find location of letter in alphabet
    letter = rotor1[pos]        # Find letter in rotor1

    ### Reflector
    pos = alpha.find(letter)
    letter = reflectorA[pos]

    ### Now go back through in the reverse order

    pos = rotor1.find(letter)
    letter = alpha[pos]

    # Now that we have been through one pass, adjust any of the rotors that need to be rotated.

    print(letter) #This one letter has been encoded


main()
