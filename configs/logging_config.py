"""
logging_config.py

Advanced Logging Configuration for multi-environment support.
Features:
1. Vibrant, high-contrast coloring for Development (Pretty Mode).
2. Structured JSON serialization for Production/Staging.
3. Sensitive data masking (PII).
4. Standard library log interception.
"""

import logging
import sys
import re
import json
from pathlib import Path
from loguru import logger
from configs.service_config import ServiceSettings, LogFormat


# Pre-compiled Regex for performance
EMAIL_PATTERN = re.compile(r"(?i)([\w\.-]+@[\w\.-]+\.\w+)")
CREDENTIAL_PATTERN = re.compile(
    r"(?i)\b(password|passwd|secret|token|api_key|authorization)\b(['\"]?\s*[:=]\s*['\"]?)([^'\"\s,{}]+)"
)
SENSITIVE_KEYWORDS = {"password", "passwd", "email", "secret", "token", "key", "authorization"}


class InterceptHandler(logging.Handler):
    """
    Redirects standard library logs to Loguru.
    Ensures a single source of truth for all system logs.
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
    Protects sensitive information from being leaked into logs.
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


def json_serializer(record):
    """
    Custom JSON serializer for structured logging.
    Formats log records into a single-line JSON object for easy ingestion.
    """
    subset = {
        "timestamp": record["time"].isoformat(),
        "level": record["level"].name,
        "message": record["message"],
        "module": record["name"],
        "function": record["function"],
        "line": record["line"],
        "extra": record["extra"],
    }
    if record["exception"]:
        subset["exception"] = record["exception"]
    
    return json.dumps(subset)


def setup_logging(config: ServiceSettings):
    """
    Initializes logging using a centralized configuration object.
    Supports environment-specific formatting (Pretty Colors vs Structured JSON).
    """
    log_path = Path(config.LOG_DIR)
    log_path.mkdir(parents=True, exist_ok=True)

    # 1. Clear existing loggers
    logger.remove()
    
    # Custom Level Colors (Perfectionist Standard)
    logger.level("DEBUG", color="<blue>")
    logger.level("INFO", color="<green>")
    logger.level("SUCCESS", color="<bold><green>")
    logger.level("WARNING", color="<yellow>")
    logger.level("ERROR", color="<red>")
    logger.level("CRITICAL", color="<bold><white><bg red>")
    
    logger.configure(patcher=mask_sensitive_data)

    # 2. Intercept Standard Logging
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    # 3. Configure Console Sink
    if config.LOG_FORMAT == LogFormat.JSON:
        # Production JSON format - using Loguru's internal serializer
        logger.add(
            sys.stderr,
            level=config.LOG_LEVEL.upper(),
            serialize=True
        )
    else:
        # Development Ultra-Vibrant Pretty format (Perfectionist Alignment)
        # Schema: [Timestamp] | Level    | Module:Func:Line - Message
        pretty_format = (
            "<blue>[</blue><green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green><blue>]</blue> "
            "<white>|</white> <level>{level: ^9}</level> <white>|</white> "
            "<cyan>{name}</cyan>:<magenta>{function}</magenta>:<yellow>{line}</yellow> "
            "<white>-</white> <level>{message}</level>"
        )
        logger.add(
            sys.stderr,
            level=config.LOG_LEVEL.upper(),
            format=pretty_format,
            colorize=True, # Force color regardless of TTY detection
        )

    # 4. Configure File Sink
    file_format = log_path / "{time:YYYY-MM}" / "{time:YYYY-MM-DD}.log"
    
    # In file, we use a cleaner version of pretty or full JSON
    file_sink_format = "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <7} | {name}:{function}:{line} - {message}"

    logger.add(
        str(file_format),
        level=config.LOG_LEVEL.upper(),
        format=file_sink_format,
        serialize=(config.LOG_FORMAT == LogFormat.JSON),
        rotation=config.LOG_ROTATION,
        retention=config.LOG_RETENTION,
        compression="zip",
        enqueue=True,
        backtrace=True,
        diagnose=config.DEBUG
    )

    logger.info(f"AUDIT | Logging system initialized | Environment: {config.ENVIRONMENT} | Format: {config.LOG_FORMAT}")