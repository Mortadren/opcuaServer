import cv2
import os

# Путь к видеофайлу
video_path = 'path'

# Создать каталог для сохранения кадров
output_directory = 'frames'
os.makedirs(output_directory, exist_ok=True)

# Открыть видеофайл
cap = cv2.VideoCapture(video_path)

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Сохранить текущий кадр как изображение
    frame_filename = os.path.join(output_directory, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_filename, frame)
    
    frame_count += 1

# Закрыть видеофайл
cap.release()

print(f'Сохранено {frame_count} кадров в каталог {output_directory}')
