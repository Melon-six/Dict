from fastapi import FastAPI
from word_lookup import find_word_definition

# 创建FastAPI实例
app = FastAPI()

# 定义一个路由，接收 word 参数并返回查询结果
@app.get("/find/{word}")
async def find_word(word: str):
    definition = find_word_definition(word)
    
    return {"word": word, "definition": definition}
