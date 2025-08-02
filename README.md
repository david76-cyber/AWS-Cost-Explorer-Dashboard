# 💸 AWS Cost Explorer Dashboard

A Flask-based web app that integrates with the **AWS Cost Explorer API** to help users track and visualize their AWS cloud spending. It supports custom date ranges, filters by service, and displays data in a user-friendly tabular format.

---

## 🚀 Features

- 🔍 Retrieve detailed AWS cost data by service and custom date range
- 📅 Filter usage by **start** and **end** dates with daily granularity
- 📊 Group costs by **AWS service dimension**
- 📋 Clean tabular display of results with **total cost summary**
- 💡 Error handling with informative messages on API failures
- 🌐 Simple and intuitive browser interface

---

## ⚙️ Tech Stack

| Component     | Tech Used                        |
|---------------|----------------------------------|
| Backend       | Python, Flask                    |
| Cloud Hosting | AWS EC2 (Ubuntu)                 |
| API           | AWS Cost Explorer (via Boto3)    |
| Auth          | IAM Role with scoped permissions |
| UI            | HTML, Bootstrap (optional)       |

---

## 🧰 Prerequisites

Before running the app, make sure you have:

- ✅ AWS Account with **Cost Explorer** enabled
- ✅ IAM user or role with `ce:GetCostAndUsage` permission
- ✅ Python 3.x and `pip` installed
- ✅ AWS credentials configured locally at `~/.aws/credentials`  
  *(or use environment variables if deploying to EC2)*

---

## 🛠️ Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/yourusername/aws-cost-explorer-dashboard.git
cd aws-cost-explorer-dashboard
2. Install Dependencies
