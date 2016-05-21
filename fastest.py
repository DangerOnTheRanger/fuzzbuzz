top = 100
six = "Buzz\nFuzz\nFuzzBuzz\nFuzz\nBuzz\nFuzzBuzz\n"
list = ["Buzz", "Fuzz", "FuzzBuzz", "Fuzz", "Buzz", "FuzzBuzz"]

sixes = (top-1)/6
remainder = top-(sixes*6)
print six*sixes, ("\n".join(list[:remainder]))
