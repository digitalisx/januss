import click


class janus:
    @click.command()
    @click.option("--all", default=False, prompt="Your name", help="The person to greet.")
    @click.option("--plugin", prompt="", help="")
    def run():
        """The Framework that Malware Analysis by Memory Comparison"""

        #TODO
        # We need to dynamically invoke volatility3 plugin objects through parameters.

        return

if __name__ == "__main__":
    janus.run()
