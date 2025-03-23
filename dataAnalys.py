import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "data3_1.xlsx"
data = pd.read_excel(file_path, engine="openpyxl")

print("Первые 5 строк данных:")
print(data.head())

print("\nИнформация о данных:")
print(data.info())

print("\nОписательная статистика:")
print(data.describe())

plt.figure(figsize=(8, 6))
sns.histplot(data["Вопрос 3"], bins=5, kde=True)
plt.title("Распределение оценок эффективности автоматизации")
plt.xlabel("Оценка (1-5)")
plt.ylabel("Количество ответов")
plt.show()

question1_counts = data["Вопрос 1"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(question1_counts, labels=question1_counts.index, autopct='%1.1f%%')
plt.title("Частота использования автоматизации")
plt.show()

tools = data["Вопрос 2"].str.split(", ", expand=True).stack().value_counts()
plt.figure(figsize=(10, 6))
tools.plot(kind="bar", color="green")
plt.title("Используемые инструменты автоматизации")
plt.xlabel("Инструменты")
plt.ylabel("Количество ответов")
plt.show()

output_file = "processed_data.csv"
data.to_csv(output_file, index=False, encoding="utf-8")
print(f"\nДанные сохранены в файл: {output_file}")