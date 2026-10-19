def completion_rate(successes, failures, timeouts):
    """Return completed tasks divided by all assigned tasks, including timeouts."""
    return successes / (successes + failures + timeouts)
