# MOUSE IN THE SPACE SUIT TUTORIAL

## HOW TO USE IT

 1. Make changes to the mod.
    
    Directories:
        MouseInSpaceSuit - mod directory to be copied to "/Documents/My Games/Kitten Space Agency".
                            All .xml, .toml files can be edited there.
        MouseInSpaceSuit/Characters - character .glTF, .glb files. They are coppied from  "src/Characters" during EXPORT.py run.
        MouseInSpaceSuit/Meshes - .glb files for the parts. They are coppied from  "src/Parts" during EXPORT.py run.
        MouseInSpaceSuit/Textures - textures for the .glb files for the parts. They are coppied from  "src/Parts" during EXPORT.py run.
        saves - save files for testing (optional and not neccessary for the mod).
        src - mod source directory. Contains all model files and textures and Blender files. The files generated there are used to update the models.

 2. Run 'Export.py' to copy all mod files into game mods directory.
 3. Launch the game.
 4. See logs folder ([text](<../../Documents/My Games/Kitten Space Agency/logs>)) for debug information.

## PARTS

### #EXPORTING GLB

    ***Important***: Use the same Blender version as it is stated in the glb files 
                    ("generator":"Khronos glTF Blender I/O v5.2",)!

    Remove ".ddd" digits in material names.
    
    Include:    checked "Scene"
    Materials:   selected "Export"

## CHARACTER EDITING

### IMPORTING THE KITTEN

    ***Important***: Use the same Blender version as it is stated in the gltf files 
                    ("generator":"Khronos glTF Blender I/O v4.5.xx",)!
    
    Importing the KSA_Cat.gltf:
        Mesh : unchecked "Merge Vertices", "Merge Material Slot when possible"
        Texture: checked "Pack Images", "Import Unused Materials & Images"
        Bones&Skin: selected Bone Dir "Blender"
                    checked "Guess Original Bind Pose"
                    Bone shape scale : 1.00
        Pipeline: checked "Import Scene as Collection", "Import Scene Extras" 

### EXPORTING THE KITTEN

    uncheck collection "glTF_not_exported"

    Format: glTF Separate  (.gltf+.bin+textures)
            checked "Keep Original"
    Include: checked "Active Scene"
    Transform: checked "+Y"
    Scene Graph: all unchecked
    Mesh: checked "Apply Modifiers", "UVs", "Normals"
    Materials: selected "Export", "Automatic"
    Unused Textures & Images: all unchecked
    Shape Keys: checked "Shape Key Normals"
    Optimize Shape Keys: checked "Use Sparse Accessor if Better" 
    Armature: checked "Use Rest Position Armature"
    Skinning: selected "4"
    Lighting: selected "Standard"
    Compression: unchecked
    Animation: Animation mode selected "Actions"
    Bake & Merge: unchecked
    Rest & Ranges: unchecked
    Armature: checked "Export all Armature Actions", "Reset Pose Bones Between Actions"
    Shape Keys Animation: checked  "Reset Shape Keys Between Actions"
    Sampling Animations: Sampling rate selected "1"
    Sampling Interpolation Fallback: selected "Linear"
    Optimize Animations: checked "Optimize Animation Size", "Force Keeping Channels for Bones"
    Extra Animations: unchecked
    Action filter: unchecked


    

    

    


