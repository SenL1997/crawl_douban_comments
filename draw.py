from os import path
import codecs
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pylab as plt
from scipy.misc import imread
font_path = './1.TTF'
# image_path = './1.png'
image_path = './3.jpg'
stopwords = STOPWORDS.union(set([x.strip() for x in open(path.join(path.dirname(__file__), 'stopwords'), encoding='utf-8').read().split('\n')]))

if __name__ == '__main__':
    d = path.dirname(__file__)
    image = imread(image_path)
    text = codecs.open(path.join(d, 'des.txt'), 'rb', encoding='utf-8').read()
    # wordcloud = WordCloud(font_path=font_path, mask=image, stopwords=stopwords, background_color='white', max_words=2000).generate(text)
    wordcloud = WordCloud(font_path=font_path, mask=image, stopwords=stopwords, background_color='white', max_words=2000, max_font_size=200).generate(text)
    image_color = ImageColorGenerator(image)
    plt.imshow(wordcloud.recolor(color_func=image_color))
    plt.axis('off')
    plt.show()
