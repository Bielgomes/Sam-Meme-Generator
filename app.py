from flask import Flask, send_file, request
from generator import gen

app = Flask(__name__)

@app.route('/api/v1/generator', methods=['GET'])
def gen_meme():
  try:
    base = request.args['base']
    logo = request.args['logo']
    logo_pos = request.args['logo_pos']
    text = request.args['text']
    meme_quality = int(request.args['meme_quality'])
    logo_opacity = int(request.args['logo_opacity'])

    tempFileObj = gen(base, logo, logo_pos, text, meme_quality, logo_opacity)

    response = send_file(tempFileObj, as_attachment=False, attachment_filename='meme.jpg')
    return response
  except:
    return "<h1 align='center'>Uepa!</h1><p align='center'>Algo deu errado.</p>"

@app.route('/api/v1/generator/download', methods=['GET'])
def download_meme():
  try:
    base = request.args['base']
    logo = request.args['logo']
    logo_pos = request.args['logo_pos']
    text = request.args['text']
    meme_quality = int(request.args['meme_quality'])
    logo_opacity = int(request.args['logo_opacity'])

    tempFileObj = gen(base, logo, logo_pos, text, meme_quality, logo_opacity)

    response = send_file(tempFileObj, as_attachment=True, attachment_filename='meme.jpg')
    return response
  except:
    return "<h1 align='center'>Uepa!</h1><p align='center'>Algo deu errado.</p>"