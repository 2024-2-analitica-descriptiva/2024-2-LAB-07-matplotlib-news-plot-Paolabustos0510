"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

"""
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import os



def pregunta_01():
    #output_dir = r"C:/Users/Olga/Documents/GitHub/2024-2-LAB-07-matplotlib-news-plot-Paolabustos0510/files/plots"
    output_dir = os.path.join(os.path.dirname(__file__), "../files/plots")
    os.makedirs(output_dir, exist_ok=True)

    plt.figure()

    # Colores
    colors = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'Lightgrey',
    }

    # Orden de capas
    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    # Grosor de líneas
    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2,
    }

    # Cargar datos
    #df = pd.read_csv(r"C:/Users/Olga/Documents/GitHub/2024-2-LAB-07-matplotlib-news-plot-Paolabustos0510/files/input/news.csv", index_col=0)
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../files/input/news.csv"))
    # Graficar líneas
    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            label=col,
            zorder=zorder[col],
            linewidth=linewidths[col],
        )

    # Título de la gráfica
    plt.title("How People Get Their News", fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    # Anotaciones iniciales y finales
    # Configurar etiquetas del eje x
    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center',
    )

    # Ajustar diseño y guardar la gráfica
    plt.tight_layout()
    #plt.savefig(r"C:/Users/Olga/Documents/GitHub/2024-2-LAB-07-matplotlib-news-plot-Paolabustos0510/files/plots/news.png")
    plt.savefig(os.path.join(os.path.dirname(__file__), "../files/plots/news.png"))
pregunta_01()
 
 