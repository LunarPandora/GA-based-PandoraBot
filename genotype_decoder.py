class GenotypeDecoder:
    
    def decode(self, genotype: str):
        # bin_conv = []

        # for c in genotype:
        # ascii_val = ord(genotype)
        # binary_val = bin(ascii_val)

            # bin_conv.append(binary_val[2:])
        
        binary_int = int(genotype, 2);
        byte_number = binary_int.bit_length() + 7 // 8
        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode()
        
        return ascii_text

