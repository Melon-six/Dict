from fastapi import FastAPI
from find import search_words

# 创建FastAPI实例
app = FastAPI()

# 定义一个路由，接收 id 参数并打印
@app.get("/find/{id}")
async def print_id(id: str):
    return {search_words(id)}

 