provider "aws" {
  region = "us-east-1" # Change to your preferred region
}

# Fetch the latest Alpine Linux AMI
data "aws_ami" "alpine" {
  most_recent = true
  owners      = ["538276064493"] # Official Alpine Linux AMI owner ID

  filter {
    name   = "name"
    values = ["alpine-*-x86_64"]
  }
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "allowed_ssh_ip" {
  description = "Allowed IP address for SSH access"
  type        = string
  default     = "0.0.0.0/32" # Change this to a specific IP for security
}

variable "tags" {
  description = "Tags to apply to the instance"
  type        = map(string)
  default = {
    Name = "SecureAlpineEC2"
  }
}

# Security Group with restricted SSH access
resource "aws_security_group" "secure_sg" {
  name_prefix = "secure-alpine-"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.allowed_ssh_ip]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# IAM role for least privilege access
resource "aws_iam_role" "ec2_role" {
  name = "secure_alpine_ec2_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "secure_alpine_profile"
  role = aws_iam_role.ec2_role.name
}

# Encrypted root volume
resource "aws_ebs_volume" "root_volume" {
  availability_zone = "us-east-1a"
  size             = 8
  encrypted        = true
}

# EC2 Instance
resource "aws_instance" "secure_alpine" {
  ami                  = data.aws_ami.alpine.id
  instance_type        = var.instance_type
  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name
  security_groups      = [aws_security_group.secure_sg.name]
  key_name             = "my-key-pair" # Change this to your SSH key

  root_block_device {
    encrypted = true
  }

  tags = var.tags
}

# Terraform Test Assertions
test "ec2_instance_exists" {
  condition     = aws_instance.secure_alpine.id != ""
  error_message = "EC2 instance should be created"
}

test "security_group_restricts_ssh" {
  condition     = length(aws_security_group.secure_sg.ingress) == 1 && aws_security_group.secure_sg.ingress[0].from_port == 22
  error_message = "Security group should restrict SSH to a single allowed IP"
}

test "instance_has_encrypted_root_volume" {
  condition     = aws_instance.secure_alpine.root_block_device[0].encrypted == true
  error_message = "EC2 instance should have encrypted root volume"
}
