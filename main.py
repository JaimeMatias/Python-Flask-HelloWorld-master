#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
    def hola():
        import clasehola
        return clasehola.hello_world()
if __name__ == '__main__':
  app.run()
