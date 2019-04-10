sed -i "s/ifsc = 1,/ifsc = 1, nmropt=1, ntr=1, restraintmask=':1-301', restraint_wt=5.0,/g" 0.5_heat_0_m.in
sed -i "s/ifsc = 1,/ifsc = 1, nmropt=1, ntr=1, restraintmask=':1-301', restraint_wt=5.0,/g" 0.5_equi_0_1.in
sed -i "s/ifsc = 1,/ifsc = 1, nmropt=1, ntr=1, restraintmask=':1-301', restraint_wt=2.0,/g" 0.5_equi_0_2.in
