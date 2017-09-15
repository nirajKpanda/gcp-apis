import io
from google.cloud import vision

v_c = vision.Client()
#filename = '220px-Kevin_Spacey,_May_2013.jpg'
filename = '220px-IPhone_X_vector.svg.png'

with io.open(filename, 'rb') as fp:
    content = fp.read()
    image = v_c.image(content=content)

lables = image.detect_labels()
for label in lables:
    print label.description
