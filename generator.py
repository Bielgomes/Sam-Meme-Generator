from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import textwrap
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
import os
import random

path = os.getcwd()

def AddOpacity(image, opacity):
    image = image.convert('RGBA')
    new_image = image.split()[3]
    new_image = ImageEnhance.Brightness(new_image).enhance(opacity)

    image.putalpha(new_image)

    return image

def gen(user_base : str, user_logo : str, logo_pos : str, user_texto : str, meme_quality : int, logo_opacity : int):
  user_texto = user_texto.upper()
  
  if logo_pos == 'center': tamanho_logo = (300, 300)
  else: tamanho_logo = (100,100)

  background = Image.new('RGB', (700,500))

  base = Image.open(f'{path}/assets/bases/{user_base}.jpg')
  logo = Image.open(f'{path}/assets/logos/{user_logo}.png')
  font = ImageFont.truetype(f'{path}/assets/fonts/roboto.ttf', size=30)

  base = base.resize((700,500), Image.ANTIALIAS)
  draw = ImageDraw.Draw(background)

  W, H = base.size
  y_texto = 5

  lines = textwrap.wrap(user_texto, width=40)

  for line in lines:
    w, h = font.getsize(line)
    draw.text(((W-w)/2, y_texto), line, font=font)
    y_texto += h + 2

  logo_position = {
    'top_left': (15, y_texto+20),
    'top_right': (580, y_texto+20),
    'bottom_left': (20,385),
    'bottom_right': (580, 385),
    'center': (200, 100),
    'random': (random.randint(20,580), random.randint(y_texto+20,385))
  }

  if len(user_texto) > 0:
    background.paste(base, (0, y_texto + 5))
  else:
    background.paste(base, (0, 0))
    
  logo = logo.resize(tamanho_logo)
  logo = AddOpacity(logo, logo_opacity/100)

  background.paste(logo, logo_position[logo_pos], logo)
  background.save(f'{path}/tmp/meme.jpg', 'JPEG', quality=meme_quality)
  
  tempFileObj = NamedTemporaryFile(mode='w+b',suffix='jpg')
  pilImage = open(f'{path}/tmp/meme.jpg','rb')
  copyfileobj(pilImage,tempFileObj)
  pilImage.close()
  remove(f'{path}/tmp/meme.jpg')
  tempFileObj.seek(0,0)

  return tempFileObj