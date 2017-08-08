# Color Picker
pick most used colors.

The file format does not matter. At least jpg and png are possible.

사진에서 많이 사용된 색을 골라줍니다. 5개까지 제대로 나오는 듯?

코드를 작성하는 것보다 라이브러리 다운로드 받는게 더더더더더 힘들었습니다..


## Requirements
- sklearn
- numpy
- matplotlib
- opencv


## How to use
### use with Flask
1. run pick_colors_with_flask.py

2. using Tool like PostMan
```
POST /pick/colors/<int:num>
Host: localhost:5000
Content-Type: multipart/form-data
Kye: img
Values: file, your image
```
I recommend that you only include `num` up to 5

3. get colors!
```
{
    "colors": [
        {
            "rgb": [ 30, 25, 24 ],
            "hex": "#1e1918"
        }
}
```

### use with argparse
```
python pick_colors_with_argparse.py --image images/your_image.png --clusters 3
```


## Reference
- [OpenCV and Python K-Means Color Clustering](http://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/)
- [Ubuntu 16.04에 opencv_contrib 포함하여 OpenCV 3.2 설치](http://webnautes.tistory.com/1030)