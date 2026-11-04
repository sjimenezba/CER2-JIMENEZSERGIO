# CER2-JIMENEZSERGIO
# Certamen 2 - Catalogo de Fundacion Patrimonio Vivo
**Autor:** Sergio Jimenez
**Ramo:** Taller de Lenguaje de Programación

## Descripcion
Aplicacion web desarrollada en Django Framework para centralizar y difundir lugares de interes patrimonial, con un sistema de catalogo publico y un area de gestion interna protegida por permisos.

## Instrucciones de ejecucion
1. **Clonar el repositorio**
    `git clone https://github.com/tu-usuario/CER2-JIMENEZSERGIO.git`
2. **Navegar a la carpeta**
    `cd CER2-JIMENEZSERGIO`
3. **Instalar dependencias**
    `pip install -r requirements.txt`
4. **Aplicar migraciones (base de datos)**
    `py manage.py makemigrations`
    `py manage.py migrate`
5. **Crear usuario administrador (para el area de gestion)**
    `py manage.py createsuperuser`
6. **Ejecutar el servidor local**
    `py manage.py runserver`

Para crear los usuarios de prueba ver [USUARIOS.md](USUARIOS.md).