#!/usr/bin/env python3
# _*_ coding: utf8 _*_
"""
app.py

Autor: Gris Iscomeback
Correo electrónico: grisiscomeback[at]gmail[dot]com
Fecha de creación: 22/02/2025
Licencia: GPL v3

Descripción:  
"""
import numpy as np
import sounddevice as sd
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt
from threading import Thread

console = Console()

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
        channels=1,
        dtype='float32'
    ) as stream:
        stream.write(tono)

def generar_y_reproducir_tono(frecuencia=440, duracion=2, amplitud=0.3, dispositivo=None):
    """Versión con barra de progreso en tiempo real"""
    try:
        if dispositivo is None:
            dispositivo = sd.default.device[1]
        
        tasa_muestreo = obtener_tasa_muestreo_valida(dispositivo)
        t = np.linspace(0, duracion, int(tasa_muestreo * duracion), False, dtype=np.float32)
        tono = amplitud * np.sin(2 * np.pi * frecuencia * t).astype(np.float32)

        # Configurar progreso ANTES de iniciar la reproducción
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            transient=True
        ) as progress:
            task = progress.add_task(f"[cyan]Reproduciendo {frecuencia}Hz...", total=duracion)
            
            # Iniciar reproducción en un hilo separado
            thread = Thread(target=reproducir_tono, args=(tono, dispositivo, tasa_muestreo))
            thread.start()
            
            # Actualizar barra mientras se reproduce
            start_time = time.time()
            while thread.is_alive():
                elapsed = time.time() - start_time
                progress.update(task, completed=min(elapsed, duracion))
                time.sleep(0.05)
            
            progress.update(task, completed=duracion)
            thread.join()
            
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
            frecuencia = Prompt.ask("\n[bold]Frecuencia en Hz[/bold]", default="440")
            if not frecuencia or float(frecuencia) <= 0:
                break
                
            duracion = Prompt.ask("[bold]Duración (segundos)[/bold]", default="2")
            
            if not generar_y_reproducir_tono(float(frecuencia), float(duracion), dispositivo=dispositivo):
                console.print("\n[bold]Dispositivos disponibles:")
                console.print(sd.query_devices())
                dispositivo = int(Prompt.ask(
                    "[bold]Ingresa número de dispositivo alternativo[/bold]",
                    default=str(dispositivo)
                ))
                
        except ValueError:
            console.print("[red]Error: Ingresa valores numéricos válidos")
        except KeyboardInterrupt:
            console.print("\n[bold yellow]Saliendo del programa...[/bold yellow]")
            break

if __name__ == "__main__":
    main()
    console.print("\n[bold green]Programa terminado.[/bold green]")
