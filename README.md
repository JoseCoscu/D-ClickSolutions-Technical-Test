# D-ClickSolutions-Technical-Test
Technical test for D'Click Solutions 
# 📚 Library Management Module (Odoo 18)

Este módulo implementa un **sistema básico de gestión de bibliotecas** en **Odoo 18**, permitiendo administrar libros, bibliotecas y realizar **reservas mediante un wizard**, con integración de **chatter**, **reglas de seguridad** y **validaciones de fechas**.

---

## 🚀 Funcionalidades

### 📖 Gestión de Libros
- Modelo `library.book`
- Campos principales:
  - Título
  - Autor
  - Fecha de publicación
- Estados del libro:
  - Available
  - Borrowed
  - Reserved
- Campo booleano `is_borrowed`
- Acciones:
  - Prestar libro
  - Devolver libro
- Integración con **Chatter** (`mail.thread`, `mail.activity.mixin`)

---

### 🏛️ Gestión de Bibliotecas
- Modelo `library.library`
- Campos:
  - Nombre de la biblioteca
- Vista tipo lista
- Datos de ejemplo cargados automáticamente

---

### 📅 Reservas de Libros (Wizard)
- Wizard `book.reservations` (`TransientModel`)
- Campos:
  - Usuario
  - Fecha de inicio de la reserva
  - Fecha final de la reserva
  - Biblioteca
- Se abre desde un botón en el formulario del libro
- El **ID del libro** se pasa por `context` usando `active_id`

---

## ⛔ Validaciones (Constraints)

- La fecha de inicio **no puede ser menor que el día actual**
- La fecha final **no puede ser menor que la fecha de inicio**

---

## 🔐 Seguridad

### `library.library`
- Lectura, creación y edición permitidas
- Eliminación restringida

### `book.reservations`
- Creación permitida
- Sin edición ni eliminación

---

## 🖥️ Vistas Implementadas

- Libros: vistas `list` y `form`
- Bibliotecas: vistas `list` y `form`
- Wizard de reservas en modal

---



## ⚙️ Instalación

1. Copiar los módulos en `addons`
2. Actualizar Apps
3. Instalar 

---

## 🧩 Requisitos

- Odoo 18
- Módulo `mail`

---

## 👨‍💻 Autor
JoseCoscu
Proyecto demo / educativo para Odoo 18
