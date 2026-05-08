import structlog

from structlog.typing import FilteringBoundLogger

logger: FilteringBoundLogger = structlog.get_logger()
_project_name: str | None = None


def init_metrics(project_name: str) -> None:
    global _project_name
    _project_name = project_name


def _build_metric_name(name: str) -> str:
    if _project_name is None:
        raise RuntimeError("Metrics are not initialized")
    if not name:
        raise ValueError("Metric name must not be empty")
    if name.startswith(f"{_project_name}."):
        return name
    return f"{_project_name}.{name}"


async def emit_metric(name: str) -> None:
    await logger.ainfo(_build_metric_name(name), kind="metrics")
