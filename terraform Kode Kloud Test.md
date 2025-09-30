terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.91.0"
    }
  }
}

provider "aws" {
  region                      = "us-east-1"
  skip_credentials_validation = true
  skip_requesting_account_id  = true
  s3_use_path_style           = true

  endpoints {
    ec2            = "http://aws:4566"
    apigateway     = "http://aws:4566"
    cloudformation = "http://aws:4566"
    cloudwatch     = "http://aws:4566"
    dynamodb       = "http://aws:4566"
    es             = "http://aws:4566"
    firehose       = "http://aws:4566"
    iam            = "http://aws:4566"
    kinesis        = "http://aws:4566"
    lambda         = "http://aws:4566"
    route53        = "http://aws:4566"
    redshift       = "http://aws:4566"
    s3             = "http://aws:4566"
    secretsmanager = "http://aws:4566"
    ses            = "http://aws:4566"
    sns            = "http://aws:4566"
    sqs            = "http://aws:4566"
    ssm            = "http://aws:4566"
    stepfunctions  = "http://aws:4566"
    sts            = "http://aws:4566"
    rds            = "http://aws:4566"
  }
}


The Nautilus DevOps team is strategizing the migration of a portion of their infrastructure to the AWS cloud. Recognizing the scale of this undertaking, they have opted to approach the migration in incremental steps rather than as a single massive transition. To achieve this, they have segmented large tasks into smaller, more manageable units. This granular approach enables the team to execute the migration in gradual phases, ensuring smoother implementation and minimizing disruption to ongoing operations. By breaking down the migration into smaller tasks, the Nautilus DevOps team can systematically progress through each stage, allowing for better control, risk mitigation, and optimization of resources throughout the migration process.


1. **Create Key Pair Using Terraform**

create a key pair using Terraform with the following requirements:

Name of the key pair should be nautilus-kp.

Key pair type must be rsa.

The private key file should be saved under /home/bob/nautilus-kp.pem.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.

2. **Create Security Group Using Terraform**


Use Terraform to create a security group under the default VPC with the following requirements:

a) The name of the security group must be nautilus-sg.

b) The description must be Security group for Nautilus App Servers.

c) Add an inbound rule of type HTTP, with a port range of 80, and source CIDR range 0.0.0.0/0.

d) Add another inbound rule of type SSH, with a port range of 22, and source CIDR range 0.0.0.0/0.

Ensure that the security group is created in the us-east-1 region using Terraform. The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.

3. **Create VPC Using Terraform**

Create a VPC named xfusion-vpc in region us-east-1 with any IPv4 CIDR block through terraform.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.


4. **Create VPC with CIDR Using Terraform**

Create a VPC named nautilus-vpc in us-east-1 region with 192.168.0.0/24 IPv4 CIDR using terraform.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.

resource "aws_vpc" "nautilus_vpc" {
  cidr_block           = "192.168.0.0/24"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "nautilus-vpc"
  }
}

5. **Create VPC with IPv6 Using Terraform**

resource "aws_vpc" "ipv6_vpc" {
  cidr_block           = "10.0.0.0/16"          # IPv4 CIDR
  assign_generated_ipv6_cidr_block = true       # Enable IPv6
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "ipv6-vpc"
  }
}

# Optional: output the IPv6 CIDR
output "ipv6_cidr_block" {
  value = aws_vpc.ipv6_vpc.ipv6_cidr_block
}

6. **Create Elastic IP Using Terraform**

For this task, allocate an Elastic IP address named xfusion-eip using Terraform.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.
Ans: 
resource "aws_eip" "xfusion_eip" {
  domain = "vpc"

  tags = {
    Name = "xfusion-eip"
  }
}

7. **Create EC2 Instance Using Terraform**

For this task, create an EC2 instance using Terraform with the following requirements:

The name of the instance must be devops-ec2.

Use the Amazon Linux ami-0c101f26f147fa7fd to launch this instance.

The Instance type must be t2.micro.

Create a new RSA key named devops-kp.

Attach the default (available by default) security group.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to provision the instance.

Ans:
resource "tls_private_key" "devops_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "devops_kp" {
  key_name   = "devops-kp"
  public_key = tls_private_key.devops_key.public_key_openssh
}

resource "aws_instance" "devops_ec2" {
  ami                    = "ami-0c101f26f147fa7fd"
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.devops_kp.key_name

  vpc_security_group_ids = [data.aws_security_group.default.id]

  tags = {
    Name = "devops-ec2"
  }
}

