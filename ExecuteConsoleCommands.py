import unreal

editor_world = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_editor_world()

commands = ['Stat FPS', 'Stat UNIT']

for command in commands:
    unreal.SystemLibrary.execute_console_command(editor_world, command)
    unreal.log('Command \'' + command + '\' executed')
