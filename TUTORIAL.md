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

    Make blender model mesh of the part.

    Check "Object Data Properties" (green upside-down trangle icon). In the field Atributes it should have "custom_normal"

### TEXTURES

    Make textures: mymodel_Diffuse.png, mymodel_Normal.png, mymodel_PBR.png (roughmetalao)

### EXPORTING GLB

    Select          All meshes
    Include     -> "Selected Objects"
    Transform   -> +Y Up
    Mesh        -> "Apply Modifiers", UV's, Normals.
    Materials   -> "No Export"

    


