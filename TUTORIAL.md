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

### EXPORTING GLB

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
    Materials: selected "ViewPort", "Automatic"
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

    Jaw, eye, tongue, meshes should stay in the same indexes. If not, KittyBody will use incorrect texture. 

### Exporting Kitten with added mesh

    Select the new mesh model 
    Add mesh model under Armature Parent
    Add vertex groups into new mesh 
    Add armature modifier and set the Vertex Group in this modifier (i.e. Head_M)
    
    Select your new mesh (model:XMouseKyborg) and switch to Edit Mode (Tab).
• Press A to select all vertices.
• Open Object Data Properties (the green triangle icon) -> Vertex Groups.
• Select the bone that should move this mesh (for example, Head_M if it is a headpiece/cyborg visor, or Chest_M / Root_M if it is body armor). If the vertex group does not exist on that mesh yet, click + and name it identically to the bone (e.g., Head_M).
• Set Weight to 1.000 and click Assign.
• Why this matters: When every single vertex has a non-zero weight to an existing skeleton bone, Blender's glTF exporter will not generate "neutral_bone"

Change export settings in Material to Materials Viewport.

Check indexes of meshes in the assets and correct if they are different (ScleraMeshIndices,FurMeshIndex)

# AI HELP


AI Mode
All
Forums
Images
Videos
Web
News
More
ERROR Unhandled exception System.Exception: SubAssetReference EyeJoint_L has no index found at KSA.SubAssetReference.GetIndex(IReadOnlyList`1 names) at KSA.BoneReference.GetIndex(Skeleton skeleton) at KSA.CharacterAvatar.InitalizeFromCharacterRef(CharacterReference characterReference) at KSA.CharacterAvatar..ctor(AssetName name) at KSA.KittenRenderable..ctor(String characterId, Boolean seated) at KSA.IVASeat.UpdateSeatedRenderable(IViewport viewport, Int32 inFrameIndex, Double dt, double4x4& matrixAsmb2Ego) at KSA.Vehicle.UpdateSeatedCrewRenderData(IViewport viewport, Int32 inFrameIndex) at KSA.Program.RenderViewport(CommandBuffer commandBuffer, IViewport viewport, Int32 frameIndex) at KSA.Program.RenderGame(AcquiredFrame frame, Double dt) at KSA.Program.Render(Double dtPlayer, FrameResult result, AcquiredFrame acquiredFrame) at KSA.Program.OnFrame(Double currentPlayerTime, Double dtPlayer) at KSA.App.Run() at KSA.Program.Main(String[] inArgs).
This crash occurs because Kitten Space Agency (KSA) failed to locate the EyeJoint_L bone inside a kitten character's 3D skeleton while rendering a seated crew member inside a vehicle (IVASeat.UpdateSeatedRenderable). 
Common Causes

    Corrupted or mismatched game files. An incomplete update or modified asset left the character definition XML expecting EyeJoint_L, while the loaded 3D mesh/skeleton file lacks that bone name.
    Outdated or incompatible mods. A custom character mod, IVA mod, or a mod compiled for an older pre-alpha build is referencing an outdated skeleton hierarchy (see the KSA Modding Wiki
    for recent asset and code changes). 
    Corrupted save or craft file. A saved vessel or crew roster entry is pointing to a broken or deprecated CharacterReference asset ID.

How to Fix It

    Disable custom mods. Temporarily remove or disable any installed mods (especially character, crew, or capsule/IVA mods) to see if the crash stops.
    Verify or reinstall game files. Re-download or repair your KSA installation through the Ahwoo launcher
    so all character skeletons and XML definitions match the current build. 
    Test a fresh save or craft. Start a new sandbox flight with a stock capsule and default crew (such as Hunter, Banjo, or Polaris). If it loads without crashing, the issue is tied to a specific saved vessel or crew roster entry. 
    Report the bug. If this happens on a clean, unmodded install after a recent update, share the full stack trace on the official Kitten Space Agency Subreddit
    or the KSA Discord linked on the Kitten Space Agency Wiki
    . 

If you'd like help narrowing this down further, let me know:

    Your current KSA build version (e.g., 2026.11.x)
    Whether you are running any mods or custom character/part files
    When the crash triggers (e.g., loading a specific saved craft, entering IVA, or launching from the editor)

I can help pinpoint the exact file or mod causing the skeleton mismatch.
AI responses may include mistakes. Learn more

    wiki.gg
    Kitten - Kitten Space Agency Wiki
    August 25, 2026 — Role: Kittens serve as crew members for player-built space vehicles in Kitten Space Agency and are managed via the Kitten Roster. ...
    wiki.gg
    Kitten Space Agency Wiki
    August 6, 2026 — # About Kitten Space Agency Kitten Space Agency (KSA) is an upcoming 3D space flight simulation game developed by RocketWerkz. The...
    Ahwoo
    Kitten Space Agency
    # Kitten Space Agency Games can inspire. Inspiration should be free. The first people to set foot on Mars will trace their journey...

I added new mesh in the KSA_Kitten.gltf when edited it in blender 4.5. How to fix the mesh so I do not get this error
This crash happens because Blender stripped, renamed, or skipped exporting the EyeJoint_L bone (or exported a second separate armature) when you re-exported KSA_Kitten.gltf.
In KSA, CharacterAvatar strictly checks the exported .gltf node hierarchy for exact bone names (EyeJoint_L, etc.) and expects a single unified skeleton. When you add a new mesh in Blender, it is easy to accidentally alter the armature or export settings so that unused leaf bones like EyeJoint_L get dropped.
Step 1: Attach Your New Mesh Properly in Blender

    Parent to the existing Armature: Select your new mesh first, then Shift + Select the original KSA kitten Armature (make sure you did not import a second armature). Press Ctrl + P and choose Armature Deform > With Empty Groups (or With Automatic Weights).
    Weight paint or assign vertices: Make sure every vertex on your new mesh is assigned to at least one existing bone (e.g., Head, Neck, or Spine) in Object Data Properties (green triangle) > Vertex Groups. Unweighted vertices or new custom bone names can break KSA's skinning loader.
    Check EyeJoint_L in the Outliner: Expand the Armature in the Outliner and verify that EyeJoint_L is still present and spelled identically (case-sensitive). Make sure neither the bone nor the Armature is hidden or excluded from export.

Step 2: Fix Blender 4.5 glTF Export Settings
When exporting via File > Export > glTF 2.0 (.glb/.gltf), check these exact settings on the right-hand panel:

    Include: Check Selected Objects (if you only selected the Armature + Meshes) and uncheck Limit to Visible if anything is hidden. Do not export extra cameras, lights, or empty helper objects.
    Data > Armature:
        Uncheck Export Deformation Bones Only. (EyeJoint_L is often used as an attachment/look-at joint without mesh weights—if Deformation Bones Only is checked, Blender deletes it on export!)
        Check Add Leaf Bones only if the original file had them, though keeping Deformation Bones Only unchecked is the main fix for missing joint nodes.
    Data > Mesh: Ensure Vertex Groups (Skinning) is enabled.
    Format: Match the original file structure—if KSA expects .gltf + .bin + textures, choose glTF Separate (.gltf + .bin + textures) rather than a single .glb.

Step 3: Verify the Exported .gltf File
Before launching KSA, open your newly exported KSA_Kitten.gltf in a text editor (like Notepad++ or VS Code) and press Ctrl + F to search for "EyeJoint_L".

    If it is found: Check that it appears inside the "nodes" array and its index is listed inside the "skins" -> "joints" array.
    If it is still missing: Check if your Armature object in Blender was renamed or if EyeJoint_L had its Deform checkbox disabled while Deformation Bones Only was still active during export.

If the error persists after re-exporting, let me know:

    What type of mesh you added (e.g., a helmet, visor, suit piece, or body part)
    Whether EyeJoint_L shows up when you search the exported .gltf text file

I can walk you through checking the .gltf "skins" and "nodes" arrays to make sure the skeleton indices match KSA's expectations.
AI responses may include mistakes. Learn more
These are the files KSA_Cat is original and MouseTheCyborg is with added one additional mesh.
Thank you for uploading both .gltf files—that makes the exact cause crystal clear!
EyeJoint_L is still in your MouseKyborg.gltf file (at node index 9), but Blender injected an extra bone called "neutral_bone" at node index 242, which shifted every mesh node's index up by 1. 
Why This Causes the Crash
In KSA_Cat.gltf, the skeleton ends at node 241 ("root"), and the meshes sit at indices 242 through 250. 
In MouseKyborg.gltf, Blender added "neutral_bone" at index 242 (and appended 242 to the end of "skins" -> "joints"), pushing "model:Eye_L" to 243 and "DeformationSystem" to 253. Blender automatically creates "neutral_bone" whenever a skinned mesh has unweighted vertices (vertices not assigned to any vertex group/bone) or when a mesh object is parented to an armature without a weight for every vertex. KSA's Skeleton loader either fails to parse the skin due to "neutral_bone" or looks up the wrong node range, causing BoneReference.GetIndex(Skeleton) to throw SubAssetReference EyeJoint_L has no index found. 
How to Fix It in Blender 4.5

    Assign 100% of vertices on model:XMouseKyborg to a bone:
        Select your new mesh (model:XMouseKyborg) and switch to Edit Mode (Tab).
        Press A to select all vertices.
        Open Object Data Properties (the green triangle icon) -> Vertex Groups.
        Select the bone that should move this mesh (for example, Head_M if it is a headpiece/cyborg visor, or Chest_M / Root_M if it is body armor). If the vertex group does not exist on that mesh yet, click + and name it identically to the bone (e.g., Head_M).
        Set Weight to 1.000 and click Assign.
        Why this matters: When every single vertex has a non-zero weight to an existing skeleton bone, Blender's glTF exporter will not generate "neutral_bone". 
    Check the Armature Modifier:
        Select model:XMouseKyborg, go to Modifiers (blue wrench icon), and ensure it has one Armature modifier pointing to DeformationSystem with Vertex Groups checked.
        Make sure model:XMouseKyborg is parented under DeformationSystem in the Outliner just like model:KittyHead and model:KittyBody. 
    Verify the Re-Exported .gltf:
        Export your .gltf again and open it in a text editor.
        Search for "neutral_bone"—it should return 0 results (just like in KSA_Cat.gltf).
        Check "skins" -> "joints": the count in "inverseBindMatrices" accessor (index 6) should drop back from 243 to 242, matching the original skeleton joint count! 

Secondary Check: Texture Paths
Notice in MouseKyborg.gltf that your new material's image URIs use relative parent paths ("../../Parts/mouse_Diffuse.png"), while the original kitten materials lost their texture links (they have no baseColorTexture in MouseKyborg.gltf, whereas KSA_Cat.gltf had "uri": "DefaultORM.png"). 

    Make sure those relative texture paths actually resolve from wherever MouseKyborg.gltf is placed in KSA's mod/asset folder, or KSA may throw a missing texture error right after loading the skeleton.

Once you assign all vertices of model:XMouseKyborg to a bone and re-export, let me know if "neutral_bone" disappears or if KSA throws any follow-up error with the new mesh's material/textures!
AI responses may include mistakes. Learn more

    Your upload·Only you can see this
    MouseKyborg.gltf
    Your upload·Only you can see this
    KSA_Cat.gltf

The game with new generated gltf fail to load, with error in the log : ERROR Unhandled exception System.Exception: Vma Failed to create buffer
 at Brutal.VulkanApi.Abstractions.BufferExExtensions.CreateBuffer(IBufferAllocator allocator, CreateInfo createInfo)
 at KSA.Rendering.Planet.PlanetTessellation.CreateVertexAttributeBuffer(String name)
 at KSA.Rendering.Planet.PlanetTessellation.CreateBuffers()
 at KSA.Rendering.Planet.PlanetTessellation..ctor(PlanetRenderer planetRenderer, Renderer renderer, Int32 frameCount, PlanetFrustumCulling frustumCulling, DescriptorSetLayoutEx celestialLayout, GpuTextureSystem textureSystem)
 at KSA.PlanetRenderer..ctor(Renderer renderer, IRenderPassInfo renderPassInfo, Int32 frameCount, GpuTextureSystem textureSystem, CloudShadowsRenderer cloudShadowsRenderer)
 at KSA.Program..ctor(IReadOnlyList`1 inArgs)
 at KSA.Program.Main(String[] inArgs).