# Get the default security group
data "aws_security_group" "default" {
  filter {
    name   = "group-name"
    values = ["default"]
  }

  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

# Get the default VPC
data "aws_vpc" "default" {
  default = true
}

# Save private key to local file (optional but helpful)
resource "local_file" "private_key" {
  content  = tls_private_key.devops_key.private_key_pem
  filename = "${path.module}/devops-kp.pem"
  file_permission = "0400"


8. **Create AMI Using Terraform**
For this task, create an AMI from an existing EC2 instance named devops-ec2 using Terraform.

Name of the AMI should be devops-ec2-ami, make sure AMI is in available state.

The Terraform working directory is /home/bob/terraform. Update the main.tf file (do not create a separate .tf file) to create the AMI.

Ans:
# Existing ami details Provision EC2 instance
resource "aws_instance" "ec2" {
  ami           = "ami-0c101f26f147fa7fd"
  instance_type = "t2.micro"
  vpc_security_group_ids = [
    "sg-b92e3cc784acd101d"
  ]

  tags = {
    Name = "devops-ec2"
  }
}

# Create AMI from the above instance
resource "aws_ami_from_instance" "devops_ami" {
  name               = "devops-ec2-ami"
  source_instance_id = aws_instance.ec2.id
  depends_on         = [aws_instance.ec2]

  lifecycle {
    create_before_destroy = true
  }

  tags = {
    Name = "devops-ec2-ami"
  }
}

# Optional: Output the AMI ID
output "ami_id" {
  value = aws_ami_from_instance.devops_ami.id
}


9. **Create EBS Volume Using Terraform**

For this task, create an AWS EBS volume using Terraform with the following requirements:

Name of the volume should be devops-volume.

Volume type must be gp3.

Volume size must be 2 GiB.

Ensure the volume is created in us-east-1.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.

resource "aws_ebs_volume" "devops_volume" {
  availability_zone = "us-east-1a"  
  size              = 2
  type              = "gp3"
  tags = {
    Name = "devops-volume"
  }
}


10. **Create Snapshot Using Terraform**
The Nautilus DevOps team has some volumes in different regions in their AWS account. They are going to setup some automated backups so that all important data can be backed up on regular basis. For now they shared some requirements to take a snapshot of one of the volumes they have.

Create a snapshot of an existing volume named xfusion-vol in us-east-1 region using terraform.

1) The name of the snapshot must be xfusion-vol-ss.

2) The description must be Xfusion Snapshot.

3) Make sure the snapshot status is completed before submitting the task.

The Terraform working directory is /home/bob/terraform. Update the main.tf file (do not create a separate .tf file) to accomplish this task.
Ans:
To accomplish this task, you need to:

Use the AWS provider in Terraform.

Locate the volume named xfusion-vol in the us-east-1 region.

Create a snapshot with the specified name and description.

Use a null_resource or local-exec provisioner to wait until the snapshot status is completed.

Ans:
resource "aws_ebs_volume" "k8s_volume" {
  availability_zone = "us-east-1a"
  size              = 5
  type              = "gp2"

  tags = {
    Name = "xfusion-vol"
  }
}

resource "aws_ebs_snapshot" "xfusion_snapshot" {
  volume_id   = aws_ebs_volume.k8s_volume.id
  description = "Xfusion Snapshot"

  tags = {
    Name = "xfusion-vol-ss"
  }
}

resource "null_resource" "wait_for_snapshot" {
  provisioner "local-exec" {
    command = "aws ec2 wait snapshot-completed --snapshot-ids ${aws_ebs_snapshot.xfusion_snapshot.id} --region us-east-1"
  }

  depends_on = [aws_ebs_snapshot.xfusion_snapshot]
}

11. **Create Alarm Using Terraform**
The Nautilus DevOps team is setting up monitoring in their AWS account. As part of this, they need to create a CloudWatch alarm.

Using Terraform, perform the following:

Task Details:
Create a CloudWatch alarm named devops-alarm.
The alarm should monitor CPU utilization of an EC2 instance.
Trigger the alarm when CPU utilization exceeds 80%.
Set the evaluation period to 5 minutes.
Use a single evaluation period.
Ensure that the entire configuration is implemented using Terraform. The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.
Ans:
# EC2 instance configuration
resource "aws_instance" "devops_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = "nautilus-key"
  tags = {
    Name = "DevOps-Instance"
  }


  associate_public_ip_address = true
}

