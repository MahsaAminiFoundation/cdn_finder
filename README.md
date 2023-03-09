# cdn_finder
Find working cloudflare pops for MahsaAminiVPN


# Using Ubuntu 22
```
python pop_checker.py
```


# Using Docker
Build docker image:

```
docker build --tag cdn-checker-docker .
```

Run the image:
```
docker run -it cdn-checker-docker
```


# Program output

After checking all the pops, the program will print something like this:
```
.
.
.
Best 10 pops:
whatruns.com,mediaad.org,avval.ir,104.22.59.173
````

Send the last line for VPN Admins to use as best pops