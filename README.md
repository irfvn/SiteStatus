# SiteStatus
SiteStatus is an automated tool to check whether the host is reachable on the web using HTTP/HTTPS protocols.

![image](https://user-images.githubusercontent.com/64763142/118615344-363f8300-b7f3-11eb-8413-2e8214135013.png)

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

![image](https://user-images.githubusercontent.com/64763142/118622699-25464000-b7fa-11eb-8ac3-e016bd4cf64e.png)
![image](https://user-images.githubusercontent.com/64763142/118622928-53c41b00-b7fa-11eb-894d-e94498265bdf.png)



### Running SiteStatus with file input
* Place a file containing the list of hosts into the same folder.
* Ensure there is only one host per line and the last line is empty.
* Default timeout is 5 seconds.


#### All results
This will output the results of whether the list of hosts are reachable on the web into specified file: 

`python status.py file <file to read> <file to output>`

eg. python status.py file Hosts.txt Results.txt

![image](https://user-images.githubusercontent.com/64763142/118617146-ed88c980-b7f4-11eb-83c0-79cadaa3e7ae.png)



#### Only Reachable Hosts
This will output the hosts reachable on the web into specified file: 

```python status.py file <file to read> <file to output> -r``` or ```python status.py file <file to read> <file to output> --reachableurl```

eg. python status.py file Hosts.txt Results.txt --reachableurl

eg. python status.py file Hosts.txt Results.txt -r

![image](https://user-images.githubusercontent.com/64763142/118622351-ce406b00-b7f9-11eb-8123-4bbe436f2552.png)
![image](https://user-images.githubusercontent.com/64763142/118622438-e87a4900-b7f9-11eb-8210-d9234846cec9.png)


## References
This will help to understand the response code: https://www.restapitutorial.com/httpstatuscodes.html
  
