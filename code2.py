import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="whitegrid")


excel_file = 'پروژه 3.xlsx'

try:
    
    df = pd.read_excel(excel_file)
except FileNotFoundError:
    
    print(f"Warning: '{excel_file}' not found. Creating the dataset from the provided structure.")
    data = {
        'Run time for different data size': ['100KB', '200KB', '300KB', '400KB', '500KB', '600KB'],
        'Alg.1': [50, 55, 60, 65, 70, 75],
        'Alg.2': [200, 220, 240, 260, 280, 300],
        'Alg.3': [100, 200, 300, 400, 500, 600]
    }
    df = pd.DataFrame(data)


df.columns = df.columns.str.strip()


mean_alg2 = df['Alg.2'].mean()
print("--- Part 2 (c): Statistical Analysis ---")
print(f"Mean execution time for Alg.2 (100KB to 600KB): {mean_alg2:.2f}\n")


new_row = {
    'Run time for different data size': '700KB',
    'Alg.1': 80,
    'Alg.2': 320,
    'Alg.3': 700
}

df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("--- Part 2 (b): Updated Dataframe with 700KB Row ---")
print(df)
print("\n")


size_col = df.columns[0] 
algorithms = [col for col in df.columns if col != size_col]


plt.figure(figsize=(10, 6))
for alg in algorithms:
    plt.plot(df[size_col], df[alg], marker='o', linewidth=2, label=alg)

plt.title('Execution Time Trend across Different Data Sizes', fontsize=14, fontweight='bold')
plt.xlabel('Data Size', fontsize=12)
plt.ylabel('Execution Time (ms)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('execution_time_line_plot.png', dpi=300)
plt.show()


df_long = pd.melt(df, id_vars=[size_col], value_vars=algorithms, 
                  var_name='Algorithm', value_name='Execution Time')

plt.figure(figsize=(10, 6))
sns.barplot(data=df_long, x=size_col, y='Execution Time', hue='Algorithm', palette='muted')
plt.title('Comparison of Algorithm Execution Times per Data Size', fontsize=14, fontweight='bold')
plt.xlabel('Data Size', fontsize=12)
plt.ylabel('Execution Time (ms)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('execution_time_bar_plot.png', dpi=300)
plt.show()


plt.figure(figsize=(8, 6))
sns.boxplot(data=df[algorithms], palette='pastel')
plt.title('Distribution of Execution Times per Algorithm (Spread Analysis)', fontsize=14, fontweight='bold')
plt.xlabel('Algorithm', fontsize=12)
plt.ylabel('Execution Time Range', fontsize=12)
plt.tight_layout()
plt.savefig('execution_time_box_plot.png', dpi=300)
plt.show()

print("All plots generated and saved successfully!")