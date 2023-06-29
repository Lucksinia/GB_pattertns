from webob import Request, Response
from urllib.parse import unquote_plus

from utils import SOLID, KISS, save_data


class API:
    def __init__(self):
        self.routes = {}
        self.solid = SOLID[0]  # for hidden principles
        self.kiss = KISS[0]

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            self.routes[f"{path}/"] = handler
            return handler

        return wrapper

    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)
        method = environ["REQUEST_METHOD"]

        print(f"method {method}")

        if method == "GET":  # example: http://127.0.0.1:8080/?lesson=3&try=17
            query_string = environ["QUERY_STRING"]
            request_params = self.parse_input_data(query_string)
            print(request_params)  # Console debug
            if request_params != {}:
                save_data(request_params, "GET")

        if method == "POST":
            content_length_data = environ["CONTENT_LENGTH"]
            content_length = int(content_length_data) if content_length_data else 0
            data = (
                environ["wsgi.input"].read(content_length)
                if content_length > 0
                else b""
            )
            data = data.decode(encoding="utf-8")

            request_params = self.parse_input_data(unquote_plus(data))

            print(request_params)  # Console debug

            if "solid" in request_params:  # if solid, then render it out
                self.solid = self.get_solid(request_params)

            if "kiss" in request_params:  # (TODO: SOLIDify it)
                self.kiss = self.get_kiss(request_params)

            if request_params != {} and "solid" not in request_params:
                save_data(request_params, "POST")

        return response(environ, start_response)

    def handle_request(self, request):
        response = Response()
        for path, handler in self.routes.items():
            if path == request.path:
                handler(request, response)
                return response
        self.response_404(response)
        return response

    def get_solid(self, request_params):
        try:
            self.solid = SOLID[int(request_params["solid"])]
            return self.solid
        except:
            pass

    def get_kiss(self, request_params):
        try:
            self.kiss = KISS[int(request_params["kiss"])]
            return self.kiss
        except:
            pass

    @staticmethod
    def response_404(response):
        response.status_code = 404
        response.text = "404 - Not found"

    @staticmethod
    def parse_input_data(data):
        result = {}
        if data:
            params = data.split("&")
            for item in params:
                k, v = item.split("=")
                result[k] = v
        return result
