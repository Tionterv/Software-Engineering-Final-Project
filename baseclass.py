import pandas as pd
import math

filepath = 'data.csv'
# from collections import

class Location:
    def __init__(self, idx, aisle, bay, capacity):
        self.idx = idx  # index
        self.aisle = aisle
        self.bay = bay
        self.capacity = capacity
        self.available = capacity
        self.categories = 0
        self.item = []  # to store all

    def add_item(self, ident, quant):
        if quant > self.available:  # cannot add
            return False
        else:
            mark = self.search_item(ident)
            self.available -= quant
            if mark == -1:  # no pre-exist item found
                self.item.append(ident, quant)
                self.categories += 1
            else:
                self.item[mark][1] += quant
            return True

    def remove_item(self, ident, quant):
        mark = self.search_item(ident)
        if mark == -1:
            return False
        else:
            if quant > self.item[mark][1]:
                return False
            else:
                self.item[mark][1] -= quant
                self.available += quant
                return True

    def search_item(self, ident):
        for i in range(self.categories):
            if self.item[i][0] == ident:
                return i
        return -1
