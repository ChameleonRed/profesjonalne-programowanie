import collections
import logging
import os.path
import pprint
import ssl
import urllib.request



def main():
    logging.basicConfig(level=logging.DEBUG)
    wiki_url = 'https://ws-export.wmcloud.org/?lang=pl&format=txt&page=Krzy%C5%BCacy_(Sienkiewicz,_1900)'
    file_name = 'text.txt'
    if not os.path.exists(file_name):
        # download
        logging.info('Downloading.')
        request = urllib.request.Request(wiki_url, headers={'User-Agent': 'FireFox'})
        with urllib.request.urlopen(request, context=ssl._create_unverified_context()) as f:
            text = f.read().decode('utf-8')
        logging.info('Downloaded.')

        # cache
        logging.info('Caching.')
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(text)
        logging.info('Cached.')
    else:
        # read
        logging.info('Reading from cache.')
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()
        logging.info('Read from cache.')
    words = text.split()
    words = [x1.strip('.,:!?„“"();—•*↑∗-') for x1 in words]
    words = [word for word in words if word.isalpha() or word.replace('-', '').isalpha()]
    unique_words = collections.Counter(words)
    logging.info('Split into %s words.', len(unique_words))

    logging.info(max(len(x) for x in words))
    # print(unique_words)
    sorted_words = sorted(unique_words.items(), key=lambda x: -len(x[0]) * x[1])
    # print(sorted_words)

    # digrams
    queue = collections.deque()
    digrams = collections.Counter()
    queue.extend(words[0:1])
    for word in words[1:]:
        queue.append(word)
        digrams.update([tuple(queue)])
        queue.popleft()

    pprint.pprint(digrams.most_common(50))

    # trigrams
    queue = collections.deque()
    trigrams = collections.Counter()
    queue.extend(words[0:2])
    for word in words[2:]:
        queue.append(word)
        trigrams.update([tuple(queue)])
        queue.popleft()

    pprint.pprint(trigrams.most_common(50))


if __name__ == '__main__':
    main()
