##20171213
from PIL import Image
import numpy as np
# import scipy
import matplotlib.pyplot as plt

##def ImageToMatrix(filename):
##    # 读取图片
##    im = Image.open(filename)
##    # 显示图片
###     im.show()  
##    width,height = im.size
##    im = im.convert("I") 
##    data = im.getdata()
##    data = np.matrix(data,dtype='float')/255.0
##    #new_data = np.reshape(data,(width,height))
##    new_data = np.reshape(data,(height,width))
##    return new_data
###     new_im = Image.fromarray(new_data)
###     # 显示图片
###     new_im.show()
##def MatrixToImage(data):
##    data = data*255
##    new_im = Image.fromarray(data.astype(np.uint8))
##    return new_im
##
##
##
##filename = 'test001.png'
##data = ImageToMatrix(filename)
##print (data)
##new_im = MatrixToImage(data)
##plt.imshow(data, cmap=plt.cm.gray, interpolation='nearest')
##new_im.show()
###new_im.save('result001.bmp')

def ClearRed(filename):
    im = Image.open(filename)
    width,height = im.size
    Img_data = im.getdata()   #ImagingCore
    Img_data = np.array(Img_data) #numpy.ndarray
    
    Img_data = Img_data.reshape(height,width,3)  #转为像素图,h和w需反写

    #print(type(Img_data[0][0][0]))
    
    for w in range(width):
        for h in range(height):
            for i in range(3):
                if i == 0:
                    Img_data[h][w][i] = 0;
                    pass
                    
    return Img_data

filename = 'test001.png'
Img = ClearRed(filename)

plt.figure("test001.png")
plt.imshow(Img/255.0)   #取值0.0～1.0
plt.axis('off')
plt.show()

