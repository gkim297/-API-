import matplotlib.pyplot as plt
import requests
import hashlib
from PIL import Image
import matplotlib.image as mpimg

#이미지 불러오기
url = 'https://blossom.or.kr/wp/wp-content/uploads/2021/11/photo_9-scaled.jpg'
r = requests.get(url, stream=True).raw

#이미지 보여주기
image = Image.open(r)
print('Image: ', image.get_format_mimetype)
image.show()
image.save('src.png')

#이미지 복사
DEFAULT_SIZE = 1024
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        data = sf.read(DEFAULT_SIZE)
        if not data:
            break

        df.write(data)

SHA_src = hashlib.sha256()
SHA_dst = hashlib.sha256()

with open('src.png', 'rb') as sf, open('dst.png', 'rb') as df:
    SHA_src.update(sf.read())
    SHA_dst.update(df.read())

print("src.png's hash : {}".format(SHA_src.hexdigest()))
print("dsc.png's hash : {}".format(SHA_dst.hexdigest()))

#이미지 가공
plt.suptitle('Image processing', fontsize=18)
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))

plt.subplot(122)
plt.title('Testing Image')
DST_IMG = mpimg.imread('dst.png')
TEST_IMG = DST_IMG[:, :, 0]
plt.imshow(TEST_IMG)
plt.show()