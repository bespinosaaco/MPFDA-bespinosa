#!/bin/bash
#SBATCH --time=00:1:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=50M
#SBATCH --output=bespinosa_acosta.out

#add modules
module load python/3.13.2 scipy-stack/2025a

virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index -r requirements.txt

python bespinosa_acosta.py

