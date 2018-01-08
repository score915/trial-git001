# -*- coding: utf-8 -*-
from google import search

def google_search(query, limit=10):
    for url in search(query, lang="jp", num=limit):
        print(url)


#def main():
#    google_search("qiita")
google_search("qiita")

#if __name__ == '__main__':
#    main()
