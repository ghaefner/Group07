# Fast calculation for 17O
python gum.py 17o_fast -m -o sd_n.txt -p 0 -n 1 -hot -1b sd_sp_np.int -2b usdb_m.int -f -d -j
# Complete calculation for 17O
python gum.py 17o -m -o sd_np.txt -p 0 -n 1 -ho -1b sd_sp_np.int -2b usdb_m.int -d
# Fast calculation for 18O
python gum.py 18o_fast -m -o sd_n.txt -p 0 -n 2 -hot -1b sd_sp_np.int -2b usdb_m.int -f -d -j
# Complete calculation for 18O
python gum.py 18o -m -o sd_np.txt -p 0 -n 2 -ho -1b sd_sp_np.int -2b usdb_m.int -d
# Fast calculation for 19O
python gum.py 19o_fast -m -o sd_n.txt -p 0 -n 3 -hot -1b sd_sp_np.int -2b usdb_m.int -f -d -j
# Complete calculation for 19O
python gum.py 19o -m -o sd_np.txt -p 0 -n 3 -ho -1b sd_sp_np.int -2b usdb_m.int -d
