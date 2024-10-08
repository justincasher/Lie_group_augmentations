# general
import numpy as np
import matplotlib.pyplot as plt
import os
import concurrent.futures
import multiprocessing as mp
import random

# torch
import torch
import torchvision 
import torchvision.transforms as transforms

# training
from training import training
    
if __name__ == '__main__' : 
    """
    Main method. Trains networks by randomly selecting deviations
    (or whatever is desired)
    """

    device = torch.device("cuda:0" if torch.cuda.is_available() else 'cpu')
    
    for i in range(10) :
        deviation = random.uniform(0, 0.015) 
        save_name = "PGL(C, 2)_dev=" + str(round(deviation, 4)) + "_pct=20_" + str(i)

        write_path = "outputs/" + name + ".txt"
        f = open(write_path, "a")
        f.write(f"---- Running PGL(C, 2) deviation {round(deviation, 4)} on {device} ----\n")
        f.close()
        
        name = "PGL(2, C)_dev=" + str(round(deviation, 4)) + "_pct=20_" + str(i+1)
        training(deviation=deviation, complexPGL2Pct=20, realPGL2SquaredPct=0, realPGL3Pct=0, save_name=save_name, device=device)
