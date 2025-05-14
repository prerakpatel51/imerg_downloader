# IMERG DOWNLOADER

A simple utility to download IMERG satellite precipitation data with one command using SLURM.

---

## 📁 Folder Structure

Place this folder inside:

nowcasting/servir_nowcasting_examples/scripts/

So the full path should look like:

nowcasting/servir_nowcasting_examples/scripts/imerg_downloader/

---

## ⚙️ Configuration

### 1. Edit the `.sh` script:

- **Update the scratch folder path**  
  Change the output directory in the `.sh` file to your personal **scratch folder path**.

- **Add trailing slash (`/`)**  
  Don't forget to add a `/` at the end of the scratch folder path to avoid path issues.

- **Set the desired date**  
  Modify the date field in the script to specify the data download range.

---

## 🚀 Submitting the Job

Before submitting the SLURM job, make sure of the following:

- ✅ You are inside the correct conda environment:
  
  ```bash
  conda activate tito_env

	•	✅ Submit the job using: sbatch imerg_download.sh



⸻

📌 Notes
	•	This downloader uses a batch SLURM job to handle large-scale downloading efficiently.
	•	Suitable for HPC environments with GPU nodes and large scratch storage.

⸻

🛠 Maintainer

For issues or contributions, please contact the repository maintainer or open an issue.

Let me know if you'd like badges, example outputs, or usage screenshots added.
