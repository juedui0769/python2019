# 示例6-9

class MacroCommand:
    def __init__(self, commands):
        self.commands = list(commands) #(1)

    def __call__(self, *args, **kwargs):
        for command in self.commands: #(2)
            command()