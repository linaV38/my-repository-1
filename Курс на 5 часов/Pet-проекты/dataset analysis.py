# Установка необходимых библиотек
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score, balanced_accuracy_score
from sklearn.preprocessing import StandardScaler


# Загрузка данных с Kaggle
df = pd.read_csv(r"C:\Users\linan\.cache\kagglehub\datasets\victoriajabdulkadir\beverage-sales-prediction\versions\1\beverage_sales.csv",
                 encoding="ISO-8859-1")

# Просмотр датасета
print(df.head())
print(df.tail(n=10))

# Первичная информация о датасете
print(df.describe())
print(df.info(show_counts=True, memory_usage=True, verbose=True))
print(df.shape) # 1000 строк, 3 столбца

# Проверка наличия нулевых значений
print(df.isnull () .sum())  # нулевых значений нет

# Проверка наличия дубликатов
df.drop_duplicates()
print(df.shape) # дубликатов нет

# Проверка наличия выбросов по столбцам Temperature и Beverage Sales
z_scores_temperature = (df["Temperature (°C)"] - np.mean(df["Temperature (°C)"])) / np.std(df["Temperature (°C)"])
threshold = 3
outliers_temperature = np.where(np.abs(z_scores_temperature) > threshold)[0]
print(outliers_temperature)

z_scores_beverage_sales = (df["Beverage Sales"] - np.mean(df["Beverage Sales"])) / np.std(df["Beverage Sales"])
threshold = 3
outliers_beverage_sales = np.where(np.abs(z_scores_beverage_sales) > threshold)[0]
print(outliers_beverage_sales) # по столбцам Temperature и Beverage Sales выбросов нет

# Разделение данных на предиктор и отклик
X = df[["Temperature (°C)", "Promotion"]]
y = df["Beverage Sales"]

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Построение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(y_pred)

# Оценка модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Среднеквадратическая ошибка (MSE): {mse}")
print(f"Коэффициент детерминации (R^2): {r2}")

# Визуализация тестовых и предсказанных данных для оценки модели
plt.scatter(y_test, y_pred)
plt.xlabel("Реальные значения")
plt.ylabel("Предсказанные значения")
plt.title("Реальные vs Предсказанные значения")
plt.show()
















