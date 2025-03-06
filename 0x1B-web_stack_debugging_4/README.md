This directory contains the web stack debugging 4 project, a last of it's kind.
The aim is to debug a web server that does terribly under pressure ie it's getting a huge amount of failed requests.
For the benchmarking, ApacheBench is used which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, 2000 requests are made to the server with 100 requests at a time but a large portion are failed requests. let’s fix our stack shall we!!
