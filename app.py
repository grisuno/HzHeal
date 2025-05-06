import numpy as np
import sounddevice as sd
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt
from threading import Thread

console = Console()

# Frecuencias predefinidas para modo mono
FRECUENCIAS_PREDEFINIDAS = {
    "1": "174 Hz (Reparación de ADN)",
    "2": "285 Hz (Curación celular)",
    "3": "396 Hz (Liberación del miedo)",
    "4": "417 Hz (Transformación y cambio)",
    "5": "528 Hz (Amor y sanación)",
    "6": "639 Hz (Mejora de relaciones)",
    "7": "741 Hz (Resolución de problemas)",
    "8": "852 Hz (Despertar espiritual)",
    "9": "432 Hz (Armónico natural)",
    "10": "440 Hz (Afinación estándar)"
}

# Niveles predefinidos del Gateway Experience (para modo binaural)
GATEWAY_PREDEFINIDOS = {
    "1": "F-10 - Separación del cuerpo (7 Hz) | 200 / 207 Hz",
    "2": "F-12 - Estabilidad mental (6 Hz) | 200 / 206 Hz",
    "3": "F-15 - Expansión de la conciencia (5 Hz) | 200 / 205 Hz",
    "4": "F-21 - Contacto con guías (4 Hz) | 200 / 204 Hz",
    "5": "F-27 - Estructuras cósmicas (3 Hz) | 200 / 203 Hz",
    "6": "F-35 - Holograma universal (2 Hz) | 200 / 202 Hz"
}

def obtener_tasa_muestreo_valida(dispositivo):
    """Obtiene una tasa de muestreo válida para el dispositivo"""
    try:
        info = sd.query_devices(dispositivo)
        return int(info['default_samplerate'])
    except:
        return 48000

def reproducir_tono(tono, dispositivo, tasa_muestreo):
    """Función para reproducir en segundo plano"""
    with sd.OutputStream(
        device=dispositivo,
        samplerate=tasa_muestreo,
        channels=tono.shape[1],
        dtype='float32'
    ) as stream:
        if not tono.flags['C_CONTIGUOUS']:
            tono = np.ascontiguousarray(tono)
        stream.write(tono)

def generar_y_reproducir(frecuencia_izquierda, frecuencia_derecha=None, duracion=2, amplitud=0.3, dispositivo=None):
    """Genera y reproduce un tono mono o binaural"""
    try:
        if dispositivo is None:
            dispositivo = sd.default.device[1]

        tasa_muestreo = obtener_tasa_muestreo_valida(dispositivo)
        t = np.linspace(0, duracion, int(tasa_muestreo * duracion), False, dtype=np.float32)

        if frecuencia_derecha is None:
            # Modo mono
            tono = amplitud * np.sin(2 * np.pi * frecuencia_izquierda * t).astype(np.float32)
            tono = np.vstack([tono, tono]).T
        else:
            # Modo binaural
            señal_izquierda = amplitud * np.sin(2 * np.pi * frecuencia_izquierda * t)
            señal_derecha = amplitud * np.sin(2 * np.pi * frecuencia_derecha * t)
            tono = np.vstack([señal_izquierda, señal_derecha]).T

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            transient=True
        ) as progress:
            task = progress.add_task(f"[cyan]Reproduciendo...", total=duracion)
            thread = Thread(target=reproducir_tono, args=(tono, dispositivo, tasa_muestreo))
            thread.start()
            start_time = time.time()
            while thread.is_alive():
                elapsed = time.time() - start_time
                progress.update(task, completed=min(elapsed, duracion))
                time.sleep(0.05)
            progress.update(task, completed=duracion)
            thread.join()

        console.print("[green]Reproducción completada.[/green]")
        return True

    except Exception as e:
        console.print(f"[red]Error: {str(e)}")
        console.print("\n[bold]Dispositivos disponibles:")
        console.print(sd.query_devices())
        return False

