#class Store_the_list_index():
#    def __init__(self):
#        self.retls = []
#    def storelist(self, element):
#        self.retls.append(element)
#        print(self.retls)

# returnls = []
# def return_total_list_element(ls : list):
#     st = ""
#     for i in list(map(str, ls)):
#         st += str(i)
#         print(i)
#     return st
# def delete0(ls : list):
#     outlist = list(map(int, ls))
#     index = 0
#     for i in outlist:
#         if i == 1:
#             break
#         else:
#             outlist.pop(0)
#     # outlist.pop(0)
#     return outlist
# class Decimal_to_binary():
#     def __init__(self):
#         raise NotImplemented # stopship 2021/07/10
#
#     def dectobin(self, num, digit = 8):
#         dtb = Decimal_to_binary()
#         digit = digit - 1
#         if digit > 0:
#             dtb.dectobin(num // 2, digit)
#         returnls.append(num % 2)
#         return return_total_list_element(delete0(returnls))
#         # self.decobin_total_list.append(num % 2)
#         # return self.decobin_total_list
# # stopship 2021/07/10

class Decimal_to_binary():
    decimalls = []
    @classmethod
    def count_dectobin(cls, num, digit = 8):
        digit = digit - 1
        if digit > 0:
            Decimal_to_binary.count_dectobin(num // 2, digit)
        Decimal_to_binary.decimalls.append(num % 2)
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

    def dectobin(self, num):
        Decimal_to_binary.count_dectobin(int(num))
        return Decimal_to_binary.return_total_list_element(Decimal_to_binary.remove_first_0_element(Decimal_to_binary.decimalls))

if __name__ == '__main__':
    dtb = Decimal_to_binary()
    print(dtb.dectobin(10))
    print(dtb.dectobin(20))