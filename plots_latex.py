import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, Command, NoEscape
from pylatex.utils import italic, NoEscape
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

from pylatex.base_classes import Environment, CommandBase, Arguments


def plotty(ord, asc, Name, end=5):
    with doc.create(TikZ()):
        plot_options = 'height=6cm, width=10cm'
        with doc.create(Axis(options=plot_options)) as plot:
            cordinates=[]
            for x in range(0,end):
                z = (ord[x], asc[x])
                cordinates.append(z)
            plot.append(Plot(name=Name, coordinates=cordinates))
            Command('xlabel', 'ciaone').dumps()





if __name__ == '__main__':

    text = np.loadtxt("convergence_test_details.txt", comments="#")

    meshsize_2D_1 = text [0:5]
    nvertices_2D_1 = text [5:10]
    errors_2D_1 = text [10:15]
    coeff_2D_1 = text [15:19]
    time_2D_1 = text [19:24]
    meshsize_2D_5 = text [24:29]
    nvertices_2D_5 = text [29:34]
    errors_2D_5 = text [34:39]
    coeff_2D_5 = text [39:43]
    time_2D_5 = text [43:48]

    meshsize_3D = text [48:53]
    nvertices_3D = text [53:58]
    errors_3D = text [58:63]
    coeff_3D = text [63:67]
    time_3D = text [67:72]

    weak_scaling_3D = text [72:77]
    strong_scaling_2D = text [77:82]


    doc = Document('basic')

    doc.preamble.append(Command('title', 'Continuous Integration'))
    doc.preamble.append(Command('author', 'MSO4SC'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))


    with doc.create(Section('2D 1 process')):

        with doc.create(Subsection('N Vertices - Convergence rate')):
            plotty(nvertices_2D_5, errors_2D_1, 'estimate', 4)

        with doc.create(Subsection('N Vertices - Errors')):
            plotty(nvertices_2D_5, errors_2D_1, 'errors')

        with doc.create(Subsection('N Vertices - Total time')):
            plotty(nvertices_2D_5, time_2D_1, 'total time')

    with doc.create(Section('2D 5 process')):

        with doc.create(Subsection('N Vertices - Convergence rate')):
            plotty(nvertices_2D_5, coeff_2D_5, 'estimate', 4)

        with doc.create(Subsection('N Vertices - Errors')):
            plotty(nvertices_2D_5, errors_2D_5, 'errors')

        with doc.create(Subsection('N Vertices - Total time')):
            plotty(nvertices_2D_5, time_2D_5, 'total time')

    with doc.create(Section('3D')):

        with doc.create(Subsection('N Processes - Strong Scaling')):
            plotty([1, 2, 4, 8], strong_scaling_2D[0:4], 't1/(tN*N)', 4)

        with doc.create(Subsection('N Processes - Weak Scaling')):
            plotty([1, 2, 4, 8], weak_scaling_3D[0:4], 't1/tN', 4)


    doc.generate_pdf('final', clean_tex=False)
