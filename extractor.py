import re,zipfile,os,rarfile,subprocess
def unCompressorZip(source_filename,dest_dir):
	print 'zip:'+source_filename
	print 'zip_folder:'+source_filename
	with zipfile.ZipFile(source_filename) as zf:
		zf.extractall(dest_dir)
		os.remove(source_filename)
	pass
def unCompressorRar(source_filename,dest_dir):
	print 'rar:'+source_filename
	print 'rar_folder:'+source_filename
	with rarfile.RarFile(source_filename) as rf:
		rf.extractall(dest_dir)
		os.remove(source_filename)
	pass
def unCompressor7z(source_filename,dest_dir):
	print '7z:'+source_filename
	print '7z_folder:'+source_filename
	subprocess.call(['7z', 'x', '-r', '-y', '-o%s' % dest_dir,source_filename], shell = False)
	os.remove(source_filename)
	pass
def doNothing(a,b):
	pass
def excute(curr_path):
	file_list = [ f for f in os.listdir(curr_path) if os.path.isfile(os.path.join(curr_path,f)) ]
	for file in file_list:
		fileName, fileExtension = os.path.splitext(file)
		caller = compressor.get(fileExtension,doNothing)
		caller(curr_path+'/'+file,curr_path+'/'+fileName)
	folder_list = [ f for f in os.listdir(curr_path) if os.path.isdir(os.path.join(curr_path,f)) ]
	for folder in folder_list:
		excute(curr_path+'/'+folder)
	pass
compressor ={
	'.zip':unCompressorZip,
	'.7z':unCompressor7z,
	'.rar':unCompressorRar
	}
curr_path = os.getcwd()
file_list = os.listdir(curr_path)
excute(curr_path)
