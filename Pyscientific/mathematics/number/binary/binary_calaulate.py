# -*- coding: utf-8 -*-
# MIT License
# Copyright (c) 2021 MinseoKang


from Decimal_to_binary import Decimal_to_binary # Load a class that converts decimal numbers to binary numbers.

class Binary(Decimal_to_binary):
    __version__ = "0.1Alpha"


if __name__ == '__main__':
    bin = Binary()
    print(bin.__version__)