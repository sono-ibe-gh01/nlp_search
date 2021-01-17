import os, glob, re


def read_documents(path):
    # データは下記からダウンロード:
    # https://www.rondhuit.com/download/ldcc-20140209.tar.gz
    documents = []
    folders = glob.glob(path)
    for folder in folders:
        category = re.split('[/\\\]', folder)[-1]
        if os.path.isdir(folder):
            files = glob.glob(folder + '/*')
            print('Found {} files in category {} ...'.format(len(files), category))
            for i, file in enumerate(files):
                if i % 30 != 0:  # デバッグ用に読み込む文書量を削減
                    continue
                f = open(file, 'r', encoding='UTF-8')
                documents.append([f.read(), category, re.split('[/\\\]', file)[-1]])
                f.close()
    print('Totally, {} documents are read.'.format(len(documents)))
    return documents

def print_search_results(scores, documents):
    print('--- search results ---')
    for i in range(10):
        print('rank {} (score: {:.7f}): {}...'
              .format(i + 1, scores[i][0], documents[scores[i][1]][0][:200].replace('\n', ' ')))
