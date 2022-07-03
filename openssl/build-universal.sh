#!/bin/bash

DIR=$(cd `dirname $0` && pwd)
cd $DIR

meson setup arm-build --buildtype=release --cross-file=arm-build.txt
meson compile -C arm-build

meson setup x64-build --buildtype=release --cross-file=x64-build.txt
meson compile -C x64-build

mkdir -p builddir/subprojects/openssl-3.0.2/libcrypto.a.p
mkdir -p builddir/subprojects/openssl-3.0.2/libssl.a.p

lipo -create -output builddir/subprojects/openssl-3.0.2/libcrypto.a arm-build/subprojects/openssl-3.0.2/libcrypto.a x64-build/subprojects/openssl-3.0.2/libcrypto.a
lipo -create -output builddir/subprojects/openssl-3.0.2/libssl.a arm-build/subprojects/openssl-3.0.2/libssl.a x64-build/subprojects/openssl-3.0.2/libssl.a

cd arm-build

for filename in subprojects/openssl-3.0.2/libcrypto.a.p/*.o; do
	if [ -f "../x64-build/$filename" ]
	then
		lipo -create -output ../builddir/$filename ../x64-build/$filename $filename
	else
		cp $filename ../builddir/$filename
	fi
done

for filename in subprojects/openssl-3.0.2/libssl.a.p/*.o; do
	if [ -f "../x64-build/$filename" ]
	then
		lipo -create -output ../builddir/$filename ../x64-build/$filename $filename
	else
		cp $filename ../builddir/$filename
	fi
done

cd ../x64-build

for filename in subprojects/openssl-3.0.2/libcrypto.a.p/*.o; do
	if [ ! -f "../arm-build/$filename" ]
	then
		cp $filename ../builddir/$filename
	fi
done

for filename in subprojects/openssl-3.0.2/libssl.a.p/*.o; do
	if [ ! -f "../arm-build/$filename" ]
	then
		cp $filename ../builddir/$filename
	fi
done
