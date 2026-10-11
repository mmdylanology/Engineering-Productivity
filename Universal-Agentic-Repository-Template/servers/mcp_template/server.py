from mcp.server.fastmcp import FastMCP

mcp = FastMCP("repo-semantic")

@mcp.tool()
def list_metrics() -> list[str]:
    """Lists all officially declared semantic metrics."""
    return ["active_users", "monthly_recurring_revenue", "churn_rate"]

@mcp.tool()
def describe_metric(metric_name: str) -> dict:
    """Returns the declared formula, dimensions, and owner of a metric."""
    return {
        "metric": metric_name,
        "status": "declared",
        "allowed_dimensions": ["user.country", "user.plan_tier"]
    }

if __name__ == "__main__":
    mcp.run()
