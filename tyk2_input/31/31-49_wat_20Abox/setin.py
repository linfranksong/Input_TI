import os

final_common = ["C1", "C2", "C3", "C4", "C5", "C6", "CL1", "C8", "O9", "N10", "C11", "C12", "C13", "N14", "C15", "C16", "N17", "C18", "O19", "CL2", "H1", "H2", "H6", "HN10", "H12", "H13", "H16", "HN17"]

dir = '/mnt/scratch/songlin3/run/tyk2/L31/wat_20Abox/ti_one-step/'
res1i='31'
res1='NNN'
res2list=LIST1

for i in res2list:
  a=i.upper()
  res2='L'+a
  filesdir = dir + "%s_%s"%(res1i,i) + "/" + "files" + "/"
  os.chdir(filesdir)
  os.system("cp ../../input-files/*in .")
  os.system("cp ../%s-%s_merged.* ."%(res1i,i))
  pdb = file.readlines(open('%s-%s_merged.pdb'%(res1i,i),'r'))
  for line in pdb:
    newlist = []
    newlist = line.split()
    if len(newlist) > 4 and newlist[3] == '%s'%(res1):
      resid1 =  newlist[4]
      os.system("sed -i 's/ZZZ/%s/g' temp_*.in"%(resid1))
      break
  for line in pdb:
    newlist = []
    newlist = line.split()
    if len(newlist) > 4 and newlist[3] == '%s'%(res2):
      resid2 =  newlist[4]
      os.system("sed -i 's/49/%s/g' temp_*.in"%(resid2))
      break
  print res1 + '>' + res2
  atmnmlist1 = []
  for line in pdb:
    newlist=[]
    newlist = line.split()
    if len(newlist) > 4 and newlist[3] == '%s'%(res1) and newlist[2] not in final_common:
      atomname = newlist[2]
      print atomname
      atmnmlist1.append(newlist[2])
  print atmnmlist1
  sc1 = ':1@'
  for num in range(0,len(atmnmlist1)):
    sc1 = sc1  + atmnmlist1[num] + ','
  print sc1
  os.system("sed -i 's/AAA/%s/g' temp_*in"%(sc1))
  ###res2
  print res2 + '>' + res1
  atmnmlist2 = []
  for line in pdb:
    newlist=[]
    newlist = line.split()
    if len(newlist) > 4 and newlist[3] == '%s'%(res2) and newlist[2] not in final_common:
      atomname = newlist[2]
      print atomname
      atmnmlist2.append(newlist[2])
  print atmnmlist2
  sc2 = ':2@'
  #print len(atmnmlist1)
  for num in range(0,len(atmnmlist2)):
    sc2 = sc2  + atmnmlist2[num] + ','
  print sc2
  os.system("sed -i 's/BBB/%s/g' temp_*in"%(sc2))
  os.system("cd ..")
  os.chdir(dir)
