import cv2
import numpy as np
import matplotlib.image as img          # pip install matplotlib
import matplotlib.pyplot as plt
from scipy.cluster.vq import whiten     # pip install scipy
from scipy.cluster.vq import kmeans
import pandas as pd                     # pip install pandas

def fetch_image(img_path):
    img = cv2.imread(img_path)
    #print(img)
    #removing white pixels
    #for i in range(len(img)):
        #if img[i] == [0,0,0] or img[i] == [255,255,255]:
            #img[i].pop()
    return img


def process_image(img_matrix):
    r = []
    g = []
    b = []
    for row in img_matrix:
        for temp_r, temp_g, temp_b, temp in row:
            r.append(temp_r)
            g.append(temp_g)
            b.append(temp_b)
    
    batman_df = pd.DataFrame({'red' : r,'green' : g,'blue' : b})
    
    batman_df['scaled_color_red'] = whiten(batman_df['red'])
    batman_df['scaled_color_blue'] = whiten(batman_df['blue'])
    batman_df['scaled_color_green'] = whiten(batman_df['green'])
    
    cluster_centers, _ = kmeans(batman_df[['scaled_color_red',
                                        'scaled_color_blue',
                                        'scaled_color_green']], 3)
    
    dominant_colors = []
    
    red_std, green_std, blue_std = batman_df[['red',
                                            'green',
                                            'blue']].std()
    
    for cluster_center in cluster_centers:
        red_scaled, green_scaled, blue_scaled = cluster_center
        dominant_colors.append((
            red_scaled * red_std / 255,
            green_scaled * green_std / 255,
            blue_scaled * blue_std / 255
        ))
    
    plt.imshow([dominant_colors])
    plt.show()


if __name__ == '__main__':
    process_image(fetch_image('image.png'))