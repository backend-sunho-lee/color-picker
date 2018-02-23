from flask import Flask, request, make_response, jsonify

from sklearn.cluster import KMeans
import cv2
import numpy as np
import utils

app = Flask(__name__)


@app.route('/pick/colors/<int:num>', methods=['POST'])
def colorPicker(num):
    _img = request.files.get('img', None)

    #: load the image and convert it from BGR to RGB so that
    #: we can dispaly it with matplotlib
    image = np.asarray(bytearray(_img.read()), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #: reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    #: cluster the pixel intensities
    clt = KMeans(n_clusters=num)
    clt.fit(image)

    #: build a histogram of clusters and then create a figure
    #: representing the number of pixels labeled to each color
    hist = utils.centroid_histogram(clt)
    colors, bar = utils.plot_colors(hist, clt.cluster_centers_)

    result = []
    for color in colors:
        temp = {}
        temp['rgb'] = color
        hexcolor = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
        temp['hex'] = hexcolor

        result.append(temp)

    return make_response(jsonify(colors=result))


if __name__ == '__main__':
    app.run()
