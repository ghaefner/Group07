import argparse
from argparse import RawTextHelpFormatter
import time

from mscheme_bits import mscheme
#from hamiltonian import hamiltonian
#from diag import diag
#from truncation import truncate
#from jcoupling import JpJm

# Define directory names for certain files
#ORBITAL_DIR="space/"
#BASIS_DIR="output/"
#INTERACTION_DIR="interaction/"

parser = argparse.ArgumentParser(description="GUMShell, an attempt at a shell model code\nAuthors: U. Gayer, G. Haefner, M. Tokieda", formatter_class=RawTextHelpFormatter)
parser.add_argument("OUTPUT_PREFIX")
parser.add_argument("-n", "--neutrons", help="Number of neutrons", type=int)
parser.add_argument("-p", "--protons", help="Number of protons", type=int)
parser.add_argument("-o", "--orbitals", help="File for the single-particle orbits")
parser.add_argument("-m", "--mscheme", help="Calculate M-scheme Slater basis", action='store_true')
parser.add_argument("-ho")
#parser.add_argument("-b", "--basis", help="File for the basis of Slater determinants")
#parser.add_argument("-t", "--truncate", help="File for the truncation method")
#parser.add_argument("-1p", "--oneparticle", help="File for the one-particle matrix elements")
#parser.add_argument("-2p", "--twoparticle", help="File for the two-particle matrix elements")
#parser.add_argument("-ho", "--hamilton", help="File for Hamiltonian matrix")
#parser.add_argument("-evec", "--eigenvectors", help="File for Eigenvectors")
args = parser.parse_args()

START = time.time()

if args.mscheme:
    if not args.orbitals:
        print("Error: main.py: Calculation of M-scheme not possible without file of single-particle orbits. Aborting.")
        exit(0)
    if not args.neutrons:
        print("Warning: main.py: Neutron number set to zero or none given. Using N = 0.")
    if not args.protons:
        print("Warning: main.py: Proton number set to zero or none given. Using Z = 0.")
    mscheme(args.orbitals, args.protons, args.neutrons, args.OUTPUT_PREFIX)

# Check several conditions
# The most important file to have are the single-particle orbitals. All calculations rely on this
#if not args.orbitals:
#    print("Warning: main.py: No file of single-particle orbitals given. Aborting.")
#    exit(0)
#
## If the number of particles is given, calculate the Slater determinant basis. If not, skip this calculation and assume
## some basis file already exists and is given to the code via the '-b' option (or use default 'basis.txt')
#
#if not args.nparticles:
#    print("Warning: main.py: No particle number specified. Skipping calculation of basis.")
#
#else:    
#    mscheme(args.orbitals, args.nparticles)
#    
#if not args.basis:
#    print("Warning: main.py: No basis file given, but one-particle and two-particle matrix elements given.")
#    print("Using standard basis file 'basis.txt'")
#    args.basis = BASIS_DIR + "basis.txt"
#    
#if args.truncate:
#    print(args.truncate)
#    truncate(args.truncate, args.basis, args.orbitals)
#    args.basis = BASIS_DIR + "basis_truncated.txt"
#
## The calculation of the Hamiltonian needs, in addition, the one- and two-particle matrix elements
#if (not args.oneparticle or not args.twoparticle):
#    print("Warning: main.py: Incomplete input for calculation of hamiltonian matrix. Aborting.")
#    exit(0)
#    
#hamiltonian(args.basis, args.oneparticle, args.twoparticle, args.orbitals)
#
#if args.hamilton:
#    diag(args.hamilton)
#
#if args.eigenvectors:
#    JpJm(args.basis, args.eigenvectors, args.orbitals)
    
STOP = time.time()

print()
print("main.py: GUMShell executed successfully, execution time: ", STOP - START, "seconds")