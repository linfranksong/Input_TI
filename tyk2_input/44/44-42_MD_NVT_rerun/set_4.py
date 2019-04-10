import os

dir = '/mnt/scratch/songlin3/run/tyk2/L44/MD_NVT_rerun/ti_one-step/44_42/'
filesdir = dir + 'files/'
temp_prodin = filesdir + 'temp_prod_4.in'
temp_pbs = filesdir + 'temp_4.pbs'

lambd = [ 0.00922, 0.04794, 0.11505, 0.20634, 0.31608, 0.43738, 0.56262, 0.68392, 0.79366, 0.88495, 0.95206, 0.99078]
for j in lambd:
  os.chdir("%6.5f" %(j))
  workdir = dir + "%6.5f" %(j) + '/'
  #prodin
  prodin = workdir + "%6.5f_prod_4.in" %(j)
  os.system("cp %s %s" %(temp_prodin, prodin))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, prodin))
  #PBS
  pbs = workdir + "%6.5f_4.pbs" %(j)
  os.system("cp %s %s" %(temp_pbs, pbs))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, pbs))
  #submit pbs 
  #os.system("qsub %s" %(pbs)) 
  os.chdir(dir)
