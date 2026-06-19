# 
The xFusionCorp Industries data science team needs a standardised Python environment for their new ML project. Set up a virtual environment with the required ML libraries on the controlplane host.


Create a Python virtual environment named ml-env under /root/code/ using python3 -m venv.

Activate the environment and install the following packages: numpy, pandas, scikit-learn, and matplotlib.

Generate a requirements.txt file using pip freeze and save it at /root/code/requirements.txt.

Ans:
# Create the virtual environment
python3 -m venv /root/code/ml-env

# Activate it
source /root/code/ml-env/bin/activate

# Upgrade pip (optional but recommended)
pip install --upgrade pip

# Install the required packages
pip install numpy pandas scikit-learn matplotlib

# Generate requirements.txt
pip freeze > /root/code/requirements.txt