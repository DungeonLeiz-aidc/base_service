"""
logging_config.py
"""

import logging
import sys
import re
from pathlib import Path
from loguru import logger
from configs.service_config import ServiceSettings

# Pre-compiled Regex for performance
EMAIL_PATTERN = re.compile(r"(?i)([\w\.-]+@[\w\.-]+\.\w+)")
CREDENTIAL_PATTERN = re.compile(
    r"(?i)\b(password|passwd|secret|token|api_key|authorization)\b(['\"]?\s*[:=]\s*['\"]?)([^'\"\s,{}]+)"
)
SENSITIVE_KEYWORDS = {"password", "passwd", "email", "secret", "token", "key", "authorization"}

class InterceptHandler(logging.Handler):
    """
    Redirects standard library logs to Loguru.
    """
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        if frame:
            logger.opt(depth=depth, exception=record.exc_info).log(
                level, record.getMessage()
            )
        else:
            logger.opt(exception=record.exc_info).log(level, record.getMessage())

def mask_sensitive_data(record):
    """
    High-performance PII masking patcher.
    """
    try:
        message = record["message"]
        message_lower = message.lower()
        
        if any(keyword in message_lower for keyword in SENSITIVE_KEYWORDS):
            message = EMAIL_PATTERN.sub("[EMAIL_MASKED]", message)
            message = CREDENTIAL_PATTERN.sub(r"\1\2[HIDDEN]", message)
            record["message"] = message
    except Exception as e:
        sys.stderr.write(f"Logging Patcher Error: {str(e)}\n")

def setup_logging(config: ServiceSettings):
    """
    Initializes logging using a centralized configuration object.
    This ensures type safety and separates concerns between config and logic.
    """
    log_path = Path(config.LOG_DIR)
    
    # Atomic infrastructure setup
    is_new_path = not log_path.exists()
    log_path.mkdir(parents=True, exist_ok=True)

    logger.remove()
    logger.configure(patcher=mask_sensitive_data)

    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    # Console Sink
    logger.add(
        sys.stderr,
        level=config.LOG_LEVEL.upper(),
        format="{time:YYYY-MM-DD HH:mm:ss} | <level>{level: <7}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
        colorize=True,
    )

    # File Sink
    file_format = log_path / "{time:YYYY-MM}" / "{time:YYYY-MM-DD}.log"
    logger.add(
        str(file_format),
        level=config.LOG_LEVEL.upper(),
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <7} | {name}:{function}:{line} - {message}",
        rotation=config.LOG_ROTATION,
        retention=config.LOG_RETENTION,
        compression="zip",
        enqueue=True,
        backtrace=True,
        diagnose=config.DEBUG
    )

    if is_new_path:
        logger.info(f"Action: Log infrastructure created at {log_path.absolute()}")
    
    logger.info("Logging system initialized via Centralized Config.")