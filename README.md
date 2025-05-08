# Apartment Sales Price Prediction
Check Presentation: https://www.canva.com/design/DAGepDAWaqs/YWldWXcH1aIpEtWax7tcAw/view?utm_content=DAGepDAWaqs&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h19c1936fa7
## Project Overview

This project aims to predict apartment sales prices in Tunis (Tunisia) based on key features such as governorate, delegation, area (m²), number of rooms, and other relevant factors. 

By leveraging real estate data scraped from three major listing websites:

- [Tayara.tn](https://www.tayara.tn/)
- [Menzili.tn](https://www.menzili.tn/)
- [Mubawab.tn](https://www.mubawab.tn/)

We used the **Scrapy framework** to extract apartment sales listings, followed by extensive **data cleaning, preprocessing, and machine learning modeling** to predict apartment prices.

## Repository Structure

```
APARTMENTS-SALES/
│-- cleaning/                               # Jupyter notebooks for data cleaning
│   ├── cleaning_menzili.ipynb
│   ├── cleaning_mubawab.ipynb
│   ├── concat_csvs.ipynb
│
│-- csv/
│   ├── after_cleaning/                     # Preprocessed and merged datasets
│   │   ├── menzili_preprocessed.csv        # Cleaned data from Menzili.tn
│   │   ├── mubawab_preprocessed.csv        # Cleaned data from Mubawab.tn
│   │   ├── tayara_preprocessed.csv         # Cleaned data from Tayara.tn
│   │   ├── mubawab_tayara.csv              # Combined dataset of Mubawab and Tayara
│   │   ├── mubawab_tayara_menzili_final.csv # Final dataset combining all three sources  <---  final
|   |
│   ├── apartments_db.menzili.csv       # Processed database from Menzili.tn
│   ├── apartments_db.mubawab.csv       # Processed database from Mubawab.tn
│   ├── apartments_db.tayara.csv        # Processed database from Tayara.tn
│
│-- json/                    # JSON data files
│
│-- modeling/                # Machine Learning models
│   ├── compressed_models/   # Trained models (CatBoost, Decision Tree, etc.)
│   ├── ML notebooks for different models
│
│-- visualization/           # Data visualization notebooks and reports
│   ├── before_cleaning/
│   ├── after_cleaning/
│   ├── data_visualization.ipynb
│
│-- ScrapyApartments/        # Scrapy spiders for data extraction
│-- venv/                    # Virtual environment (if applicable)
│-- .gitignore
│-- README.md                # Project documentation
│-- requirements.txt         # Dependencies
```

## Technologies Used

- **Python** 🐍
- **Scrapy** for Web Scraping 🕷️
- **Pandas, NumPy** for Data Processing 📊
- **Scikit-Learn, CatBoost, XGBoost** for Machine Learning 🤖
- **Matplotlib, Seaborn** for Data Visualization 📈
- **Jupyter Notebooks** for experimentation 📑

## Machine Learning Models Used

We experimented with multiple regression models to predict apartment prices:

**Linear Regression** - **Decision Tree Regressor** - **Random Forest Regressor** - **Support Vector Machine (SVM) Regressor** - **XGBoost** - **CatBoost**

## How to Use

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run Web Scraping (Scrapy)

Navigate to the `ScrapyApartments` directory and run:

```bash
scrapy crawl <spider_name>
```

Replace `<spider_name>` with the appropriate scraper (e.g., `tayara`, `menzili`, `mubawab`).

### 3️⃣ Data Cleaning & Preprocessing

Execute Jupyter notebooks from the `cleaning/` folder to clean and preprocess the data.

### 4️⃣ Train ML Models

Run the notebooks in `modeling/` to train and evaluate different machine learning models.

### 5️⃣ Visualize Results

Use the `visualization/` notebooks to analyze and interpret the dataset.

## Results & Insights

- **Data Insights:** After data cleaning, we observed key pricing trends across different regions and property sizes.
- **Model Performance:** CatBoost and XGBoost outperformed other models in terms of accuracy and predictive performance.
- **Feature Importance:** Location, apartment size, and number of rooms were the most influential factors affecting prices.

## Contributors
Asma Elhadj
Ilef Chebil
Taher Nouira



