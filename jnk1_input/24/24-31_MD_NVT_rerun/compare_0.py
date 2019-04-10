import os


equiin= file.readlines(open('0.5_min_0.in','r'))
for line in equiin:
  if "scmask1" in line:
    a,b=line.split('\n')
    c,d=a.split('=')
  if "scmask2" in line:
    aa,bb=line.split('\n')
    cc,dd=aa.split('=')


equiin= file.readlines(open('previous_equi_0.in','r'))
for line in equiin:
  if "scmask1" in line:
    ra,rb=line.split('\n')
    rc,rd=ra.split('=')
  if "scmask2" in line:
    raa,rbb=line.split('\n')
    rcc,rdd=raa.split('=')

if d != rd:
   print 'sc1 not'
   print d
   print rd

if dd !=rdd:
   print 'sc2 not'
   print dd
   print rdd
