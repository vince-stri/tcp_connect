# tcp_connect
```sh
 usage: tconnect.py [-h] -m {client,server} -H HOST
                   (-i INP | -p [PORT ...])

TConnect : test for a TCP connection.

options:
  -h, --help            show this help message and exit
  -m {client,server}, --mode {client,server}
                        Server or client mode
  -H HOST, --host HOST  Server: listening interface (ip); Client:      
                        Host server to reach
  -i INP, --inp INP     Port list from a text file (one port per       
                        line). Override --port option
  -p [PORT ...], --port [PORT ...]
                        Port list (separated by a space)

```