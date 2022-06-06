banner = """
SpeedyClient cli

    This is a client for the Nfs underground game.\n\n

    Scr44gr@v0.1.0
"""

if __name__ == "__main__":
    from speedy_client.core.speed import SpeedApi

    speed_api: SpeedApi = SpeedApi()
    ip_address: str = input("Enter the ip address of the server: ")
    if not speed_api.is_game_running():
        print("The game is not running.")
        exit(1)

    result: bool = speed_api.set_game_ip(ip_address)
    if result:
        print("The ip address is set correctly.")
        input("Press enter to exit.")
    else:
        print("The ip address is not set correctly.")
        print("Please check if the game is running.")
        input("Press enter to exit.")
