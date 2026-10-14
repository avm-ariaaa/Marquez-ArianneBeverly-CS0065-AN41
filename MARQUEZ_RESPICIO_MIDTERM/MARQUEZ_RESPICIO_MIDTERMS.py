# PART 4: RECREATE THE PROCESS IN PYTHON

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, 
                             recall_score, f1_score, confusion_matrix)

print("\nProgrammed by: Arianne Beverly Marquez & Lester Anthony Respicio\n")

print("\nInitializing and loading csv...\n")

# 1. Load the Dataset
file_path = "MARQUEZ_RESPICIO_CS0065 MIDTERM - Sheet1.csv"
df = pd.read_csv(file_path)

# 2. Exclude identifiers & Prepare X (Inputs) and y (Target)
feature_cols = ['CALORIES (kcal)', 'SUGAR (g)', 'FAT (g)', 'PROTEIN (g)', 'SODIUM (mg)']
X = df[feature_cols]
y = df['CATEGORY']

# 3. Stratified Partitioning (80/20 matching Table Partitioner)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.20, 
    stratify=y, 
    random_state=42
)

# 4. Define and Train Pipelines (Handling Median Imputation + Model Training)
dt_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('classifier', DecisionTreeClassifier(criterion='gini', min_samples_split=2, random_state=42))
])
dt_pipeline.fit(X_train, y_train)
dt_predictions = dt_pipeline.predict(X_test)

rf_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('classifier', RandomForestClassifier(n_estimators=100, criterion='gini', random_state=42))
])
rf_pipeline.fit(X_train, y_train)
rf_predictions = rf_pipeline.predict(X_test)


# --- EVALUATION OUTPUT ---

def evaluate_model(name, y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    rec = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    
    print(f"{name.upper()} EVALUATION")
    print(f"{'='*35}")
    print(f"{'Metric':<15} | {'Score':<15}")
    print(f"{'-'*15}-+-{'-'*15}")
    print(f"{'Accuracy':<15} | {acc:.4f}")
    print(f"{'Precision':<15} | {prec:.4f}")
    print(f"{'Recall':<15} | {rec:.4f}")
    print(f"{'F1-Score':<15} | {f1:.4f}")
    print(f"{'='*35}\n")
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("\n")

evaluate_model("Decision Tree", y_test, dt_predictions)
evaluate_model("Random Forest", y_test, rf_predictions)

# 5. Save the Selected Pipeline for Streamlit (Part 5)
joblib.dump(dt_pipeline, 'meal_category_model.pkl')
print("Pipeline saved successfully as 'meal_category_model.pkl'")