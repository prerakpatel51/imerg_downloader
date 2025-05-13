#!/bin/bash

#SBATCH --job-name=imerg_download_data
#SBATCH --partition=main
#SBATCH --cpus-per-task=4            # Cores per task (>1 if multithread tasks)
#SBATCH --mem=26000                  # Real memory (RAM) required (MB)
#SBATCH --time=2-24:00:00              # Total run time limit (HH:MM:SS)

#SBATCH --error=/home/pp1171/main/nowcasting/servir_nowcasting_examples/slurm_outputs/test_job.%J.err 
#SBATCH --output=/home/pp1171/main/nowcasting/servir_nowcasting_examples/slurm_outputs/test_job.%J.out

# Set up scratch directory
SCRATCH_DIR="/scratch/pp1171/imerg_data/"
mkdir -p $SCRATCH_DIR  # Create directory if it doesn't exist

# Load conda properly
source /home/pp1171/anaconda3/etc/profile.d/conda.sh

# Activate environment
conda activate tito_env

# Download directly to scratch
python3 download_range_imerg.py $SCRATCH_DIR 2010-01-01 2018-01-01

# Optional: Sync back to home when done (if needed)
# rsync -av $SCRATCH_DIR/ /home/pp1171/main/nowcasting/servir_nowcasting_examples/scripts/download_imerg_data/data/
