import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
import time
import pyautogui

# 如果需要，设置tesseract.exe的路径
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_preprocessing(image):
    # 将图像转换为灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 进行阈值处理，二值化图像
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return thresh

def click_text_containing_num():
    screen = np.array(ImageGrab.grab())
    # 预处理图像
    processed_image = image_preprocessing(screen)

    # 使用pytesseract进行OCR，获取详细数据
    custom_config = r'--oem 3 --psm 6'
    data = pytesseract.image_to_data(processed_image, config=custom_config, output_type=pytesseract.Output.DICT)

    # 输出识别到的所有文本
    found_num = False
    for i in range(len(data['text'])):
        text = data['text'][i].strip()  # 去掉前后的空白
        if text:  # 仅输出非空文本
            print(f"识别到的文本: '{text}'，位置: ({data['left'][i]}, {data['top'][i]})")
            if 'num' in text:  # 判断文本中是否包含"num"
                pyautogui.click(data['left'][i], data['top'][i])
                found_num = True

    return found_num

# 主循环
time.sleep(3)
while True:
    time.sleep(0.2)
    if click_text_containing_num():
        print('已点击包含"num"的文本')
    else:
        pyautogui.click(764,581)




