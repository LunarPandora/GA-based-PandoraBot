class GenotypeDecoder:
    
    def decode(self, genotype: str):
        bin_conv = []

        for c in genotype:
            ascii_val = ord(c)
            binary_val = bin(ascii_val)

            bin_conv.append(binary_val[2:])

        return bin_conv


# a = GenotypeDecoder()
# print(a.decode('Hello world'))
