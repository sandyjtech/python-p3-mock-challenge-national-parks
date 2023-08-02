#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip



sandy = Visitor("Sandy")
alex = Visitor("Alex")

park1 = NationalPark("cool park")
park2 = NationalPark("cool park 2")

trip1 = Trip(sandy, park1, "today", "tommorrow")

trip2 = Trip(alex, park1, "today", "tommorrow")
trip3 = Trip(alex, park1, "today", "tommorrow")

trip4 = Trip(alex, park2, "today", "tommorrow")
trip5 = Trip(alex, park2, "today", "tommorrow")
trip6 = Trip(alex, park2, "today", "tommorrow")
trip7 = Trip(alex, park2, "today", "tommorrow")

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    ipdb.set_trace()
