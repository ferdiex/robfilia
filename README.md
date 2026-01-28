## Robfilia: Filosofía de la IA + Robótica Generativa (PyBullet)
---

Este proyecto explora cómo la IA generativa puede diseñar robots en formato URDF y simularlos en PyBullet, conectando práctica técnica con análisis filosófico.

## Instalación
---

pip install -r requirements.txt

Nota: antes se usaba environment.yml para conda, pero en macOS puede dar problemas con versiones. Ahora usamos requirements.txt sin fijar versiones.

## Estructura del proyecto
---

project/
robots/            URDFs generados por IA o diseñados manualmente
src/               simuladores en Python y CLI principal
tests/             validadores de URDF
docs/              bitácora y documentación filosófica
world/             planos y entornos
README.md          instrucciones generales

## Uso básico
---

1. Generar un URDF con IA usando el siguiente prompt:

Genera un archivo URDF válido para PyBullet que describa un robot sencillo con estas reglas:
- Entre 3 y 6 links conectados en estructura de árbol sin ciclos
- Joints solo de tipo fixed o revolute, cada revolute con limit y axis
- Cada link debe incluir inertial, collision y visual
- Usa geometrías simples box cylinder sphere con tamaños realistas en metros
- Masas entre 0.05 y 3 kg por link
- El robot debe iniciar sobre un plano a z ≈ 0.3 m
Devuelve solo el contenido URDF sin explicaciones

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
---

La simulación puede correr en dos modos: tiempo real y fast mode. En tiempo real la simulación avanza con pausas para coincidir con la física real. En fast mode avanza lo más rápido posible.

Existen dos formas de activar fast mode:

1. Desde CLI usando el flag --fast
python src/app.py simulate robots/mi_robot.urdf --fast
python src/app.py simulate-torque robots/arm_bot.urdf --fast

2. Dentro de la simulación presionando la barra espaciadora para alternar entre tiempo real y fast mode.

## Bitácora
---

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
---

Creatividad: puede la IA crear diseños originales o solo reconfigura patrones estadísticos  
Ontología: qué clase de entidad es un robot generado por texto y realizado en un simulador  
Epistemología: la IA sabe física al proponer un URDF o solo correlaciona lenguaje  
Ética: quién es el autor responsable del diseño y qué riesgos implica delegar la morfología a la IA  
Uso del Simulador: El uso de simuladores de robots en IA generativa nos acerca realmente a comprender la inteligencia, o es solo un ejercicio técnico sin iluminación filosófica  
Aceleración de la IA: La aceleración de la IA generativa indica que vamos hacia la singularidad o una "IA fuerte", como discuten pioneros del aprendizaje profundo y pensadores como Yann LeCun  

## Protocolo experimental
---

Generar robots con IA  
Validar URDFs  
Simular en PyBullet  
Registrar resultados en bitácora  
Reflexionar filosóficamente  

## Ejemplo de ejecución
---

python src/app.py validate robots/minimal_bot.urdf  
python src/app.py simulate robots/minimal_bot.urdf  
python src/app.py simulate robots/minimal_bot.urdf --fast  
python src/app.py simulate-torque robots/arm_bot.urdf  
python src/app.py simulate-torque robots/arm_bot.urdf --fast  

## Bibliografía sugerida
---

Boden The Creative Mind  
Dennett The Intentional Stance  
Searle Minds Brains and Programs  
Simondon Du mode d existence des objets techniques  
Heidegger Ser y tiempo  
Aristóteles Metafísica  
Kant Crítica de la razón pura  
Chalmers Reality Plus Virtual Worlds and the Problems of Philosophy  

## Primeros pasos en GitHub
---

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
