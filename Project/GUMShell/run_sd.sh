#!/bin/bash
#python main.py -o "space/sd.sp" -n 2 -1p "interaction/sd_sp.int" -2p "interaction/usdb_m.int" -ho "hamiltonian/Hamiltonian.txt"
python3 main.py -o "space/sd.sp" -n 6 -1p "interaction/sd_sp.int" -2p "interaction/usdb_m.int" -ho "hamiltonian/Hamiltonian.txt" #-t "truncation/truncation.txt"
#python3 -m cProfile -o cProfile.out main.py -o "space/sd.sp" -n 2 -1p "interaction/sd_sp.int" -2p "interaction/usdb_m.int" -ho "hamiltonian/Hamiltonian.txt" #-t "truncation/truncation.txt"
#python3 main.py -o "space/sd.sp" -n 2 -1p "interaction/sd_sp.int" -2p "interaction/usdb_m.int" -ho "hamiltonian/Hamiltonian.txt"
