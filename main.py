import anyio
import dagger
import sys


async def main(args):
    cfg = dagger.Config(log_output=sys.stdout)
    cfg.console.quiet = True
    cfg.console.force_terminal = True
    cfg.console.force_interactive = False
    async with dagger.Connection(cfg) as conn:
        await (
            conn.container(platform=dagger.Platform("linux/amd64"))
            .from_("alpine:latest")
            .with_default_args(["echo", "Hello, World!"])
            .sync()
        )


if __name__ == "__main__":
    anyio.run(main, sys.argv[1:])
