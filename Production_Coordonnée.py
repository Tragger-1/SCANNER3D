import cv2
import numpy as np
import os
import math
import Transmission_Données
#import matplotlib.pyplot as plt
from PIL import Image
def Production_coordonees_3D():
    # Initialiser le nuage de points
    point_cloud = []
    laser_angle=15
    rotation_angle=1.8
    # Parcourir toutes les images
    for i in range(200):  # Supposons que nous ayons 200 images
        # Lire l'image en couleur
        img_path = os.path.join('/home/pi/images_Scanner', f'RESULT_{i}.png')
        img = cv2.imread(img_path)

        # Vérifier si l'image a été chargée correctement
        if img is None:
            print(f"Erreur lors du chargement de l'image {img_path}")
            continue

            # Parcourir chaque pixel de l'image
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                # Si le pixel n'est pas noir
                if np.any(img[i, j] != [0, 0, 0]):
                    # Ajouter les coordonnées et les valeurs de couleur au nuage de points
                    #y = i / 100
                    # Calculer les coordonnées x et z en utilisant l'angle de rotation
                    #radius = j  # La distance du pixel à l'axe de rotation est utilisée comme rayon
                    #angle = math.radians(1.8)  # L'angle de rotation
                    #x = (radius * math.cos(angle)) / 100
                    #z = (radius * math.sin(angle)) / 100
                    r, g, b = img[i, j] / 255.0  # Normaliser les couleurs à [0, 1]
                    #point_cloud.append([x, y, z, r, g, b])

                    x = j
                    y = i
                    z = j / np.tan(np.deg2rad(laser_angle))
                    # Rotate the point around the y-axis
                    x_rot = x * np.cos(np.deg2rad(rotation_angle)) - z * np.sin(np.deg2rad(rotation_angle))
                    z_rot = x * np.sin(np.deg2rad(rotation_angle)) + z * np.cos(np.deg2rad(rotation_angle))
                    # Add the point to the point cloud
                    point_cloud.append([x_rot, y, z_rot])
                    Transmission_Données.Transmission_Donnee(x_rot/100,y/100,z_rot/100,r,g,b)
                    # Ajouter le point et la couleur au nuage de points
                    #point_cloud.append([x, y, z, r, g, b])
                    #print("x: ",x,"y: ", y,"z: ", z,"la couleur est :", " red ", r," green ", g, " blue ", b)

        # Convertir le nuage de points en tableau numpy
    print("production des coordonnees 3D | Ok")