# CloudWatch Metric Alarm for CPU Utilization
resource "aws_cloudwatch_metric_alarm" "devops_alarm" {
  alarm_name                = "devops-alarm"
  comparison_operator       = "GreaterThanThreshold"
  evaluation_periods        = 1
  metric_name               = "CPUUtilization"
  namespace                 = "AWS/EC2"
  period                    = 300 # 5 minutes (in seconds)
  statistic                 = "Average"
  threshold                 = 80
  alarm_description         = "This alarm triggers when CPU utilization exceeds 80% for the EC2 instance"
  insufficient_data_actions = []

  dimensions = {
    InstanceId = aws_instance.devops_instance.id
  }


}


12. **Create Public S3 Bucket Using Terraform**
As part of the data migration process, the Nautilus DevOps team is actively creating several S3 buckets on AWS. They plan to utilize both private and public S3 buckets to store the relevant data. Given the ongoing migration of other infrastructure to AWS, it is logical to consolidate data storage within the AWS environment as well.

Create a public S3 bucket named datacenter-s3-28669 using Terraform.

Ensure the bucket is accessible publicly once created by setting the proper ACL.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.

Notes:

Create the resources only in the us-east-1 region.
Right-click under the EXPLORER section in VS Code and select Open in Integrated Terminal to launch the terminal.
The name of the S3 bucket should be based on datacenter-s3-28669.
You can use the ACL settings to ensure the bucket is publicly accessible.

Ans:
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "nautilus_public_bucket" {
  bucket = "datacenter-s3-27747"

  tags = {
    Name        = "Public S3 Bucket"
    Environment = "DevOps"
  }
}

resource "aws_s3_bucket_public_access_block" "nautilus_public_bucket_access" {
  bucket = aws_s3_bucket.nautilus_public_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "nautilus_public_bucket_acl" {
  depends_on = [
    aws_s3_bucket_public_access_block.nautilus_public_bucket_access,
  ]
  bucket = aws_s3_bucket.nautilus_public_bucket.id
  acl    = "public-read"
}


13. **Create Private S3 Bucket Using Terraform**
As part of the data migration process, the Nautilus DevOps team is actively creating several S3 buckets on AWS using Terraform. They plan to utilize both private and public S3 buckets to store the relevant data. Given the ongoing migration of other infrastructure to AWS, it is logical to consolidate data storage within the AWS environment as well.

Create an S3 bucket using Terraform with the following details:

1) The name of the S3 bucket must be nautilus-s3-27083.

2) The S3 bucket must block all public access, making it a private bucket.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.

Notes:

Use Terraform to provision the S3 bucket.
Right-click under the EXPLORER section in VS Code and select Open in Integrated Terminal to launch the terminal.
Ensure the resources are created in the us-east-1 region.
The bucket must have block public access enabled to restrict any public access.

Ans: 
resource "aws_s3_bucket" "nautilus_bucket" {
  bucket = "nautilus-s3-27083"
}

resource "aws_s3_bucket_public_access_block" "nautilus_bucket_block" {
  bucket = aws_s3_bucket.nautilus_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

14. **Create IAM User Using Terraform**

When establishing infrastructure on the AWS cloud, Identity and Access Management (IAM) is among the first and most critical services to configure. IAM facilitates the creation and management of user accounts, groups, roles, policies, and other access controls. The Nautilus DevOps team is currently in the process of configuring these resources and has outlined the following requirements:

For this task, create an IAM user named iamuser_anita using terraform. The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.
Ans:
# Create IAM user named iamuser_anita
resource "aws_iam_user" "iamuser_anita" {
  name = "iamuser_anita"
}

15. **Create IAM Group Using Terraform**
The jim DevOps team has been creating a couple of services on AWS cloud. They have been breaking down the migration into smaller tasks, allowing for better control, risk mitigation, and optimization of resources throughout the migration process. Recently they came up with requirements mentioned below.

Create an IAM group named iamgroup_jim using terraform.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.
ans:
resource "aws_iam_group" "jim_group" {
  name = "iamgroup_jim"
}
16. **Create IAM Policy Using Terraform**
When establishing infrastructure on the AWS cloud, Identity and Access Management (IAM) is among the first and most critical services to configure. IAM facilitates the creation and management of user accounts, groups, roles, policies, and other access controls. The Nautilus DevOps team is currently in the process of configuring these resources and has outlined the following requirements.

Create an IAM policy named iampolicy_james in us-east-1 region using Terraform. It must allow read-only access to the EC2 console, i.e., this policy must allow users to view all instances, AMIs, and snapshots in the Amazon EC2 console.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.
Ans:

data "aws_iam_policy_document" "ec2_read_only" {
  statement {
    effect = "Allow"

    actions = [
      "ec2:DescribeInstances",
      "ec2:DescribeImages",
      "ec2:DescribeSnapshots",
      "ec2:DescribeVolumes",
      "ec2:DescribeTags",
      "ec2:DescribeSecurityGroups",
      "ec2:DescribeKeyPairs",
      "ec2:DescribeVpcs",
      "ec2:DescribeSubnets",
      "ec2:DescribeNetworkInterfaces",
    ]

    resources = ["*"]
  }
}

resource "aws_iam_policy" "iampolicy_james" {
  name        = "iampolicy_james"
  description = "Read-only access to EC2 console - view instances, AMIs, and snapshots"
  policy      = data.aws_iam_policy_document.ec2_read_only.json
}


17. **Create DynamoDB Table Using Terraform**
The Nautilus DevOps team needs to set up a DynamoDB table for storing user data. They need to create a DynamoDB table with the following specifications:

1) The table name should be datacenter-users.

