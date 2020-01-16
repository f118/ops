import subprocess as sp, time
sp.Popen('E:\\ffmpeg\\bin\\ffmpeg -ss 2 -t 5 -i C:\\Users\magic.yang\\Videos\\test_clip.avi -s 320*240 -f image2 -r 1 e:\\ffmpeg\\bin\\gif\\b-%03d.jpeg')
time.sleep(2)
sp.call('E:\\ffmpeg\\bin\\ffmpeg -f image2 -framerate 3 -s 320*240 -i e:\\ffmpeg\\bin\\gif\\a-%03d.jpeg e:\\ffmpeg\\bin\\b.gif')
print ('over')
