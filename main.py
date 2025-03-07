from fastapi import FastAPI
from find_word_dir import search_words

# 创建FastAPI实例
app = FastAPI()

# 定义一个路由，接收 word 参数并返回查询结果
@app.get("/find/{word}")
async def find_word(word: str):
    definition = search_words(word)
    
    return {"word": word, "definition": definition}
