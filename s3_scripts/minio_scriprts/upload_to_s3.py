import os
from datetime import timedelta

from dotenv import load_dotenv
from minio import Minio
from tqdm import tqdm

load_dotenv()

minio_bucket = os.getenv('MINIO_BUCKET')
minio_access_key = os.getenv('MINIO_ACCESS_KEY')
minio_secret_key = os.getenv('MINIO_SECRET_KEY')
minio_url = os.getenv('MINIO_URL')

# Порог для использования multipart upload (100 МБ)
MULTIPART_THRESHOLD = 100 * 1024 * 1024  # 100 МБ
# Размер части для multipart upload (50 МБ)
MULTIPART_SIZE = 50 * 1024 * 1024  # 50 МБ


class ProgressFile:
    """Wrapper для файла с отслеживанием прогресса загрузки"""
    def __init__(self, file_obj, progress_bar):
        self._file = file_obj
        self._progress_bar = progress_bar
        
    def read(self, size=-1):
        data = self._file.read(size)
        if data:
            self._progress_bar.update(len(data))
        return data
    
    def __getattr__(self, name):
        return getattr(self._file, name)


def upload_to_s3(file_path):
    """
    Загружает файл в MinIO с поддержкой больших файлов через multipart upload.
    
    Args:
        file_path: Путь к файлу для загрузки
        
    Returns:
        Presigned URL для доступа к загруженному файлу
    """
    minio_client = Minio(
        minio_url,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=True
    )
    
    if minio_client is None:
        return None
    
    file_size = os.path.getsize(file_path)
    object_name = file_path.split('/')[-1]
    
    # Определяем content_type на основе расширения файла
    content_type = 'application/csv'
    if file_path.endswith('.csv'):
        content_type = 'text/csv'
    elif file_path.endswith('.json'):
        content_type = 'application/json'
    elif file_path.endswith('.txt'):
        content_type = 'text/plain'
    
    print(f"📤 Начинаю загрузку файла: {object_name}")
    print(f"📊 Размер файла: {file_size / (1024**3):.2f} ГБ")
    
    # Используем потоковую загрузку с прогресс-баром
    with open(file_path, 'rb') as upload_file:
        # Создаем прогресс-бар
        with tqdm(
            total=file_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            desc="Загрузка",
            ncols=100
        ) as pbar:
            # Оборачиваем файл для отслеживания прогресса
            progress_file = ProgressFile(upload_file, pbar)
            
            # Для больших файлов используем multipart upload
            if file_size > MULTIPART_THRESHOLD:
                print("🔄 Использую multipart upload для большого файла...")
                put_result = minio_client.put_object(
                    bucket_name=minio_bucket,
                    object_name=object_name,
                    data=progress_file,
                    length=file_size,
                    content_type=content_type,
                    part_size=MULTIPART_SIZE
                )
            else:
                # Для маленьких файлов используем обычную загрузку
                put_result = minio_client.put_object(
                    bucket_name=minio_bucket,
                    object_name=object_name,
                    data=progress_file,
                    length=file_size,
                    content_type=content_type
                )
    
    print(f"\n✅ Файл успешно загружен: {put_result.object_name}")
    
    # Генерируем presigned URL
    url = minio_client.presigned_get_object(
        bucket_name=minio_bucket,
        object_name=put_result.object_name,
        expires=timedelta(days=7)
    )
    
    print(f"🔗 Presigned URL создан (действителен 7 дней)")
    return url


if __name__ == "__main__":
    print(upload_to_s3("/Users/s.usynin/Desktop/devices.Q4.csv"))