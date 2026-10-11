import os
import sys

# --- 核心修复：强行加载 GTK 运行环境 ---
gtk_path = r'D:\999\GTK3-Runtime Win64\bin'
if sys.platform == 'win32' and os.path.exists(gtk_path):
    # 告诉 Python 3.8+ 允许从这个目录加载 DLL
    os.add_dll_directory(gtk_path)
    # 将路径加入环境变量，确保子进程也能找到
    os.environ['PATH'] = gtk_path + os.pathsep + os.environ['PATH']
# ------------------------------------

from dotenv import load_dotenv
import logging
from pathlib import Path

# Create logs directory if it doesn't exist
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        # File handler for general application logs
        logging.FileHandler('logs/app.log'),
        # Stream handler for console output
        logging.StreamHandler()
    ]
)

# Suppress verbose fontTools logging
logging.getLogger('fontTools').setLevel(logging.WARNING)
logging.getLogger('fontTools.subset').setLevel(logging.WARNING)
logging.getLogger('fontTools.ttLib').setLevel(logging.WARNING)

# Suppress verbose httpx logging (API请求日志)
logging.getLogger('httpx').setLevel(logging.WARNING)

# Suppress other verbose logs
logging.getLogger('uvicorn').setLevel(logging.WARNING)
logging.getLogger('uvicorn.access').setLevel(logging.WARNING)

# Create logger instance
logger = logging.getLogger(__name__)

load_dotenv()

from backend.server.server import app

if __name__ == "__main__":
    import uvicorn
    
    logger.info("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)