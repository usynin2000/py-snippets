import os
import subprocess


def convert_videos_in_dir_h264(
    input_folder: str,
    output_folder: str,
    max_videos: int = 0,
):

    os.makedirs(output_folder, exist_ok=True)
    counter = 0
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".mp4"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"converted_{filename}")

            if os.path.exists(output_path):
                print(f"Файл {output_path} уже существует. Пропускаем...")
                continue

            command = [
                "ffmpeg",
                "-i", input_path,
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p", 
                "-c:a", "aac",
                "-movflags", "+faststart",
                output_path,
            ]

            print(f"Конвертируем {filename}\n")
            subprocess.run(command)
            print(f"Готово: {output_path}\n")
            counter += 1
            print(f"Конвертировано {counter} видео")
            if counter == max_videos:
                break


if __name__ == "__main__":
    input_folder = "/Users/s.usynin/Desktop/загс"
    output_folder = "/Users/s.usynin/Desktop/загс_converted"
    max_videos = 3
    convert_videos_in_dir_h264(input_folder, output_folder, max_videos)