# Input_TI
Please read the following note carefully before using the files.

1) Folder meaning:  e.g. CDK2_input/L29/29-26_MD_NVT_rerun, means CDK2 system, ligand name 29, mutating ligand 29 to ligand 26 in protein.

2) Inside each mutation folder. 

2.1) Equilibration at lambda=0.5. 

Files I used for my calculation: 0.5_min_0.in, 0.5_heat_0.in, 0.5_equi_0.in, min.pbs, heat.pbs, equi.pbs. File generated: 0.5_equi_0.rst.

Since 0.5_heat_0.in did not perform gradual heating, for future usage, please use following files for better heating and equilibration.

Files for future usage: 0.5_min_0.in, 0.5_heat_0_m.in, 0.5_equi_0_1.in, 0.5_equi_0_2.in, 0.5_equi_0_3.in, min.pbs, heat_m.pbs, equi_1.pbs, equi_2.pbs, equi_3.pbs. File will be generated: 0.5_equi_0_3.rst.

2.2) 12 lambda windows equilibration and sampling.

Files I used for my calculation: (temp_equi_1.in, temp_equi_2.in, temp_prod_1-7.in, temp_1ns_equi_1.pbs, temp_1ns_equi_2.pbs, temp_1-7.pbs)  or (temp_equi.in, temp_prod_1-5.in, temp_1ns_equi.pbs, temp_1-5.pbs).

Since temp_equi_1.in or temp_equi.in did not take the velocity from 0.5_equi_0.rst, for future usage, please use following files to take the velocity from 0.5 equilibrated structure.

Files for future usage: (temp_equi_1_m.in, temp_equi_2.in, temp_prod_1-7.in, temp_1ns_equi_1_m.pbs, temp_1ns_equi_2.pbs, temp_1-7.pbs)  or (temp_equi_m.in, temp_prod_1-5.in, temp_1ns_equi_m.pbs, temp_1-5.pbs).

