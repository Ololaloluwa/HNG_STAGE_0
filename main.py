from fastapi import FastAPI,status
from datetime import timezone,datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/" ,status_code = status.HTTP_200_OK )
def user_id():
  date_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
  return {
  "email": "olola1720@gmail.com",
  "current_datetime":  date_time,
  "github_url": "<https://github.com/yourusername/your-repo>"
}