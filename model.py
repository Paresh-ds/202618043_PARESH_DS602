import pandas as pd
import statsmodels.api as sm


# ==========================================
# 1. LOAD DATASET
# ==========================================

DATA_PATH = "data/california_housing_updated.csv"

df = pd.read_csv(DATA_PATH)


# ==========================================
# 2. DEFINE VARIABLES
# ==========================================

FEATURES = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
    "Latitude",
    "Longitude"
]

TARGET = "MedHouseVal"


# ==========================================
# 3. CREATE X AND y
# ==========================================

X = df[FEATURES]

y = df[TARGET]


# ==========================================
# 4. ADD INTERCEPT
# ==========================================

X = sm.add_constant(X)


# ==========================================
# 5. FIT OLS REGRESSION MODEL
# ==========================================

model = sm.OLS(y, X).fit()