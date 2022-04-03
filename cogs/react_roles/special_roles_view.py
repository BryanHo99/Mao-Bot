import config
from cogs.react_roles.roles_view import RolesView


class SpecialRolesView(RolesView):
    def __init__(self):
        super().__init__("Special Roles")
        self.description = self.get_description()

    @staticmethod
    def get_description():
        return (
            f"These roles are only given to members that fulfill certain requirements within the server.\n\n"
            f"💠 <@&{config.MAO_ROLE_ID}>\n"
            f"Exclusive role solely for the Bunch of maos gang.\n\n"
            f"🔧 <@&{config.BOT_DEV_ROLE_ID}>\n"
            f"Members that contribute to the development of Mao Bot. "
            f"If you are interested in contributing, please contact <@{config.SCARLET_SPARK_ID}> to get you started."
        )

