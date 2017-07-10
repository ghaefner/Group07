nucpe /home/ghaefner/Dokumente/nushellx/sps/usdb.int       usdb.int     
         
nudel o_170010.trl
nudel o_170010.lnz
nudel o_170010.tmp
nudel o_170010.lev
nudel o_170110.trl
nudel o_170110.lnz
nudel o_170110.tmp
nudel o_170110.lev
nudel o_170210.trl
nudel o_170210.lnz
nudel o_170210.tmp
nudel o_170210.lev
nudel o_170310.trl
nudel o_170310.lnz
nudel o_170310.tmp
nudel o_170310.lev
nudel o_170410.trl
nudel o_170410.lnz
nudel o_170410.tmp
nudel o_170410.lev
nudel o_170510.trl
nudel o_170510.lnz
nudel o_170510.tmp
nudel o_170510.lev
         
nuaddint o_170bb.addint o_170.int o_170.ant
nucp  o_170.ppar p.par
nucp  o_170.npar n.par
nudel o_170sl.inf
NuShellX < o_170.modelx > o_170mod.out
NuShellX < o_170.levelx > o_170lev.out
nucp nul > opd.dat
source shellx.bat > o_170.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  bb0101.lph o_170010.eng o_170.modelx o_170.levelx bb0101.lpe > nucp.txt
nuren o_170010.lp bb0101.lp
nuren o_170010.ls bb0101.ls
nuren o_170010.nhw bb0101.nhw
nucp  bb0103.lph o_170110.eng o_170.modelx o_170.levelx bb0103.lpe > nucp.txt
nuren o_170110.lp bb0103.lp
nuren o_170110.ls bb0103.ls
nuren o_170110.nhw bb0103.nhw
nucp  bb0105.lph o_170210.eng o_170.modelx o_170.levelx bb0105.lpe > nucp.txt
nuren o_170210.lp bb0105.lp
nuren o_170210.ls bb0105.ls
nuren o_170210.nhw bb0105.nhw
nucp  bb0107.lph o_170310.eng o_170.modelx o_170.levelx bb0107.lpe > nucp.txt
nuren o_170310.lp bb0107.lp
nuren o_170310.ls bb0107.ls
nuren o_170310.nhw bb0107.nhw
nucp  bb0109.lph o_170410.eng o_170.modelx o_170.levelx bb0109.lpe > nucp.txt
nuren o_170410.lp bb0109.lp
nuren o_170410.ls bb0109.ls
nuren o_170410.nhw bb0109.nhw
nucp  bb010b.lph o_170510.eng o_170.modelx o_170.levelx bb010b.lpe > nucp.txt
nuren o_170510.lp bb010b.lp
nuren o_170510.ls bb010b.ls
nuren o_170510.nhw bb010b.nhw
nulev o_17b     
levp o_17b     
