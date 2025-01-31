# HNG Stage 0 Public API Deployment

## DESCIPTION
Devlopment and deployment of a public API that return your registered HNG12 slack workspace, current datetime in ISO 8601 and GitHub URL

## INSTALLATION
Run the code to install requirements needed
```sh
  python -m pip install -r Requirements.txt
```
## RUN SEVER 
To start the server,run
```sh
    uvicorn main.app --reload
```
## API Specification
### Endpoint
 GET returns email,current datetime is ISO 8601 and the Github URL
#### Endpoint URL
```sh
    https://hngstage0-production-b2cc.up.railway.app/
```

### Example of the required JSON Response Format 
```sh
{
  "email": "olola1720@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Ololaloluwa/HNG_STAGE_0"
}

```
## BACKLINKS
[https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)
