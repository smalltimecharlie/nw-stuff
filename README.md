# Secure Alpine EC2 Terraform Project

This Terraform project provisions a highly secure EC2 instance running the latest version of Alpine Linux.

## Features
- **Configurable instance size and tags**
- **Security group with minimal access (SSH allowed only from a specific IP)**
- **IAM role with least privilege**
- **Encrypted root volume**
- **Latest Alpine Linux AMI retrieval**

## Prerequisites
- Terraform installed (>= 1.6)
- AWS CLI configured with appropriate permissions
- An SSH key pair available in AWS

## Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/secure_alpine_ec2.git
   cd secure_alpine_ec2
   ```
2. Initialize Terraform:
   ```sh
   terraform init
   ```
3. Plan the deployment:
   ```sh
   terraform plan
   ```
4. Apply the configuration:
   ```sh
   terraform apply -auto-approve
   ```
5. Run tests:
   ```sh
   terraform test
   ```
6. Destroy resources when done:
   ```sh
   terraform destroy -auto-approve
   ```

## Security Notes
- Ensure the `allowed_ssh_ip` variable is set to a trusted IP.
- Use an appropriate IAM policy for the EC2 instance.
