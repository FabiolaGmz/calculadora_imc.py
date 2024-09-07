# Calculadora de Índice de Masa Corporal (IMC)

## Descripción

Este proyecto consiste en una calculadora de Índice de Masa Corporal (IMC) en Python, desarrollada como primer proyecto del M1 del bootcamp de Fundamentos de Python en U Camp. El programa solicita al usuario su nombre completo, edad, peso y estatura, y luego calcula su IMC. Además, clasifica el IMC en diferentes categorías y proporciona una evaluación basada en el resultado.

## Objetivos

- Capturar los datos introducidos por el usuario.
- Validar los datos para asegurar que sean correctos y no estén vacíos.
- Calcular el IMC utilizando la fórmula: IMC = Peso / (Estatura^2).
- Mostrar los resultados junto con la categoría correspondiente del IMC.
- Aprender y aplicar técnicas de validación de datos y operaciones matemáticas en Python.

### `calculadora_imc.py`

Este archivo contiene el código fuente de la calculadora IMC. El código realiza las siguientes operaciones:

1. **Captura de Datos**: Solicita al usuario su nombre completo, edad, peso y estatura. Asegura que la entrada no esté vacía y que los valores numéricos sean válidos.
2. **Cálculo del IMC**: Calcula el IMC usando la fórmula: IMC = Peso / (Estatura^2).
3. **Clasificación del IMC**: Clasifica el IMC en una de las siguientes categorías:
   - Delgadez severa
   - Delgadez moderada
   - Delgadez leve
   - Normal
   - Sobrepeso
   - Obesidad leve
   - Obesidad media
   - Obesidad mórbida
4. **Salida de Datos**: Imprime los resultados junto con la clasificación del IMC.

### Funciones Principales

- **`validar_numero(mensaje, tipo_dato)`**: Valida que la entrada del usuario sea un número y del tipo adecuado.
- **`validar_no_vacio(mensaje)`**: Asegura que la entrada del usuario no esté vacía.
- **`calcular_imc(peso, estatura)`**: Calcula el IMC.
- **`clasificar_imc(imc)`**: Clasifica el IMC en una categoría.
- **`main()`**: Función principal que gestiona la ejecución del programa.

## Reflexiones del Proyecto

A través de este proyecto, he aprendido la importancia de validar los datos del usuario para evitar errores en el programa. El uso de funciones como `int` y `float` para la conversión de datos, así como la validación de entradas, ha sido fundamental. La implementación de la fórmula general para el cálculo del IMC me ha permitido mejorar mis habilidades en Python y entender mejor cómo manejar datos de entrada en aplicaciones reales. Este proyecto ha sido una excelente oportunidad para fortalecer mis conocimientos en el lenguaje Python.

## Contribuciones

Si tienes sugerencias para mejorar este proyecto o quieres contribuir, siéntete libre de hacer un pull request. ¡Tu ayuda será bienvenida!

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto conmigo:

- LinkedIn: [Fabiola Gomez](https://www.linkedin.com/in/fabiola-gomez-576784269)
- Instagram: [@fabiolagmz09](https://www.instagram.com/fabiolagmz09/)
