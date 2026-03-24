#  Student Performance Predictor & Personalized Academic Advisor  
### *(Mainly for VIT Bhopal Students,trained on there data !)*

---

##  Overview

This project is a **Machine Learning-based system** designed to help students at **VIT Bhopal** analyze and improve their academic performance.

It predicts student marks based on key academic factors and provides:
-  GPA estimation  
-  Personalized improvement suggestions  

---

##  Problem Statement

Students often struggle to understand:

- How daily habits impact academic performance  
- Reasons behind low GPA  
- What actions to take for improvement  

This leads to:
- Poor academic planning  
- Low GPA  
- Increased stress  

---

##  Solution

This system solves the problem by:

-  Predicting marks using Machine Learning  
-  Converting marks into GPA (VIT grading system)  
-  Generating personalized suggestions  
-  Helping students make smarter academic decisions  

---

##  Features

-  Marks prediction using ML model  
-  GPA calculation (VIT system)  
-  Personalized suggestions engine  
-  Interactive UI with Streamlit  
-  Real-time predictions  

---

##  How It Works

1. User inputs:
   - Study Hours  
   - Attendance (%)  
   - Assignment Score  
   - Previous GPA  

2. Model predicts marks  

3. System converts marks → Grade → GPA  

4. Personalized suggestions are generated  

---

##  Tech Stack

- **Python**  
- **Pandas & NumPy**  
- **Scikit-learn**  
- **Streamlit**  

---

##  Project Structure

```
Student-Performance-Predictor/
│
├── data/
│   └── student_data.csv
│
├── model/
│   └── model.pkl
│
├── app.py
├── train_model.py
├── utils.py
├── requirements.txt
└── README.md
```

---

##  How to Run

###  Clone Repository
```bash
git clone https://github.com/your-username/Student-Performance-Predictor.git
cd Student-Performance-Predictor
```

###  Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

###  Install Dependencies
```bash
pip install -r requirements.txt
```

###  Train Model
```bash
python train_model.py
```

###  Run App
```bash
streamlit run app.py
```

---

##  Inputs

- Study Hours per Day  
- Attendance (%)  
- Assignment Score  
- Previous GPA  

---

##  Outputs

- Predicted Marks  
- Grade (S, A, B, C, D, F)  
- Estimated GPA  
- Personalized Suggestions  

---

##  VIT Grading System

| Marks | Grade | GPA |
|------|------|-----|
| 90+  | S    | 10  |
| 80–89 | A   | 9   |
| 70–79 | B   | 8   |
| 60–69 | C   | 7   |
| 50–59 | D   | 6   |
| <50  | F    | 0   |

---

##  Suggestion Logic

- Low Attendance → Maintain above 75%  
- Low Study Hours → Study 2–3 hours daily  
- Low Assignment Score → Improve assignment quality  
- Low Marks → Revise concepts consistently  

---

##  Example Output

```
Predicted Marks: 78  
Grade: B  
GPA: 8  

Suggestions:
- Increase study hours  
- Improve assignments  
- Maintain attendance  
```

---

##  Machine Learning Model

- **Model Used:** Linear Regression  

### Why Linear Regression?
- Simple and interpretable  
- Efficient for small datasets  
- Suitable for continuous prediction (marks)  

---

##  Learning Outcomes

- Built end-to-end ML pipeline  
- Learned model training & evaluation  
- Integrated ML with UI (Streamlit)  
- Solved real-world academic problem  
- Practiced GitHub project structuring  

---

##  Challenges Faced

- Creating realistic dataset  
- Integrating model with UI  
- Designing meaningful suggestions  

---

##  Future Scope

- Use real-world student dataset  
- Add subject-wise predictions  
- Deploy as web app  
- Use advanced ML models  

---

## Author

**Divyansh**  
CSE Core Student  
VIT Bhopal  

---

##  Conclusion

This project shows how Machine Learning can be used to **predict performance, provide insights, and guide students** toward better academic outcomes in a simple, practical way.