2) The primary key should be datacenter_id (String).

3) The table should use PAY_PER_REQUEST billing mode.

Use Terraform to create this DynamoDB table. The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to create the DynamoDB table.
Ans:
resource "aws_dynamodb_table" "datacenter_users" {
  name         = "datacenter-users"
  billing_mode = "PAY_PER_REQUEST"

  hash_key = "datacenter_id"

  attribute {
    name = "datacenter_id"
    type = "S"
  }

  tags = {
    Environment = "dev"
    Project     = "nautilus"
  }
}
18. **Create Kinesis Stream Using Terraform**
The Nautilus DevOps team needs to create an AWS Kinesis data stream for real-time data processing. This stream will be used to ingest and process large volumes of streaming data, which will then be consumed by various applications for analytics and real-time decision-making.

The stream should be named xfusion-stream.

Use Terraform to create this Kinesis stream.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.

Note:

Right-click under the EXPLORER section in VS Code and select Open in Integrated Terminal to launch the terminal.
Before submitting the task, ensure that terraform plan returns No changes. Your infrastructure matches the configuration.
Ans:

resource "aws_kinesis_stream" "xfusion-stream" {
  name             = "xfusion-stream"
  shard_count      = 1
  retention_period = 24

  shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
  ]

  stream_mode_details {
    stream_mode = "PROVISIONED"
  }

  tags = {
    Environment = "Production"
    Team        = "Nautilus DevOps"
  }
}
terraform init
terraform apply --auto-approve
terraform plan



19. **Create SNS Topic Using Terraform**
The Nautilus DevOps team needs to set up an SNS topic for sending notifications. They need to create an SNS topic with the following specifications:

1) The topic name should be nautilus-notifications.

Use Terraform to create this SNS topic. The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.
Ans:
resource "aws_sns_topic" "nautilus-notifications" {
  name = "nautilus-notifications"
}

20. **Create SSM Parameter Using Terraform**
The Nautilus DevOps team needs to create an SSM parameter in AWS with the following requirements:

1) The name of the parameter should be datacenter-ssm-parameter.

2) Set the parameter type to String.

3) Set the parameter value to datacenter-value.

4) The parameter should be created in the us-east-1 region.

5) Ensure the parameter is successfully created using terraform and can be retrieved when the task is completed.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.
Ans:
resource "aws_ssm_parameter" "datacenter-ssm-parameter" {
  name  = "datacenter-ssm-parameter"
  type  = "String"
  value = "datacenter-value"
}
# To verify the parameter was created and can be retrieved:
aws ssm get-parameter --name datacenter-ssm-parameter --region us-east-1
aws --endpoint-url=http://localhost:4566 ssm get-parameter --name datacenter-ssm-parameter --region us-east-1

21. **CloudWatch Setup Using Terraform**
The Nautilus DevOps team needs to set up CloudWatch logging for their application. They need to create a CloudWatch log group and log stream with the following specifications:

1) The log group name should be xfusion-log-group.

2) The log stream name should be xfusion-log-stream.

Use Terraform to create the CloudWatch log group and log stream. The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.

Ans:
resource "aws_cloudwatch_log_group" "xfusion-log-group" {
  name = "xfusion-log-group"

  tags = {
    Environment = "production"
    Application = "serviceA"
  }
}

resource "aws_cloudwatch_log_stream" "xfusion-log-stream" {
  name           = "xfusion-log-stream"
  log_group_name = aws_cloudwatch_log_group.xfusion-log-group.name
}

22. **CloudFormation Template Deployment Using Terraform**
The Nautilus DevOps team is working on automating infrastructure deployment using AWS CloudFormation. As part of this effort, they need to create a CloudFormation stack that provisions an S3 bucket with versioning enabled.

Create a CloudFormation stack named datacenter-stack using Terraform. This stack should contain an S3 bucket named datacenter-bucket-1350 as a resource, and the bucket must have versioning enabled. The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.
Ans:

