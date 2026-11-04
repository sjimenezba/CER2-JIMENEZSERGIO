# Usuarios y permisos para pruebas

Para probar el control de acceso (RF10, RF11 y RF12) se necesitan 3 usuarios.

## 1. Superusuario
Desde la terminal:

    py manage.py createsuperuser

Con este usuario se entra a Django Admin en http://127.0.0.1:8000/admin

## 2. Crear usuarios desde Django Admin
Ingresar a /admin con el superusuario y ir a **Usuarios > Añadir usuario**.

### Usuario `editor` (con permisos)
- Usuario: `editor`
- Contraseña: `editor12345`
- Guardar. Luego, en la sección **Permisos de usuario**, agregar:
  - `catalogoPatrimonio | lugar patrimonial | Can add lugar patrimonial`
  - `catalogoPatrimonio | lugar patrimonial | Can change lugar patrimonial`
- No marcar "Es staff" ni "Es superusuario".
- Guardar.

### Usuario `lector` (sin permisos)
- Usuario: `lector`
- Contraseña: `lector12345`
- Guardar sin asignar permisos.

## 3. Pruebas
| Usuario | Resultado esperado |
|---|---|
| Sin sesión | Ve catálogo y detalle. Al entrar a /gestion/ lo redirige al login |
| lector | Entra al Panel de Gestión, no ve los botones Agregar/Editar y recibe 403 al ir directo a /gestion/agregar/ |
| editor | Puede agregar y editar lugares |
| superusuario | Acceso total, incluido /admin |