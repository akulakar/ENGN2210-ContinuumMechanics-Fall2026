"""Schematic for the channel-flow temperature problem (CouetteFlow.qmd)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle

plt.rcParams.update({"mathtext.fontset": "cm", "font.family": "serif", "font.size": 13})

h = 1.0
x1min, x1max = -3.2, 5.2
fig, ax = plt.subplots(figsize=(9.0, 3.9))

# Temperature field t = T0 + dT*x1 shown as a horizontal colour ramp
cmap = LinearSegmentedColormap.from_list("temp", ["#cfe3f5", "#ffffff", "#f7cfc4"])
ramp = np.linspace(0, 1, 256)[None, :]
ax.imshow(ramp, extent=[x1min, x1max, -h, h], aspect="auto", cmap=cmap, zorder=0)

# Fixed plates (hatched walls)
for y0, sgn in [(h, 1), (-h, -1)]:
    ax.add_patch(Rectangle((x1min, y0 if sgn > 0 else y0 - 0.22), x1max - x1min, 0.22,
                           facecolor="#dddddd", edgecolor="k", hatch="////", lw=1.2, zorder=2))
    ax.plot([x1min, x1max], [y0, y0], "k", lw=1.6, zorder=3)
ax.text(x1min + 0.05, h + 0.36, "fixed plate", ha="left", va="center", fontsize=11)
ax.text(x1min + 0.05, -h - 0.36, "fixed plate", ha="left", va="center", fontsize=11)

# Velocity profile v1 = Vmax (1 - (x2/h)^2) drawn at x1 = xp
xp, scale = 2.4, 1.5
ax.plot([xp, xp], [-h, h], color="0.35", lw=1, ls="--", zorder=3)
ys = np.linspace(-h, h, 200)
ax.plot(xp + scale * (1 - (ys / h) ** 2), ys, color="#1f4e9c", lw=1.6, zorder=3)
for y in np.linspace(-0.8, 0.8, 9):
    L = scale * (1 - (y / h) ** 2)
    ax.annotate("", xy=(xp + L, y), xytext=(xp, y),
                arrowprops=dict(arrowstyle="-|>", color="#1f4e9c", lw=1.1, mutation_scale=10), zorder=3)
ax.text(xp + scale + 0.08, 0.1, r"$V_{\max}$", color="#1f4e9c", va="bottom", fontsize=14)
ax.text(xp + 0.75, h + 0.36, r"$v_1 = V_{\max}\left(1-x_2^2/h^2\right)$", color="#1f4e9c", fontsize=12, ha="center", va="center")

# Coordinate axes at origin (centreline)
ax.annotate("", xy=(1.1, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color="k", lw=1.4, mutation_scale=12), zorder=5)
ax.annotate("", xy=(0, 0.75), xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color="k", lw=1.4, mutation_scale=12), zorder=5)
ax.text(1.15, -0.02, r"$x_1$", va="center", fontsize=14)
ax.text(0.05, 0.77, r"$x_2$", va="bottom", fontsize=14)

# Particle P at x = (0, 0)
ax.plot(0, 0, "o", ms=8, mfc="#c0392b", mec="k", zorder=6)
ax.text(-0.12, -0.12, r"$P$", ha="right", va="top", fontsize=14, color="#c0392b")
ax.text(-0.12, -0.42, r"$\mathbf{x} = (0,0)$ at $t = 1\,\mathrm{s}$", ha="right", va="top",
        fontsize=11, color="#c0392b")

# Gap dimension 2h
xd = -2.7
ax.annotate("", xy=(xd, h), xytext=(xd, -h),
            arrowprops=dict(arrowstyle="<|-|>", color="k", lw=1, mutation_scale=10), zorder=5)
ax.text(xd + 0.08, 0.3, r"$2h$", va="center", fontsize=14)

# Temperature annotation
ax.annotate("", xy=(x1max - 0.2, -h - 0.75), xytext=(x1min + 0.2, -h - 0.75),
            arrowprops=dict(arrowstyle="-|>", color="0.25", lw=1.1, mutation_scale=10),
            annotation_clip=False)
ax.text(1.0, -h - 0.82, r"temperature $t(\mathbf{x}) = T_0 + \Delta T\,x_1$ increases with $x_1$",
        ha="center", va="top", fontsize=12, color="0.2")
ax.text(0.0, h + 0.36, r"$t = T_0$ on $x_1 = 0$", ha="center", va="center", fontsize=11)
ax.plot([0, 0], [-h, h], color="0.5", lw=0.8, ls=":", zorder=1)

ax.set_xlim(x1min - 0.05, x1max + 0.05)
ax.set_ylim(-h - 1.25, h + 0.55)
ax.set_aspect("equal")
ax.axis("off")
fig.savefig("couette_flow.svg", bbox_inches="tight", pad_inches=0.05)
fig.savefig("couette_flow.png", dpi=150, bbox_inches="tight", pad_inches=0.05)
