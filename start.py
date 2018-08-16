"""
scrapy框架程序启动文件
"""
import scrapy.cmdline


def main():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'chinahr'])


if __name__ == '__main__':
    main()
