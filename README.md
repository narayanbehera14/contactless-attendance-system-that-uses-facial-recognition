# 🚀 Contactless Attendance System using AWS Face Recognition

A cloud-native, serverless attendance system that uses **Amazon Rekognition** to recognize employees and automatically mark attendance without any physical contact.

The application captures an employee's face through a web camera, uploads the image to Amazon S3, triggers AWS Lambda for face recognition, stores attendance in DynamoDB, and displays attendance status in real time.

---

## 🌐 Live Demo

**Frontend (AWS Amplify)**

https://main.d3qytyd1a704f3.amplifyapp.com/

---

## ✨ Features

- 📷 Contactless face-based attendance
- ☁️ Fully Serverless Architecture
- ⚡ Real-time attendance marking
- 🔍 Face recognition using Amazon Rekognition
- 📝 Automatic Clock-In & Clock-Out
- 👤 Detects Unknown Person
- 🚫 Detects No Face Found
- 📊 Attendance history dashboard
- 🌍 Hosted on AWS Amplify
- 🔒 Secure pre-signed S3 image uploads

---

# 🛠 Tech Stack

### Frontend

- React.js
- Axios
- React Webcam

### Backend

- AWS Lambda
- Amazon API Gateway
- Amazon S3
- Amazon Rekognition
- Amazon DynamoDB

### DevOps / Cloud

- AWS Amplify
- IAM
- CloudWatch
- GitHub

---

# 🏗 Architecture

```
                React Frontend
                      │
                      │
          Capture Face using Webcam
                      │
                      ▼
        API Gateway (/upload-url)
                      │
                      ▼
        Lambda (Generate Upload URL)
                      │
                      ▼
           Upload Image to Amazon S3
                      │
          S3 Object Created Event
                      │
                      ▼
      Lambda (Recognize Employee)
                      │
      Amazon Rekognition Search Face
                      │
          ┌───────────┴────────────┐
          │                        │
      Employee Found         Unknown/No Face
          │                        │
          ▼                        ▼
   Update Attendance        Store Recognition Result
          │                        │
          └───────────┬────────────┘
                      ▼
             DynamoDB Tables
                      │
                      ▼
        API Gateway (/attendance-result)
                      │
                      ▼
            React Frontend Result
```

---

# 📂 Project Structure

```
attendance-project/

├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── lambda/
│   ├── generate_upload_url/
│   ├── recognize_employee/
│   ├── register_employee_face/
│   ├── get_all_attendance/
│   └── get_attendance_result/
│
├── iam/
├── README.md
```

---

# AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon API Gateway
- Amazon Rekognition
- Amazon DynamoDB
- AWS Amplify
- AWS IAM
- Amazon CloudWatch

---

# DynamoDB Tables

## Employees

| Partition Key |
|--------------|
| employee_id |

Stores employee details.

---

## Attendance

| Partition Key | Sort Key |
|--------------|----------|
| employee_id | date |

Stores attendance records.

---

## RecognitionResults

| Partition Key |
|--------------|
| image_key |

Stores latest recognition result.

---

# Attendance Flow

### 1. Capture Face

The React application captures a webcam image.

↓

### 2. Upload Image

Frontend requests a pre-signed S3 URL.

↓

### 3. Store Image

Image uploads directly to Amazon S3.

↓

### 4. Trigger Lambda

S3 ObjectCreated event invokes Lambda.

↓

### 5. Face Recognition

Amazon Rekognition searches the employee collection.

↓

### 6. Attendance Processing

If matched:

- Clock In
- Clock Out
- Already Clocked Out

Otherwise:

- Unknown Person
- No Face Detected

↓

### 7. Save Result

Recognition result is stored inside DynamoDB.

↓

### 8. Frontend Displays Result

Frontend polls the result and shows attendance status.

---

# Supported Recognition Results

✅ Clock In Successful

✅ Clock Out Successful

✅ Already Clocked Out Today

❌ Unknown Person

❌ No Face Detected

---

# API Endpoints

## Generate Upload URL

```
POST /upload-url
```

Returns a pre-signed S3 upload URL.

---

## Attendance Result

```
GET /attendance-result?key=<image_key>
```

Returns recognition result.

---

## Attendance History

```
GET /attendance/all
```

Returns all attendance records.

---

# Screenshots

Add screenshots here.

```
screenshots/

Home.png

Attendance.png

Recognition.png

Dashboard.png
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/narayanbehera14/contactless-attendance-system-that-uses-facial-recognition.git
```

Go to project

```bash
cd contactless-attendance-system-that-uses-facial-recognition
```

Install frontend

```bash
cd frontend

npm install
```

Run

```bash
npm run dev
```

---

# Deployment

Frontend

- AWS Amplify

Backend

- AWS Lambda
- Amazon API Gateway
- Amazon S3
- DynamoDB
- Rekognition

---

# Future Improvements

- Employee Registration UI
- Admin Authentication
- JWT Authentication
- Live Attendance Dashboard
- Email Notifications
- Multi-Office Support
- Attendance Reports (PDF/Excel)
- Analytics Dashboard

---

# Author

**Narayan Behera**

MCA Student | Cloud & DevOps Enthusiast

- GitHub: https://github.com/narayanbehera14
- LinkedIn: https://www.linkedin.com/in/narayanbehera

---

# License

This project is licensed under the MIT License.
````

This README follows the structure commonly used in professional open-source projects and clearly documents your serverless AWS architecture and live demo. ([github.com][1])

[1]: https://github.com/Mina329/attendo?utm_source=chatgpt.com "GitHub - Mina329/attendo: Attendo (Attendance Management System based on face recognition - Graduation Project) · GitHub"
