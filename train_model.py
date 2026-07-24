import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("data/dataset.csv")

le_goal = LabelEncoder()
le_risk = LabelEncoder()
le_rec = LabelEncoder()

df["Goal"] = le_goal.fit_transform(df["Goal"])
df["Risk"] = le_risk.fit_transform(df["Risk"])
df["Recommendation"] = le_rec.fit_transform(df["Recommendation"])

X = df.drop("Recommendation", axis=1)
y = df["Recommendation"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "model/model.pkl")
joblib.dump(le_goal, "model/goal_encoder.pkl")
joblib.dump(le_risk, "model/risk_encoder.pkl")
joblib.dump(le_rec, "model/recommendation_encoder.pkl")

print("Model trained successfully!")