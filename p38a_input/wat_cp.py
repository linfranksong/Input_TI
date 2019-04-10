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
    os.system("rm -r %s-%s_wat_20Abox"%(i,newlist[n]))
    os.system("mkdir %s-%s_wat_20Abox"%(i,newlist[n]))
    wdir = resdir + '%s-%s_wat_20Abox'%(i,newlist[n])
    os.chdir(wdir)
    os.system("cp /mnt/home/songlin3/Schrodinger_FEP_set/p38a_input/L%s/%s-%s_wat_20Abox/* ."%(res2,i,newlist[n]))
    os.system("cp -r /mnt/home/songlin3/Schrodinger_FEP_set/p38a_input/L%s/%s-%s_wat_20Abox/files/ ."%(res2,i,newlist[n]))
    #### equi
    os.system("cp 0.5_equi_0.in 0.5_equi_0_1.in")
    os.system("cp 0.5_equi_0.in 0.5_equi_0_3.in")
    os.system("sed -i 's/nstlim = 1000000/nstlim = 200000/g' 0.5_equi_0_1.in")
    os.system("cp 0.5_equi_0_1.in 0.5_equi_0_2.in")
    os.system("sed -i 's/nstlim = 1000000/nstlim = 600000/g' 0.5_equi_0_3.in")
    os.system("cp equi.pbs equi_1.pbs")
    os.system("sed -i 's/0.5_equi_0/0.5_equi_0_1/g' equi_1.pbs")
    os.system("sed -i 's/-x 0.5_equi_0_1.netcdf/-x 0.5_equi_0_1.netcdf -ref 0.5_heat_0.rst/g' equi_1.pbs")
    os.system("cp equi.pbs equi_2.pbs")
    os.system("sed -i 's/0.5_equi_0/0.5_equi_0_2/g' equi_2.pbs")
    os.system("sed -i 's/-x 0.5_equi_0_2.netcdf/-x 0.5_equi_0_2.netcdf -ref 0.5_equi_0_1.rst/g' equi_2.pbs"
)
    os.system("sed -i 's/0.5_heat_0.rst/0.5_equi_0_1.rst/g' equi_2.pbs")
    os.system("cp equi.pbs equi_3.pbs")
    os.system("sed -i 's/0.5_equi_0/0.5_equi_0_3/g' equi_3.pbs")
    os.system("sed -i 's/-x 0.5_equi_0_3.netcdf/-x 0.5_equi_0_3.netcdf -ref 0.5_equi_0_2.rst/g' equi_3.pbs"
)
    os.system("sed -i 's/0.5_heat_0.rst/0.5_equi_0_2.rst/g' equi_3.pbs")
    ###  heat
    os.system("cat 0.5_heat_0.in /mnt/ls15/scratch/users/songlin3/run/TI_input/p38a_input/heat_gradual > 0.5_heat_0_m.in")
    os.system("cp /mnt/ls15/scratch/users/songlin3/run/TI_input/p38a_input/sed_wat.sh .")
    os.system("sh sed_wat.sh")
    os.system("rm sed_wat.sh")
    os.system("cp heat.pbs heat_m.pbs")
    os.system("sed -i 's/-x 0.5_heat_0.netcdf/-x 0.5_heat_0.netcdf -ref 0.5_min_0.rst/g' heat_m.pbs")
    os.system("sed -i 's/0.5_heat_0.in/0.5_heat_0_m.in/g' heat_m.pbs")
    ### setpy
    os.system("rm set.py")
    os.system("rm files/temp.pbs")
    ### setpy
    os.system("cp set_1ns_equi.py set_1ns_equi_m.py")
    os.system("sed -i 's/equi.in/equi_m.in/g' set_1ns_equi_m.py")
    os.system("sed -i 's/temp_1ns_equi.pbs/temp_1ns_equi_m.pbs/g' set_1ns_equi_m.py")
    os.system("sed -i 's/0.5_equi_0.rst/0.5_equi_0_3.rst/g' set_1ns_equi_m.py")
    ### pbs
    os.system("cp files/temp_1ns_equi.pbs files/temp_1ns_equi_m.pbs")
    os.system("sed -i 's/0.5_equi_0.rst/0.5_equi_0_3.rst/g' files/temp_1ns_equi_m.pbs")
    os.system("sed -i 's/XXX_equi.in/XXX_equi_m.in/g' files/temp_1ns_equi_m.pbs")
    ###equi_input
    os.system("cp files/temp_equi.in files/temp_equi_m.in")
    os.system("sed -i 's/ntx    = 1/ntx    = 5/g' files/temp_equi_m.in")
    os.system("sed -i 's/irest  = 0,/irest  = 1,/g' files/temp_equi_m.in")
    os.chdir(resdir)
  os.chdir(dir)
