import logging
import traceback
from fastapi import FastAPI, HTTPException
from fastapi.logger import logger as fastapi_logger
from pydantic import BaseModel
from typing import Optional
import os

# 配置日志
log_file_path = "logs/service.log"
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI(title="Error Logging Service", version="1.0.0")

# 添加全局异常处理中间件，将未捕获异常的Traceback写入日志
@app.middleware("http")
async def log_exceptions(request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        # 记录完整的Traceback到日志
        logger.error(f"未捕获异常: {str(e)}", exc_info=True)
        raise e

class ErrorMessage(BaseModel):
    message: str
    error_type: Optional[str] = None

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Service is running"}

@app.get("/trigger-index-error")
async def trigger_index_error(index: int = 0):

    logger.info(f"Triggering IndexError with index: {index}")
    # 创建一个长度为3的列表
    sample_list = [1, 2, 3]
    
    # 直接访问，不做边界校验，产生原生未捕获异常，生成完整Traceback
    result = sample_list[index]
    return {"result": result}

@app.get("/error-log-test")
async def error_log_test():
    """
    测试错误日志记录的接口
    """
    logger.info("Testing error logging")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    
    return {"message": "Log test completed, check logs/service.log"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)