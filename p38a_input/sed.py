import os

# parameter set up
dir = '/mnt/ls15/scratch/users/songlin3/run/TI_input/p38a_input/'

f = open('muta_list_f', 'r')

for line in f:
  i, mu_list = line.split()[:2]
  newlist=mu_list.split(',')
  print i
  res2= i
  resdir = dir + 'L%s/'%(res2)
  os.chdir(resdir)
  for n in range(0,len(newlist)):
    wdir = resdir + '%s-%s_MD_NVT_rerun'%(i,newlist[n])
    os.chdir(wdir)
    if "heat.pbs" not in os.listdir("."):
       print os.getcwd()
       os.system("sed -i 's/mpirun -np $num $exe -O -i 0.5_heat_0.in/#mpirun -np $num $exe -O -i 0.5_heat_0.in/g' equi_2.pbs")
       os.system("sed -i 's/mpirun -np $num $exe -O -i 0.5_heat_0.in/#mpirun -np $num $exe -O -i 0.5_heat_0.in/g' equi_3.pbs")
    os.chdir(resdir)
  os.chdir(dir)
