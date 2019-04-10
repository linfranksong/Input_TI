import os

dir = '/mnt/scratch/songlin3/run/mcl1/L40/MD_NVT_rerun/ti_one-step/40_29/'
filesdir = dir + 'files/'
temp_equiin = filesdir + 'temp_equi_2.in'
temp_pbs = filesdir + 'temp_1ns_equi_2.pbs'

lambd = [ 0.00922, 0.04794, 0.11505, 0.20634, 0.31608, 0.43738, 0.56262, 0.68392, 0.79366, 0.88495, 0.95206, 0.99078]
for j in lambd:
  os.chdir("%6.5f" %(j))
  workdir = dir + "%6.5f" %(j) + '/'
  #equiin
  eqin = workdir + "%6.5f_equi_2.in" %(j)
  os.system("cp %s %s" %(temp_equiin, eqin))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, eqin))
  #PBS
  pbs = workdir + "%6.5f_1ns_equi_2.pbs" %(j)
  os.system("cp %s %s" %(temp_pbs, pbs))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, pbs))
  #submit pbs 
  #os.system("qsub %s" %(pbs)) 
  os.chdir(dir)
