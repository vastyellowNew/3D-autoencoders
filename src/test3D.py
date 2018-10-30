import mayavi.mlab
import numpy

data = (100, 100, 100)
data = numpy.zeros(data)
data[0:1, 0:1, 0:1] = 1
data[4:5, 4:5, 4:5] = 1

xx, yy, zz = numpy.where(data == 1)

mayavi.mlab.points3d(xx, yy, zz,
                     mode="cube",
                     color=(0, 1, 0),
                     scale_factor=1)

mayavi.mlab.show()