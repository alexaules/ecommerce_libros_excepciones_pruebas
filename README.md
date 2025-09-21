
# 📚 eCommerce Libros – Patrones y Pruebas en Python

## 📖 Descripción del Proyecto
Este proyecto implementa una plataforma **e-Commerce** simplificada para la venta de libros, desarrollada en **Python**.  
El objetivo principal es demostrar el uso de **patrones de diseño**, **manejo de excepciones personalizadas** y **pruebas unitarias**, garantizando un sistema robusto y fácil de mantener.  
Incluye:
- Gestión de productos, usuarios y carritos de compra.
- Excepciones específicas para manejar errores comunes en plataformas e-Commerce.
- Pruebas unitarias para validar la lógica de negocio.
- Diagramas UML actualizados en PlantUML y Mermaid para la arquitectura del sistema.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje de programación:** Python 3.10+
- **Framework de pruebas:** Pytest
- **Generación de diagramas UML:** PlantUML y Mermaid
- **Control de versiones:** Git y GitHub

## ⚙️ Implementación
1. **Estructura del proyecto**  
   ```
   ecommerce_libros_patrones_py/
   ├─ ecommerce/
   │  ├─ exceptions.py         
   │  ├─ models/               
   │  └─ services/             
   ├─ tests/                   
   ├─ uml/                     
   ├─ demo.py
   ├─ README.md
   ├─ requirements.txt
   └─ .gitignore
   ```

2. **Instalación de dependencias**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar pruebas unitarias**  
   ```bash
   pytest -q
   ```

4. **Visualización de diagramas UML**  
   - PlantUML: abre `uml/ecommerce_uml.puml` o usa PlantUML Online.  
   - Mermaid: previsualiza `uml/ecommerce_uml.mmd` directamente en GitHub.

## 🖼️ Capturas de la Aplicación
*(Agrega tus capturas aquí)*  

## 🚧 Desafíos Enfrentados y Soluciones
| Desafío | Solución |
|---------|----------|
| Manejar errores de inventario sin corromper el estado del carrito. | Se implementó `InventoryInsufficientError` y validaciones previas, además de restaurar stock en caso de errores. |
| Simular pagos fallidos para pruebas. | Se creó `PaymentGateway` configurable para pruebas de casos de éxito y fallo. |
| Mantener coherencia de datos entre operaciones. | Uso de atomicidad: revertir cambios en caso de fallo parcial. |
| Crear pruebas unitarias claras y completas. | Se usó Pytest para cubrir casos felices y de error. |

## 📌 Buenas Prácticas
- Excepciones específicas de dominio.
- Validaciones previas en operaciones críticas.
- Diseño modular y documentado.

## 👥 Autores
- **Alexis Aules** – Estudiante de Maestría en Ingeniería de Software  
- **Mateo (Asistente de IA)** – Soporte técnico
