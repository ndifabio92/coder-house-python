# Proyecto Final - Curso Python - Coder House

Este es el proyecto final del curso de Python de Coder House. La aplicación se encarga de gestionar clientes y actividades dentro de un gimnasio.

## Descripción de las Apps

### Activity

La aplicación Activity permite gestionar las actividades del gimnasio mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar). Cada actividad puede tener características como nombre, descripción, y precio.

### Activity Price

Se encarga de modificar los precios de las actividades, pero generando un historial de los mismo para no perder los precios viejos.

### Promotion

La aplicación Promotion permite establecer promociones que combinan dos actividades diferentes y asignan un nuevo precio para fomentar la inscripción. Esto es útil para ofrecer descuentos o paquetes especiales a los clientes.

## Tecnologías utilizadas

- **Python** 3.9+
- **Django** 4.x
- **SQLite** (Base de datos por defecto)
- **Django REST Framework** (API)
- **Bootstrap 5** (para el frontend)

## Requisitos previos

- Tener instalado [Python 3.9+](https://www.python.org/downloads/)
- Tener instalado [pip](https://pip.pypa.io/en/stable/installation/)

## Instalación y ejecución

Sigue los pasos a continuación para levantar la aplicación localmente.

### 1. Clona el repositorio

```bash
git clone https://github.com/ndifabio92/coder-house-python.git
cd coder-house-python/proyecto_final
```

### 2. Ejecutar las Migrates

```bash
python manage.py migrate
```

### 3. Ejecutar Servidor de desarrollo

```bash
python manage.py runserver
```

### 4. Ir al Navegador y poner la siguiente ruta

```bash
http://127.0.0.1:8000
```
