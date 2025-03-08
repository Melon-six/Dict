from fastapi import FastAPI
from find_word_dir import search_words
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 添加 CORSMiddleware 中间件，允许所有来源进行跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头部
)


# 创建FastAPI实例
app = FastAPI()

# 定义一个路由，接收 word 参数并返回查询结果
@app.get("/find/{word}")
async def find_word(word: str):
    definition = search_words(word)
    
    return {"word": word, "definition": definition}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)