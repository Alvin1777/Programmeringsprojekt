import pickle
from classes import *
from functions import *
from main import *



data_to_save = []




print(data_to_save)

filename = 'SaveFile'
outfile = open(filename,'wb')

pickle.dump(data_to_save,outfile)
outfile.close()

infile = open(filename,'rb')
saved_stats = pickle.load(infile)
infile.close()

print(saved_stats)
