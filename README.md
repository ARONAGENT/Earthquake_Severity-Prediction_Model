## 🌋 Earthquake Severity Prediction Model - Nepal (Django Project)

### 🔢 Project Title
**Earthquake Severity Prediction Web App Using Django & Simple Linear Regression**

---

### 🗂️ Overview
This project integrates a machine learning model into a Django web application to predict the **severity (magnitude)** of earthquakes in Nepal. It combines backend development with data science, providing a user-friendly interface for users to interact with the prediction model.

---

### 🧠 Problem Statement
Nepal lies in a seismically active zone, making earthquake prediction a critical challenge. This project uses historical data to estimate earthquake severity and visualize risk-prone areas.

---

### 📊 Dataset & Analysis
The dataset includes historical earthquake records from Nepal with the following fields:
- **Date**
- **Time**
- **Latitude**
- **Longitude**
- **Depth (km)**
- **Magnitude**
  and so on......

#### Analysis Highlights (in Jupyter Notebook)
- Cleaned data and removed nulls
- Explored distributions and correlations
- Visualized trends and outliers

📁 The notebook used for this analysis is available as: `nepal_earthquake.ipynb`

---

### 📈 Visualizations
- Correlation heatmaps
- Regression line between depth and magnitude
- Earthquake frequency trends
- Box plots

🖼️ **1 sample image visualization included in the repo.**
![image](https://github.com/user-attachments/assets/0853708c-5ecb-4d75-8710-9ba1d9d24f25)


---

### 🛠️ Model Development
- **Model**: Simple Linear Regression (from Scikit-learn)
- **Target Variable**: Serverity Normalized
- **Input Feature**: hazard, exposure, housing, poverty, vulnerability

#### Training Steps:
1. Preprocessing data
2. Splitting into train/test
3. Training the Linear Regression model
4. Evaluating with MAE, MSE, and R² Score

---

### 🌐 Web Application Features
This Django app includes:
- **User-friendly interface**
- **Input form** to provide depth value for prediction
- **Output result** showing predicted earthquake severity
- **Top 10 high-risk zones** displayed with earthquake severity data

#### 🔍 Pages/Screenshots:
1. **Homepage Interface**  
![1](https://github.com/user-attachments/assets/e1b3d5d6-b898-46d3-a13a-8e9de1a9131d)


2. **Top 10 Risk Areas View**  
![2](https://github.com/user-attachments/assets/000e4bb2-0635-4611-a7c6-b6a596c2e55c)


3. **Prediction Form Page**  
![3](https://github.com/user-attachments/assets/3ae09f35-72ba-48ae-a9b5-0c0a6bd83a39)


4. **Severity Result Display**  

📸 All screenshots are available in the `/prediction model earthquake/
/` directory.
<br>

![4](https://github.com/user-attachments/assets/a7f90bd8-9662-43ba-99a6-27854200118f)

---

### ⚖️ Limitations
- Uses only depth for prediction
- Linear model assumes simple relationships, limiting accuracy
- Cannot predict earthquake occurrence, only estimated Severity Normalized

---

### 🚀 Future Enhancements
- Add more seismic features (region, tectonic plate data)
- Implement ensemble or tree-based models
- Add live earthquake data APIs for real-time predictions
- Deploy to cloud with Docker & CI/CD

---

### ▶️ How to Run the Project
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Start the server: `python manage.py runserver`
4. Access via `http://127.0.0.1:8000/`

To explore the analysis, open `nepal_earthquake.ipynb` in Jupyter Notebook.


### 🙏 Acknowledgements
- Nepal seismic data sources
- Libraries: Pandas, Matplotlib, Seaborn, Sklearn, Django
- Community contributions and inspiration