def main():
    console.print("[bold green]Generador de Tonos[/bold green] [blue]con Rich[/blue]")
    console.print("[yellow]Presiona Ctrl+C para salir[/yellow]\n")

    dispositivo = 16  # dmix

    while True:
        try:
            modo = Prompt.ask("\n[bold]Elige un modo (1 mono/2 binaural):[/bold]", choices=["1", "2"], default="1")
            if modo == "1":
                console.print("[bold cyan]Modo Mono[/bold cyan]")
                console.print("[bold]Frecuencias predefinidas:[/bold]")
                for key, value in FRECUENCIAS_PREDEFINIDAS.items():
                    console.print(f"{key}: {value}")
                seleccion = Prompt.ask("[bold]Elige una opción[/bold]", choices=list(FRECUENCIAS_PREDEFINIDAS.keys()) + ["custom"])
                if seleccion == "custom":
                    frecuencia = float(Prompt.ask("[bold]Ingresa tu propia frecuencia en Hz[/bold]", default="440"))
                else:
                    frecuencia = float(FRECUENCIAS_PREDEFINIDAS[seleccion].split()[0])
                duracion = float(Prompt.ask("[bold]Duración (segundos)[/bold]", default="5"))
                generar_y_reproducir(frecuencia, duracion=duracion, dispositivo=dispositivo)

            elif modo == "2":
                console.print("[bold cyan]Modo Binaural[/bold cyan]")
                usar_predefinido = Prompt.ask("[bold]Usar configuraciones predefinidas del Gateway Experience?[/bold]",
                                              choices=["s", "n"], default="s")
                if usar_predefinido == "s":
                    console.print("[bold]Niveles predefinidos del Gateway Experience:[/bold]")
                    for key, value in GATEWAY_PREDEFINIDOS.items():
                        console.print(f"{key}: {value}")

                    seleccion = Prompt.ask("[bold]Elige una opción[/bold]",
                                           choices=list(GATEWAY_PREDEFINIDOS.keys()) + ["custom"])

                    if seleccion == "custom":
                        frecuencia_base = float(Prompt.ask("[bold]Frecuencia base en Hz[/bold]", default="300"))
                        diferencia = float(Prompt.ask("[bold]Diferencia binaural en Hz[/bold]", default="10"))
                    else:
                        # Extraer frecuencias desde la descripción
                        descripcion = GATEWAY_PREDEFINIDOS[seleccion]
                        partes = descripcion.split("|")[1].strip().split("/")
                        frecuencia_izquierda = float(partes[0].strip())
                        frecuencia_derecha = float(partes[1].strip().split(" ")[0])
                        duracion = float(Prompt.ask("[bold]Duración (segundos)[/bold]", default="10"))
                        generar_y_reproducir(frecuencia_izquierda, frecuencia_derecha, duracion=duracion, dispositivo=dispositivo)
                        continue  # Saltar la parte inferior ya ejecutada

                else:
                    frecuencia_base = float(Prompt.ask("[bold]Frecuencia base en Hz[/bold]", default="300"))
                    diferencia = float(Prompt.ask("[bold]Diferencia binaural en Hz[/bold]", default="10"))
                    frecuencia_izquierda = frecuencia_base - diferencia / 2
                    frecuencia_derecha = frecuencia_base + diferencia / 2

                duracion = float(Prompt.ask("[bold]Duración (segundos)[/bold]", default="10"))
                generar_y_reproducir(frecuencia_izquierda, frecuencia_derecha, duracion=duracion, dispositivo=dispositivo)

        except ValueError:
            console.print("[red]Error: Ingresa valores numéricos válidos")
        except KeyboardInterrupt:
            console.print("\n[bold yellow]Saliendo del programa...[/bold yellow]")
            break

if __name__ == "__main__":
    main()
    console.print("\n[bold green]Programa terminado.[/bold green]")
