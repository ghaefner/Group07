nucpe /home/ghaefner/Dokumente/nushellx/sps/sd.sp          sd.sp        
nucpe /home/ghaefner/Dokumente/nushellx/sps/usdb.int       usdb.int     
         
nudel na230043.trl
nudel na230043.lnz
nudel na230043.tmp
nudel na230043.lev
nudel na230143.trl
nudel na230143.lnz
nudel na230143.tmp
nudel na230143.lev
nudel na230243.trl
nudel na230243.lnz
nudel na230243.tmp
nudel na230243.lev
nudel na230343.trl
nudel na230343.lnz
nudel na230343.tmp
nudel na230343.lev
nudel na230443.trl
nudel na230443.lnz
nudel na230443.tmp
nudel na230443.lev
nudel na230543.trl
nudel na230543.lnz
nudel na230543.tmp
nudel na230543.lev
         
nuaddint na230bb.addint na230.int na230.ant
nucp  na230.ppar p.par
nucp  na230.npar n.par

nudel na230sl.inf
NuShellX < na230.modelx > na230mod.out
NuShellX < na230.levelx > na230lev.out
source shellx.bat > na230.cpu
nuren shellx.bat shellx1.bat
nucp  bb3701.lph na230043.eng na230.modelx na230.levelx bb3701.lpe > nucp.txt
nuren na230043.lp bb3701.lp
nuren na230043.ls bb3701.ls
nuren na230043.nhw bb3701.nhw
nucp  bb3703.lph na230143.eng na230.modelx na230.levelx bb3703.lpe > nucp.txt
nuren na230143.lp bb3703.lp
nuren na230143.ls bb3703.ls
nuren na230143.nhw bb3703.nhw
nucp  bb3705.lph na230243.eng na230.modelx na230.levelx bb3705.lpe > nucp.txt
nuren na230243.lp bb3705.lp
nuren na230243.ls bb3705.ls
nuren na230243.nhw bb3705.nhw
nucp  bb3707.lph na230343.eng na230.modelx na230.levelx bb3707.lpe > nucp.txt
nuren na230343.lp bb3707.lp
nuren na230343.ls bb3707.ls
nuren na230343.nhw bb3707.nhw
nucp  bb3709.lph na230443.eng na230.modelx na230.levelx bb3709.lpe > nucp.txt
nuren na230443.lp bb3709.lp
nuren na230443.ls bb3709.ls
nuren na230443.nhw bb3709.nhw
nucp  bb370b.lph na230543.eng na230.modelx na230.levelx bb370b.lpe > nucp.txt
nuren na230543.lp bb370b.lp
nuren na230543.ls bb370b.ls
nuren na230543.nhw bb370b.nhw
nulev na23b     
levp na23b     
