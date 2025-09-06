import time
from tqdm import tqdm

# tqdm = taqaddum (تقدّم) — арабское слово, означающее «прогресс» или «продвижение вперёд».

for i in tqdm(range(100), desc="Processing data"):
    time.sleep(1)