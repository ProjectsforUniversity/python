# install and import Flask framework
#pip install flask
from flask import Flask

app = Flask(__name__)
# define flask route
@app.route('/')
def home():
  return "Welcome to the URL shortener!"
# implement shortening logic
@app.route('/shorten/<path:url>')
def shorten(url):
  # generate unique identifier
  short_id = str(len(urls) + 1)
  urls[short_id] = url
  # Return the shortened URL
  shortened_url = f"http://your-domain.com/{short_id}"
  return f"shortened URL: {shortened_url}"
# redirect to original URL
@app.route('/<short_id>')
def redirect_url(short_id):
  if short_id in urls:
    original_url = urls[short_id]
    return redirect(original_url)
  else:
    return "URL not found"
# run application
if __name__ == '__main__':
  app.run()
