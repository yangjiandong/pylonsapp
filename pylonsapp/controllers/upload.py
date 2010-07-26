import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from pylonsapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UploadController(BaseController):

    def index(self):
        return render('/form/uploadform.html')

    def upload(self):
        import os
        from pylons import config
        import shutil

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

        return 'Successfully uploaded: %s, description: %s' %(
                myfile.filename,
                request.POST['description'])
