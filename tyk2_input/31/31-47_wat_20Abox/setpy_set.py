import os

final_common = ["C1", "C2", "C3", "C4", "C5", "C6", "CL1", "C8", "O9", "N10", "C11", "C12", "C13", "N14", "C15", "C16", "N17", "C18", "O19", "CL2", "H1", "H2", "H6", "HN10", "H12", "H13", "H16", "HN17"]

# parameter set up
dir = '/mnt/scratch/songlin3/run/tyk2/L31/wat_20Abox/ti_one-step/'
res1i='31'
res1='NNN'
res2list=LIST1

#need input files: uniq.json, protein.pdb, ions_wat.pdb, mol2, frcmod, tleap.in, 

#need to modify files: set.py, temp.pbs

for i in res2list:
  res2='L'+ i.upper()
  workdir = dir + "%s_%s"%(res1i,i) + "/"
  os.chdir(workdir)
  os.system("cp ../files/set*.py .")
  os.system("sed -i 's/47/%s/g' set*.py"%(i))
  os.chdir(dir)
