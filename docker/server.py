from logging import StreamHandler
from requestlogger import WSGILogger, ApacheFormatter


from app import wsgi

app = wsgi()

app_w_logging = WSGILogger(app,
                           [StreamHandler(),],
                           ApacheFormatter(),
                           ip_header='X-Forwarded-For')

if __name__ == '__main__':
    import argparse
    import bjoern

    parser = argparse.ArgumentParser()

    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', default=8080, type=int)

    args = parser.parse_args()

    print(f'Starting server on {args.host}:{args.port}')
    bjoern.run(app_w_logging, args.host, int(args.port))
