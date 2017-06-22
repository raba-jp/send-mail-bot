# coding: utf-8

import os
from flask import Flask
from flask import render_template
# from slackclient import SlackClient

web = Flask(__name__)


def main():
    web.logger.info('Debug: {0}'.format(os.getenv('FLASK_DEBUG')))
    SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN')
    # slack_client = SlackClient(SLACK_API_TOKEN)

    if SLACK_API_TOKEN is None:
        raise RuntimeError()

    web.run()


@web.route("/")
def index():
    return render_template('index.html', message="Hello world")


if __name__ == '__main__':
    main()
