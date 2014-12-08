#extractor.py
===
Now only support for .zip,rar and .7z files.
##Installation&Prerequisite
###For .zip
Run the extractor.py directly.
###For .rar
1.pip install rarfile<br>
2.Download “RAR 4.20 for Mac OS X” (or a later version if there is one) from RARLab.<br>
3.cd ~/Downloads/rarosx-4.2.0/rar<br>
4.sudo install -c -o $USER unrar /usr/local/bin <br>
5.sudo install -c -o $USER rar /usr/local/bin<br>
Using in command line => unrar x /path/to/file.part01.rar<br/>
Reference:<a href="https://rarfile.readthedocs.org/en/latest/index.html">href=https://rarfile.readthedocs.org/en/latest/index.html</a>

###For .7z
1.brew update<br>
2.brew install p7zip<br>
Using command line => 7z x /path/to/file.7z

##Usage
Put this python scipt with your compressed files(or folder) in the same path,and excute it with commandline.
The script will recursively scan your files and subfolder find your compressed file and extract it.