resource "aws_cloudformation_stack" "datacenter_stack" {
  name          = "datacenter-stack"
  template_body = <<TEMPLATE
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "DatacenterBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "datacenter-bucket-1350",
        "VersioningConfiguration": {
          "Status": "Enabled"
        }
      }
    }
  }
}
TEMPLATE
}

23. **OpenSearch Setup Using Terraform**
The Nautilus DevOps team needs to set up an Amazon OpenSearch Service domain to store and search their application logs. The domain should have the following specification:

1) The domain name should be nautilus-es.

2) Use Terraform to create the OpenSearch domain. The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.


Notes:

The Terraform working directory is /home/bob/terraform.

Right-click under the EXPLORER section in VS Code and select Open in Integrated Terminal to launch the terminal.

Before submitting the task, ensure that terraform plan returns No changes. Your infrastructure matches the configuration.

The OpenSearch domain creation process may take several minutes. Please wait until the domain is fully created before submitting.
Ans:
resource "aws_opensearch_domain" "nautilus-es" {
  domain_name    = "nautilus-es"
  engine_version = "OpenSearch_1.0"

  cluster_config {
    instance_type  = "t3.small.search"
    instance_count = 1
  }

  tags = {
    Name        = "nautilus-es"
    Environment = "Production"
  }
}

24. **Secrets Manager Setup Using Terraform**
The Nautilus DevOps team needs to store sensitive data securely using AWS Secrets Manager. They need to create a secret with the following specifications:

1) The secret name should be datacenter-secret.

2) The secret value should contain a key-value pair with username: admin and password: Namin123.

3) Use Terraform to create the secret in AWS Secrets Manager.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to accomplish this task.
Ans:

resource "aws_secretsmanager_secret" "datacenter_secret" {
  name = "datacenter-secret"
}

resource "aws_secretsmanager_secret_version" "datacenter_secret_value" {
  secret_id = aws_secretsmanager_secret.datacenter_secret.id
  secret_string = jsonencode({
    username = "admin"
    password = "Namin123"
  })
}

25. **Change Instance Type Using Terraform**
During the migration process, the Nautilus DevOps team created several EC2 instances in different regions. They are currently in the process of identifying the correct resources and utilization and are making continuous changes to ensure optimal resource utilization. Recently, they discovered that one of the EC2 instances was underutilized, prompting them to decide to change the instance type. Please make sure the Status check is completed (if it's still in Initializing state) before making any changes to the instance.

Change the instance type from t2.micro to t2.nano for nautilus-ec2 instance using terraform.

Make sure the EC2 instance nautilus-ec2 is in running state after the change.

The Terraform working directory is /home/bob/terraform. Update the main.tf file (do not create a separate .tf file) to change the instance type.

Existing Resource details:
# Provision EC2 instance
resource "aws_instance" "ec2" {
  ami           = "ami-0c101f26f147fa7fd"
  instance_type = "t2.micro"
  subnet_id     = ""
  vpc_security_group_ids = [
    "sg-de0362e46c40b108a"
  ]

  tags = {
    Name = "nautilus-ec2"
  }
}
Ans: 
Jsut modify instance_type = "t2.nano"


26. **Attach Elastic IP Using Terraform**
The Nautilus DevOps team has been creating a couple of services on AWS cloud. They have been breaking down the migration into smaller tasks, allowing for better control, risk mitigation, and optimization of resources throughout the migration process. Recently they came up with requirements mentioned below.

There is an instance named datacenter-ec2 and an elastic-ip named datacenter-ec2-eip in us-east-1 region. Attach the datacenter-ec2-eip elastic-ip to the datacenter-ec2 instance using Terraform only. The Terraform working directory is /home/bob/terraform. Update the main.tf file (do not create a separate .tf file) to attach the specified Elastic IP to the instance.

Exiting Resource dwetails:

# Provision EC2 instance
resource "aws_instance" "ec2" {
  ami           = "ami-0c101f26f147fa7fd"
  instance_type = "t2.micro"
  subnet_id     = "subnet-6763211e33dc589a4"
  vpc_security_group_ids = [
    "sg-573b177b96a489f77"
  ]

  tags = {
    Name = "datacenter-ec2"
  }
}

# Provision Elastic IP
resource "aws_eip" "ec2_eip" {
  tags = {
    Name = "datacenter-ec2-eip"
  }
}
Ans:
resource "aws_eip_association" "eip_assoc" {
  instance_id   = aws_instance.ec2.id
  allocation_id = aws_eip.ec2_eip.id
}
27. **Attach Policy Using Terraform**
An IAM user named iamuser_ravi and a policy named iampolicy_ravi already exists. Use Terraform to attach the IAM policy iampolicy_ravi to the IAM user iamuser_ravi. The Terraform working directory is /home/bob/terraform. Update the main.tf file (do not create a separate .tf file) to attach the specified IAM policy to the IAM user.

Ans:

# Create IAM user
resource "aws_iam_user" "user" {
  name = "iamuser_ravi"

  tags = {
    Name = "iamuser_ravi"
  }
}

# Create IAM Policy
resource "aws_iam_policy" "policy" {
  name        = "iampolicy_ravi"
  description = "IAM policy allowing EC2 read actions for ravi"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["ec2:Read*"]
        Resource = "*"
      }
    ]
  })
}

