#!/usr/bin/env python


import svglue
import csv
from enum import Enum
import argparse


def waitForResponse(x): 
    out, err = x.communicate() 
    if x.returncode < 0: 
        r = "Popen returncode: " + str(x.returncode)
        raise OSError(r)   
        
def exportToPDF(svg_file, pdf_file, method):
    if method == ExportCore.inkscape:
        from subprocess import Popen
        
        x = Popen(['/usr/bin/inkscape', svg_file, \
       '--export-pdf=%s' % pdf_file])
        try:
            waitForResponse(x)
        except OSError:
            print('OSError')
    elif method == ExportCore.cairosvg:
        import cairosvg
        
        cairosvg.svg2pdf(url= svg_file, write_to= pdf_file.format(count))



class ExportCore(Enum):
    inkscape = 'inkscape'
    cairosvg = 'cairosvg'

    def __str__(self):
        return self.value

parser = argparse.ArgumentParser()
parser.add_argument('name',
                    help="name of svg (template) and csv (data names) files")
parser.add_argument('export', nargs='?', const=ExportCore.cairosvg, type=ExportCore, choices=list(ExportCore),
                    help="export to PDF svgs files using inkscape or cairosvg lib")
args = parser.parse_args()
print(args)

if args.name != None:
    svg_filename = '{}.svg'.format(args.name)
    csv_filename = '{}.csv'.format(args.name)

    # load the template from a file
    tpl = svglue.load(file=svg_filename)



    with open(csv_filename, encoding = "ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            # replace some text
            fullname = '{} {}'.format(row[0], row[1])
            tpl.set_text('textVAR_name', fullname )
            #print(f'\t{row[0]} {row[1]}')
            
            # to render the template, cast it to a string. this also allows passing it
            # as a parameter to set_svg() of another template
            src = str(tpl)
            
            count += 1;
            
            base_filename = '{} ({})'.format(args.name, fullname)
            
            svgout_filename = '{}.svg'.format(base_filename)
            print(svgout_filename)
            
            with open(svgout_filename, 'w') as svgout:
                svgout.write(src)
                
                
            if args.export != None:
                pdfout_filename = '{}.pdf'.format(base_filename)
                exportToPDF(svgout_filename, pdfout_filename, args.export)
            
