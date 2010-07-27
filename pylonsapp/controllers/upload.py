# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from pylonsapp.lib.base import BaseController, render
import os
from pylons import config
import shutil

log = logging.getLogger(__name__)

class UploadController(BaseController):

    def index(self):
        return render('/form/uploadform.html')

    def upload(self):
        import os
        from pylons import config
        import shutil

        # 注意需手工建下上载目录 data/uploads
        myfile = request.POST['myfile']
        permanent_file = open(
                    os.path.join(
                        config['app_conf']['permanent_store'],
                        myfile.filename.replace(os.sep, '_')
                    ),
                    'wb'
        )

        shutil.copyfileobj(myfile.file, permanent_file)
        myfile.file.close()
        permanent_file.close()

        return 'Successfully uploaded: %s, description: %s' % (
                myfile.filename,
                request.POST['description'])

    # http://localhost:5000/upload/download?requested_filename=somefile
    def download(self):
        from mimetypes import guess_type
        requested_filename = request.params['requested_filename']
        filename = os.path.join(
                                config['app_conf']['permanent_store'],
                                requested_filename.replace(os.sep, '_')
                                )
        if not os.path.exists(filename):
            return 'No such file'

        permanent_file = open(filename, 'rb')
        data = permanent_file.read()
        permanent_file.close()
        response.content_type = guess_type(filename)[0] or 'text/plain'

        # 采用强制下载
        response.headers['Content-Disposition'] = 'attachment; filename="%s"'%(requested_filename)

        return data
