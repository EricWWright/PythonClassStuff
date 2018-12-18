# Pickle It
# Demonstrates pickling and shelving data

import pickle
import shelve

# print("Pickling lists.")
# variety = ["dill", "sweet", "hot"]
# shape = ["whole", "spear", "chip"]
# brand = ["Vlassic", "Kosher", "Heinz", "Claussen"]
# f = open("pickles1.dat","wb") #wb = write in binary .dat = data file
# pickle.dump(variety, f)
# pickle.dump(shape, f)
# pickle.dump(brand, f)
# f.close()

# print("\nUnpickling lists.")
# f = open("pickles1.dat", "rb") #rb = read binary
# variety = pickle.load(f)
# shape = pickle.load(f)
# brand = pickle.load(f)
# print(variety)
# print(shape)
# print(brand)
# f.close()

print("\nShelving lists.")
s = shelve.open("pickles2.dat")
s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]
s.sync()

print("\nRetrieving lists from a shelved file:")
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])
s.close()