# Attach IAM Policy to IAM User
resource "aws_iam_user_policy_attachment" "attachment" {
  user       = aws_iam_user.user.name
  policy_arn = aws_iam_policy.policy.arn
}


28. **Enable S3 Versioning Using Terraform**
Data protection and recovery are fundamental aspects of data management. It's essential to have systems in place to ensure that data can be recovered in case of accidental deletion or corruption. The DevOps team has received a requirement for implementing such measures for one of the S3 buckets they are managing.

The S3 bucket name is datacenter-s3-7640, enable versioning for this bucket using Terraform.

The Terraform working directory is /home/bob/terraform. Update the main.tf file (do not create a different .tf file) to accomplish this task.
Ans:
resource "aws_s3_bucket" "s3_ran_bucket" {
  bucket = "datacenter-s3-7640"
  
  tags = {
    Name = "datacenter-s3-7640"
  }
}

resource "aws_s3_bucket_acl" "s3_ran_bucket_acl" {
  bucket = aws_s3_bucket.s3_ran_bucket.id
  acl    = "private"
}

resource "aws_s3_bucket_versioning" "versioning_s3_ran_bucket" {
  bucket = aws_s3_bucket.s3_ran_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

29. **Delete Backup from S3 Using Terraform**
The Nautilus DevOps team is currently engaged in a cleanup process, focusing on removing unnecessary data and services from their AWS account. As part of the migration process, several resources were created for one-time use only, necessitating a cleanup effort to optimize their AWS environment.

A S3 bucket named devops-bck-27254 already exists.

1) Copy the contents of devops-bck-27254 S3 bucket to /opt/s3-backup/ directory on terraform-client host (the landing host once you load this lab).

2) Delete the S3 bucket devops-bck-27254.

3) Use the AWS CLI through Terraform to accomplish this task—for example, by running AWS CLI commands within Terraform. The Terraform working directory is /home/bob/terraform. Update the main.tf file (do not create a separate .tf file) to accomplish this task.

Ans:
# Step 1: Use the local-exec provisioner to run AWS CLI commands and copy S3 bucket contents to the local filesystem
resource "null_resource" "copy_s3_to_local" {
  provisioner "local-exec" {
    command = "aws s3 sync s3://devops-bck-27254 /opt/s3-backup/"
  }
}

# Step 2: Delete the S3 bucket after copying the contents
resource "null_resource" "delete_bucket" {
  depends_on = [null_resource.copy_s3_to_local]  # Ensures the bucket is deleted only after the copy

  provisioner "local-exec" {
    command = "aws s3 rb s3://devops-bck-27254 --force"  # Deletes the bucket after it is emptied
  }
}
30. **Delete EC2 Instance Using Terraform**
During the migration process, several resources were created under the AWS account. Some of these test resources are no longer needed at the moment, so we need to clean them up temporarily. One such instance is currently unused and should be deleted.

1) Delete the ec2 instance named devops-ec2 present in us-east-1 region using terraform. Make sure to keep the provisioning code, as we might need to provision this instance again later.

2) Before submitting your task, make sure instance is in terminated state.

The Terraform working directory is /home/bob/terraform.

Ans:
terraform destroy --auto-approve
or 
terraform destroy -target=aws_instance.devops_ec2 -auto-approve

Verify:
aws ec2 describe-instances \
  --region us-east-1 \
  --filters "Name=tag:Name,Values=devops-ec2" \
  --query "Reservations[*].Instances[*].State.Name" \
  --output text


31. **Delete IAM Group Using Terraform**
The Nautilus DevOps team is currently engaged in a cleanup process, focusing on removing unnecessary data and services from their AWS account. As part of the migration process, several resources were created for one-time use only, necessitating a cleanup effort to optimize their AWS environment.

Delete an IAM group named iamgroup_rose using terraform. Make sure to keep the provisioning code, as we might need to provision this instance again later.

