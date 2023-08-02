#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip



sandy = Visitor("Sandy")

park1 = NationalPark("cool park")

trip1 = Trip(sandy, park1, "today", "tommorrow")






if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    ipdb.set_trace()
