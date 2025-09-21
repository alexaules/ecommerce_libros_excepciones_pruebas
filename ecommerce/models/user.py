from dataclasses import dataclass

@dataclass
class User:
    id: str
    name: str
    email: str

    def masked_email(self) -> str:
        local, _, domain = self.email.partition("@")
        if len(local) <= 2:
            return "***@" + domain
        return local[0] + "***" + local[-1] + "@" + domain