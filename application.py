from flask import Flask, render_template
# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/sling/<video_id>')
def video(video_id):
    mp4_url = 'https://s3-us-west-2.amazonaws.com/slinger-prod2/vo/{0}'.format(video_id)
    hls_url = 'https://s3-us-west-2.amazonaws.com/slinger-prod2/v/{0}/{0}.m3u8'.format(video_id)
    return render_template( "video.html", hls_url=hls_url, mp4_url=mp4_url)


@application.route('/ping')
def ping():
    return 'pong'

# run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = False
    application.run()