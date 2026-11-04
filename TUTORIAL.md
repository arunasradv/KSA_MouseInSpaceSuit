# MOUSE IN THE SPACE SUIT TUTORIAL

## HOW TO USE IT

 1. Make changes to the mod.
 2. Run 'Export.py' to copy all mod files into game mods directory.
 3. Launch the game.
 4. See logs folder ([text](<../../Documents/My Games/Kitten Space Agency/logs>)) for debug information.

## CHARACTER EDITING

### EXPORTING THE KITTEN
    
    (Currently export from blender fails...)

    Select all in the "DeformationSystem"
        
    Export options:
        - Format: glTF Separate (.gltf+.bin+textures)
        - Keep Original
        - Include: Selected Objects
        - Skinning
        - Animation: Animation Mode Actions

## PARTS

### BLENDER MODEL

    ***Important***: Use the same Blender version as it is stated in the gltf/glb files 
                    ("generator":"Khronos glTF Blender I/O v4.5.48",)!

### EXPORTING GLB

    Include     -> "Scene"
    Materials   -> "Export", remove ".ddd" digits in material names.
    

    

    


