# SiteStatus
SiteStatus is an automated tool to check whether the host is reachable on the web using HTTP/HTTPS protocols.



## Installation
### Github
```
git clone https://github.com/irfvn/SiteStatus.git
cd SiteStatus
pip install -r requirements.txt
```

## Usage
This will display help for the tool:

`python status.py --help` or  `python status.py manual`


### Running SiteStatus with a single host
This is return whether the host is reachable on the web and its response code: 

```python status.py url <url of website>```

eg. python status.py url www.google.com





### Running SiteStatus with file input
* Place a file containing the list of hosts into the same folder.
* Ensure there is only one host per line and the last line is empty.
* Default timeout is 5 seconds.


#### All results
This will output the results of whether the list of hosts are reachable on the web into specified file: 

`python status.py file <file to read> <file to output>`

eg. python status.py file Hosts.txt Results.txt





#### Only Reachable Hosts
This will output the hosts reachable on the web into specified file: 

```python status.py file <file to read> <file to output> -r``` or ```python status.py file <file to read> <file to output> --reachableurl```

eg. python status.py file Hosts.txt Results.txt --reachableurl

eg. python status.py file Hosts.txt Results.txt -r




## References
This will help to understand the response code: https://www.restapitutorial.com/httpstatuscodes.html
  