Your skeleton structure in the new MouseKyborg.gltf is fixed (neutral_bone is gone, "skins" has 242 joints, and EyeJoint_L is clean). 
However, the new crash (System.Exception: Vma Failed to create buffer inside PlanetTessellation.CreateVertexAttributeBuffer during Program..ctor) is a GPU memory (VRAM) allocation failure triggered during engine startup, before the character even renders.
Why This Happened

    Vulkan Memory Allocator (Vma) ran out of free VRAM or hit a driver allocation limit while allocating large vertex buffers for planet tessellation at startup.
    The new mesh's vertex/index size or loose texture files likely pushed VRAM usage over your GPU's available budget, or another GPU-heavy program (like Blender still open in the background!) was holding onto VRAM. Notice that model:XMouseKyborg alone adds 10,721 vertices and 62,256 indices, plus three external PNG textures (mouse_Diffuse.png, mouse_PBR.png, mouse_Normal.png). 

How to Fix It

    Close Blender and other GPU apps before launching KSA: Having Blender open with a high-poly scene active consumes a large chunk of VRAM that Vma needs when initializing KSA's planet renderer.
    Check your custom texture resolutions (mouse_*.png): Ensure mouse_Diffuse.png, mouse_PBR.png, and mouse_Normal.png are not oversized (e.g., 4K or 8K uncompressed PNGs). Resize them to 1024x1024 or 2048x2048 to dramatically lower VRAM overhead.
    Fix the broken relative image paths in MouseKyborg.gltf: Even though your XML defines <PbrMaterial Id="XMouseKyborg">, MouseKyborg.gltf still embeds "uri": "../../Parts/mouse_Diffuse.png" in its "images" block. In Blender, remove the image texture nodes from the shader before exporting (or clear the "images"/"textures" arrays in the .gltf if KSA overrides materials via XML) so KSA's glTF loader doesn't try to load invalid relative paths. 
    Decimate model:XMouseKyborg if VRAM remains tight: If you are on a GPU with 4–6 GB VRAM, using a Decimate modifier in Blender to bring model:XMouseKyborg from ~20,750 triangles down to ~3,000–5,000 triangles will match the poly budget of the stock kitten meshes (KittyHead is 4,194 tris; KittyBody is 6,522 tris). 

