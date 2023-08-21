##User 1 codes:

import imageio
import numpy as np
import os
import struct

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def mse2psnr(x):
	return -10.*np.log(x)/np.log(10.)

def write_image_imageio(img_file, img, quality):
	img = (np.clip(img, 0.0, 1.0) * 255.0 + 0.5).astype(np.uint8)
	kwargs = {}
	if os.path.splitext(img_file)[1].lower() in [".jpg", ".jpeg"]:
		if img.ndim >= 3 and img.shape[2] > 3:
			img = img[:,:,:3]
		kwargs["quality"] = quality
		kwargs["subsampling"] = 0
	imageio.imwrite(img_file, img, **kwargs)

def read_image_imageio(img_file):
	img = imageio.imread(img_file)
	img = np.asarray(img).astype(np.float32)
	if len(img.shape) == 2:
		img = img[:,:,np.newaxis]
	return img / 255.0

def srgb_to_linear(img):
	limit = 0.04045
	return np.where(img > limit, np.power((img + 0.055) / 1.055, 2.4), img / 12.92)
