from SRobj import *
r=image()
r.glCreateWindow(920,920)
r.glClear()
r.glViewPort(459,459,920,920)
r.readObj("Chibirobo.obj")
r.glFinish()
