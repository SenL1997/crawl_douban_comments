import os
from pyltp import Segmentor, SentenceSplitter
import codecs


LTP_DATA_DIR = './ltp_data'
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')

segmentor = Segmentor()
segmentor.load_with_lexicon(cws_model_path, './extension')

if __name__ == '__main__':
    with codecs.open('des.txt', 'wb', encoding='utf-8') as f:
        f1 = codecs.open('./comments_1.txt', 'rb', encoding='utf-8')
        for line in f1:
            des = ' '.join(segmentor.segment(line))
            f.write(des)
        f1.close()
        f2 = codecs.open('./comments_2.txt', 'rb', encoding='utf-8')
        for line in f2:
            des = ' '.join(segmentor.segment(line))
            f.write(des)
        f2.close()

