#!/bin/sh

cat << EOF > ./spec.yaml
stages:
  - build
  - pack

builds:
  build:
    base: harbor.shopeemobile.com/cloud/aws-sdk-cpp:1.9.31
    repo: ssh://gitlab@git.garena.com:2222/shopee/cloud/rocksdb.git
    version: "$CI_COMMIT_SHA"
    commands:
      - >
        apk update &&
        apk add coreutils git cmake make gcc g++ bash &&
        apk add musl-dev linux-headers boost-dev &&
        apk add zlib zlib-dev lz4 lz4-dev snappy snappy-dev &&
        apk add libbz2 bzip2-dev zstd zstd-libs zstd-dev &&
        apk add openssl-dev &&
        apk add dpkg-dev dpkg &&
        mkdir build && cd build &&
        cmake .. -DCMAKE_BUILD_TYPE=$BUILD_TYPE -DBUILD_SHARED_LIBS=ON \
        -DCMAKE_PREFIX_PATH=/usr -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib \
        -DWITH_JEMALLOC=OFF -DWITH_GFLAGS=OFF \
        -DWITH_SNAPPY=ON -DWITH_LZ4=ON -DWITH_ZLIB=ON \
        -DWITH_ZSTD=on -DWITH_BZ2=on \
        -DWITH_AWSS3=ON -DUSE_RTTI=1 &&
        DISABLE_JEMALLOC=1 make rocksdb-shared -j8 DEBUG_LEVEL=$DEBUG &&
        make install PREFIX=/usr
    cache:
      "/usr/include/rocksdb": "/usr/include/rocksdb"
      "/usr/lib/librocksdb.a": "/usr/lib/librocksdb.a"
      "/usr/lib/librocksdb.so.6.26.0": "/usr/lib/librocksdb.so.6.26.0"
  pack:
    base: harbor.shopeemobile.com/cloud/aws-sdk-cpp:1.9.31
    commands:
      - >
        apk update &&
        apk add snappy zlib lz4 lz4-dev boost libbz2 zstd zstd-libs &&
        ln -s /usr/lib/librocksdb.so.6.26.0 /usr/lib/librocksdb.so.6.26 &&
        ln -s /usr/lib/librocksdb.so.6.26.0 /usr/lib/librocksdb.so.6 &&
        ln -s /usr/lib/librocksdb.so.6.26.0 /usr/lib/librocksdb.so
EOF
