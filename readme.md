requirements: docker, python

libraries: fastapi, uvicorn, pydantic

How to use:
```bash
 git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-II/Ex1_YanivLavi.git
 cd Ex1_YanivLavi
 docker build -t fastapi_demo .
 docker run -ti -p 8989:8080 fastapi_demo
 python test.py
```
