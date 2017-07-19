import argparse
from argparse import RawTextHelpFormatter
import time

from mscheme_bits import mscheme
from hamiltonian import hamiltonian
from truncation import truncate
from truncation import mzero
from diag import diag
from jcoupling import JpJm

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
parser.add_argument("-ho", "--hamiltonian", help="Set up the hamiltonian matrix", action='store_true')
parser.add_argument("-hot", "--hamiltonian_truncated", help="Set up the hamiltonian matrix in the truncated basis", action='store_true')
parser.add_argument("-t", "--truncate", help="File for the truncation method")
parser.add_argument("-1b", "--onebody", help="File for the one-body matrix elements")
parser.add_argument("-2b", "--twobody", help="File for the two-body matrix elements")
parser.add_argument("-d", "--diag", help="Diagonalize Hamiltonian", action="store_true")
parser.add_argument("-f", "--fast", help="Calculate only M = 0 states", action="store_true")
parser.add_argument("-j", "--jvalues", help="Determine value of J for eigenvectors", action="store_true")
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
    mscheme(args.orbitals, args.neutrons, args.protons, args.OUTPUT_PREFIX)

if args.truncate:
    if not args.orbitals:
        print("Error: main.py: Basis truncation not possible without file of single-particle orbits. Aborting.")
        exit(0)
    truncate(args.truncate, args.OUTPUT_PREFIX + "_basis.txt", args.orbitals, args.OUTPUT_PREFIX)

if args.fast:
    if not args.orbitals:
        print("Error: main.py: Basis truncation not possible without file of single-particle orbits. Aborting.")
        exit(0)
    if not args.hamiltonian_truncated:
        print("Error: main.py: The fast option has to be used with a truncated hamiltonian, i.e. run with the '-hot' option. Aborting.")
        exit(0)
    if args.neutrons % 2 == 0 and args.protons % 2 == 0:
        mzero(args.OUTPUT_PREFIX + "_basis.txt", args.OUTPUT_PREFIX, True)        
    elif args.neutrons % 2 == 1 and args.protons % 2 == 1:
        mzero(args.OUTPUT_PREFIX + "_basis.txt", args.OUTPUT_PREFIX, True)        
    else:
        mzero(args.OUTPUT_PREFIX + "_basis.txt", args.OUTPUT_PREFIX, False)        
        
if args.hamiltonian:
    if not args.onebody:
        print("Error: main.py: Calculation of Hamiltonian matrix not possible without file of one-body interactions. Aborting.")
        exit(0)
    if not args.twobody:
        print("Error: main.py: Calculation of Hamiltonian matrix not possible without file of two-body interaction. Aborting.")
        exit(0)
    hamiltonian(args.OUTPUT_PREFIX + "_basis.txt", args.onebody, args.twobody, args.OUTPUT_PREFIX)

if args.hamiltonian_truncated:
    if not args.onebody:
        print("Error: main.py: Calculation of Hamiltonian matrix not possible without file of one-body interactions. Aborting.")
        exit(0)
    if not args.twobody:
        print("Error: main.py: Calculation of Hamiltonian matrix not possible without file of two-body interaction. Aborting.")
        exit(0)
    hamiltonian(args.OUTPUT_PREFIX + "_basis_truncated.txt", args.onebody, args.twobody, args.OUTPUT_PREFIX)

if args.diag:
    diag(args.OUTPUT_PREFIX + "_hamiltonian.txt", args.OUTPUT_PREFIX)
    
if args.jvalues:
    if not args.orbitals:
        print("Error: main.py: Calculation of J not possible without file of single-particle orbits. Aborting.")
        exit(0)   
    JpJm(args.OUTPUT_PREFIX + "_basis_truncated.txt", args.OUTPUT_PREFIX + "_eigenvectors.txt", args.orbitals, args.OUTPUT_PREFIX) 
    
STOP = time.time()

print()
print("main.py: GUMShell executed successfully, execution time: ", STOP - START, "seconds")