# Preentrega 3 Comision 56065

## Nombre

- Andres Ramirez
- Link de LinkedIn

##  Resumen del Proyecto

- Simulando una tienda de musica con framework Django

## Pasos para ejecutar el proyecto

- [Link de Github](https://github.com/aramirezaliste/TuPrimeraPagina-Andres)
- Clonar proyecto
- Instalar dependencias
        - Dependencias ocupadas (Listadas en requeriments.txt)
            asgiref==3.7.2
            beautifulsoup4==4.12.3
            certifi==2023.11.17
            charset-normalizer==3.3.2
            defusedxml==0.7.1
            Django==4.2.9
            django-bootstrap-icons==0.8.7
            django-bootstrap-v5==1.0.11
            idna==3.6
            requests==2.31.0
            soupsieve==2.5
            sqlparse==0.4.4
            urllib3==2.1.0


- Para instalar las dependencias utilizadas en el proyecto:
    - Crear un entorno virtual de python
        ```
           $ python3 -m venv .venv
        ```
    - Activar el entorno virtual
        ```
           $ source .venv/bin/activate
        ```
    - Instalar paquete desde requeriments.txt
         ```
           $ pip3 install -r requeriments.txt
        ```

- Como ejecutar la aplicacion web en el servidor local
    Despues de instalar las dependecias requeridas,
    En la terminal dirigirse a la carpeta donde se encuentra manage.py
    y ejecutar el siguiente codigo.
    ```
        $ python3 manage.py runserver
    ```
