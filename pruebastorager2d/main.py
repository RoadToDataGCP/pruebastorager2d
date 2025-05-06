from google.cloud import storage

def main():
    # Nombre del bucket y carpeta de destino
    bucket_name = 'pruebastorager2d'
    destination_blob_name = 'output/archivo.txt'
    
    # Contenido a escribir
    content = 'estoy vivo!'
    
    # Inicializa el cliente de Google Cloud Storage
    storage_client = storage.Client()
    
    # Obtiene el bucket
    bucket = storage_client.bucket(bucket_name)
    
    # Crea un blob en la ruta de destino
    blob = bucket.blob(destination_blob_name)
    
    # Sube el contenido al blob
    blob.upload_from_string(content)
    
    print(f"Archivo {destination_blob_name} subido al bucket {bucket_name}.")

if __name__ == '__main__':
    main()

