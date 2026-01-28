import xml.etree.ElementTree as ET
import sys

def validate_urdf(path: str):
    try:
        tree = ET.parse(path)
        root = tree.getroot()
    except Exception as e:
        print(f"Error al leer URDF: {e}")
        return False

    ok = True
    for link in root.findall("link"):
        if link.find("inertial") is None:
            print(f"Falta inertial en link {link.attrib['name']}")
            ok = False
        if link.find("visual") is None:
            print(f"Falta visual en link {link.attrib['name']}")
            ok = False
        if link.find("collision") is None:
            print(f"Falta collision en link {link.attrib['name']}")
            ok = False
    return ok

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python tests/validator.py robots/mi_robot.urdf")
        sys.exit(1)
    result = validate_urdf(sys.argv[1])
    print("URDF válido" if result else "URDF inválido")
