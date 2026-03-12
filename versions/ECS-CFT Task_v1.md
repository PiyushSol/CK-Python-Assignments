🚀 Three-Tier Application Deployment on AWS ECS (EC2 Launch Type) using CloudFormation
📌 Project Overview

This project demonstrates a production-style 3-tier web application architecture deployed on Amazon ECS (EC2 Launch Type) using Infrastructure as Code (AWS CloudFormation).

The application consists of:

Web Tier (Frontend) – React application

App Tier (Backend) – Node.js + Express API

Database Tier – Amazon RDS (MySQL)

Load Balancer – Application Load Balancer (ALB)

Container Registry – Amazon ECR

Compute – ECS Cluster using EC2 instances (Self-managed)

All infrastructure components were created using CloudFormation templates.

🏗 Architecture Diagram
Internet
   ↓
Application Load Balancer (Public Subnets)
   ├── /        → Web Tier (React - Port 80)
   └── /api/*   → App Tier (Node.js - Port 4000)
                      ↓
                      RDS MySQL (Private Subnets)
🧱 Infrastructure Components
✅ Networking

Custom VPC

2 Public Subnets (for ALB)

2 Private Subnets (for ECS + RDS)

Internet Gateway

Route Tables

Security Groups with restricted access

✅ ECS Cluster (EC2 Launch Type)

Self-managed EC2 instances

Auto Scaling Group

Launch Template

IAM Role for ECS instances

Docker installed

ECS agent running

✅ Container Registry (ECR)

Backend repository

Frontend repository

Docker images pushed manually from build server EC2

✅ Load Balancer

Internet-facing Application Load Balancer

Listener on port 80

Target Group (Web Tier – Port 80)

Target Group (App Tier – Port 4000)

Path-based routing:

/ → Web Tier

/api/* → App Tier

✅ Database

Amazon RDS MySQL

Private Subnets

Not publicly accessible

Security group allowing access only from ECS instances

🛠 Deployment Flow
1️⃣ Build & Push Docker Images
Backend
docker build -t three-tier-backend:v1 .
docker tag three-tier-backend:v1 <account-id>.dkr.ecr.us-east-1.amazonaws.com/three-tier-backend:v1
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/three-tier-backend:v1
Frontend
docker build -t three-tier-frontend:v1 .
docker tag three-tier-frontend:v1 <account-id>.dkr.ecr.us-east-1.amazonaws.com/three-tier-frontend:v1
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/three-tier-frontend:v1
2️⃣ Create Task Definitions

Web Tier Task Definition

App Tier Task Definition

3️⃣ Create ECS Services

Web Tier Service attached to web target group

App Tier Service attached to app target group

4️⃣ Configure ALB Routing
Path Pattern	Target Group
/	Web Tier
/api/*	App Tier
🐞 Major Issues Faced & How We Solved Them

This project involved deep debugging across networking, containers, ECS, ALB, and database layers.

❌ Issue 1: ECS Instances Not Registering to Cluster

Cause: Incorrect AMI (ARM vs x86 mismatch)
Fix: Used ECS-Optimized AMI for correct architecture.

❌ Issue 2: IAM PassRole Error

Cause: Service-linked role misuse
Fix: Used proper IAM Role attached via Instance Profile.

❌ Issue 3: Docker Permission Denied

Cause: User not part of docker group
Fix:

sudo usermod -aG docker ec2-user
❌ Issue 4: ALB Target Unhealthy

Cause: Dynamic port mapping requires allowing ephemeral ports
Fix: Security Group update:

Allowed 1024-65535 from ALB SG to ECS SG

❌ Issue 5: 502 Bad Gateway

This was the most critical debugging stage.

Root Causes Encountered:
1️⃣ Backend Listening on localhost
app.listen(4000, 'localhost') ❌

Fix:

app.listen(4000, '0.0.0.0') ✅

Containers must bind to 0.0.0.0.

2️⃣ ALB Routing Mismatch

Frontend was calling:

/transaction

But ALB rule expected:

/api/*

Fix:

Updated frontend API calls to:

/api/transaction

And updated backend routes accordingly.

3️⃣ RDS Security Group Blocking Access

Even though RDS was reachable via DNS, connection was hanging.

Fix:

Added inbound rule on RDS SG:

MySQL (3306)

Source: ECS Instance Security Group

4️⃣ Database Schema Mismatch

Backend error:

ER_BAD_FIELD_ERROR: Unknown column 'description'

Root cause:

Table had column desc but backend expected description.

Fix:

CREATE TABLE transactions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  amount VARCHAR(100),
  description VARCHAR(255)
);
❌ Issue 6: ECS Using Old Docker Image

ECS does NOT auto-update images tagged latest.

Fix:

Created new task definition revision

Forced new deployment

Verified running container via:

docker ps
docker logs <container-id>
🔍 Deep Debugging Techniques Used

docker logs

docker ps

nc <rds-endpoint> 3306

telnet

ALB target health inspection

CloudFormation stack status analysis

Security group tracing

Path-based routing validation

Curl testing against mapped host ports

🎓 Key Learnings

502 errors usually mean backend crash or invalid response.

Healthy target group ≠ working application.

Containers must bind to 0.0.0.0.

ALB routing must match frontend API paths.

ECS does not auto-pull new latest images.

Database schema mismatches can crash Node apps.

Security Groups are stateful firewalls inside VPC.

Versioning Docker images is best practice.

🛡 Security Considerations

RDS is private (not publicly accessible)

App Tier runs in private subnets

Only ALB is public

Database accessible only from ECS instances

No hardcoded public DB access

📂 Repository Structure
/cloudformation
   ├── vpc.yaml
   ├── alb.yaml
   ├── app-target-group.yaml
   ├── appservice.yaml
   ├── webservice.yaml
   └── ecs-cluster.yaml

/application-code
   ├── web-tier/
   └── app-tier/
🚀 Final Result

The application now:

Loads frontend via ALB

Routes /api/* to backend

Backend connects to RDS

CRUD operations work successfully

Fully private database layer

Production-style architecture achieved

📌 Future Improvements

Switch to awsvpc network mode

Add HTTPS with ACM

Add Auto Scaling policies

Store DB credentials in Secrets Manager

Add CloudWatch structured logging

Implement CI/CD pipeline

🏁 Conclusion

This project demonstrates:

Real-world 3-tier architecture

Infrastructure as Code

ECS EC2 launch type mastery

Advanced debugging across multiple AWS services

Production-grade networking and routing setup

This is not a tutorial deployment — it is a fully engineered cloud system.

👨‍💻 Author

Built and debugged end-to-end using AWS ECS, ALB, RDS, ECR, and CloudFormation.