The Terraform working directory is /home/bob/terraform.
Ans:
terraform destroy --auto-approve
or 
terraform destroy -target=aws_iam_group.iamgroup_rose -auto-approve

32. **Delete IAM Role Using Terraform**
Delete the IAM role named iamrole_siva using Terraform. Make sure to keep the provisioning code, as we might need to provision this instance again later.

The Terraform working directory is /home/bob/terraform.
Ans:
terraform destroy --auto-approve

33. **Delete VPC Using Terraform**
Delete a VPC named xfusion-vpc present in us-east-1 region using Terraform. Make sure to keep the provisioning code, as we might need to provision this instance again later.

The Terraform working directory is /home/bob/terraform.
Ans:
terraform destroy --auto-approve

34. **Copy Data to S3 Using Terraform**
The Nautilus DevOps team is presently immersed in data migrations, transferring data from on-premise storage systems to AWS S3 buckets. They have recently received some data that they intend to copy to one of the S3 buckets.

S3 bucket named datacenter-cp-8421 already exists. Copy the file /tmp/datacenter.txt to s3 bucket datacenter-cp-8421 using Terraform. The Terraform working directory is /home/bob/terraform. Update the main.tf file (do not create a separate .tf file) to accomplish this task.
Existed main.tf
resource "aws_s3_bucket" "my_bucket" {
  bucket = "datacenter-cp-8421"
  acl    = "private"

  tags = {
    Name        = "datacenter-cp-8421"
  }
}
Ans:
Add this block below your existing aws_s3_bucket resource:
resource "aws_s3_object" "datacenter_file" {
  bucket = aws_s3_bucket.my_bucket.bucket
  key    = "datacenter.txt"
  source = "/tmp/datacenter.txt"
  etag   = filemd5("/tmp/datacenter.txt")
}


35. **VPC Variable Setup Using Terraform**
The Nautilus DevOps team is automating VPC creation using Terraform to manage networking efficiently. As part of this task, they need to create a VPC with specific requirements.

For this task, create an AWS VPC using Terraform with the following requirements:

The VPC name nautilus-vpc should be stored in a variable named KKE_vpc.

The VPC should have a CIDR block of 10.0.0.0/16.

Note:

The configuration values should be stored in a variables.tf file.

The Terraform script should be structured with a main.tf file referencing variables.tf.

The Terraform working directory is /home/bob/terraform.
Ans:
variables.tf
variable "KKE_vpc" {
  description = "Name of the VPC"
  type        = string
  default     = "nautilus-vpc"
}

variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

main.tf
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr_block

  tags = {
    Name = var.KKE_vpc
  }
}

36. **Security Group Variable Setup Using Terraform**
The Nautilus DevOps team is enhancing infrastructure automation and needs to provision a Security Group using Terraform with specific configurations.

For this task, create an AWS Security Group using Terraform with the following requirements:

The Security Group name devops-sg should be stored in a variable named KKE_sg.
Note:

1. The configuration values should be stored in a variables.tf file.

2. The Terraform script should be structured with a main.tf file referencing variables.tf.
Ans:
# variables.tf
variable "KKE_sg" {
  description = "Name of the Security Group"
  type        = string
  default     = "devops-sg"
}

variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "KKE_vpc" {
  description = "Name of the VPC"
  type        = string
  default     = "devops-vpc"
}


# Main.tf
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr_block

  tags = {
    Name = var.KKE_vpc
  }
}

resource "aws_security_group" "devops" {
  name        = var.KKE_sg
  description = "Security group for DevOps"
  vpc_id      = aws_vpc.main.id  

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = var.KKE_sg
  }
}

37. **Elastic IP Variable Setup Using Terraform**
The Nautilus DevOps team is strategizing the migration of a portion of their infrastructure to the AWS cloud. As part of this phased migration approach, they need to allocate an Elastic IP address to support external access for specific workloads.

For this task, create an AWS Elastic IP using Terraform with the following requirement:

The Elastic IP name nautilus-eip should be stored in a variable named KKE_eip. The Terraform working directory is /home/bob/terraform.
Note:

The configuration values should be stored in a variables.tf file.

The Terraform script should be structured with a main.tf file referencing variables.tf

Ans:

variables.tf
variable "KKE_eip" {
  description = "Name tag for the Elastic IP"
  type        = string
  default     = "nautilus-eip"
}

Main.tf
resource "aws_eip" "nautilus" {
  vpc = true

  tags = {
    Name = var.KKE_eip
  }
}

38. **User Variable Setup Using Terraform**
The Nautilus DevOps team is automating IAM user creation using Terraform for better identity management.

