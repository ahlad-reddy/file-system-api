from flask import Flask, request, jsonify
import os
from pwd import getpwuid

ROOT_DIR = 'data'

def create_app():
  app = Flask(__name__)

  @app.route('/')
  @app.route('/<path:subpath>')
  def api(subpath="", methods=['GET']):
    if request.method == 'GET':
      path = os.path.join(ROOT_DIR, subpath)
      if os.path.isdir(path):
        files = []
        dirs = []
        for f in os.listdir(path):
          fp = os.path.join(path, f)
          if os.path.isfile(fp):
            stats = os.stat(fp)
            files.append({ 
              'name': f, 
              'owner': getpwuid(stats.st_uid).pw_name, 
              'size': stats.st_size, 
              'permissions': oct(stats.st_mode)[-3:],
            })
          else:
            dirs.append(f)
        return jsonify({ 'files': files, 'directories': dirs })
      elif os.path.isfile(path):
        file = open(path, 'r')
        return jsonify({ 'content': file.read() })
      else:
        return jsonify({ 'error': 'path does not exist'})

  return app