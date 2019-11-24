# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: world_bank_excel.py
@time: 2018/6/30 下午3:21

这一行开始写关于本文件的说明与解释
"""
import logging
import os

import requests
import tqdm
from pyquery import PyQuery as pq


def get_url_list():
    wb_url = 'https://data.worldbank.org.cn'
    root_url = 'https://data.worldbank.org.cn/country'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.3.1250981148.1530342937; _gid=GA1.3.942515468.1530342937; uvts=7gXZC41o09odqcs5; _4c_=fVLZbuM4EPwVgcDmyaF46KAMGIEvJJlBHOQYA7MvBi9bgmXJoaQoB%2FLvadrZIJvBrh4oFlndXdXsV9TntkJDGnPCIx4JnmbxAG3tc4OGr0jv%2Ffrol7vVNJdVZctgKV0hVWnREBmrg752pQmUrLaBka0MXvLAPrVogDpXAiVv230zDEN%2Fhw9cT8W122BdhbruqtY9hyrvWlmdPRa2H%2BlcOh8%2Fsa28K1pfZwFQubpvrAM0zV29s0GSwqmujSfQDHMcAV6DYkRZTDJBaSTw0RjLuCfXYApdSQ1bZ9fWuUO6fxT2fY%2BVLEyHdb0Ly6LanoGF0aWd3LPbdfOw0%2BfP%2By2bjbt6%2BvPlYVHO6k31Y54sdL9Y5X%2Bf6u63Wu4uu8Xy9GLuXrq2ny2jzeNJb0Yn9qEwI5MyJdhaE0KShDALf%2F%2FxWPEUkFfYHP3%2Bq09w3Fq389phe311f7uazMfT68VX7WpT1kqW0HlMKcOsTnFl21CFTfP1cvAXI72qimZv%2FIPASUjDC8wSzMJGCJERxpKUEBanZ%2BObyYiejG%2FmIwp19zAFKIZNWWtIBcBWXtr5ePXrcvafTX8boKfjeAEWggrCwU4LkyGS6GAfGK4wH3OGBNUmlTSLuTZSRtAsHkueGCVSwYnwT3fMB5VEFiUZ5ZBgD%2FkO8fSzHI9TP84R%2ByhHo89y3sqBDZP%2BTRz5U9znW6zA8P%2BERt9D397eAQ%3D%3D',
        'Host': 'data.worldbank.org.cn',
        'If-None-Match': 'W/"46911-R6hI3+xgGicp+6kjVKpwYA"',
        'Referer': 'https://data.worldbank.org/country',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    res = requests.get(root_url, headers)

    url_list = []
    if res.status_code == 200:
        res_utf = (res.content).decode('utf-8')
        country_nums = len(pq(res_utf)('.nav-item'))
        for i in range(country_nums):
            res_table = pq(pq(res_utf)('.nav-item')[i])
            res_li = res_table('li')
            for i in range(len(res_li)):
                country_url = pq(pq(res_li)[i])('a').attr('href')
                country = pq(pq(res_li)[i])('a').text()
                url_list.append((country, wb_url + country_url))
                print('country:', country)
    return url_list


def save_excel_url():
    save_list = []
    url_list = get_url_list()
    for url_tuple in url_list:
        url = url_tuple[1]
        country = url_tuple[0]
        print("正在获取[{}]的EXCEL地址:".format(country))
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.3.1250981148.1530342937; _gid=GA1.3.942515468.1530342937; uvts=7gXZC41o09odqcs5; _4c_=fVLZbuM4EPwVgcDmyaF46KAMGIEvJNlFHORYAzMvBi9bgmXJoaQoB%2FLvadqZILPBjh6obrJYXdXsV9TntkJDGnPCYyKSKEmSAdra5wYNX5He%2B%2FXRL3eraS6rypbBUrpCqtKiITJWB33tShMoWW0DI1sZvOSBfWrRAHWuBEjetvtmGIb%2BDB%2BwHoprt8G6CnXdVa17DlXetbI6eyxsP9K5dP7%2BxLbyrmh9nQWkytV9Yx1k09zVOxskKezq2ngAzTDHEeRrUIwoi0kmKI0EPhiLWMY9uAZT6EpqCJ1dW%2BcOdL8U9n2PlSxMh3W9C8ui2p6BhdGlndyz23XzsNPnz%2Fstm427evrPy8OinNWb6u95stD9YpX%2FPNXdD7XcXXaL5enF3L10bT9bRpvHk96MTuxDYUYmZUqwtSaEJAlhFv7%2B47HiKWReYXP0%2B1ufYLu1bue1Q3h9dX%2B7mszH0%2BvFV%2B1qU9ZKltB5TCnDrE5xZdtQhU3z9XDwFyO9qopmb%2FyDwE5IwwvMEszCRgiREcaSlBAWp2fjm8mInoxv5iMKdfcwBdBYiMpaAxdktvLazserfy9n%2F9v1twF6Os5XxFPKKUko%2BGlhNGDYDv4B4QrzMWhIUG1SSbOYayNlBN3iseSJUSIVnAj%2Fdkc%2BqCSyKMkoB4I98B3uA%2FlHOR6nPBKg4qMcjT7LeS9HNBz%2BRx35ru7zNVbg%2BE93vzl7e3sH',
            'Host': 'data.worldbank.org.cn',
            'If-None-Match': 'W/"3ed70-ZDoDyD/pAoppwhz6LOpE/Q"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }

        res = requests.get(url, headers)
        if res.status_code == 200:
            res_utf = res.content.decode('utf-8')
            # print(res_utf)
            res_excel = pq(pq(pq(pq(res_utf)('.buttonGroup'))('div'))('a')[2]).attr('href')
            res_csv = pq(pq(pq(pq(res_utf)('.buttonGroup'))('div'))('a')[0]).attr('href')
            save_list.append((country, res_excel))
            print(res_excel)
            print('\n*****************************************\n')
    return save_list


def download_excel(path):
    download_list = [url[1] for url in save_excel_url()]
    with open(os.path.join(path, 'download_excel.sh'), mode='w', encoding='utf-8') as f:
        for i in download_list:
            download_str = 'wget {}'.format(i)
            print(download_str)
            f.write(download_str + '\n')
    print('||||||||||||||||||\n下载脚本完成，移步{}运行{}进行下载\n||||||||||||||||||'.format(path, 'download_excel.sh'))
    script_file = 'sh {}/download_excel.sh'.format(path)
    os.system(script_file)


def download(url, dst):
    """
    给定 url，目标路径，stream 下载，附进度条
    :param url: str，下载 url
    :param dst: str，目标路径
    :return: 文件大小
    """
    print('-----url---->>', url)
    try:
        with requests.get(url, stream=True, timeout=3) as r:
            if r.status_code == 404:
                print('404')
                return 0
            file_size = int(r.headers.get('Content-Length'))
    except Exception as e:
        logging.warning(e)
        return 0

    if os.path.exists(dst):
        first_byte = os.path.getsize(dst)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size
    logging.info('--- %s is downloading... ---' % url)
    header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
    pbar = tqdm.tqdm(
        total=file_size, initial=first_byte,
        unit='B', unit_scale=True, desc=url.split('/')[-1])
    try:
        req = requests.get(url, headers=header, stream=True, timeout=3)
    except Exception as e:
        logging.warning(e)
        return 0
    with(open(dst, 'ab')) as f:
        try:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)
        except Exception as e:
            logging.warning(e)
    pbar.close()
    return file_size


if __name__ == '__main__':
    path = '/data/share/excel/world_bank'
    download_excel(path)

    #
    # <section class="nav-item" data-reactid="326"><h3 data-reactid="327">不</h3>
    #     <ul data-reactid="328">
    #         <li data-reactid="329"><a data-customlink="nl:body content" data-text="不丹" href="/country/bhutan?view=chart"
    #                                   data-reactid="330">不丹</a></li>
    #     </ul>
    # </section>
    #

