import tensorflow as tf
from tensorflow.python.client import device_lib


def get_available_devices():
    local_device_protos = tf.config.list_physical_devices()
    return [x.name for x in local_device_protos]


print(get_available_devices())
# my output was => ['/device:CPU:0']
# good output must be => ['/device:CPU:0', '/device:GPU:0']