For this task, create an AWS IAM User using Terraform with the following requirements:

The IAM User name iamuser_mariyam should be stored in a variable named KKE_user.
Note:

1. The configuration values should be stored in a variables.tf file.

2. The Terraform script should be structured with a main.tf file referencing variables.tf.
The Terraform working directory is /home/bob/terraform.

Ans:
variable "KKE_user" {
  description = "The name of the IAM user"
  type        = string
  default     = "iamuser_mariyam"
}  resource "aws_iam_user" "user" {
  name = var.KKE_user  # Reference the KKE_user variable
}

output "iam_user_name" {
  value = aws_iam_user.user.name
}

39. **Role Variable Setup Using Terraform**
The Nautilus DevOps team is automating IAM role creation using Terraform to streamline permissions management. As part of this task, they need to create an IAM role with specific requirements.

For this task, create an AWS IAM role using Terraform with the following requirements:

The IAM role name iamrole_kirsty should be stored in a variable named KKE_iamrole.
Note:

1. The configuration values should be stored in a variables.tf file.

2. The Terraform script should be structured with a main.tf file referencing variables.tf.
Ans:
variable "KKE_iamrole" {
  description = "The name of the IAM role"
  type        = string
  default     = "iamrole_kirsty"
}

resource "aws_iam_role" "this" {
  name = var.KKE_iamrole

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}
40. **Policy Variable Setup Using Terraform**
The Nautilus DevOps team is automating IAM policy creation using Terraform to enhance security and access management. As part of this task, they need to create an IAM policy with specific requirements.

For this task, create an AWS IAM policy using Terraform with the following requirements:

The IAM policy name iampolicy_yousuf should be stored in a variable named KKE_iampolicy.
Note:

The configuration values should be stored in a variables.tf file.

The Terraform script should be structured with a main.tf file referencing variables.tf.

Ans:
variable "KKE_iampolicy" {
  default     = "iampolicy_yousuf"
  type        = string
  description = "Name of the IAM policy"
}

resource "aws_iam_policy" "yousuf_policy" {
  name        = var.KKE_iampolicy
  description = "IAM policy created by Terraform for user Yousuf"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "ec2:Describe*",
          "s3:ListAllMyBuckets"
        ]
        Effect   = "Allow"
        Resource = "*"
      }
    ]
  })
}

**Level 2**
# Q1 Create VPC and Subnet Using Terraform
# Q2 Launch EC2 in Private VPC Subnet Using Terraform
# Q3 Replace Existing EC2 Instance via Terraform
# Q4 Deploy Multiple EC2 Instances with Terraform
# Q5 Associate Elastic IP with EC2 Instance Using Terraform
# Q6 Launch EC2 Instance from Custom AMI Using Terraform
# Q7 Stream Kinesis Data to CloudWatch Using Terraform
# Q8 Sync Data to S3 Bucket with Terraform
# Q9 Prevent S3 Bucket Deletion via Terraform
# Q10 Grant EC2 Access to S3 Bucket Using Terraform
# Q11 Implement S3 Lifecycle Management Policy Using Terraform
# Q12 Integrate SNS with SQS for Messaging Using Terraform
# Q13 Attach IAM Role with Inline Policy Using Terraform
# Q14 Provision IAM User with Terraform
# Q15 Attach IAM Policy for DynamoDB Access Using Terraform
# Q16 Send Notifications from IAM Events to SNS Using Terraform
# Q17 Access Secrets Manager with IAM Role Using Terraform
# Q18 Create and Configure Alarm Using CloudWatch Using Terraform
# Q19 Configure CloudWatch to Trigger SNS Alerts Using Terraform
# Q20 Create DynamoDB Table Using CloudFormation Using Terraform

**Level 3**
# Q1 Managing Scalable NoSQL Databases with Amazon DynamoDB Using Terraform
# Q2 Building a Real-Time Data Ingestion Pipeline with Kinesis Firehose Using Terraform
# Q3 Enforcing IAM Naming Standards and Permissions Using Terraform
# Q4 Streaming Secure Data with Kinesis, STS, and S3 Integration Using Terraform
# Q5 Implementing Encryption at Rest with AWS KMS Using Terraform
# Q6 Deploying a Multi-Tier Architecture on AWS Using Terraform
# Q7 Managing Multiple S3 Buckets with Fine-Grained Access Policies Using Terraform
# Q8 Hosting a Static Website on Amazon S3 with Custom Configuration Using Terraform
# Q9 Storing and Accessing Sensitive Data Securely with AWS Secrets Manager Using Terraform
# Q10 Managing Terraform Workspaces for Environment Isolation Using Terraform

**Level 4**