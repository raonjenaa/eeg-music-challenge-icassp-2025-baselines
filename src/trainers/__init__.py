import pkgutil
import importlib.util

__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    if is_pkg or "." in module_name:
        continue
    __all__.append(module_name)
    
    # 수정된 부분
    spec = loader.find_spec(module_name)
    if spec is None:
        raise ImportError(f"Module {module_name} not found")
    _module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(_module)
    
    globals()[module_name] = _module

# find module 수정 전
# __all__ = []
# for loader, module_name, is_pkg in  pkgutil.walk_packages(__path__):
#     if is_pkg or "." in module_name:
#         continue
#     __all__.append(module_name)
#     _module = loader.find_module(module_name).load_module(module_name)
#     globals()[module_name] = _module

