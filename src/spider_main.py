# coding:utf-8

from src import html_downloader, email_manager

if __name__ == '__main__':
    downloader = html_downloader.HtmlDownloader()
    emailmanager = email_manager.EmailManager()

    jokes = downloader.download()
    emailmanager.send_email(jokes)

    print('send success!')
