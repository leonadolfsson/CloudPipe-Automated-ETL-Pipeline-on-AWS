# 🌐 CloudPipe: Automated ETL Pipeline on AWS

## 🚀 Project Overview

CloudPipe is a fully automated ETL (Extract, Transform, Load) pipeline built on AWS. It leverages S3, Lambda, Glue, Athena, EventBridge, and SNS to automate data ingestion, transformation, and storage, providing query-ready data, monitoring, and notifications.

This project demonstrates how to build a serverless, event-driven data pipeline, ideal for beginners exploring cloud ETL solutions or real-world data workflows.

---

## 🏗 Architecture & Flow

Here’s how the pipeline works step by step:

![CloudPipe ETL Pipeline](flowchart (2).png)

---

## ✨ Features

✅ Automated Data Ingestion: Upload raw data to S3 → Lambda triggers Glue ETL job.

✅ Serverless ETL: Glue handles transformations, aggregations, and schema adjustments.

✅ Query-Ready Output: Cleaned data stored in S3 Load folder for Athena queries.

✅ Event-Driven Notifications: SNS sends email alerts on job success/failure.

✅ Monitoring: EventBridge monitors Glue jobs and integrates with CloudWatch logs.

### IAM Roles Used:

- AmazonS3FullAccess

- AWSGlueConsoleFullAccess

- AWSLambdaBasicExecutionRole-16bd2fd9-dce5-455f-a28e-6727ebe454af

---

## 📝 Step-by-Step Implementation

### 1️⃣ S3 Setup

- Created two buckets/folders:

- Extract: Upload raw data (e.g., Titanic dataset)

- Load: Stores transformed and aggregated data

### 2️⃣ Lambda Function

- Triggered automatically on new file uploads to Extract.

- Initiates the AWS Glue ETL job.

- Code deployed and tested successfully.

### 3️⃣ AWS Glue ETL Job

- Drops unnecessary fields

- Aggregates data using GROUP BY passenger ID

- Converts passenger ID from string → integer

- Counts number of passengers per aggregation

- Saves processed data in Load folder on S3

### 4️⃣ Validation Using Athena

- Run SQL queries to ensure:

- Duplicates removed

- Aggregations and schema changes are correct

### 5️⃣ SNS Notifications

- Created SNS Topic: s3-glue-s3-notif

- Added email subscription → Notifies on ETL job success/failure

### 6️⃣ EventBridge & CloudWatch Monitoring

- EventBridge monitors Glue job completion

- Triggers SNS notifications on success/failure

- CloudWatch logs track pipeline execution

  ---

## 📸 Screenshots

Add screenshots to showcase your project visually:

S3 Buckets (Extract & Load)

Lambda Function Configuration

Glue ETL Job & Transformations

Athena Queries

SNS Notifications

EventBridge & CloudWatch Logs

---

## 💡 Key Learnings

- Understanding serverless ETL pipelines on AWS

- Event-driven architecture using Lambda + EventBridge + SNS

- Hands-on experience with AWS Glue transformations and schema changes

- Querying and validating ETL data using Athena

- Managing IAM roles and permissions for secure access

  ---

## 📌 Conclusion

This project demonstrates a complete end-to-end AWS ETL pipeline that is:

- Fully automated & serverless

- Event-driven & monitored

- Scalable & cost-efficient

- Perfect for data engineering beginners and practical implementation in cloud data workflows.


## 🛡 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 👩‍💻 Author

Sakshi Khandagale

Email: sakshiik95@gmail.com

