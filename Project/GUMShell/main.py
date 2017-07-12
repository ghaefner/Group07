import argparse
from argparse import RawTextHelpFormatter

from mscheme import mscheme
from hamiltonian import hamiltonian
from diag import diag

# Define directory names for certain files
#ORBITAL_DIR="space/"
BASIS_DIR="output/"
#INTERACTION_DIR="interaction/"

parser = argparse.ArgumentParser(description="GUMShell, an attempt at a shell model code\nAuthors: U. Gayer, G. Haefner, M. Tokieda", formatter_class=RawTextHelpFormatter)
parser.add_argument("-n", "--nparticles", help="Number of particles", type=int)
parser.add_argument("-o", "--orbitals", help="File for the single-particle orbits")
parser.add_argument("-b", "--basis", help="File for the basis of Slater determinants")
parser.add_argument("-1p", "--oneparticle", help="File for the one-particle matrix elements")
parser.add_argument("-2p", "--twoparticle", help="File for the two-particle matrix elements")
parser.add_argument("-ho", "--hamiltonian", help="File for Hamiltonian matrix")
args = parser.parse_args()

# Check several conditions
# The most important file to have are the single-particle orbitals. All calculations rely on this
if not args.orbitals:
    print("Warning: main.py: No file of single-particle orbitals given. Aborting.")
    exit(0)

# If the number of particles is given, calculate the Slater determinant basis. If not, skip this calculation and assume
# some basis file already exists and is given to the code via the '-b' option (or use default 'basis.txt')

if not args.nparticles:
    print("Warning: main.py: No particle number specified. Skipping calculation of basis.")

else:    
    mscheme(args.orbitals, args.nparticles)

# The calculation of the Hamiltonian needs, in addition, the one- and two-particle matrix elements
if (not args.oneparticle or not args.twoparticle):
    print("Warning: main.py: Incomplete input for calculation of hamiltonian matrix. Aborting.")
    exit(0)

if not args.basis:
    print("Warning: main.py: No basis file given, but one-particle and two-particle matrix elements given.")
    print("Using standard basis file 'basis.txt'")
    args.basis = BASIS_DIR + "basis.txt"
    
hamiltonian(args.basis, args.oneparticle, args.twoparticle, args.orbitals)

