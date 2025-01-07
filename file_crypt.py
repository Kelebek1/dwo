from Crypto.Cipher import AES
import struct

xor_last_bytes = [
    0x30, 0xF9, 0x85, 0xBE, 0x44, 0x25, 0xA4, 0xD0, 0xA5, 0x21, 0x31, 0x86, 0x62, 0x52, 0xE7, 0x4D, 
    0xDD, 0x10, 0x33, 0xF5, 0xB5, 0x00, 0x21, 0x41, 0xF5, 0x54, 0xAF, 0xA6, 0x15, 0x3B, 0x99, 0xCF, 
    0x5D, 0x86, 0xD2, 0x36, 0xCE, 0x6D, 0x28, 0xC0, 0x53, 0x73, 0xE7, 0xD1, 0x3C, 0x00, 0x80, 0x50, 
    0x9D, 0xB0, 0x4A, 0xCB, 0x10, 0x32, 0x7C, 0x08, 0x54, 0xBB, 0xF5, 0xD9, 0xD3, 0x9E, 0x5B, 0x65, 
    0xA6, 0x4E, 0xD8, 0x66, 0x2B, 0x31, 0xF7, 0xB1, 0xCD, 0xEB, 0x05, 0x1F, 0x8C, 0x26, 0x40, 0x27, 
    0x80, 0xC2, 0xE3, 0x20, 0x9E, 0x3A, 0xA5, 0xC4, 0x91, 0xB5, 0xCE, 0xB5, 0x8C, 0x08, 0x90, 0x94, 
    0x48, 0xCA, 0x20, 0x1F, 0x9B, 0xE5, 0xE6, 0xCE, 0x6D, 0x30, 0xDA, 0xB7, 0x1D, 0x84, 0x58, 0xDA, 
    0xBA, 0x2C, 0x3E, 0xF6, 0xFB, 0x4E, 0x3E, 0xB4, 0x27, 0x5F, 0xD0, 0x53, 0x0E, 0x1B, 0x96, 0xB1, 
    0x59, 0x68, 0xD0, 0xC8, 0x52, 0x0F, 0xBF, 0x39, 0x10, 0xE1, 0x69, 0x03, 0x56, 0xFF, 0xDD, 0x27, 
    0x0E, 0x11, 0x11, 0xAB, 0xC1, 0x2E, 0x00, 0xED, 0xCE, 0x05, 0x8F, 0x7C, 0x8E, 0xCD, 0x3B, 0x0B, 
    0x47, 0x1D, 0x75, 0x76, 0x55, 0x2C, 0x65, 0x3C, 0x0D, 0x6C, 0x45, 0xF6, 0x5E, 0x79, 0x49, 0xE0, 
    0xEE, 0x27, 0xDF, 0x4B, 0x89, 0x66, 0xD7, 0x21, 0xB1, 0x66, 0xAF, 0x92, 0x06, 0xF9, 0xE3, 0x0E, 
    0x5B, 0xC1, 0x12, 0xDE, 0xEF, 0xEB, 0x10, 0x9E, 0xB9, 0xA2, 0x30, 0xD7, 0xE1, 0xE7, 0xF5, 0x49, 
    0xC0, 0x4F, 0xC7, 0x72, 0x58, 0x28, 0x3D, 0xF3, 0x3C, 0x63, 0x1C, 0x72, 0xFF, 0xE9, 0x24, 0x27, 
    0x1E, 0x29, 0xE2, 0x10, 0xD4, 0xBD, 0xB0, 0xBF, 0x2B, 0xB4, 0x5E, 0xF1, 0x39, 0xF8, 0x04, 0x9B, 
    0xAE, 0x52, 0xB1, 0x77, 0x0A, 0xEC, 0x0C, 0x37, 0x66, 0xF4, 0x84, 0x73, 0xE9, 0xAA, 0x61, 0x4B, 
    0x33, 0xE0, 0x3F, 0xC4, 0x46, 0x7E, 0x23, 0x75, 0x08, 0xBF, 0xB1, 0x19, 0x88, 0x30, 0xB1, 0x20, 
    0x65, 0xC3, 0xD2, 0xCD, 0xF0, 0x97, 0x3E, 0x26, 0x8E, 0xDC, 0x65, 0x9A, 0x1C, 0xA9, 0x2B, 0xD3, 
    0x79, 0x69, 0xAC, 0xA8, 0x38, 0x6C, 0xF9, 0x5B, 0x48, 0x97, 0xFE, 0x71, 0x95, 0xF0, 0xD5, 0x81,
]

def crypt(data, type):
    if len(data) < 0x10:
        return data

    key = b"1SOiLZyKB9BOW6Ivj5UAne0r6bVVCILb"
    iv = b"\xE1\xC1\xC4\x9F\x9A\x30\x19\x34\x1E\xA8\x20\xF9\x9F\xD0\x9A\x83"
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    rem = len(data) % 0x10
    aes_data = data[:len(data) - rem]

    if type == "dec":
        last_encrypted_block = aes_data[-0x10:]
        out_data = cipher.decrypt(aes_data)
    elif type == "enc":
        out_data = cipher.encrypt(aes_data)
        last_encrypted_block = out_data[-0x10:]
    else:
        print(f"Invalid de/crypt type {type}")
        exit()

    if rem:
        last_data = data[len(data) - rem:]
        last_encrypted_byte = last_encrypted_block[0]

        out_last_bytes = bytes()

        for i in range(rem):
            rdx = (last_encrypted_byte * 0xAF286BCB) >> 32
            #print(f"1 rdx 0x{rdx:X}")
            eax = (last_encrypted_byte - rdx) >> 1
            #print(f"2 eax 0x{eax:X}")
            eax += rdx
            #print(f"3 eax 0x{eax:X}")
            eax >>= 0x4
            #print(f"4 eax 0x{eax:X}")
            eax *= 0x13
            #print(f"5 eax 0x{eax:X}")

            ecx = last_encrypted_byte - eax
            #print(f"6 ecx 0x{ecx:X}")
            ecx <<= 0x4
            #print(f"7 ecx 0x{ecx:X}")

            byte = last_data[i]

            if type == "dec":
                #print(f"byte 0x{byte:X} last_encrypted_byte 0x{last_encrypted_byte:X}")

                new_byte = xor_last_bytes[ecx + i] ^ byte
                #print(f"new_byte = 0x{xor_last_bytes[ecx + i]:X} ^ 0x{byte:X} = 0x{new_byte:X}")
                new_byte ^= last_encrypted_block[i]
                #print(f"new_byte ^= 0x{last_encrypted_block[i]:X} = 0x{new_byte:X}")

                last_encrypted_byte = byte

            elif type == "enc":
                #print(f"0x{byte:X}")

                new_byte = last_encrypted_block[i]
                #print(f"new_byte = 0x{last_encrypted_block[i]:X}")

                new_byte ^= xor_last_bytes[ecx + i] ^ byte
                #print(f"new_byte = 0x{xor_last_bytes[ecx + i]:X} ^ 0x{byte:X} = 0x{new_byte:X}")

                last_encrypted_byte = new_byte

            out_last_bytes += struct.pack("<B", new_byte)


        out_data += out_last_bytes

    return out_data
