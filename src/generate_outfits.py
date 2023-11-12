## Generate new outfits

def generate_new_outfits_optimized(tabla_final, original_outfit, similarity_groups):
    new_outfits = []
    for prenda in original_outfit:
        # Extraer detalles de la prenda actual
        prenda_details = tabla_final[tabla_final['cod_modelo_color'] == prenda].iloc[0]
        color_spec = prenda_details['des_color_specification_esp']
        product_type = prenda_details['des_product_type']

        # Encontrar prendas similares
        similar_prendas = similarity_groups.get((color_spec, product_type), [])
        
        # Generar nuevos outfits reemplazando la prenda actual con cada prenda similar
        for similar_prenda in similar_prendas:
            if similar_prenda != prenda and similar_prenda not in original_outfit:  # Evitar duplicados
                new_outfit = [p if p != prenda else similar_prenda for p in original_outfit]
                new_outfits.append(new_outfit)

    return new_outfits

def recomendar_outfits(cod_modelo_color, G):
    recomendaciones = set()
    # Buscar todos los nodos conectados a la pieza de ropa dada
    for neighbor in G.neighbors(cod_modelo_color):
        recomendaciones.add(neighbor)
    return list(recomendaciones)