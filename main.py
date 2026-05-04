"""
MIT License

Copyright (c) 2026 Gökhan Çoban, Şahan Burak Ergüzel, Atakan Mert Çağlayan,
Mert Yücel, Abdullahi Ahmed Mohomed & Abdirahman Mahamed Abdikani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pandas as pd
from matplotlib import pyplot as plt

df_1 = pd.read_csv("50kgs_sc1_group1.csv", sep=";")
df_2 = pd.read_csv("75kgs_sc2_group3.csv", sep=";")
df_3 = pd.read_csv("120kgs_sc3_group3.csv", sep=";")

df_1.columns = df_1.columns.str.strip()
df_2.columns = df_2.columns.str.strip()
df_3.columns = df_3.columns.str.strip()


time_col = df_1.columns[0]
temp_col = df_1.columns[1]

plt.figure(figsize=(12, 6))

plt.plot(df_1[time_col], df_1[temp_col], label=r"$\it{50\ kg}$", marker="o")
plt.plot(df_2[time_col], df_2[temp_col], label=r"$\it{75\ kg}$", marker="o")
plt.plot(df_3[time_col], df_3[temp_col], label=r"$\it{120\ kg}$", marker="o")

plt.xlabel(r"Time, $\it{a}$")
plt.ylabel(r"Temperature, $\it{degC}$")
plt.xlim(0, 30)
plt.ylim(120, 250)
plt.xticks(range(0, 31, 5))
plt.yticks(range(120, 246, 10))
plt.title("Thermal Breakthrough Curve Comparison")
plt.text(0.98, 0.005, '© PETE 509 - METU 2025s - Group 3', fontsize=8, color='gray', ha='right', va='bottom', transform=plt.gca().transAxes, alpha=0.5)
plt.legend()
plt.grid(True)

plt.show()
