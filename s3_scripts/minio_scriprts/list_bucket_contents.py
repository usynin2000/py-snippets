import os

from dotenv import load_dotenv
from minio import Minio
from minio.error import S3Error

load_dotenv()

# Настройки подключения
minio_bucket = os.getenv('MINIO_BUCKET')
minio_access_key = os.getenv('MINIO_ACCESS_KEY')
minio_secret_key = os.getenv('MINIO_SECRET_KEY')
minio_url = os.getenv('MINIO_URL')


def list_bucket_contents(bucket_name=None, prefix=""):
    """
    Просматривает содержимое бакета MinIO
    
    Args:
        bucket_name: Имя бакета (по умолчанию используется minio_bucket)
        prefix: Префикс для фильтрации объектов (опционально)
    """
    try:
        # Создаем клиент MinIO
        minio_client = Minio(
            minio_url,
            access_key=minio_access_key,
            secret_key=minio_secret_key,
            secure=True
        )
        
        # Используем указанный бакет или по умолчанию
        target_bucket = bucket_name or minio_bucket
        
        # Проверяем существование бакета
        if not minio_client.bucket_exists(target_bucket):
            print(f"❌ Бакет '{target_bucket}' не существует!")
            return
        
        print(f"📦 Содержимое бакета: {target_bucket}")
        print("-" * 80)
        
        # Получаем список объектов
        objects = minio_client.list_objects(
            target_bucket,
            prefix=prefix,
            recursive=True
        )
        
        file_count = 0
        total_size = 0
        
        for obj in objects:
            file_count += 1
            size = obj.size
            total_size += size
            
            # Форматируем размер файла
            size_str = format_size(size)
            
            # Выводим информацию об объекте
            print(f"📄 {obj.object_name}")
            print(f"   Размер: {size_str}")
            print(f"   Дата изменения: {obj.last_modified}")
            if obj.etag:
                print(f"   ETag: {obj.etag}")
            print()
        
        # Итоговая статистика
        print("-" * 80)
        print(f"Всего файлов: {file_count}")
        print(f"Общий размер: {format_size(total_size)}")
        
    except S3Error as e:
        print(f"❌ Ошибка S3: {e}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")


def format_size(size_bytes):
    """Форматирует размер файла в читаемый вид"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


if __name__ == "__main__":
    # Просмотр всего содержимого бакета
    list_bucket_contents()
    
    # Пример с фильтрацией по префиксу (раскомментируйте при необходимости):
    # list_bucket_contents(prefix="some_prefix")