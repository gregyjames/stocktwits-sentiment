#interface to stocktwits API
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Streamer():

    def __init__(self):
        self.url = "https://api.stocktwits.com/api/2/"
        self.headers = {'Content-Type': 'application/json'}

    def get_user_msgs(self, user_id, since=0, max=0, limit=0, callback=None, filter=None):

        """Returns the most recent 30 messages for the specified user.

        Args:
            user_id (int) = User ID or Username of the stream's user
                            you want to show (Required)
            since (int) = Returns results with an ID greater than (
                          more recent than) the specified ID.
            max (int) = Returns results with an ID less than
                        (older than) or equal to the specified ID.
            limit (int) = Default and max limit is 30.
                          This limit must be a number under 30.
            callback = Define your own callback function name,
                       add this parameter as the value.
            filter (string) = Filter messages by links, charts, or videos.
                              (Optional)

        Return:
            raw_json (dict) = The JSON output unparsed

        """

        url = self.url + 'streams/user/' + user_id + '.json'

        data = {
                 'since': '{}'.format(since),
                 'max': '{}'.format(max),
                 'limit': '{}'.format(limit),
                 # Fix when you figure out what this is
                 # 'callback' : '{}'.format(None),
                 'filter': '{}'.format(filter)
                }

        r = requests.get(url, headers=self.headers, params=data)
        if r.status_code != 200:
            raise Exception('Unable to Return Request {}'
                            .format(r.status_code))

        raw_json = r.json()
        return raw_json

    def get_symbol_msgs(self, symbol_id, since=0, max=0, limit=0, callback=None, filter=None):

        '''Returns the most recent 30 messages for the specified symbol.

        Args:
            symbol_id:	Ticker symbol, Stock ID, or
                        RIC code of the symbol (Required)
            since:	Returns results with an ID greater than (more recent than)
                    the specified ID.
            max:	Returns results with an ID less than (older than) or
                    equal to the specified ID.
            limit:	Default and max limit is 30. This limit must be a
                    number under 30.
            callback:	Define your own callback function name,
                        add this parameter as the value.
            filter:	Filter messages by links, charts, videos,
                    or top. (Optional)

        Return:
            raw_json (dict) = The JSON output unparsed

        '''

        url = self.url + 'streams/symbol/' + symbol_id + '.json'

        data = {
                 'since': '{}'.format(since),
                 'max': '{}'.format(max),
                 'limit': '{}'.format(limit),
                 # Fix when you figure out what this is
                 # 'callback' : '{}'.format(None),
                 'filter': '{}'.format(filter)
                }

        r = requests.get(url, headers=self.headers, params=data)
        if r.status_code != 200:
            raise Exception('Unable to Return Request {}'
                            .format(r.status_code))

        raw_json = r.json()
        return raw_json

    def get_specified_conversation_msgs(self, conversation_id, since=0, max=0, limit=0, callback=None):

        '''

        Args:
            conversation_id:	The message ID of the parent message
                                to a conversation. (Required)
            since:	Returns results with an ID greater than (more recent than)
                    the specified ID.
            max:	Returns results with an ID less than (older than) or equal
                    to the specified ID.
            limit:	Default and max limit is 30. This limit must be a
                    number under 30.
            callback:	Define your own callback function name, add this
                        parameter as the value.

        Return:
            raw_json (dict) = The JSON output unparsed

        '''

        url = self.url + 'streams/conversation/' + conversation_id + '.json'

        data = {
                 'since': '{}'.format(since),
                 'max': '{}'.format(max),
                 'limit': '{}'.format(limit)
                 # Fix when you figure out what this is
                 # 'callback' : '{}'.format(None),
                }

        r = requests.get(url, headers=self.headers, params=data)
        if r.status_code != 200:
            raise Exception('Unable to Return Request {}'
                            .format(r.status_code))

        raw_json = r.json()
        return raw_json
