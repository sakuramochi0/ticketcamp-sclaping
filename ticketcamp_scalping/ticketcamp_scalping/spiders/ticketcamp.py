# -*- coding: utf-8 -*-
import re
from dateutil.parser import parse
import scrapy


class TicketcampSpider(scrapy.Spider):
    name = 'ticketcamp'
    allowed_domains = ['ticketcamp.net']

    def start_requests(self):
        """作品一覧を作成して、各作品を parse_work() に渡して処理する。"""
        work_url_base = 'https://ticketcamp.net/{work}-tickets/?count=all&extra_payment=all&filter=active&origin=&place_id=&section_id=all&sort=new#ticket-list-content/'

        # TODO: プリティーリズム以外の作品を集めてくる
        works = ['prettyrhythm']
        for work in works:
            work_url = work_url_base.format(work=work)
            yield scrapy.Request(work_url, self.parse_work)

    def parse_work(self, response):
        """各作品ごとのチケット一覧ページを処理する。"""
        tickets = response.css('.content ul.row')
        for t in tickets:
            # リストから取得できるチケット情報を data に保存しておく
            data = {}
            data['user_id'] = response.css('li::attr(data-owner-id)').extract_first()
            data['url'] = t.css('.h a::attr(href)').extract_first()
            m = re.search(r'event-(\d+)/(\d+)/', data['url'])
            data['event_id'] = m.group(1)
            data['ticket_id'] = m.group(2)
            data['event_group_name'] = t.css('.h a::text').extract_first().strip()
            # チケット枚数は「n枚」と「n〜m枚」の場合がある。
            # 後者の場合はバラ売りが可能であることを示しているだけで、
            # 実質的にm枚販売していることになるので、m枚と見なすことにする
            ticket_num = t.css('.ticket-num').extract_first()
            data['ticket_num'] = int(re.search(r'〜?(\d+)', ticket_num).group(0))
            data['price'] = int(t.css('.ticket-price::attr(data-price)').extract_first())

            # チケット詳細ページの URL を取得して移動する
            request = scrapy.Request(data['url'], self.parse_ticket)
            request.meta['data'] = data
            yield request

        # 100件を超える場合には「次へ」ボタンがあるため、
        # 次のページのURLを取得して、その URL で再び `parse()` を呼び出す
        next_url = response.css('li.next a::attr(href)').extract_first()
        next_url = response.urljoin(next_url)
        yield scrapy.Request(next_url, self.parse)

    def parse_ticket(self, response):
        """チケット詳細ページを処理する。"""
        data = response.meta['data']

        # チケット情報を取得
        headers = response.css('.module-ticket-info table tr th::text').extract()
        elements = response.css('.module-ticket-info table tr td')
        for header, element in zip(headers, elements):
            if header == '公演名':
                url = element.css('a::attr(href)').extract_first()
                data['event_group_id'] = re.search(r'\d+$', url).group(0)
            if header == '登録日':
                time_str = element.css('::text').extract_first().strip()
                time_str = ' '.join(re.split(r'\([月火水木金土日]\)', time_str))
                data['created_time'] = parse(time_str, yearfirst=True)

        # ユーザー情報を取得
        
        yield data
        
            
