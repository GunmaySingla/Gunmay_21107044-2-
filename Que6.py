num_1 = int(input('Enter first number [a]'))
num_2 = int(input('Enter second number [b]'))

ex_or = num_1^num_2

binary_exor = bin(ex_or)
bin_string = str(binary_exor)

flipped_bits = bin_string.count('1')

print ("Number of bits needed to be flipped to convert ‘a’ to ‘b’ are:", flipped_bits)