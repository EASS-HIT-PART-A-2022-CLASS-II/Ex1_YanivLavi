requirements: docker, python

libraries: fastapi, uvicorn, pydantic

How to use:
```bash
 git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-II/Ex1_YanivLavi.git
 cd Ex1_YanivLavi
 docker build -t fastapi_demo .
 docker run -ti -p 8989:8080 fastapi_demo
```

Try to add a new track using curl or using docs http://127.0.0.1:8989/docs 
```
curl -X 'POST' \
  'http://127.0.0.1:8989/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 0,
  "name": "asdasd",
  "artist": "asdsad",
  "type": "mp3",
  "length": "3:14",
  "size": "12155KB",
  "created": "12/12/2013",
  "path": "/sdad/asddasd/sad.mp3"
}'

 ```
