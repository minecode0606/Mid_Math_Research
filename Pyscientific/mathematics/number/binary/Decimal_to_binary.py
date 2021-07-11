class Decimal_to_binary:
    @classmethod
    def count_dectobin(cls, num, digit=8):
        """
        This function converts the given decimal number
        to binary and stores it as a list in the decimalls
        variable.
        :param num:
        :param digit:
        :return type : none:
        """
        digit = digit - 1
        if digit > 0:
            Decimal_to_binary.count_dectobin(num // 2, digit)
        try:
            Decimal_to_binary.decimalls.append(num % 2)
        except AttributeError:
            raise TypeError("not before use the dectobin() staticmethod")

    @classmethod
    def return_total_list_element(cls, ls: list):
        st = ""
        for i in list(map(str, ls)):
            st += str(i)
        return st

    @classmethod
    def remove_first_0_element(cls, ls: list):
        outlist = list(map(int, ls))
        returnls = outlist
        index = 0
        for i in outlist:
            if i == 0:
                index += 1
            elif i == 1:
                break
        return returnls[index:len(returnls)]


    @staticmethod
    def dectobin(num):
        Decimal_to_binary.decimalls = []
        Decimal_to_binary.count_dectobin(int(num))
        return Decimal_to_binary.return_total_list_element(Decimal_to_binary.remove_first_0_element(Decimal_to_binary.decimalls))

if __name__ == '__main__':
    dtb = Decimal_to_binary()
    print(dtb.dectobin(10))
    print(dtb.dectobin(20))
