import typer
import os
from simulate import simulate_robot
from simulate_with_torque import simulate_robot_with_torque
from validator import validate_urdf

app = typer.Typer()

@app.command()
def simulate(urdf: str, fast: bool = False):
    """
    Simula un robot URDF en PyBullet.
    Usa --fast para arrancar directamente en fast mode.
    """
    if not os.path.exists(urdf):
        typer.echo(f"Archivo no encontrado: {urdf}")
        raise typer.Exit(code=1)
    simulate_robot(urdf, gui=True, fast_mode=fast)

@app.command()
def simulate_torque(urdf: str, fast: bool = False):
    """
    Simula un robot URDF en PyBullet aplicando torque sinusoidal.
    Usa --fast para arrancar directamente en fast mode.
    """
    if not os.path.exists(urdf):
        typer.echo(f"Archivo no encontrado: {urdf}")
        raise typer.Exit(code=1)
    simulate_robot_with_torque(urdf, gui=True, fast_mode=fast)

@app.command()
def validate(urdf: str):
    """
    Valida un archivo URDF antes de simularlo.
    """
    if not os.path.exists(urdf):
        typer.echo(f"Archivo no encontrado: {urdf}")
        raise typer.Exit(code=1)
    ok = validate_urdf(urdf)
    if ok:
        typer.echo("URDF válido")
    else:
        typer.echo("URDF inválido")

if __name__ == "__main__":
    app()
