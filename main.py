from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from find_word_dir import search_words  # 确保 `search_words` 函数正确导入

# 创建 FastAPI 应用
app = FastAPI()

# 添加 CORS 允许所有来源
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法（GET, POST, etc.）
    allow_headers=["*"],  # 允许所有头部信息
)

# API 端点：查询单词
@app.get("/find/{word}")
async def find_word(word: str):
    definition = search_words(word)  # 假设 search_words 返回字符串
    return {"word": word, "definition": definition}

# 运行服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
