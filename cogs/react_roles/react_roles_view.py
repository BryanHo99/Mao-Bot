import config
from cogs.react_roles.roles_view import RolesView


class ReactRolesView(RolesView):
    def __init__(self):
        self.dota_emoji = "⚔"
        self.genshin_emoji = "🏔"
        self.description = self.get_description()
        super().__init__("Notification Roles")

    def get_description(self):
        return (
            f"React the following roles to be notified for games.\n"
            f"A schedule system is planned to be implemented in the future which will mention these roles.\n\n"
            f"{self.dota_emoji} <@{config.DOTA_ROLE_ID}>\n"
            f"Get this role to be notified for Dota games.\n\n"
            f"{self.genshin_emoji} @{config.GENSHIN_ROLE_ID}>\n"
            f"Get this role to be notified for Genshin games."
        )
