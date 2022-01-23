pkgname = "gnutls"
pkgver = "3.7.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-zlib", "--disable-guile", "--disable-static",
    "--disable-valgrind-tests", "--disable-rpath",
    "--with-default-trust-store-file=/etc/ssl/certs/ca-certificates.crt",
]
hostmakedepends = ["pkgconf", "gettext-tiny"]
makedepends = [
    "nettle-devel", "libtasn1-devel", "libidn2-devel", "libgpg-error-devel",
    "libunistring-devel", "zlib-devel", "lzo-devel", "p11-kit-devel",
    "unbound-devel", "trousers-devel",
]
# dlopened
depends = ["libtspi"]
pkgdesc = "GNU Transport Layer Security library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gnutls.org"
source = f"https://www.gnupg.org/ftp/gcrypt/{pkgname}/v{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "646e6c5a9a185faa4cea796d378a1ba8e1148dbb197ca6605f95986a25af2752"
# interactive
options = ["!check"]

@subpackage("gnutls-devel")
def _devel(self):
    self.depends += ["trousers-devel"]

    return self.default_devel(extra = ["usr/share/info"])

@subpackage("gnutls-progs")
def _progs(self):
    return self.default_progs()
