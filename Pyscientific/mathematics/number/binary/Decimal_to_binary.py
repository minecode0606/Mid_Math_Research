class Decimal_to_binary:
    """
    This class was created to convert decimal to binary.
    """
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
        """
        This function prints all the elements in a list.
        :param ls:
        :return st :
        """
        st = ""
        for i in list(map(str, ls)):
            st += str(i)
        return st

    @classmethod
    def remove_first_0_element(cls, ls: list):
        """
        This function removes 0's from the list until 1 is found.
        :param ls:
        :return:
        """
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
        """
        This method converts a decimal number to a binary number.
        :param num:
        :return:
        """
        Decimal_to_binary.decimalls = []
        Decimal_to_binary.count_dectobin(int(num)) # convert decimal to binary
        # this method has ploblem.. later, I'll fix it

        # return Decimal_to_binary.return_total_list_element( # Print all elements in a list
        #     Decimal_to_binary.remove_first_0_element( # Remove 0 before 1 in list
        #         Decimal_to_binary.decimalls # List of decimal to binary numbers
        #     )
        # ) # stopship 2021/07/11

        return NotImplemented

if __name__ == '__main__':
    dtb = Decimal_to_binary()
    print(dtb.dectobin(10))
    print(dtb.dectobin(20))
