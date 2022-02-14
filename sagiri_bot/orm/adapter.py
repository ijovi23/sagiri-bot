import yaml
from sqlalchemy.pool import NullPool


def get_adapter(url: str) -> dict:
    with open('config.yaml', 'r', encoding='utf-8') as f:
        configs = yaml.load(f.read(), yaml.BaseLoader)
    if adapters := configs.get("database_related"):
        adapter = None
        if url.startswith("mysql"):
            adapter = adapters.get("mysql")
            if adapter['disable_pooling']:
                return {"poolclass": NullPool}
            for key in adapter.keys():
                adapter[key] = int(adapter[key])
        return adapter if adapter else {}
    return {}
