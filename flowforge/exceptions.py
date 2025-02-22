class FlowForgeError(Exception):
    """Base exception for FlowForge errors."""
    pass

class TaskTimeoutError(FlowForgeError):
    """Raised when a task exceeds its timeout."""
    pass

class TaskRetryError(FlowForgeError):
    """Raised when a task fails after all retries."""
    pass
