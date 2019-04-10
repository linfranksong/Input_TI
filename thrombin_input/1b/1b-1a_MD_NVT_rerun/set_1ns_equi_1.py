import os

dir = '/mnt/ls15/scratch/users/songlin3/run/thrombin/ligand_final/final/1b_resp/MD_NVT_rerun/ti_one-step/1b_1a/'
filesdir = dir + 'files/'
temp_equiin = filesdir + 'temp_equi_1.in'
temp_pbs = filesdir + 'temp_1ns_equi_1.pbs'

lambd = [ 0.00922, 0.04794, 0.11505, 0.20634, 0.31608, 0.43738, 0.56262, 0.68392, 0.79366, 0.88495, 0.95206, 0.99078]
for j in lambd:
  os.system("rm -r %6.5f" %(j)) 
  os.system("mkdir %6.5f" %(j)) 
  os.chdir("%6.5f" %(j))
  os.system("rm *")
  workdir = dir + "%6.5f" %(j) + '/'
  #equiin
  eqin = workdir + "%6.5f_equi_1.in" %(j)
  os.system("cp %s %s" %(temp_equiin, eqin))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, eqin))
  #PBS
  pbs = workdir + "%6.5f_1ns_equi_1.pbs" %(j)
  os.system("cp %s %s" %(temp_pbs, pbs))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, pbs))
  #top
  os.system("cp ../1b-1a_merged.prmtop .")
  os.system("cp ../0.5_equi_0.rst .")
  #submit pbs 
  os.system("qsub %s" %(pbs)) 
  os.chdir(dir)
