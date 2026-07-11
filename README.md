# 🚀 Contactless Attendance System using facial recognition

![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![React](https://img.shields.io/badge/React-18-blue)
![Python](https://img.shields.io/badge/Python-3.12-yellow)
![Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![DynamoDB](https://img.shields.io/badge/Amazon-DynamoDB-blue)
![S3](https://img.shields.io/badge/Amazon-S3-green)
![API Gateway](https://img.shields.io/badge/API-Gateway-red)
![License](https://img.shields.io/badge/License-MIT-green)

A **serverless Contactless Attendance System** built using **AWS Rekognition, AWS Lambda, Amazon S3, DynamoDB, API Gateway, and React.js**.

Employees simply capture their face using a webcam. The image is uploaded securely to Amazon S3 using a pre-signed URL. Amazon Rekognition identifies the employee, and attendance is automatically marked in DynamoDB. An Admin Dashboard displays all attendance records in real time.

---

# 📌 Features

- ✅ Face Recognition Attendance
- ✅ Contactless Clock In / Clock Out
- ✅ Employee Registration
- ✅ Automatic Attendance Logging
- ✅ Admin Dashboard
- ✅ REST APIs using API Gateway
- ✅ Serverless AWS Architecture
- ✅ React Frontend
- ✅ Secure Image Upload using Pre-Signed URLs
- ✅ Real-time Attendance Records
- ✅ Built completely using AWS CLI

---

# 🏗 System Architecture

```
                     React Frontend
              (Camera + Admin Dashboard)
                         │
                         │ HTTP
                         ▼
                  Amazon API Gateway
                         │
     ┌───────────────────┼────────────────────┐
     │                   │                    │
     ▼                   ▼                    ▼
Generate Upload     Get Attendance     Get All Attendance
URL Lambda            Lambda              Lambda
     │                   │                    │
     ▼                   ▼                    ▼
 Amazon S3          DynamoDB           DynamoDB
     │
     │ S3 Event Trigger
     ▼
Recognize Employee Lambda
     │
     ▼
Amazon Rekognition
     │
     ▼
Employees Table
     │
     ▼
Attendance Table
```

---

# 🔄 Project Workflow

### Step 1

User opens the React application.

↓

### Step 2

The webcam opens automatically.

↓

### Step 3

User clicks **Capture Face**.

↓

### Step 4

React requests a **Pre-Signed Upload URL** from API Gateway.

↓

### Step 5

GenerateUploadURL Lambda returns a secure upload URL.

↓

### Step 6

The captured image is uploaded directly to Amazon S3.

↓

### Step 7

Amazon S3 triggers the **recognizeEmployee** Lambda.

↓

### Step 8

Lambda sends the image to Amazon Rekognition.

↓

### Step 9

Rekognition identifies the employee.

↓

### Step 10

Employee details are fetched from the Employees DynamoDB table.

↓

### Step 11

Attendance is updated:

- First scan → Clock In
- Second scan → Clock Out

↓

### Step 12

Frontend requests attendance status.

↓

### Step 13

Attendance details are displayed.

↓

### Step 14

Admin Dashboard shows all attendance records.

---

# ☁️ AWS Services Used

| AWS Service | Purpose |
|-------------|---------|
| Amazon Rekognition | Facial Recognition |
| AWS Lambda | Backend Logic |
| Amazon S3 | Image Storage |
| Amazon DynamoDB | Employee & Attendance Database |
| Amazon API Gateway | REST APIs |
| AWS IAM | Roles & Permissions |
| Amazon CloudWatch | Logs & Monitoring |
| AWS CLI | Infrastructure Management |

---

# 💻 Tech Stack

## Frontend

- React.js
- Vite
- Axios
- React Webcam

## Backend

- Python 3.12
- Boto3

## Cloud

- AWS Lambda
- Amazon S3
- Amazon Rekognition
- Amazon DynamoDB
- API Gateway
- IAM
- CloudWatch

---

# 📂 Project Structure

```
attendance-project/

│
├── frontend/
│   ├── src/
│   │
│   ├── components/
│   │      Camera.jsx
│   │
│   ├── pages/
│   │      AdminDashboard.jsx
│   │
│   ├── services/
│   │      api.js
│   │
│   ├── App.jsx
│   └── main.jsx
│
├── lambda/
│
│   ├── generate_upload_url/
│   │      lambda_function.py
│
│   ├── register_employee/
│   │      lambda_function.py
│
│   ├── recognize_employee/
│   │      lambda_function.py
│
│   ├── get_attendance_result/
│   │      lambda_function.py
│
│   └── get_all_attendance/
│          lambda_function.py
│
├── screenshots/
│
├── architecture/
│
└── README.md
```

---

# 🗄 Database Design

## Employees Table

| Attribute | Description |
|------------|-------------|
| employee_id | Employee ID (Partition Key) |
| name | Employee Name |
| department | Department |

Example

```
employee_id : 101
name : Narayan Behera
department : IT
```

---

## Attendance Table

| Attribute | Description |
|------------|-------------|
| employee_id | Partition Key |
| date | Sort Key |
| clock_in | Clock In Time |
| clock_out | Clock Out Time |
| status | Present |

Example

```
employee_id : 101
date : 2026-07-11
clock_in : 09:05:10
clock_out : 18:20:11
status : Present
```

---

# 🌐 API Endpoints

## Generate Upload URL

```
POST /upload-url
```

Returns

```json
{
  "uploadUrl": "...",
  "key": "employee.jpg"
}
```

---

## Get Attendance

```
GET /attendance
```

Returns

```json
{
  "employee_id":"101",
  "clock_in":"09:10",
  "clock_out":"",
  "status":"Present"
}
```

---

## Get All Attendance

```
GET /attendance/all
```

Returns

```json
[
  {
    "employee_id":"101",
    "date":"2026-07-11",
    "clock_in":"09:10",
    "clock_out":"18:00",
    "status":"Present"
  }
]
```

---

# 📸 Screenshots

## Employee Panel

> Add your screenshot here

```
screenshots/employee-panel.png
```

---

## Face Recognition

> Add your screenshot here

```
screenshots/capture-face.png
```

---

## Admin Dashboard

> Add your screenshot here

```
screenshots/admin-dashboard.png
```

---

## AWS Architecture

> Add your architecture diagram

```
architecture/aws-architecture.png
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/narayanbehera14/contactless-attendance-system-that-uses-facial-recognition.git
```

```
cd contactless-attendance-system-that-uses-facial-recognition
```

---

## Install Frontend

```bash
cd frontend
npm install
```

---

## Run Frontend

```bash
npm run dev
```

Application runs at

```
http://localhost:5173
```

---

# ☁️ AWS Setup

Create the following AWS resources:

- Amazon S3 Bucket
- Rekognition Collection
- Employees DynamoDB Table
- Attendance DynamoDB Table
- API Gateway
- IAM Roles
- Lambda Functions

Deploy the following Lambda functions:

- generateUploadURL
- registerEmployeeFace
- recognizeEmployee
- getAttendanceResult
- getAllAttendance

---

# 🔐 IAM Permissions

The Lambda execution roles require permissions for:

- Amazon S3
- Amazon Rekognition
- Amazon DynamoDB
- CloudWatch Logs

---

# 🚀 Future Improvements

- Admin Login Authentication
- Employee Login
- Attendance Analytics Dashboard
- Monthly Reports
- Excel Export
- PDF Report Generation
- Email Notifications
- Leave Management System
- QR Code Attendance
- Multi-Camera Support
- CI/CD using GitHub Actions
- Docker Deployment
- Terraform Infrastructure as Code

---

# 📚 Learning Outcomes

This project helped me gain hands-on experience with:

- Serverless Computing
- AWS Lambda Development
- Amazon Rekognition
- API Gateway
- DynamoDB Design
- Event-Driven Architecture
- IAM Roles & Policies
- Amazon S3
- React.js Integration
- AWS CLI
- Cloud-Based Application Development

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Narayan Behera

**MCA Student | AWS Cloud | DevOps | Full Stack Developer**

### GitHub

https://github.com/narayanbehera14

### LinkedIn

https://www.linkedin.com/in/your-linkedin-profile

---

## 🙏 Acknowledgements

- Amazon Web Services (AWS)
- React.js
- Vite
- Axios
- Boto3
- Open Source Community
