#!/bin/bash
#SBATCH --qos=debug
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --core-spec=4
#SBATCH --tasks-per-node=8
#SBATCH --constraint=knl

module load vasp/5.4.4-knl
cd data
for d in ./*/ ; do (cd "$d" && srun vasp_std > output.txt); done
