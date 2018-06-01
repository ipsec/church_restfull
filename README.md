Create application at:
```
http://localhost:8000/o/applications/
```


Request token with:
```
curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/
```

Request Example:
```
curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/
```


Details: 

https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html#step-4-get-your-token-and-use-your-api
