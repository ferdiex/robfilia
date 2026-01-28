import pybullet as p
import pybullet_data
import time
import sys

def simulate_robot(urdf_path: str,
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
    for j in range(num_joints):
        ji = p.getJointInfo(robot, j)
        print(f"  - {j}: name={ji[1].decode()} type={ji[2]} axis={ji[13]}")

    # --- ZOOM INICIAL DE CÁMARA ---
    p.resetDebugVisualizerCamera(cameraDistance=1.0,
                                 cameraYaw=45,
                                 cameraPitch=-35,
                                 cameraTargetPosition=[0, 0, 0.3])

    # --- FAST MODE toggle ---
    last_space_toggle = False

    for _ in range(sim_steps):
        keys = p.getKeyboardEvents()
        space_pressed = 32 in keys and keys[32] & p.KEY_IS_DOWN
        if space_pressed and not last_space_toggle:
            fast_mode = not fast_mode
            print("[INFO] Fast mode ON." if fast_mode else "[INFO] Real-time mode ON.")
        last_space_toggle = space_pressed

        p.stepSimulation()

        if not fast_mode:
            time.sleep(time_step)
        else:
            time.sleep(0.0001)

    p.disconnect()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python src/simulate.py robots/mi_robot.urdf")
        sys.exit(1)

    simulate_robot(sys.argv[1])
