import argparse
from argparse import RawTextHelpFormatter

from mscheme import mscheme
from hamiltonian import hamiltonian.py

ORBITAL_DIR="space/"
BASIS_DIR="output/"
INTERACTION_DIR="hamiltonian/"

parser = argparse.ArgumentParser(description="GUMShell, an attempt at a shell model code\nAuthors: U. Gayer, G. Haefner, M. Tokieda", formatter_class=RawTextHelpFormatter)
parser.add_argument("-n", "--nparticles", help="Number of particles", type=int)
parser.add_argument("-o", "--orbitals", help="File for the single-particle orbits")
parser.add_argument("-b", "--basis", help="File for the basis of Slater determinants")
parser.add_argument("-1p", "--oneparticle", help="File for the one-particle matrix elements")
parser.add_argument("-2p", "--twoparticle", help="File for the two-particle matrix elements")
args = parser.parse_args()

if args.orbitals and not args.nparticles:
    print("Warning: main.py: File of single-particle orbitals given, but no particle number specified. Using n = 1.")
    args.nparticles = 1

if args.orbitals:
    mscheme(ORBITAL_DIR + args.orbitals, args.nparticles)



