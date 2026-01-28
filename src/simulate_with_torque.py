import pybullet as p
import pybullet_data
import time
import math
import sys

def simulate_robot_with_torque(urdf_path: str,
                               gui: bool = True,
                               fast_mode: bool = False,
                               sim_steps: int = 20000,
                               time_step: float = 1.0/240.0,
                               base_pos=(0, 0, 0.3),
                               gravity=(0, 0, -9.8)):
    client_mode = p.GUI if gui else p.DIRECT
    physicsClient = p.connect(client_mode)

    p.setGravity(*gravity)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setTimeStep(time_step)

    plane = p.loadURDF("plane.urdf")

    try:
        robot = p.loadURDF(urdf_path, basePosition=list(base_pos))
    except Exception as e:
        print(f"Error al cargar URDF '{urdf_path}': {e}")
        p.disconnect()
        return

    num_joints = p.getNumJoints(robot)
    print(f"Robot cargado: {urdf_path}")
    print(f"Joints: {num_joints}")

    # Desactivar motores automáticos en todos los joints
    for j in range(num_joints):
        p.setJointMotorControl2(robot, j,
                                controlMode=p.VELOCITY_CONTROL,
                                force=0)

    amplitude = 2.0   # fuerza máxima
    frequency = 1.0   # Hz

    # --- ZOOM INICIAL DE CÁMARA ---
    p.resetDebugVisualizerCamera(cameraDistance=1.0,
                                 cameraYaw=45,
                                 cameraPitch=-35,
                                 cameraTargetPosition=[0, 0, 0.3])

    # --- FAST MODE toggle ---
    last_space_toggle = False

    for step in range(sim_steps):
        keys = p.getKeyboardEvents()
        space_pressed = 32 in keys and keys[32] & p.KEY_IS_DOWN
        if space_pressed and not last_space_toggle:
            fast_mode = not fast_mode
            print("[INFO] Fast mode ON." if fast_mode else "[INFO] Real-time mode ON.")
        last_space_toggle = space_pressed

        # Aplica torque sinusoidal con desfase distinto en cada joint
        for j in range(num_joints):
            phase = j * (math.pi / 2)  # desfase entre segmentos
            torque = amplitude * math.sin(2 * math.pi * frequency * step * time_step + phase)
            p.setJointMotorControl2(bodyUniqueId=robot,
                                    jointIndex=j,
                                    controlMode=p.TORQUE_CONTROL,
                                    force=torque)

        p.stepSimulation()

        if not fast_mode:
            time.sleep(time_step)
        else:
            time.sleep(0.0001)

    p.disconnect()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python src/simulate_with_torque.py robots/stick_bot.urdf")
        sys.exit(1)

    simulate_robot_with_torque(sys.argv[1])
