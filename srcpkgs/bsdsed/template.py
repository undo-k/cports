pkgname = "bsdsed"
version = "0.99.1"
revision = 1
bootstrap = True
build_style = "gnu_makefile"
make_cmd = "bmake"
short_desc = "The sed(1) utility from FreeBSD"
maintainer = "q66 <daniel@octaforge.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdsed"
distfiles = [f"https://github.com/chimera-linux/bsdsed/archive/refs/tags/v{version}.tar.gz"]
checksum = ["aecd6385ef4ebe97831e92c5d1505f6f054beca17f2a2953874e6326a0afc15b"]
