from numba import cuda
import numpy
cuda.select_device( 0 )

x=3
@cuda.jit
def increment_by_one(B):
    tx = cuda.threadIdx.x
    bx = cuda.blockIdx.x
    B[tx] *= x


A = numpy.array([1])

threadsperblock = 1
blockspergrid = 1
increment_by_one[blockspergrid, threadsperblock](A)

print(A,)
