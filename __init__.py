from invoke import Collection

from . import dotenv, env, internal, jupyter

ns = Collection(env, jupyter, dotenv)
ns.configure({"run": {"shell": internal.shell, "pty": internal.pty,}})
