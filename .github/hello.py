import os
import sys
import platform
from datetime import datetime

def main():
    # 1. Читаем секрет (если он не задан — берём заглушку)
    api_key = os.environ.get("MY_API_KEY", "NOT_SET")
    if api_key != "NOT_SET":
        # Никогда не печатаем ключ целиком — только длину/факт наличия
        print(f"✅ Секрет получен (длина: {len(api_key)} символов)")
    else:
        print("⚠️  Секрет MY_API_KEY не задан — работаем без него")

    # 2. Информация о среде
    print(f"🐍 Python: {sys.version.split()[0]}")
    print(f"💻 Платформа: {platform.system()} {platform.release()}")
    print(f"🕒 Время запуска: {datetime.now().isoformat()}")

    # 3. Создаём файл-отчёт (его подхватит upload-artifact)
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("=== Отчёт робота ===\n")
        f.write(f"Python: {sys.version.split()[0]}\n")
        f.write(f"OS: {platform.system()} {platform.release()}\n")
        f.write(f"Time: {datetime.now().isoformat()}\n")
        f.write(f"Secret set: {api_key != 'NOT_SET'}\n")

    print("📄 report.txt создан")

if __name__ == "__main__":
    main()
