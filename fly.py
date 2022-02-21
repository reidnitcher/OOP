import insect_class as I

#legs = int(i)

mosquito = I.Insect(2,4)
housefly = I.Insect(3,6)

mosquito.fight_length()
housefly.flight_length()

print("the mosquito can fly up to", mosquito.get_flight(), "miles.")

print("the housefly can fly up", housefly.get_flight(), "miles.")
     