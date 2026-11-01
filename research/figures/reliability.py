"""Rebuild the illustrative reliability figure; requires matplotlib 3.9.2."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'experiments'))
from reliability import completion
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def build(destination):
    plt.rcParams.update({'svg.hashsalt':'intent-native-paper','font.family':'DejaVu Sans','font.size':11})
    fig,ax=plt.subplots(figsize=(10,5.5),layout='constrained')
    fig.set_facecolor('#fcfbf7'); ax.set_facecolor('#fcfbf7')
    for p,color in ((.95,'#a55a37'),(.98,'#176b75'),(.995,'#263d64')):
        ax.plot(range(1,31),[completion(p,n) for n in range(1,31)],color=color,label=f'p = {p}',linewidth=2)
    ax.set(xlabel='Required steps (n)',ylabel='Completion probability',ylim=(0,1),xlim=(1,30),title='Reliable steps do not guarantee a reliable workflow')
    ax.grid(alpha=.15); ax.legend(title='Conditional step success',frameon=False)
    fig.supxlabel('ILLUSTRATIVE · independent steps; no recovery; q = 0 · not measured agent performance',fontsize=9)
    fig.savefig(destination,format='svg',metadata={'Date':None,'Description':'Synthetic reliability curves: p to the power n, for p 0.95, 0.98 and 0.995.'})
    plt.close(fig)

if __name__=='__main__':
    build(Path(__file__).resolve().parents[2]/'paper/figures/reliability.svg')
