# Python stub file generated by Cython 0.29.35 And CyStub.py

import contextlib
import os
import threading
import traceback
class DuktapeError(Exception):
    pass

class DuktapeThreadError(DuktapeError):
    pass

class JSError(Exception):
    pass

class DuktapeContext(object):
    def _check_thread(self): ...
    def set_globals(self, **kwargs): ...
    def get_global(self, name): ...
    def set_base_path(self, path): ...
    def eval_js(self, src): ...
    def eval_js_file(self, src_path): ...
    def get_file_path(self, src_path): ...
    def _eval_js(self, eval_function): ...
    def make_jsref(self, index: int): ...

class JSRef(object):
    def __init__(self, py_ctx: DuktapeContext, ref_index: int): ...
    def to_js(self): ...
    def __del__(self): ...

class JSProxy(object):
    def __init__(self, ref: JSRef, bind_proxy): ...
    def __setattr__(self, name, value): ...
    def __getattr__(self, name): ...
    def __getitem__(self, name): ...
    def __repr__(self): ...
    def __call__(self, *args): ...
    def new(self, *args): ...
    def __nonzero__(self): ...
    def __len__(self): ...
    def __iter__(self): ...
    def to_js(self): ...

@contextlib.contextmanager
def wrap_python_exception(py_ctx: DuktapeContext): ...
