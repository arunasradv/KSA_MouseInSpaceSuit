#The script ot export the files into mod directory and save files into the saves directory in Documents/Kitten Space Agency.
#It will copy Textures and Meshes into local directory MouseInSpaceSuit, 
# and then copy the entire MouseInSpaceSuit directory into the mod directory in Documents/Kitten Space Agency.
#Edit *xml files in MouseInSpaceSuit directory and then use the script. 
import os

user_documents_path = os.path.expanduser("~/Documents")
mod_directory = os.path.join(user_documents_path, "My Games", "Kitten Space Agency", "mods")
mod_name = "MouseInSpaceSuit"
mod_path = os.path.join(mod_directory, mod_name)

#EXPORT FOR PARTS 
#Copy *.png from /src/Parts/ into /MouseInSpaceSuit/Textures
textures_directory = os.path.join("MouseInSpaceSuit",  "Textures")
os.makedirs(textures_directory, exist_ok=True)
os.system(f"cp -r 'src/Parts'/*.png '{textures_directory}/'")

#Copy *.glb from /src/Parts/ into /MouseInSpaceSuit/Meshes
meshes_directory = os.path.join("MouseInSpaceSuit", "Meshes")
os.makedirs(meshes_directory, exist_ok=True)
os.system(f"cp -r 'src/Parts'/*.glb '{meshes_directory}/'")

#EXPORT FOR CHARACTERS 
#Copy /src/Characters/Mouse/*glb into /MouseInSpaceSuit/Characters/Mouse
character_list = ["Mouse"]

for character in character_list:
    character_directory = os.path.join("MouseInSpaceSuit", "Characters", character)
    os.makedirs(character_directory, exist_ok=True)
    os.system(f"cp -r 'src/Characters/{character}'/*.gltf '{character_directory}/'")
    os.system(f"cp -r 'src/Characters/{character}'/*.bin '{character_directory}/'")

#Delete previous mod directory if it exists

if os.path.exists(mod_path):
    import shutil
    shutil.rmtree(mod_path)

#Create the mod directory and copy all files and directories in the MouseInSpaceSuit into mod_path. Support path with spaces.
os.makedirs(mod_path)
os.system(f"cp -r '{mod_name}'/* '{mod_path}/'")

# Copy 'saves/*' directory into Documents/Kitten Space Agency
saves_directory = os.path.join(user_documents_path, "My Games", "Kitten Space Agency", "saves")
os.makedirs(saves_directory, exist_ok=True)
os.system(f"cp -r 'saves'/* '{saves_directory}/'")

#Write success message
print(f"Exported saves/* to {saves_directory}")
print(f"Exported {mod_name} to {mod_path}")
