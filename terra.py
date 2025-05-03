'''
to configure python to terraform to create respurces on Azure, first install terraform in your desktop.
Then using pip instll python-Terraform, install terraform in python.
Under Python folder only, create a terraform folder, under terraform folder create main.tf
add provider details to main.tf and add resource code to be created on azure.
mentioned main.tf dorectory path, also mention terraform installed folder path.
update terrafor foledr path to environment variables.
'''

import os
from python_terraform import Terraform

# Set working directory to the folder containing your Terraform configuration
os.chdir(r'C:\Users\nileshc13\AppData\Local\Programs\Python\terra-automate')

# Initialize Terraform
tf = Terraform(terraform_bin_path=r'C:\Terraform\terraform.exe')
print("Initializing Terraform...")
init_return_code, init_stdout, init_stderr = tf.init()
print(init_stdout)

# Plan the changes and save the plan file
print("Planning Terraform changes...")
plan_return_code, plan_stdout, plan_stderr = tf.plan(out='planfile.tfplan')
print(plan_stdout)

# Apply using the saved plan file
print("Applying Terraform changes...")
apply_return_code, apply_stdout, apply_stderr = tf.apply('planfile.tfplan')
print(apply_stdout)
