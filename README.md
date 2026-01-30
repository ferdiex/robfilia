## Robfilia: Filosofía de la IA + Robótica Generativa (PyBullet)
---

Este proyecto explora cómo la IA generativa puede diseñar robots en formato URDF y simularlos en PyBullet, conectando práctica técnica con análisis filosófico.

## Instalación

pip install -r requirements.txt

Nota: se puede usar environment.yml en conda, pero en macOS puede dar problemas con versiones. Es mejor requirements.txt sin fijar versiones.

## Estructura del proyecto

robfilia/

robots/            URDFs generados por IA o diseñados manualmente

src/               simuladores en Python, CLI principal y validador de URDF

docs/              bitácora y documentación filosófica

world/             planos y entornos

README.md          instrucciones generales

## Uso básico

1. Generate a URDF with AI using the following prompt:

Generate a valid URDF file for PyBullet that describes a simple robot with these rules:
• Between 3 and 6 links connected in a tree structure without cycles
• Joints only of type fixed or revolute; each revolute must include a limit and an axis
• Each link must include inertial, collision, and visual elements
• Use simple geometries (box, cylinder, sphere) with realistic sizes in meters
• Masses between 0.05 and 3 kg per link
• The robot must start on a plane at approximately z ≈ 0.3 m
Return only the URDF content without explanations.

Prueba mejorar el prompt para generar robots más interesantes.

2. Guardar el archivo en la carpeta robots con nombre mi_robot.urdf

3. Validar el robot
python src/app.py validate robots/mi_robot.urdf

4. Simular el robot
python src/app.py simulate robots/mi_robot.urdf

5. Simular con torque sinusoidal
python src/app.py simulate-torque robots/arm_bot.urdf

Nota: además de robots simples con un solo joint, ya es posible crear robots con al menos dos articulaciones. Explora cómo se comportan en la simulación y documenta tu experiencia en la bitácora.

## Fast mode

La simulación puede correr en dos modos: tiempo real y fast mode. En tiempo real la simulación avanza con pausas para coincidir con la física real. En fast mode avanza lo más rápido posible.

Existen dos formas de activar fast mode:

1. Desde CLI usando el flag --fast

python src/app.py simulate robots/mi_robot.urdf --fast

python src/app.py simulate-torque robots/arm_bot.urdf --fast

2. Dentro de la simulación presionando la barra espaciadora para alternar entre tiempo real y fast mode.

## Bitácora

Cada estudiante debe documentar su experiencia en docs/bitacora.md con el siguiente formato:

Robot: mi_robot.urdf

Prompt usado: copiar aquí

Resultado de validación: válido o errores

Observación en simulación: se cayó estable osciló

Preguntas filosóficas:

Creatividad: es un diseño nuevo o recombinado

Ontología: qué tipo de entidad es este robot

Epistemología: qué revela su comportamiento sobre simular vs comprender

Ética: quién es el autor del diseño

## Preguntas filosóficas centrales

Creatividad: puede la IA crear diseños originales o solo reconfigura patrones estadísticos  

Ontología: qué clase de entidad es un robot generado por texto y realizado en un simulador  

Epistemología: la IA sabe física al proponer un URDF o solo correlaciona lenguaje  

Ética: quién es el autor responsable del diseño y qué riesgos implica delegar la morfología a la IA  

Uso del Simulador: El uso de simuladores de robots en IA generativa nos acerca realmente a comprender la inteligencia, o es solo un ejercicio técnico sin iluminación filosófica  

Aceleración de la IA: La aceleración de la IA generativa indica que vamos hacia la singularidad o una "IA fuerte", como discuten pioneros del aprendizaje profundo y pensadores como Yann LeCun  

## Protocolo experimental

Generar robots con IA  
Validar URDFs  
Simular en PyBullet  
Registrar resultados en bitácora  
Reflexionar filosóficamente  

## Ejemplo de ejecución

python src/app.py validate robots/minimal_bot.urdf  
python src/app.py simulate robots/minimal_bot.urdf  
python src/app.py simulate robots/minimal_bot.urdf --fast  
python src/app.py simulate-torque robots/arm_bot.urdf  
python src/app.py simulate-torque robots/arm_bot.urdf --fast  

## Bibliografía sugerida

- Boden, M. A. (2004). The creative mind: Myths and mechanisms (2nd ed.). Routledge.
- Dennett, D. C. (1987). The intentional stance. MIT Press.
- Searle, J. R. (1980). Minds, brains, and programs. Behavioral and Brain Sciences, 3(3), 417–424. https://doi.org/10.1017/S0140525X00005756 (doi.org in Bing)
- Simondon, G. (1958). Du mode d’existence des objets techniques. Aubier.
- Heidegger, M. (1927/1993). Ser y tiempo (J. Gaos, Trans.). Trotta. (Original work published 1927)
- Aristóteles. (1994). Metafísica (M. Candel Sanmartín, Trans.). Gredos. (Original work published ca. 4th century BCE)
- Kant, I. (1781/1998). Crítica de la razón pura (M. García Morente, Trans.). Alfaguara. (Original work published 1781)
- Chalmers, D. J. (2022). Reality+: Virtual worlds and the problems of philosophy. W. W. Norton & Company.

## Primeros pasos en GitHub

Clonar el repositorio desde GitHub:
git clone https://github.com/ferdiex/robfilia

cd robfilia

Instalar dependencias:
pip install -r requirements.txt

Validar un robot:
python src/app.py validate robots/mi_robot.urdf

Simular en tiempo real:
python src/app.py simulate robots/mi_robot.urdf

Simular en fast mode desde el inicio:
python src/app.py simulate robots/mi_robot.urdf --fast

Simular con torque sinusoidal:
python src/app.py simulate-torque robots/arm_bot.urdf

Simular con torque en fast mode:
python src/app.py simulate-torque robots/arm_bot.urdf --fast

Alternativamente, dentro de la simulación se puede presionar la barra espaciadora para alternar entre tiempo real y fast mode.
