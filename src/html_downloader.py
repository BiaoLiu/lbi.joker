# coding:utf-8

import urllib.request
import json
from src import redis_manager

url = 'http://api.1-blog.com/biz/bizserver/xiaohua/list.do?maxXhid={0}&minXhid={1}&size={2}'
size = 5

class HtmlDownloader():
    def download(self):
        try:
            r = redis_manager.getrediscli()

            # 获取已有的最大笑话ID
            maxxhid = r.get('s:joke:maxxhid')
            # 获取已有的最小笑话ID
            minxhid = r.get('s:joke:minxhid')

            if not maxxhid or not minxhid:
                url2 = url.format('', '', size)
            else:
                url2 = url.format(maxxhid, minxhid, size)

            req = urllib.request.Request(url2)
            response = urllib.request.urlopen(req)
            content = response.read().decode()

            jokes = []
            if content:
                result = json.loads(content)['detail']

                # 设置已有的最大笑话ID
                if result[0]['xhid'] > int(maxxhid):
                    r.set('s:joke:maxxhid', result[0]['xhid'])

                for item in result:
                    content = item['content']
                    picurl = item['picUrl']
                    minxhid = item['xhid']

                    jokes.append(dict(content=content, picurl=picurl))

                # 设置已有的最小笑话ID
                r.set('s:joke:minxhid', minxhid)

            # content包含BOM字符 将BOM字符去掉
            # if content.startswith(u'\ufeff'):
            #     content = content.encode('utf8')[3:].decode('utf8')

            return jokes
        except Exception as e:
            print(e)
            return []
