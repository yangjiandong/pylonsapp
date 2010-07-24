pylons 0.9.7
===============

2010.07.24
-----------

1. 采用虚拟python，建立0.97开发环境

   a. Download the virtualenv.py script from http://pylonsbook.com/virtualenv.py.

   b. Create a virtual Python environment in a directory called env so that packages you install for Pylons do not affect any other programs using Python on your system:

      $ python virtualenv.py --no-site-packages env

   c. Windows users would use Scripts instead of bin in the above command but full details are explained later in the Windows-specific instructions.
      Use the easy_install program (which was automatically installed into your virtual Python environment by the previous command) to install Pylons:

      $ env/bin/easy_install "Pylons==0.9.7"

      env/Scripts/easy_install ...

   假设路径为D:\workspace\python\workspace\myenv\0.97\env

   以后运行时需指定该路径，如 D:\workspace\python\workspace\myenv\0.97\env\Scripts\paster create -t pylons HelloWorld

   或先运行D:\workspace\python\workspace\myenv\0.97\env\Scripts\activate.bat，设置虚拟路径优先


2. easy_install

   easy_install -f http://pylonshq.com/download/0.9.6.2/ "Pylons==0.9.6.2"
   easy_install -f http://pylonshq.com/download/ Pylons
   or
   easy_install PasteDeploy-1.5.tar.gz

   proxy
   set HTTP_PROXY=http://your.proxy.com:yourPort
   export HTTP_PROXY="http://user:password@yourproxy.com:port"

3. git

   增加git仓库 http://github.com/yangjiandong/sshapp
   git remote add origin git@github.com:yangjiandong/pythonapp.git

   git push origin master:refs/heads/master


   --END