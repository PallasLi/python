'''
Created on 2016年3月24日

@author: lyt
验证码识别
'''
try:
  import pytesseract
  from PIL import Image
except ImportError:
  print ('模块导入错误,请使用pip安装,pytesseract依赖以下库：')
  print ('http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil')
  print ('http://code.google.com/p/tesseract-ocr/')
  raise SystemExit

image = Image.open(r'G:\new_frame\pyTest\com\pallasli\study\1.png')
vcode = pytesseract.image_to_string(image)
print (vcode)