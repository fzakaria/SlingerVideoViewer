import os
from flask import Flask, render_template
# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.config.from_object('config.DevelopmentConfig')
if 'CONFIG_SETTINGS' in os.environ:
    application.config.from_object(os.environ['CONFIG_SETTINGS'])

@application.route('/sling/<video_id>')
def video(video_id):
    mp4_url = 'https://s3-us-west-2.amazonaws.com/slinger-prod2/vo/{0}'.format(video_id)
    hls_url = 'https://s3-us-west-2.amazonaws.com/slinger-prod2/v/{0}/{0}.m3u8'.format(video_id)
    show_disqus = application.config['ENABLE_DISQUS']
    return render_template( "video.html", show_disqus=show_disqus, hls_url=hls_url, mp4_url=mp4_url)


@application.route('/ping')
def ping():
    return 'pong'

# run the application.
if __name__ == "__main__":
    application.run()