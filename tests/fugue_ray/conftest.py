from importlib.util import find_spec

collect_ignore_glob = [] if find_spec("ray") else ["*.py"]
