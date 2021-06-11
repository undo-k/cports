pkgname = "bsdgrep"
version = "1.0.2"
revision = 1
wrksrc = f"bsdgrep-{version}"
bootstrap = True
build_style = "gnu_makefile"
make_cmd = "bmake"
makedepends = ["bzip2-devel", "zlib-devel", "musl-fts-devel"]
short_desc = "FreeBSD grep(1)"
maintainer = "q66 <daniel@octaforge.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdgrep"
distfiles = [f"https://github.com/chimera-linux/bsdgrep/archive/refs/tags/v{version}.tar.gz"]
checksum = ["7641226235bbd78e58b7fe80bebe22c0b60591bd06e20203543312eb5e8ff1dc"]
