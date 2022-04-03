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
            f"{self.dota_emoji} <@&959713387959418991>\n"
            f"Get this role to be notified for Dota games.\n\n"
            f"{self.genshin_emoji} <@&959713202155974677>\n"
            f"Get this role to be notified for Genshin games."
        )
