# 🎓 Student Performance Prediction Pipeline

An end-to-end Machine Learning pipeline project that predicts student academic performance using educational and demographic data.

This project demonstrates:
- Data preprocessing
- Feature engineering
- Machine Learning model training
- Model evaluation
- Automated testing
- CI/CD pipeline automation using GitHub Actions and Jenkins

---

# 🚀 Project Overview

The objective of this project is to build a scalable and automated Machine Learning pipeline capable of predicting student math performance based on multiple educational and demographic factors.

The project focuses on implementing industry-oriented ML development workflows by combining:
- Machine Learning
- Automation
- Testing
- CI/CD Integration

This repository showcases practical implementation of production-style Machine Learning pipelines.

---

# ✨ Features

- 📊 Student performance prediction using Machine Learning
- 🧹 Data preprocessing and categorical feature encoding
- 🤖 Random Forest Regression model training
- 📈 Model evaluation using R² Score
- 💾 Model saving using Joblib
- ✅ Automated testing using Pytest
- ⚙️ CI/CD automation using GitHub Actions
- 🔄 Jenkins pipeline integration
- 📁 Structured project architecture

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Pytest
- GitHub Actions
- Jenkins

---

# 📂 Project Structure

```text
student-performance-pipeline/
│
├── data/
│   └── student_data.csv
│
├── src/
│   ├── train.py
│   └── test_model.py
│
├── .github/
│   └── workflows/
│       └── ml-pipeline.yml
│
├── Jenkinsfile
├── requirements.txt
└── README.md
```

---

# 🔍 Machine Learning Workflow

The project follows a complete ML pipeline workflow:

### 1. Data Loading
- Reads the dataset using Pandas.

### 2. Data Preprocessing
- Handles categorical variables using One-Hot Encoding.
- Separates features and target variable.

### 3. Train-Test Split
- Splits dataset into training and testing datasets.

### 4. Model Training
- Uses Random Forest Regressor from Scikit-learn.

### 5. Model Evaluation
- Evaluates model performance using R² Score.

### 6. Model Saving
- Stores trained model using Joblib.

### 7. Automated Testing
- Executes test cases using Pytest.

### 8. CI/CD Execution
- Automates workflow using GitHub Actions and Jenkins.

---

# 🤖 Model Used

## Random Forest Regressor

The project uses the **Random Forest Regressor** algorithm to predict student math scores based on input features.

### Why Random Forest?
- Handles complex relationships effectively
- Reduces overfitting
- Provides stable prediction performance
- Works well with structured datasets

---

# 📈 Evaluation Metric

The model performance is evaluated using:

## R² Score

R² Score measures how well the model explains variation in the target variable.

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/sidhi02/student-performance-pipeline.git
cd student-performance-pipeline
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Execute the training pipeline:

```bash
python src/train.py
```

---

# 🧪 Run Tests

```bash
python -m pytest src/test_model.py -v
```

---

# 🔄 CI/CD Pipeline

## GitHub Actions

The project includes an automated GitHub Actions workflow that runs on every push to the repository.

### Workflow Tasks
- Checkout Repository
- Setup Python Environment
- Install Dependencies
- Execute Tests
- Train ML Model

---

## Jenkins Pipeline

The repository also includes a Jenkins pipeline configuration.

### Jenkins Stages
- Code Checkout
- Dependency Installation
- Automated Testing
- Model Training

---

# 📚 Key Learnings

Through this project, the following concepts were implemented:

- End-to-end Machine Learning pipeline development
- Data preprocessing and feature engineering
- Regression model training and evaluation
- Model persistence using Joblib
- Automated testing using Pytest
- CI/CD workflow automation
- GitHub Actions integration
- Jenkins pipeline implementation

---

# 💡 Future Improvements

- Add Streamlit deployment interface
- Implement hyperparameter tuning
- Add Docker containerization
- Deploy model using cloud services
- Add model monitoring and logging

---

# 👩‍💻 Author

## Sidhi Deshmukh

Aspiring Data Analyst & Data Science Enthusiast passionate about:
- Machine Learning
- Business Intelligence
- Data Visualization
- Analytics Applications

---