One XML Detail to Double-Check Once It Boots
In your XML, you added <MeshIndex Value="9"/> to <HeadMeshIndices>. 

    Keep 9 in <HeadMeshIndices> only if model:XMouseKyborg is a head/helmet piece that should move/hide with the head.
    If model:XMouseKyborg is a suit/body attachment, move <MeshIndex Value="9"/> into <SuitMeshIndices> instead. 

If the Vma Failed to create buffer error still appears after closing Blender, let me know how much VRAM your GPU has and the pixel dimensions of your mouse_*.png textures so we can size the assets to fit your memory budget.
AI responses may include mistakes. Learn more

    Your upload·Only you can see this
    CharacterAssets.xml
    Your upload·Only you can see this
    MouseKyborg.gltf
    Your upload·Only you can see this
    KSA_Cat.gltf

Added decimation modifier with Ratio 0.1. Changed gltf export setting of Material to Materials Viewport (fixed issue the loading issue, so the idea in No 3  worked). VRAM usage is 4+ GB.  Total VRAM 7GB out of 8GB was free.  Now I see the mouse model in the game. Thanks.
Awesome—glad to hear SqueakMouse is showing up in-game now!
Setting Blender's glTF material export to Viewport (or No Export) is a great trick for KSA modding because it strips out the relative PNG paths that conflict with KSA's XML <PbrMaterial> overrides, and bringing the poly count down with the 0.1 Decimate modifier keeps it right in line with the stock character assets.
If you run into any issues with facial expressions, helmet visibility (HeadMeshIndices vs. SuitMeshIndices), or material shading on your new cyborg mouse character, let me know and we can fine-tune the XML or weights!
AI responses may include mistakes. Learn more
Ask about



    

    

    


