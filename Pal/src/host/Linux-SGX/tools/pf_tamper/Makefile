include ../../../../../../Scripts/Makefile.configs
include ../../../../../../Scripts/Makefile.rules

CFLAGS += -I../.. \
          -I../common \
          -I../../protected-files \
          -I../../../../../include/lib \
          -D_GNU_SOURCE

LDLIBS += -L../common \
          -L../../../../../lib/crypto/mbedtls/install/lib \
          -lsgx_util -lmbedcrypto

PREFIX ?= /usr/local

pf_tamper: pf_tamper.o
	$(call cmd,csingle)

.PHONY: all
all: pf_tamper

.PHONY: install
install:
	install -D pf_tamper -t ${PREFIX}/bin

.PHONY: clean
clean:
	$(RM) *.o pf_tamper

.PHONY: distclean
distclean: clean
