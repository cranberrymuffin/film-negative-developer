import numpy as np
import matplotlib.pyplot as plt
import sys
import cv2

def single_channel_colorbalance(img, channel_no):
	"""
	a simple method to color balance a 1-channel image
	
	Parameters:
	1) img- a n channel numpy array representing an image (float32)
	2) channel_no- the channel to rebalance

	Returns
	An image with 1-channel (specified by parameter channel_no) remapped to be between 0.0-1.0 (float32)
	"""
	channel = img[:, :, channel_no]
	return (channel - np.min(channel))/(np.max(channel) - np.min(channel))


def simple_colorbalance(img):
	"""
	a simple method to color balance a 3-channel image
	
	Parameters:
	1) img- a 3 channel numpy array representing an image (float32)

	Returns
	An image with each channel remapped to be between 0.0-1.0 (float32)
	"""

	channel_1 = single_channel_colorbalance(img, 0)
	channel_2 = single_channel_colorbalance(img, 1)
	channel_3 = single_channel_colorbalance(img, 2)

	return np.stack((channel_1, channel_2, channel_3), axis = -1)

def invert_film_negative(img):
	"""
	Parameters:
	1) img- a 3-channel np array representing film negative

	Returns:
	an inverted film negative
	"""
	return 1.0 - img.astype('float32')

def read_negative(img_filename):
	"""
	Parameters:
	1) file name- a string representing the location of a scan of a film negative

	Returns:
	an rgb (float32) 3-channel array representing the film negative
	"""
	return cv2.cvtColor(cv2.imread(img_filename), cv2.COLOR_BGR2RGB).astype('float32')


for i in range(1, len(sys.argv)):
    file_name = sys.argv[i]
    img_rgb = simple_colorbalance(invert_film_negative(read_negative(file_name)))
    plt.imshow(img_rgb)
    plt.show()
    writeable_img =  (cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR) * 255).astype('uint8')
    cv2.imwrite("processed_" + str(i) + ".png", writeable_img)
