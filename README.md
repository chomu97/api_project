# This is api project test.
## OPEN API library.
## How To Install?
```bash
pip install git+https://github.com/chomu97/api_project.git
```

## HOW TO USE?
```
from my_api import naver_api
naver_api.search_api(url, client_id, client_secret, params)
naver_api.translate_api(text, url,client_id, client_secret, source ="ko", target ="en")
```
### OPEN API reference.
#### search
https://developers.naver.com/docs/serviceapi/search/blog/blog.md#%EB%B8%94%EB%A1%9C%EA%B7%B8
#### papago
https://developers.naver.com/docs/papago/papago-nmt-api-reference.md
