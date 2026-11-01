"""Rebuild the illustrative marketplace figure; requires matplotlib 3.9.2."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'experiments'))
from marketplace import evolve
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def build(destination):
    plt.rcParams.update({'svg.hashsalt':'intent-native-paper','font.family':'DejaVu Sans','font.size':11})
    fig,ax=plt.subplots(figsize=(10,5.5),layout='constrained')
    fig.set_facecolor('#fcfbf7'); ax.set_facecolor('#fcfbf7')
    values=[i/100 for i in range(101)]
    for start,color in ((.05,'#a55a37'),(.95,'#176b75')):
        ax.plot(values,[evolve(start,8,p)['users'] for p in values],color=color,label=f'Initial participation {start}',linewidth=2)
    ax.set(xlabel='Assumed portability parameter (m)',ylabel='Host participation after 400 steps',ylim=(0,1),xlim=(0,1),title='Tipping depends on assumptions about host-specific feedback')
    ax.grid(alpha=.15); ax.legend(frameon=False)
    fig.supxlabel('UNESTIMATED MODEL · b = 8; outside-option offset = -4 · not market share or welfare',fontsize=9)
    fig.savefig(destination,format='svg',metadata={'Date':None,'Description':'Toy two-sided participation model showing dependence on initial conditions and a portability parameter.'})
    plt.close(fig)

if __name__=='__main__':
    build(Path(__file__).resolve().parents[2]/'paper/figures/marketplace.svg')
