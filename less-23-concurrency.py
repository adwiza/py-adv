import urllib3
import threading


class FetchUrls(threading.Thread):
    """
    Thread checking URLs.
    """

    def __init__(self, urls, output):
        """
        Constructor.
        :param urls: list of urls to check
        :param outputs: file to write urls output
        """
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output

    def run(self):
        """
        Thread run method. Check URLs one by one.
        :return:
        """
        while self.urls:
            url = self.urls.pop()
            req = urllib3.request(url=url, method='GET')
            try:
                d = urllib3.HTTPResponse(req)
            except urllib3.response.HTTPError as e:
                print('URL %s failed: %s' % (url, e))
            self.output.write(d.read())
            print('Write done by %s' % self.name)
            print('URL %s fetched by %s' % (url, self.name))


def main():
    # list 1 of urls to fetch
    urls1 = ['https://google.com', 'https://ye.com']
    urls2 = ['https://yahoo.com', 'https://youtube.com']
    f = open('output.txt', 'w+')
    t1 = FetchUrls(urls1, f)
    t2 = FetchUrls(urls2, f)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()


if __name__ == '__main__':
    main()






