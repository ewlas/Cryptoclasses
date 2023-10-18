class MyBigInt:
    def __init__(self):
        pass

    def setHex(self, hex_str: str): 
        self.arr = []
        for c in hex_str: 
            match c: 
                case '0': num = 0b0000
                case '1': num = 0b0001
                case '2': num = 0b0010
                case '3': num = 0b0011
                case '4': num = 0b0100
                case '5': num = 0b0101
                case '6': num = 0b0110
                case '7': num = 0b0111
                case '8': num = 0b1000
                case '9': num = 0b1001
                case 'a': num = 0b1010
                case 'b': num = 0b1011
                case 'c': num = 0b1100
                case 'd': num = 0b1101
                case 'e': num = 0b1110
                case 'f': num = 0b1111
                case _: print("lox")
            self.arr.append(num) 

    def getHex(self):
        self.hex = "" 
        for num in self.arr:
            match num:
                case 0: ch = '0'
                case 1: ch = '1'
                case 2: ch = '2'
                case 3: ch = '3'
                case 4: ch = '4'
                case 5: ch = '5'
                case 6: ch = '6'
                case 7: ch = '7'
                case 8: ch = '8'
                case 9: ch = '9'
                case 10: ch = 'a'
                case 11: ch = 'b'
                case 12: ch = 'c'
                case 13: ch = 'd'
                case 14: ch = 'e'
                case 15: ch = 'f'
                case _: print("double lox")
            self.hex += ch
        return self.hex


    def getArr(self):
        print(self.arr) 

    def inv(self):
        inverted_arr = [] 
        for num in self.arr:
            bit_s = format(num, "b").zfill(4)
            inverse_s = ''
            for i in bit_s:
                if i == '0':
                    inverse_s += '1'
                else:
                    inverse_s += '0' 
            inverted_arr.append(int(inverse_s, 2))
        inverted_hex = "" 
        for num in inverted_arr:
            match num:
                case 0: ch = '0'
                case 1: ch = '1'
                case 2: ch = '2'
                case 3: ch = '3'
                case 4: ch = '4'
                case 5: ch = '5'
                case 6: ch = '6'
                case 7: ch = '7'
                case 8: ch = '8'
                case 9: ch = '9'
                case 10: ch = 'a'
                case 11: ch = 'b'
                case 12: ch = 'c'
                case 13: ch = 'd'
                case 14: ch = 'e'
                case 15: ch = 'f'
                case _: print("double lox")
            inverted_hex += ch
        return inverted_hex



hex_str = "51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4"
numberA = MyBigInt()
numberA.setHex(hex_str)
hex_res = numberA.getHex()
print(hex_str == hex_res)
test_str = "AE409F7BEB52A8D95C3E413F670884E4AB004D878072AD758B3E280219B8F15B".lower()
print(numberA.inv() == test_str)
