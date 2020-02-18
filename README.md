# Input_TI
Please read the following note carefully before using the files.

1) Folder meaning:  e.g. CDK2_input/L29/29-26_MD_NVT_rerun, means CDK2 system, ligand name 29, mutating ligand 29 to ligand 26 in protein.

2) Inside each mutation folder. 

2.1) Equilibration at lambda=0.5. 

Input files: 0.5_min_0.in, 0.5_heat_0.in, 0.5_equi_0.in, min.pbs, heat.pbs, equi.pbs. Output files: 0.5_equi_0.rst.

"0.5_heat_0.in" heats the system at ps timescale, for longer heating and equilibration, please use following files:

Input files: 0.5_min_0.in, 0.5_heat_0_m.in, 0.5_equi_0_1.in, 0.5_equi_0_2.in, 0.5_equi_0_3.in, min.pbs, heat_m.pbs, equi_1.pbs, equi_2.pbs, equi_3.pbs. Output files: 0.5_equi_0_3.rst.

2.2) 12 lambda windows equilibration and sampling.

Input files: (temp_equi_1.in, temp_equi_2.in, temp_prod_1-7.in, temp_1ns_equi_1.pbs, temp_1ns_equi_2.pbs, temp_1-7.pbs)  or (temp_equi.in, temp_prod_1-5.in, temp_1ns_equi.pbs, temp_1-5.pbs).

"temp_equi_1.in" or "temp_equi.in" did not take the velocity from 0.5_equi_0.rst, to take the velocity from 0.5 equilibrated structure, please use following files:

Input files: (temp_equi_1_m.in, temp_equi_2.in, temp_prod_1-7.in, temp_1ns_equi_1_m.pbs, temp_1ns_equi_2.pbs, temp_1-7.pbs)  or (temp_equi_m.in, temp_prod_1-5.in, temp_1ns_equi_m.pbs, temp_1-5.pbs).

