'''from PythonMagick import Image
Image("D:\Emmanuel ministries Hyderabad\22.jpg").write("clipboard:")'''

'''import shutil

original = r'D:\Emmanuel ministries Hyderabad\22.jpg'
target = r'clipboard:'

shutil.copy2(original,target)'''

'''import pyperclip
pyperclip.copy('D:\\Emmanuel ministries Hyderabad\\22.jpg')'''

from io import BytesIO
import win32clipboard
from PIL import Image

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

filepath = 'D:\\Emmanuel ministries Hyderabad\\22.jpg'
image = Image.open(filepath)

output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()

send_to_clipboard(win32clipboard.CF_DIB, data)

