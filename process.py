import pickle

with open('sample2.pkl', 'rb') as f:
    car_list = pickle.load(f)

print car_list
