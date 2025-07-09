import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import os

def run_analysis(file_name):
    try:
        # 1. Load Excel from 'data' folder
        base_dir = os.path.dirname(os.path.abspath(__file__))  
        file_path = os.path.join(base_dir, "data", file_name)

        xls = pd.ExcelFile(file_path)
        sheet_names = xls.sheet_names

        if len(sheet_names) < 2:
            print("Error: The Excel file must have at least two sheets.")
            return

        sheet_a, sheet_b = sheet_names[0], sheet_names[1]
        print(f"Using sheets: {sheet_a} (A), {sheet_b} (B)")

        df_a = pd.read_excel(xls, sheet_name=sheet_a)
        df_b = pd.read_excel(xls, sheet_name=sheet_b)

        # 2. Extract coordinates
        x_a, y_a = df_a['경도'].values, df_a['위도'].values
        x_b, y_b = df_b['LON'].values, df_b['LAT'].values

        # 3. Common longitude axis
        x_common = np.linspace(min(x_a.min(), x_b.min()), max(x_a.max(), x_b.max()), 200)

        # 4. Interpolation
        interp_a = interp1d(x_a, y_a, kind='linear', fill_value="extrapolate")
        interp_b = interp1d(x_b, y_b, kind='linear', fill_value="extrapolate")

        y_a_interp = interp_a(x_common)
        y_b_interp = interp_b(x_common)

        # 5. Distance
        euclidean_dist = np.linalg.norm(y_a_interp - y_b_interp)
        mean_abs_dist = np.mean(np.abs(y_a_interp - y_b_interp))

        print("\n[Result]")
        print(f"Euclidean distance: {euclidean_dist:.4f}")
        print(f"Mean absolute distance: {mean_abs_dist:.6f}")

        # 6. Plot
        plt.figure(figsize=(10, 5))
        plt.plot(x_common, y_a_interp, label="Line A (Interpolated)", linestyle='--')
        plt.plot(x_common, y_b_interp, label="Line B (Interpolated)", linestyle='--')
        plt.scatter(x_a, y_a, color='blue', label="Line A Original", s=30)
        plt.scatter(x_b, y_b, color='orange', label="Line B Original", s=30)
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title(f"sheet_1 vs sheet_2 Line Comparison")
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"[ERROR] {e}")
        input("Press Enter to exit...")  
