import unreal

packages = []
editor_world = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_editor_world()
packages.append(editor_world.get_outermost())

level_actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem).get_all_level_actors()

for actor in level_actors:
    # A potential sublevel
    actor_world = actor.get_outer()

    actor_class = actor.get_class()
    asset_path = actor_class.get_path_name().removesuffix('_C')
    asset = unreal.find_asset(asset_path)
    blueprint = unreal.BlueprintEditorLibrary.get_blueprint_asset(asset)

    if blueprint:
        blueprint.modify()
        #unreal.BlueprintEditorLibrary.compile_blueprint(blueprint)
        actor_world.modify()
        package = actor_class.get_outermost()
        if package not in packages:
            packages.append(package)

    # A level might be dirty even if no blueprint actor has been found
    level_package = actor_world.get_outermost()
    if level_package not in packages:
        packages.append(level_package)

unreal.EditorLoadingAndSavingUtils.save_packages_with_dialog(packages, True)

unreal.log('Attempted to save all Blueprint Actors in the level: ' + editor_world.get_name())
