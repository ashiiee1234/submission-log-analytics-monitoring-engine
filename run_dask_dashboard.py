"""
Start the Dask distributed cluster with the Bokeh dashboard.
Dashboard URL is printed; open it in your browser to monitor workers and tasks.
"""
import sys

# Ensure project root is on path so 'backend' is importable
sys.path.insert(0, ".")


def main():
    from backend.config.dask_config import start_dask

    print("Starting Dask cluster with dashboard...")
    client = start_dask(dashboard_port=8790)
    dashboard_url = client.dashboard_link
    print()
    print("=" * 60)
    print("Dask dashboard is running.")
    print("Open in browser:", dashboard_url)
    print("=" * 60)
    print()
    print("Press Enter to shut down the cluster and exit.")
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        pass
    finally:
        client.close()
        print("Cluster stopped.")


if __name__ == "__main__":
    main()
