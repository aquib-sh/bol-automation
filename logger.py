class Logger:
    def __init__(self):
        self.colors = {
                "WHITE":    "\033[1;0m",
                "GREY":     "\033[1;30m",
                "RED":      "\033[1;31m",
                "GREEN":    "\033[1;32m",
                "YELLOW":   "\033[1;33m",
                "BLUE":     "\033[1;34m",
                "PINK":     "\033[1;35m",
                "CYAN":     "\033[1;36m"
            }

    def __log(self, color, tag, message):
        """Base message format for all logs."""
        print(self.colors[color] + tag + "\t" + self.colors["WHITE"] + message)

    def error(self, message):
        self.__log("RED", "[ERROR]", message)

    def info(self, message):
        self.__log("GREEN", "[INFO]", message)

    def debug(self, message):
        self.__log("GREY", "[DEBUG]", message)
