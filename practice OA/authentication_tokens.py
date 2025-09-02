from typing import List


class TokenManager:
    def __init__(self, expiry_limit):
        self.expiry_dates = {}
        self.expired = set()
        self.not_expired = set()
        self.expiry_limit = expiry_limit

    def insert(self, token_id, time):
        if token_id not in self.expired and token_id not in self.expiry_dates:
            self.expiry_dates[token_id] = time+self.expiry_limit
            self.not_expired.add(token_id)

    def update_expiries(self, time):
        for token_id in self.expiry_dates:
            if self.expiry_dates[token_id] < time and token_id in self.not_expired:
                self.not_expired.remove(token_id)
                self.expired.add(token_id)

    def reset(self, token_id, time):
        if token_id in self.expired or self.expiry_dates[token_id] >= time:
            self.expiry_dates[token_id] = time+self.expiry_limit

        elif token_id in self.not_expired:
            self.not_expired.remove(token_id)
            self.expired.add(token_id)

    def return_active_length(self):
        return len(self.not_expired)


def number_tokens(commands: List[List[int]], expiry_limit: int) -> int:
    manager = TokenManager(expiry_limit=expiry_limit)
    max_time = commands[-1][2]
    for command in commands:
        cmd = command[0]
        token_id = command[1]
        T = command[2]

        if cmd == 0:
            manager.insert(token_id=token_id, time=T)

        else:
            manager.reset(token_id=token_id, time=T)

    manager.update_expiries(time=max_time)
    return manager.return_active_length()


if __name__ == "__main__":
    expiry_limit = 4
    commands = [[0, 1, 1], [0, 2, 2], [1, 1, 5], [1, 2, 7]]
    print("Ans =", number_tokens(commands=commands, expiry_limit=expiry_limit))
