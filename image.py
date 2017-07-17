import re
import os
import time
import json
import requests
import urllib.request
from images_jason import jason_text

z = jason_text()
for i in range(0, len(z)):
	image_url = z[i]['url']
	image_name = z[i]['fileName']

	file_path = os.environ['HOME'] + '/Pictures/farcon_images/' + image_name
	if os.path.exists(file_path) is False:
		urllib.request.urlretrieve(image_url, filename=file_path)
	else:
		pass


