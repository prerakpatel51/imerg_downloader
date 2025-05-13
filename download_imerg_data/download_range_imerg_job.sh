#!/bin/bash


#SBATCH --job-name imerg_download_data

#SBATCH --partition=gpu1
#SBATCH --cpus-per-task=4            # Cores per task (>1 if multithread tasks)
#SBATCH --mem=26000                  # Real memory (RAM) required (MB)
#SBATCH --time=24:00:00              # Total run time limit (HH:MM:SS)

#SBATCH --error=/home1/ppatel2025/ppworktp/nowcasting/servir_nowcasting_examples/slurm_outputs/test_job.%J.err 
#SBATCH --output=/home1/ppatel2025/ppworktp/nowcasting/servir_nowcasting_examples/slurm_outputs/test_job.%J.out

# export CUDA_VISIBLE_DEVICES=4

conda init
conda activate tito_env

nvidia-smi
python3 download_range_imerg.py data 2002-04-01 2002-04-04 
python3 download_range_imerg.py data 2002-04-01 2002-04-04 
python3 download_range_imerg.py data 2002-04-01 2002-04-04 
