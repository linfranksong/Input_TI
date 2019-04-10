import os

dir = '/mnt/scratch/songlin3/run/p38a/L3FN/MD_NVT_rerun/ti_one-step/3FN_2P/'
filesdir = dir + 'files/'
temp_equiin = filesdir + 'temp_equi_1_m.in'
temp_pbs = filesdir + 'temp_1ns_equi_1_m.pbs'

lambd = [0.56262, 0.68392, 0.79366, 0.88495, 0.95206, 0.99078]
for j in lambd:
  os.chdir("%6.5f" %(j))
  workdir = dir + "%6.5f" %(j) + '/'
  #equiin
  eqin = workdir + "%6.5f_equi_1_m.in" %(j)
  os.system("cp %s %s" %(temp_equiin, eqin))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, eqin))
  #PBS
  pbs = workdir + "%6.5f_1ns_equi_1_m.pbs" %(j)
  os.system("cp %s %s" %(temp_pbs, pbs))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, pbs))
  #top
  os.system("cp ../3FN-2P_merged.prmtop .")
  os.system("cp ../0.5_equi_0_3.rst .")
  #submit pbs 
  os.system("qsub %s" %(pbs)) 
  os.chdir(dir)
