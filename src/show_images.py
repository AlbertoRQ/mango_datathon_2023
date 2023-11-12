
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import ast
import io

def mostrar_imagen(product_data, codigo_ropa):
    
    prenda = product_data[product_data["cod_modelo_color"] == codigo_ropa]
    prenda_filename = prenda["des_filename"].iloc[0]
    # Cargar la imagen
    img = Image.open(prenda_filename)
    # /home/mroliva/DatathonCode/datathon/datathon/images
    # Mostrar la imagen
    plt.imshow(img)
    plt.axis('off')  # Ocultar los ejes
    plt.show()


def mostrar_outfit(dataset_o, dataset_f, num_outfit):
    filas = 4
    columnas = 4
    
    items = dataset_o[dataset_o["cod_outfit"]==num_outfit]["cod_modelo_color"].iloc[0]
    items = ast.literal_eval(items)
    path_items_list = []
    for item in items:
        prenda = dataset_f[dataset_f["cod_modelo_color"] == item]
        prenda_filename = prenda["des_filename"].iloc[0]
        path_items_list.append(prenda_filename)
    
    fig, axes = plt.subplots(filas, columnas, figsize=(15, 15))  # Ajusta el tamaño según necesites
    axes = axes.flatten()

    for i, nombre_imagen in enumerate(path_items_list):
        img = Image.open("/Users/joelg/defdatathon/mango_datathon_2023/"+nombre_imagen)
        axes[i].imshow(img)
        axes[i].axis('off')  # Ocultar los ejes
        
    # Ocultar subplots vacíos si existen
    for j in range(i + 1, filas * columnas):
        axes[j].axis('off')

    plt.tight_layout()
    
    # Convertir la figura a un buffer de imagen PNG
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    
    # Retornar el buffer para que pueda ser mostrado en Streamlit
    return buf