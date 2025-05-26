from pypette import PyPette, redirect
from pypette import static_file

app = PyPette()


@app.route("/static/:filename", method='GET')
def static(request, filename):
    rv = static_file(request, filename, 'static')
    return rv


@app.route('/')
def home(request):
    return redirect(request, '/image/1')


@app.route('/image/:image_id')
def show_image(request, image_id):

    image_id = int(image_id)
    if image_id < 1 or image_id > 5:
        return redirect(request, '/image/1')

    prev_id = image_id - 1 if image_id > 1 else 5
    next_id = image_id + 1 if image_id < 5 else 1
    numbers = range(1,6)
    return app.templates.load('base.tpl').render(locals())


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, app)
    print("Serving on port 8000...")
    httpd.serve_forever()
