stages:
  - build
  - pack

builds:
  build:
    base: alpine
    repo: ssh://gitlab@git.garena.com:2222/shopee/cloud/rocksdb.git
    version: "HEAD"
    dir: "/base/rocksdb"
    submodule: true
    commands:
      - >
        apk update && 
        apk add git cmake make gcc g++ &&
        apk add patch zlib-dev curl-dev openssl-dev &&
        cd /base && git clone https://github.com/aws/aws-sdk-cpp.git &&
        cp rocksdb/s3.patch aws-sdk-cpp/ &&
        cd aws-sdk-cpp &&
        git checkout 1.9.31 &&
        git submodule update --init --recursive &&
        patch -p1 -i s3.patch &&
        mkdir build && cd build && 
        cmake .. -DBUILD_ONLY=s3 -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_SHARED_LIBS=ON -DCUSTOM_MEMORY_MANAGEMENT=0 &&
        make -j 8 &&
        make install
    cache:
      "/usr/lib/cmake/AWSSDK": "/usr/lib/cmake/AWSSDK"
      "/usr/lib/cmake": "/usr/lib/cmake"
      "/usr/lib/aws-crt-cpp/cmake": "/usr/lib/aws-crt-cpp/cmake"
      "/usr/lib/aws-c-common/cmake": "/usr/lib/aws-c-common/cmake"
      "/usr/lib/s2n/cmake": "/usr/lib/s2n/cmake"
      "/usr/lib/aws-c-io/cmake": "/usr/lib/aws-c-io/cmake"
      "/usr/lib/aws-c-cal/cmake": "/usr/lib/aws-c-cal/cmake"
      "/usr/lib/aws-c-compression/cmake": "/usr/lib/aws-c-compression/cmake"
      "/usr/lib/aws-c-http/cmake": "/usr/lib/aws-c-http/cmake"
      "/usr/lib/aws-c-auth/cmake": "/usr/lib/aws-c-auth/cmake"
      "/usr/lib/aws-c-mqtt/cmake": "/usr/lib/aws-c-mqtt/cmake"
      "/usr/lib/aws-checksums/cmake": "/usr/lib/aws-checksums/cmake"
      "/usr/lib/aws-c-event-stream/cmake": "/usr/lib/aws-c-event-stream/cmake"
      "/usr/lib/aws-c-s3/cmake": "/usr/lib/aws-c-s3/cmake"
      "/usr/include/s2n.h": "/usr/include/s2n.h"
      "/usr/include/aws": "/usr/include/aws"
      "/usr/lib/libaws-c-auth.so.1.0.0": "/usr/lib/libaws-c-auth.so.1.0.0"
      "/usr/lib/libaws-c-cal.so.1.0.0": "/usr/lib/libaws-c-cal.so.1.0.0"
      "/usr/lib/libaws-c-common.so.1.0.0": "/usr/lib/libaws-c-common.so.1.0.0"
      "/usr/lib/libaws-c-compression.so.1.0.0": "/usr/lib/libaws-c-compression.so.1.0.0"
      "/usr/lib/libaws-c-event-stream.so.1.0.0": "/usr/lib/libaws-c-event-stream.so.1.0.0"
      "/usr/lib/libaws-c-http.so.1.0.0": "/usr/lib/libaws-c-http.so.1.0.0"
      "/usr/lib/libaws-c-io.so.1.0.0": "/usr/lib/libaws-c-io.so.1.0.0"
      "/usr/lib/libaws-c-mqtt.so.1.0.0": "/usr/lib/libaws-c-mqtt.so.1.0.0"
      "/usr/lib/libaws-c-s3.so.1.0.0": "/usr/lib/libaws-c-s3.so.1.0.0"
      "/usr/lib/libaws-checksums.so.1.0.0": "/usr/lib/libaws-checksums.so.1.0.0"
      "/usr/lib/libaws-cpp-sdk-core.so": "/usr/lib/libaws-cpp-sdk-core.so"
      "/usr/lib/libaws-cpp-sdk-s3.so": "/usr/lib/libaws-cpp-sdk-s3.so"
      "/usr/lib/libaws-crt-cpp.so": "/usr/lib/libaws-crt-cpp.so"
      "/usr/lib/libs2n.so": "/usr/lib/libs2n.so"
      "/usr/lib/libtesting-resources.so": "/usr/lib/libtesting-resources.so"
  pack:
    base: alpine
    commands:
      - >
        apk update &&
        apk add zlib curl openssl &&
        ln -s /usr/lib/libaws-c-auth.so.1.0.0 /usr/lib/libaws-c-auth.so &&
        ln -s /usr/lib/libaws-c-cal.so.1.0.0 /usr/lib/libaws-c-cal.so &&
        ln -s /usr/lib/libaws-c-common.so.1.0.0 /usr/lib/libaws-c-common.so &&
        ln -s /usr/lib/libaws-c-common.so.1.0.0 /usr/lib/libaws-c-common.so.1 &&
        ln -s /usr/lib/libaws-c-compression.so.1.0.0 /usr/lib/libaws-c-compression.so &&
        ln -s /usr/lib/libaws-c-compression.so.1.0.0 /usr/lib/libaws-c-compression.so.0unstable &&
        ln -s /usr/lib/libaws-c-event-stream.so.1.0.0 /usr/lib/libaws-c-event-stream.so &&
        ln -s /usr/lib/libaws-c-http.so.1.0.0 /usr/lib/libaws-c-http.so &&
        ln -s /usr/lib/libaws-c-io.so.1.0.0 /usr/lib/libaws-c-io.so &&
        ln -s /usr/lib/libaws-c-mqtt.so.1.0.0 /usr/lib/libaws-c-mqtt.so &&
        ln -s /usr/lib/libaws-c-s3.so.1.0.0 /usr/lib/libaws-c-s3.so &&
        ln -s /usr/lib/libaws-c-s3.so.1.0.0 /usr/lib/libaws-c-s3.so.0unstable &&
        ln -s /usr/lib/libaws-checksums.so.1.0.0 /usr/lib/libaws-checksums.so
