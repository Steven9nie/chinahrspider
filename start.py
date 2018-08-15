import scrapy.cmdline


def main():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'chinahr'])


if __name__ == '__main__':
    main()
