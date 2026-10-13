"""
Written by Ava Polzin (ava.polzin [at] utoronto.ca) to accompany ngps_pipeline and PypeIt for reducing Palomar/NGPS data.

For some reason none of the headers are exactly how they're supposed to be... (last used Oct. 12, 2026)

This code is an attempt to automate overwriting the problem frame types/lack of lamp details.

Plan is to just grab the data from the night-specific directory, like "preprocess_ngps.py 20260129".
Will handle appending "raw" to directory name, but should include path between working directory and 
night-specific directory in input.


Other things necessary to make the NGPS reduction work out of the box that require reinstallation of the reduction packages:
- In order to make the rest of the pipeline work with PypeIt, you may need to toggle "_require_ug_only_cals = False" 
under PypeIt/pypeit/spectrographs/p200_ngps.py > P200NGPSSpectrograph_g and P200NGPSSpectrograph_u. Otherwise global
calibration files will be ignored in the reduction.
- Similarly, you should ensure that your chosen standard is listed in the STANDARDS tuple in ngps_pipeline/reduce.py.
Otherwise, you will have to add the object name associated with your standard for the flux calibration to move forward.
If it is not in STANDARDS, it will also need to be added to the "for stub in ..." line of ngps_pipeline/finalize.py.
- If the u-band reduction is still not working, comment out "_wave_lamps", "_wave_lamps_wvrng", and "_arc_idnames" in 
PypeIt/pypeit/spectrographs/p200_ngps.py > P200NGPSSpectrograph_u. (He lamps were not used when I observed, but if this is 
not the case for you, it's possible that you'll need to amend the "lamps" list here to account for He, while retaining the 
arguments in the P200NGPSSpectrograph_u class.)
"""

from astropy.io import fits
from glob import glob
import sys

dirname = sys.argv[1]

files = glob(dirname+'/raw/*.fits')
lamps = ['THAR', 'FEAR', 'BLUC', 'REDC']
for f in files:
    fhdu = fits.open(f, mode = 'update')

    ## assuredly better ways to do this, but doing it explicitly to detangle later
    phd = fhdu[0].header
    for ll in lamps:
        if 'LAMP'+ll not in phd:
            if phd['IMGTYPE'] == ll:
                phd['LAMP'+ll] = 'T'
            if phd['IMGTYPE'] != ll:
                phd['LAMP'+ll] = 'F'

        if 'LAMP'+ll in phd: #probably unnecessary, but this ensures consistent formatting
            phd['LAMP'+ll] = str(phd['LAMP'+ll])[0]

    fhdu.close()



