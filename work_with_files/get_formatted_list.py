import csv
import json
from datetime import datetime
from pathlib import Path

TAKE = 2000

MIN_SKIP = 5500


formatted_list = []
with open("/Users/s.usynin/Desktop/ururu_export_accounts.csv", "r") as file:
    reader = csv.reader(file)
    for idx, row in enumerate(reader):
        if idx < MIN_SKIP:
            continue
        if len(formatted_list) >= TAKE:
            break
        formatted_list.append(row[0])
print(formatted_list)

# Сохраняем результат в файл в той же директории
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = Path(__file__).parent
output_path = output_dir / f"formatted_list_{timestamp}_take{TAKE}_skip{MIN_SKIP}.txt"
output_path.write_text(json.dumps(formatted_list, ensure_ascii=False, indent=4))
print(f"Результат сохранен в {output_path}")