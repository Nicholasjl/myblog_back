#!/usr/bin/python
# -*- coding:utf-8 -*-

"""Documentation"""

from sanic import Sanic, response
from sanic_cors import CORS, cross_origin
from sanic.exceptions import *
import markdown
import os
import aiofiles


import generate

app = Sanic()
CORS(app)


@app.route("/api/articles/")
async def article_list(request):
    _json = generate.get_article_list()
    return response.json(_json)
    
@app.route("/api/upload/", methods=['POST'])
async def article_list(request):

    f = request.files.get('file')
    [pwd] = request.args['pwd']
    
    if await generate.checkPassword(pwd):
        
        async with aiofiles.open(os.path.join('articles',f.name[:-3]+'.html'),mode='w',encoding='utf-8') as html:
            file = markdown.markdown(f.body.decode())
            await html.write(file)
        return response.text('上传成功')
    return response.text('口令错误')


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5002,

        debug=True,
    )
    pass
