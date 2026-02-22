# 1. Берем легкий образ Python
FROM python:3.11-slim

# 2. Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# 3. Копируем список зависимостей
COPY requirements.txt .

# 4. Устанавливаем библиотеки (тот самый Flask и др.)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем весь остальной код приложения (наш main.py)
COPY . .

# 6. Команда, которая запустит приложение при старте контейнера
CMD ["python", "main.py"]

