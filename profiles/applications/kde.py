import archinstall
packages = "plasma-meta kde-applications-meta sddm plasma-wayland-session"
if "nvidia" in _gfx_driver_packages:
	packages = packages + " egl-wayland"
installation.add_additional_packages(packages)