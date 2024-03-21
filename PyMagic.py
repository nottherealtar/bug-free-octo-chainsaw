import pymem
import pymem.process

def get_player_position():
    # """
    # Retrieves the position of the player in the game.

    # Returns:
    #     Tuple[float, float, float]: The x, y, and z coordinates of the player's position.
    # """
    # Open the process
    pm = pymem.Pymem('cs2.exe')

    # Get the base address of the client.dll module
    client = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll

    # Define the offsets
    local_player_offset = 0xD3AC5C
    m_vecOrigin = 0x138

    # Read the local player address
    local_player = pm.read_int(client + local_player_offset)

    # Read the player's position
    player_x = pm.read_float(local_player + m_vecOrigin + 0x4)
    player_y = pm.read_float(local_player + m_vecOrigin + 0x8)
    player_z = pm.read_float(local_player + m_vecOrigin)

    return player_x, player_y, player_z

# Usage
x, y, z = get_player_position()
# Do something with x, y, z