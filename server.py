#!/usr/bin/env python3
import inspect, os, sys
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler as CGIHandler

def display_server_info(port):
    main_module_dirname = os.path.dirname(os.path.abspath(sys.argv[0]))
    print("Server's root directory:", main_module_dirname)
    print("Server's CGI directories:", CGIHandler.cgi_directories)
    print("Starting HTTP Server on port:", port)

def configure_server(host_ip):
    return HTTPServer((host_ip, 80), CGIHandler)

def main():
    try:
        server = configure_server(sys.argv[1])
    except Exception as e:
        print("Unable to start server:", e)
        return
    try:
        display_server_info(server.server_port)
        server.serve_forever()
    except BaseException as base:
        print()
        print("Exception:", base, "Shutting Down Server", sep="\n")
        server.shutdown()

if __name__ == "__main__":
    main()                                                                          
