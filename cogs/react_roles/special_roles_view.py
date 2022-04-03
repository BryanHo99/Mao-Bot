from cogs.react_roles.roles_view import RolesView


class SpecialRolesView(RolesView):
    def __init__(self):
        super().__init__("Special Roles")
        self.description = self.get_description()

    @staticmethod
    def get_description():
        return f"""
            💠 <@&959795082708520980>: Exclusive role for the Bunch of maos gang.
            🔧 <@&959713538782400542>: Contributors of the Mao Bot.
        """
