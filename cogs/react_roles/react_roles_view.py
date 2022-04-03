from cogs.react_roles.roles_view import RolesView


class ReactRolesView(RolesView):
    def __init__(self):
        super().__init__("Notification Roles")
        self.description = self.get_description()

    @staticmethod
    def get_description():
        return f"""
            React the following roles to be notified for games.
            A schedule system is planned to be implemented in the future
            which will mention these roles.
            
            ⚔ <@&959713387959418991>: Get this role to be notified for Dota games.
            🏔 <@&959713202155974677>: Get this role to be notified for Genshin games.
        """
