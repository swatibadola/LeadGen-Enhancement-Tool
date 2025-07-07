# LeadGen - Enhancement - Tool
This repository contains a Streamlit-based web app that helps you process, clean, score, and export leads for CRM integration.<br>

It was developed as part of an assignment project to demonstrate practical data processing, validation, and user interface design.

## 🚀 Features
✅ Upload leads data as CSV <br>
✅ Remove duplicate companies <br>
✅ Validate email addresses <br>
✅ Calculate customizable lead scores <br>
✅ Preview intermediate and final processed leads <br>
✅ Generate CRM-ready CSV file <br>
✅ Friendly UI with error handling<br>


## 📂 Repository Contents
app.py — Main Streamlit application file <br>
features/ — Contains modular feature scripts:<br>
• deduplication.py<br>
• email_validation.py<br>
• lead_scoring.py<br>
• crm_export.py<br>

utils/ — Contains helper functions:<br>
• helpers.py<br>

sample_data.csv — Sample dataset to test the app<br>
.gitignore — Ignores Python cache and temporary files<br>
README.md — Setup guide and project overview

## 📸 Screenshots
Below are some screenshots of the LeadGen Prototype Tool in action:

### 🏠 Home Page
![alt text](<WhatsApp Image 2025-07-07 at 20.35.20_7e8ee3ef.jpg>)

### 📂 Upload Leads CSV
![alt text](<WhatsApp Image 2025-07-07 at 20.35.18_e5b37640.jpg>)

### ⚙️ Processing Steps Selection
![alt text](<WhatsApp Image 2025-07-07 at 20.35.19_edb12537.jpg>)

### 📊 Processed Leads Preview
![alt text](<WhatsApp Image 2025-07-07 at 20.35.20_645ec2e6.jpg>)

### 📤 CRM-Ready CSV Export
![alt text](<WhatsApp Image 2025-07-07 at 20.35.19_17287c44.jpg>)

## 🛠️ Setup Instructions
### 1️⃣ Clone the repository
>git clone https://github.com/yourusername/leadgen-prototype-tool.git<br>
cd leadgen-prototype-tool

### 2️⃣ Create a virtual environment (recommended)
>python -m venv venv<br>
>source venv/bin/activate   FOR  (macOS/Linux) <br>
>env\Scripts\activate     FOR  (Windows) <br>

### 3️⃣ Install dependencies
>pip install -r requirements.txt

### 4️⃣ Run the Streamlit app
>streamlit run app.py


## 📦 Dataset
A sample dataset (sample_data.csv) is included in the repository to demonstrate the app’s features.<br>
✅ Note: If you plan to upload your own leads file, ensure it includes required columns like Company and Company Email.

## 📝 CRM Export
The app supports generating a CRM-ready CSV matching standard CRM schemas (e.g., HubSpot/Pipedrive).<br>
You can download the processed leads in a format suitable for CRM import.

## ⚠️ Known Limitations
Large files (10k+ leads) may slow down processing in Streamlit.<br>

Uploaded data must contain key columns like 'Company' and 'Company Email'.<br>

Email validation uses regex only; it doesn't verify if email addresses exist.

## 🙌 Acknowledgements
This tool was created as part of an assignment.
Feel free to reuse, improve, or customize it.

## 📩 Connect with Me
🔗 [LinkedIn](https://www.linkedin.com/in/swati-badola-b28a2722a/)

#### Happy Coding!