import pathlib
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import vplot

import vplanet

# Path hacks
path = pathlib.Path(__file__).parents[0].absolute()
sys.path.insert(1, str(path.parents[0]))
from get_args import get_args

# Tweaks
plt.rcParams.update({"font.size": 16, "legend.fontsize": 16})

#
s_yr = 3600.0 * 24 * 365
filepref = "TidalEarth"

# Run vplanet
out = vplanet.run(path / "vpl.in", units=False)

heating = out.c.PowerEqtide + out.c.RadPowerMan

fig = plt.figure(figsize=(6.5, 6))
plt.subplot(2, 1, 1)
# plt.plot(
#     out.b.Time,
#     out.b.TMan,
#     color=vplot.colors.red,
#     label='b'
# )
plt.plot(
    out.c.Time,
    out.c.TMan,
    color='k'
    #label='c'
)

#plt.legend(loc="best")
plt.ylabel("Mantle Temperature (K)")
plt.title("LP 890-9 c")
plt.xlabel("Time (Gyr)")
plt.xscale("log")
plt.ylim([2400,3400])

plt.subplot(2, 1, 2)
#plt.plot(out.b.Time, out.b.PowerEqtide, color=vplot.colors.red,linestyle=(0, (5, 10)))
plt.plot(out.c.Time, out.c.PowerEqtide, color=vplot.colors.red,linestyle='dashed',label='Tidal Heating')

#plt.plot(out.b.Time, out.b.RadPowerMan, color=vplot.colors.red,linestyle='dotted')
plt.plot(out.c.Time, out.c.RadPowerMan, color=vplot.colors.red,linestyle='dotted',label='Radiogenic Heating')
plt.plot(out.c.Time, heating, color=vplot.colors.red,label='Total Heating')


#plt.plot(out.b.Time, out.b.HflowUMan, color=vplot.colors.red)
plt.plot(out.c.Time, out.c.HflowUMan, color=vplot.colors.pale_blue,linestyle='dashed',label='Convective Cooling')
# plt.plot(
#     out.b.Time, out.b.HflowMeltMan, color=vplot.colors.red, linestyle="-"
# )
plt.plot(
    out.c.Time, out.c.HflowMeltMan, color=vplot.colors.pale_blue, linestyle='dotted',label='Eruptive Cooling'
)

#plt.plot(out.b.Time, out.b.HflowSecMan, color=vplot.colors.red,linestyle='dashdot')
plt.plot(out.c.Time, out.c.HflowSurf, color=vplot.colors.pale_blue,label='Total Cooling')



plt.legend(loc='lower right',fontsize=8)
plt.ylabel("Mantle Heating, Cooling (TW)")
plt.xlabel("Time (Gyr)")
plt.xscale("log")
plt.yscale("log")
plt.ylim([1e-6,1e6])

# Save
ext = get_args().ext
fig.savefig(path / f"flows.{ext}", bbox_inches="tight", dpi=600)
