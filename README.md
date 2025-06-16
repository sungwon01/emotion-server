# emotion-server
```
emotion-api-server
├─ .venv
│  ├─ bin
│  │  ├─ Activate.ps1
│  │  ├─ activate
│  │  ├─ activate.csh
│  │  ├─ activate.fish
│  │  ├─ distro
│  │  ├─ dotenv
│  │  ├─ fastapi
│  │  ├─ httpx
│  │  ├─ normalizer
│  │  ├─ openai
│  │  ├─ pip
│  │  ├─ pip3
│  │  ├─ pip3.9
│  │  ├─ python
│  │  ├─ python3
│  │  ├─ python3.9
│  │  ├─ tqdm
│  │  ├─ uvicorn
│  │  ├─ watchfiles
│  │  └─ websockets
│  ├─ include
│  ├─ lib
│  │  └─ python3.9
│  │     └─ site-packages
│  │        ├─ PyYAML-6.0.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ top_level.txt
│  │        ├─ _distutils_hack
│  │        │  ├─ __init__.py
│  │        │  └─ override.py
│  │        ├─ _yaml
│  │        │  └─ __init__.py
│  │        ├─ aiofiles
│  │        │  ├─ __init__.py
│  │        │  ├─ base.py
│  │        │  ├─ os.py
│  │        │  ├─ ospath.py
│  │        │  ├─ tempfile
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ temptypes.py
│  │        │  └─ threadpool
│  │        │     ├─ __init__.py
│  │        │     ├─ binary.py
│  │        │     ├─ text.py
│  │        │     └─ utils.py
│  │        ├─ aiofiles-24.1.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     ├─ LICENSE
│  │        │     └─ NOTICE
│  │        ├─ annotated_types
│  │        │  ├─ __init__.py
│  │        │  ├─ py.typed
│  │        │  └─ test_cases.py
│  │        ├─ annotated_types-0.7.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ anyio
│  │        │  ├─ __init__.py
│  │        │  ├─ _backends
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _asyncio.py
│  │        │  │  └─ _trio.py
│  │        │  ├─ _core
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _asyncio_selector_thread.py
│  │        │  │  ├─ _eventloop.py
│  │        │  │  ├─ _exceptions.py
│  │        │  │  ├─ _fileio.py
│  │        │  │  ├─ _resources.py
│  │        │  │  ├─ _signals.py
│  │        │  │  ├─ _sockets.py
│  │        │  │  ├─ _streams.py
│  │        │  │  ├─ _subprocesses.py
│  │        │  │  ├─ _synchronization.py
│  │        │  │  ├─ _tasks.py
│  │        │  │  ├─ _tempfile.py
│  │        │  │  ├─ _testing.py
│  │        │  │  └─ _typedattr.py
│  │        │  ├─ abc
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _eventloop.py
│  │        │  │  ├─ _resources.py
│  │        │  │  ├─ _sockets.py
│  │        │  │  ├─ _streams.py
│  │        │  │  ├─ _subprocesses.py
│  │        │  │  ├─ _tasks.py
│  │        │  │  └─ _testing.py
│  │        │  ├─ from_thread.py
│  │        │  ├─ lowlevel.py
│  │        │  ├─ py.typed
│  │        │  ├─ pytest_plugin.py
│  │        │  ├─ streams
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ buffered.py
│  │        │  │  ├─ file.py
│  │        │  │  ├─ memory.py
│  │        │  │  ├─ stapled.py
│  │        │  │  ├─ text.py
│  │        │  │  └─ tls.py
│  │        │  ├─ to_interpreter.py
│  │        │  ├─ to_process.py
│  │        │  └─ to_thread.py
│  │        ├─ anyio-4.9.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        ├─ bson
│  │        │  ├─ __init__.py
│  │        │  ├─ _cbson.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ _cbsonmodule.c
│  │        │  ├─ _cbsonmodule.h
│  │        │  ├─ _helpers.py
│  │        │  ├─ binary.py
│  │        │  ├─ bson-endian.h
│  │        │  ├─ buffer.c
│  │        │  ├─ buffer.h
│  │        │  ├─ code.py
│  │        │  ├─ codec_options.py
│  │        │  ├─ datetime_ms.py
│  │        │  ├─ dbref.py
│  │        │  ├─ decimal128.py
│  │        │  ├─ errors.py
│  │        │  ├─ int64.py
│  │        │  ├─ json_util.py
│  │        │  ├─ max_key.py
│  │        │  ├─ min_key.py
│  │        │  ├─ objectid.py
│  │        │  ├─ py.typed
│  │        │  ├─ raw_bson.py
│  │        │  ├─ regex.py
│  │        │  ├─ son.py
│  │        │  ├─ time64.c
│  │        │  ├─ time64.h
│  │        │  ├─ time64_config.h
│  │        │  ├─ time64_limits.h
│  │        │  ├─ timestamp.py
│  │        │  ├─ typings.py
│  │        │  └─ tz_util.py
│  │        ├─ certifi
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ cacert.pem
│  │        │  ├─ core.py
│  │        │  └─ py.typed
│  │        ├─ certifi-2025.4.26.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  └─ top_level.txt
│  │        ├─ charset_normalizer
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ api.py
│  │        │  ├─ cd.py
│  │        │  ├─ cli
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __main__.py
│  │        │  ├─ constant.py
│  │        │  ├─ legacy.py
│  │        │  ├─ md.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ md.py
│  │        │  ├─ md__mypyc.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ models.py
│  │        │  ├─ py.typed
│  │        │  ├─ utils.py
│  │        │  └─ version.py
│  │        ├─ charset_normalizer-3.4.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  └─ top_level.txt
│  │        ├─ click
│  │        │  ├─ __init__.py
│  │        │  ├─ _compat.py
│  │        │  ├─ _termui_impl.py
│  │        │  ├─ _textwrap.py
│  │        │  ├─ _winconsole.py
│  │        │  ├─ core.py
│  │        │  ├─ decorators.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ formatting.py
│  │        │  ├─ globals.py
│  │        │  ├─ parser.py
│  │        │  ├─ py.typed
│  │        │  ├─ shell_completion.py
│  │        │  ├─ termui.py
│  │        │  ├─ testing.py
│  │        │  ├─ types.py
│  │        │  └─ utils.py
│  │        ├─ click-8.1.8.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ distro
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ distro.py
│  │        │  └─ py.typed
│  │        ├─ distro-1.9.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        ├─ distutils-precedence.pth
│  │        ├─ dns
│  │        │  ├─ __init__.py
│  │        │  ├─ _asyncbackend.py
│  │        │  ├─ _asyncio_backend.py
│  │        │  ├─ _ddr.py
│  │        │  ├─ _features.py
│  │        │  ├─ _immutable_ctx.py
│  │        │  ├─ _trio_backend.py
│  │        │  ├─ asyncbackend.py
│  │        │  ├─ asyncquery.py
│  │        │  ├─ asyncresolver.py
│  │        │  ├─ dnssec.py
│  │        │  ├─ dnssecalgs
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ cryptography.py
│  │        │  │  ├─ dsa.py
│  │        │  │  ├─ ecdsa.py
│  │        │  │  ├─ eddsa.py
│  │        │  │  └─ rsa.py
│  │        │  ├─ dnssectypes.py
│  │        │  ├─ e164.py
│  │        │  ├─ edns.py
│  │        │  ├─ entropy.py
│  │        │  ├─ enum.py
│  │        │  ├─ exception.py
│  │        │  ├─ flags.py
│  │        │  ├─ grange.py
│  │        │  ├─ immutable.py
│  │        │  ├─ inet.py
│  │        │  ├─ ipv4.py
│  │        │  ├─ ipv6.py
│  │        │  ├─ message.py
│  │        │  ├─ name.py
│  │        │  ├─ namedict.py
│  │        │  ├─ nameserver.py
│  │        │  ├─ node.py
│  │        │  ├─ opcode.py
│  │        │  ├─ py.typed
│  │        │  ├─ query.py
│  │        │  ├─ quic
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _asyncio.py
│  │        │  │  ├─ _common.py
│  │        │  │  ├─ _sync.py
│  │        │  │  └─ _trio.py
│  │        │  ├─ rcode.py
│  │        │  ├─ rdata.py
│  │        │  ├─ rdataclass.py
│  │        │  ├─ rdataset.py
│  │        │  ├─ rdatatype.py
│  │        │  ├─ rdtypes
│  │        │  │  ├─ ANY
│  │        │  │  │  ├─ AFSDB.py
│  │        │  │  │  ├─ AMTRELAY.py
│  │        │  │  │  ├─ AVC.py
│  │        │  │  │  ├─ CAA.py
│  │        │  │  │  ├─ CDNSKEY.py
│  │        │  │  │  ├─ CDS.py
│  │        │  │  │  ├─ CERT.py
│  │        │  │  │  ├─ CNAME.py
│  │        │  │  │  ├─ CSYNC.py
│  │        │  │  │  ├─ DLV.py
│  │        │  │  │  ├─ DNAME.py
│  │        │  │  │  ├─ DNSKEY.py
│  │        │  │  │  ├─ DS.py
│  │        │  │  │  ├─ EUI48.py
│  │        │  │  │  ├─ EUI64.py
│  │        │  │  │  ├─ GPOS.py
│  │        │  │  │  ├─ HINFO.py
│  │        │  │  │  ├─ HIP.py
│  │        │  │  │  ├─ ISDN.py
│  │        │  │  │  ├─ L32.py
│  │        │  │  │  ├─ L64.py
│  │        │  │  │  ├─ LOC.py
│  │        │  │  │  ├─ LP.py
│  │        │  │  │  ├─ MX.py
│  │        │  │  │  ├─ NID.py
│  │        │  │  │  ├─ NINFO.py
│  │        │  │  │  ├─ NS.py
│  │        │  │  │  ├─ NSEC.py
│  │        │  │  │  ├─ NSEC3.py
│  │        │  │  │  ├─ NSEC3PARAM.py
│  │        │  │  │  ├─ OPENPGPKEY.py
│  │        │  │  │  ├─ OPT.py
│  │        │  │  │  ├─ PTR.py
│  │        │  │  │  ├─ RESINFO.py
│  │        │  │  │  ├─ RP.py
│  │        │  │  │  ├─ RRSIG.py
│  │        │  │  │  ├─ RT.py
│  │        │  │  │  ├─ SMIMEA.py
│  │        │  │  │  ├─ SOA.py
│  │        │  │  │  ├─ SPF.py
│  │        │  │  │  ├─ SSHFP.py
│  │        │  │  │  ├─ TKEY.py
│  │        │  │  │  ├─ TLSA.py
│  │        │  │  │  ├─ TSIG.py
│  │        │  │  │  ├─ TXT.py
│  │        │  │  │  ├─ URI.py
│  │        │  │  │  ├─ WALLET.py
│  │        │  │  │  ├─ X25.py
│  │        │  │  │  ├─ ZONEMD.py
│  │        │  │  │  └─ __init__.py
│  │        │  │  ├─ CH
│  │        │  │  │  ├─ A.py
│  │        │  │  │  └─ __init__.py
│  │        │  │  ├─ IN
│  │        │  │  │  ├─ A.py
│  │        │  │  │  ├─ AAAA.py
│  │        │  │  │  ├─ APL.py
│  │        │  │  │  ├─ DHCID.py
│  │        │  │  │  ├─ HTTPS.py
│  │        │  │  │  ├─ IPSECKEY.py
│  │        │  │  │  ├─ KX.py
│  │        │  │  │  ├─ NAPTR.py
│  │        │  │  │  ├─ NSAP.py
│  │        │  │  │  ├─ NSAP_PTR.py
│  │        │  │  │  ├─ PX.py
│  │        │  │  │  ├─ SRV.py
│  │        │  │  │  ├─ SVCB.py
│  │        │  │  │  ├─ WKS.py
│  │        │  │  │  └─ __init__.py
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ dnskeybase.py
│  │        │  │  ├─ dsbase.py
│  │        │  │  ├─ euibase.py
│  │        │  │  ├─ mxbase.py
│  │        │  │  ├─ nsbase.py
│  │        │  │  ├─ svcbbase.py
│  │        │  │  ├─ tlsabase.py
│  │        │  │  ├─ txtbase.py
│  │        │  │  └─ util.py
│  │        │  ├─ renderer.py
│  │        │  ├─ resolver.py
│  │        │  ├─ reversename.py
│  │        │  ├─ rrset.py
│  │        │  ├─ serial.py
│  │        │  ├─ set.py
│  │        │  ├─ tokenizer.py
│  │        │  ├─ transaction.py
│  │        │  ├─ tsig.py
│  │        │  ├─ tsigkeyring.py
│  │        │  ├─ ttl.py
│  │        │  ├─ update.py
│  │        │  ├─ version.py
│  │        │  ├─ versioned.py
│  │        │  ├─ win32util.py
│  │        │  ├─ wire.py
│  │        │  ├─ xfr.py
│  │        │  ├─ zone.py
│  │        │  ├─ zonefile.py
│  │        │  └─ zonetypes.py
│  │        ├─ dnspython-2.7.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ docker
│  │        │  ├─ __init__.py
│  │        │  ├─ _version.py
│  │        │  ├─ api
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ build.py
│  │        │  │  ├─ client.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ container.py
│  │        │  │  ├─ daemon.py
│  │        │  │  ├─ exec_api.py
│  │        │  │  ├─ image.py
│  │        │  │  ├─ network.py
│  │        │  │  ├─ plugin.py
│  │        │  │  ├─ secret.py
│  │        │  │  ├─ service.py
│  │        │  │  ├─ swarm.py
│  │        │  │  └─ volume.py
│  │        │  ├─ auth.py
│  │        │  ├─ client.py
│  │        │  ├─ constants.py
│  │        │  ├─ context
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ api.py
│  │        │  │  ├─ config.py
│  │        │  │  └─ context.py
│  │        │  ├─ credentials
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ constants.py
│  │        │  │  ├─ errors.py
│  │        │  │  ├─ store.py
│  │        │  │  └─ utils.py
│  │        │  ├─ errors.py
│  │        │  ├─ models
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ configs.py
│  │        │  │  ├─ containers.py
│  │        │  │  ├─ images.py
│  │        │  │  ├─ networks.py
│  │        │  │  ├─ nodes.py
│  │        │  │  ├─ plugins.py
│  │        │  │  ├─ resource.py
│  │        │  │  ├─ secrets.py
│  │        │  │  ├─ services.py
│  │        │  │  ├─ swarm.py
│  │        │  │  └─ volumes.py
│  │        │  ├─ tls.py
│  │        │  ├─ transport
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ basehttpadapter.py
│  │        │  │  ├─ npipeconn.py
│  │        │  │  ├─ npipesocket.py
│  │        │  │  ├─ sshconn.py
│  │        │  │  └─ unixconn.py
│  │        │  ├─ types
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ containers.py
│  │        │  │  ├─ daemon.py
│  │        │  │  ├─ healthcheck.py
│  │        │  │  ├─ networks.py
│  │        │  │  ├─ services.py
│  │        │  │  └─ swarm.py
│  │        │  ├─ utils
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ build.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ decorators.py
│  │        │  │  ├─ fnmatch.py
│  │        │  │  ├─ json_stream.py
│  │        │  │  ├─ ports.py
│  │        │  │  ├─ proxy.py
│  │        │  │  ├─ socket.py
│  │        │  │  └─ utils.py
│  │        │  └─ version.py
│  │        ├─ docker-7.1.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ dotenv
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ cli.py
│  │        │  ├─ ipython.py
│  │        │  ├─ main.py
│  │        │  ├─ parser.py
│  │        │  ├─ py.typed
│  │        │  ├─ variables.py
│  │        │  └─ version.py
│  │        ├─ exceptiongroup
│  │        │  ├─ __init__.py
│  │        │  ├─ _catch.py
│  │        │  ├─ _exceptions.py
│  │        │  ├─ _formatting.py
│  │        │  ├─ _suppress.py
│  │        │  ├─ _version.py
│  │        │  └─ py.typed
│  │        ├─ exceptiongroup-1.3.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ fastapi
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ _compat.py
│  │        │  ├─ applications.py
│  │        │  ├─ background.py
│  │        │  ├─ cli.py
│  │        │  ├─ concurrency.py
│  │        │  ├─ datastructures.py
│  │        │  ├─ dependencies
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ models.py
│  │        │  │  └─ utils.py
│  │        │  ├─ encoders.py
│  │        │  ├─ exception_handlers.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ logger.py
│  │        │  ├─ middleware
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ cors.py
│  │        │  │  ├─ gzip.py
│  │        │  │  ├─ httpsredirect.py
│  │        │  │  ├─ trustedhost.py
│  │        │  │  └─ wsgi.py
│  │        │  ├─ openapi
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ constants.py
│  │        │  │  ├─ docs.py
│  │        │  │  ├─ models.py
│  │        │  │  └─ utils.py
│  │        │  ├─ param_functions.py
│  │        │  ├─ params.py
│  │        │  ├─ py.typed
│  │        │  ├─ requests.py
│  │        │  ├─ responses.py
│  │        │  ├─ routing.py
│  │        │  ├─ security
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ api_key.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ http.py
│  │        │  │  ├─ oauth2.py
│  │        │  │  ├─ open_id_connect_url.py
│  │        │  │  └─ utils.py
│  │        │  ├─ staticfiles.py
│  │        │  ├─ templating.py
│  │        │  ├─ testclient.py
│  │        │  ├─ types.py
│  │        │  ├─ utils.py
│  │        │  └─ websockets.py
│  │        ├─ fastapi-0.115.12.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ gridfs
│  │        │  ├─ __init__.py
│  │        │  ├─ asynchronous
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ grid_file.py
│  │        │  ├─ errors.py
│  │        │  ├─ grid_file.py
│  │        │  ├─ grid_file_shared.py
│  │        │  ├─ py.typed
│  │        │  └─ synchronous
│  │        │     ├─ __init__.py
│  │        │     └─ grid_file.py
│  │        ├─ h11
│  │        │  ├─ __init__.py
│  │        │  ├─ _abnf.py
│  │        │  ├─ _connection.py
│  │        │  ├─ _events.py
│  │        │  ├─ _headers.py
│  │        │  ├─ _readers.py
│  │        │  ├─ _receivebuffer.py
│  │        │  ├─ _state.py
│  │        │  ├─ _util.py
│  │        │  ├─ _version.py
│  │        │  ├─ _writers.py
│  │        │  └─ py.typed
│  │        ├─ h11-0.16.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE.txt
│  │        │  └─ top_level.txt
│  │        ├─ httpcore
│  │        │  ├─ __init__.py
│  │        │  ├─ _api.py
│  │        │  ├─ _async
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ connection_pool.py
│  │        │  │  ├─ http11.py
│  │        │  │  ├─ http2.py
│  │        │  │  ├─ http_proxy.py
│  │        │  │  ├─ interfaces.py
│  │        │  │  └─ socks_proxy.py
│  │        │  ├─ _backends
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ anyio.py
│  │        │  │  ├─ auto.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ mock.py
│  │        │  │  ├─ sync.py
│  │        │  │  └─ trio.py
│  │        │  ├─ _exceptions.py
│  │        │  ├─ _models.py
│  │        │  ├─ _ssl.py
│  │        │  ├─ _sync
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ connection_pool.py
│  │        │  │  ├─ http11.py
│  │        │  │  ├─ http2.py
│  │        │  │  ├─ http_proxy.py
│  │        │  │  ├─ interfaces.py
│  │        │  │  └─ socks_proxy.py
│  │        │  ├─ _synchronization.py
│  │        │  ├─ _trace.py
│  │        │  ├─ _utils.py
│  │        │  └─ py.typed
│  │        ├─ httpcore-1.0.9.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE.md
│  │        ├─ httptools
│  │        │  ├─ __init__.py
│  │        │  ├─ _version.py
│  │        │  └─ parser
│  │        │     ├─ __init__.py
│  │        │     ├─ cparser.pxd
│  │        │     ├─ errors.py
│  │        │     ├─ parser.cpython-39-x86_64-linux-gnu.so
│  │        │     ├─ parser.pyx
│  │        │     ├─ python.pxd
│  │        │     ├─ url_cparser.pxd
│  │        │     ├─ url_parser.cpython-39-x86_64-linux-gnu.so
│  │        │     └─ url_parser.pyx
│  │        ├─ httptools-0.6.4.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ top_level.txt
│  │        ├─ httpx
│  │        │  ├─ __init__.py
│  │        │  ├─ __version__.py
│  │        │  ├─ _api.py
│  │        │  ├─ _auth.py
│  │        │  ├─ _client.py
│  │        │  ├─ _config.py
│  │        │  ├─ _content.py
│  │        │  ├─ _decoders.py
│  │        │  ├─ _exceptions.py
│  │        │  ├─ _main.py
│  │        │  ├─ _models.py
│  │        │  ├─ _multipart.py
│  │        │  ├─ _status_codes.py
│  │        │  ├─ _transports
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ asgi.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ default.py
│  │        │  │  ├─ mock.py
│  │        │  │  └─ wsgi.py
│  │        │  ├─ _types.py
│  │        │  ├─ _urlparse.py
│  │        │  ├─ _urls.py
│  │        │  ├─ _utils.py
│  │        │  └─ py.typed
│  │        ├─ httpx-0.28.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ licenses
│  │        │     └─ LICENSE.md
│  │        ├─ idna
│  │        │  ├─ __init__.py
│  │        │  ├─ codec.py
│  │        │  ├─ compat.py
│  │        │  ├─ core.py
│  │        │  ├─ idnadata.py
│  │        │  ├─ intranges.py
│  │        │  ├─ package_data.py
│  │        │  ├─ py.typed
│  │        │  └─ uts46data.py
│  │        ├─ idna-3.10.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.md
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ jiter
│  │        │  ├─ __init__.py
│  │        │  ├─ __init__.pyi
│  │        │  ├─ jiter.cpython-39-x86_64-linux-gnu.so
│  │        │  └─ py.typed
│  │        ├─ jiter-0.10.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ motor
│  │        │  ├─ __init__.py
│  │        │  ├─ _version.py
│  │        │  ├─ aiohttp
│  │        │  │  └─ __init__.py
│  │        │  ├─ core.py
│  │        │  ├─ core.pyi
│  │        │  ├─ docstrings.py
│  │        │  ├─ frameworks
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ asyncio
│  │        │  │  │  └─ __init__.py
│  │        │  │  └─ tornado
│  │        │  │     └─ __init__.py
│  │        │  ├─ metaprogramming.py
│  │        │  ├─ motor_asyncio.py
│  │        │  ├─ motor_asyncio.pyi
│  │        │  ├─ motor_common.py
│  │        │  ├─ motor_gridfs.py
│  │        │  ├─ motor_gridfs.pyi
│  │        │  ├─ motor_tornado.py
│  │        │  ├─ motor_tornado.pyi
│  │        │  ├─ py.typed
│  │        │  └─ web.py
│  │        ├─ motor-3.7.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ multipart
│  │        │  ├─ __init__.py
│  │        │  ├─ decoders.py
│  │        │  ├─ exceptions.py
│  │        │  └─ multipart.py
│  │        ├─ openai
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ _base_client.py
│  │        │  ├─ _client.py
│  │        │  ├─ _compat.py
│  │        │  ├─ _constants.py
│  │        │  ├─ _exceptions.py
│  │        │  ├─ _extras
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _common.py
│  │        │  │  ├─ numpy_proxy.py
│  │        │  │  ├─ pandas_proxy.py
│  │        │  │  └─ sounddevice_proxy.py
│  │        │  ├─ _files.py
│  │        │  ├─ _legacy_response.py
│  │        │  ├─ _models.py
│  │        │  ├─ _module_client.py
│  │        │  ├─ _qs.py
│  │        │  ├─ _resource.py
│  │        │  ├─ _response.py
│  │        │  ├─ _streaming.py
│  │        │  ├─ _types.py
│  │        │  ├─ _utils
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _logs.py
│  │        │  │  ├─ _proxy.py
│  │        │  │  ├─ _reflection.py
│  │        │  │  ├─ _resources_proxy.py
│  │        │  │  ├─ _streams.py
│  │        │  │  ├─ _sync.py
│  │        │  │  ├─ _transform.py
│  │        │  │  ├─ _typing.py
│  │        │  │  └─ _utils.py
│  │        │  ├─ _version.py
│  │        │  ├─ cli
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _api
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _main.py
│  │        │  │  │  ├─ audio.py
│  │        │  │  │  ├─ chat
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ completions.py
│  │        │  │  │  ├─ completions.py
│  │        │  │  │  ├─ files.py
│  │        │  │  │  ├─ image.py
│  │        │  │  │  └─ models.py
│  │        │  │  ├─ _cli.py
│  │        │  │  ├─ _errors.py
│  │        │  │  ├─ _models.py
│  │        │  │  ├─ _progress.py
│  │        │  │  ├─ _tools
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _main.py
│  │        │  │  │  ├─ fine_tunes.py
│  │        │  │  │  └─ migrate.py
│  │        │  │  └─ _utils.py
│  │        │  ├─ helpers
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ local_audio_player.py
│  │        │  │  └─ microphone.py
│  │        │  ├─ lib
│  │        │  │  ├─ .keep
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _old_api.py
│  │        │  │  ├─ _parsing
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _completions.py
│  │        │  │  │  └─ _responses.py
│  │        │  │  ├─ _pydantic.py
│  │        │  │  ├─ _tools.py
│  │        │  │  ├─ _validators.py
│  │        │  │  ├─ azure.py
│  │        │  │  └─ streaming
│  │        │  │     ├─ __init__.py
│  │        │  │     ├─ _assistants.py
│  │        │  │     ├─ _deltas.py
│  │        │  │     ├─ chat
│  │        │  │     │  ├─ __init__.py
│  │        │  │     │  ├─ _completions.py
│  │        │  │     │  ├─ _events.py
│  │        │  │     │  └─ _types.py
│  │        │  │     └─ responses
│  │        │  │        ├─ __init__.py
│  │        │  │        ├─ _events.py
│  │        │  │        ├─ _responses.py
│  │        │  │        └─ _types.py
│  │        │  ├─ pagination.py
│  │        │  ├─ py.typed
│  │        │  ├─ resources
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ audio
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ audio.py
│  │        │  │  │  ├─ speech.py
│  │        │  │  │  ├─ transcriptions.py
│  │        │  │  │  └─ translations.py
│  │        │  │  ├─ batches.py
│  │        │  │  ├─ beta
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ assistants.py
│  │        │  │  │  ├─ beta.py
│  │        │  │  │  ├─ chat
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ chat.py
│  │        │  │  │  │  └─ completions.py
│  │        │  │  │  ├─ realtime
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ realtime.py
│  │        │  │  │  │  ├─ sessions.py
│  │        │  │  │  │  └─ transcription_sessions.py
│  │        │  │  │  └─ threads
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ messages.py
│  │        │  │  │     ├─ runs
│  │        │  │  │     │  ├─ __init__.py
│  │        │  │  │     │  ├─ runs.py
│  │        │  │  │     │  └─ steps.py
│  │        │  │  │     └─ threads.py
│  │        │  │  ├─ chat
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ chat.py
│  │        │  │  │  └─ completions
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ completions.py
│  │        │  │  │     └─ messages.py
│  │        │  │  ├─ completions.py
│  │        │  │  ├─ containers
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ containers.py
│  │        │  │  │  └─ files
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ content.py
│  │        │  │  │     └─ files.py
│  │        │  │  ├─ embeddings.py
│  │        │  │  ├─ evals
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ evals.py
│  │        │  │  │  └─ runs
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ output_items.py
│  │        │  │  │     └─ runs.py
│  │        │  │  ├─ files.py
│  │        │  │  ├─ fine_tuning
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ alpha
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ alpha.py
│  │        │  │  │  │  └─ graders.py
│  │        │  │  │  ├─ checkpoints
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ checkpoints.py
│  │        │  │  │  │  └─ permissions.py
│  │        │  │  │  ├─ fine_tuning.py
│  │        │  │  │  └─ jobs
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ checkpoints.py
│  │        │  │  │     └─ jobs.py
│  │        │  │  ├─ images.py
│  │        │  │  ├─ models.py
│  │        │  │  ├─ moderations.py
│  │        │  │  ├─ responses
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ input_items.py
│  │        │  │  │  └─ responses.py
│  │        │  │  ├─ uploads
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ parts.py
│  │        │  │  │  └─ uploads.py
│  │        │  │  └─ vector_stores
│  │        │  │     ├─ __init__.py
│  │        │  │     ├─ file_batches.py
│  │        │  │     ├─ files.py
│  │        │  │     └─ vector_stores.py
│  │        │  ├─ types
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ audio
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ speech_create_params.py
│  │        │  │  │  ├─ speech_model.py
│  │        │  │  │  ├─ transcription.py
│  │        │  │  │  ├─ transcription_create_params.py
│  │        │  │  │  ├─ transcription_create_response.py
│  │        │  │  │  ├─ transcription_include.py
│  │        │  │  │  ├─ transcription_segment.py
│  │        │  │  │  ├─ transcription_stream_event.py
│  │        │  │  │  ├─ transcription_text_delta_event.py
│  │        │  │  │  ├─ transcription_text_done_event.py
│  │        │  │  │  ├─ transcription_verbose.py
│  │        │  │  │  ├─ transcription_word.py
│  │        │  │  │  ├─ translation.py
│  │        │  │  │  ├─ translation_create_params.py
│  │        │  │  │  ├─ translation_create_response.py
│  │        │  │  │  └─ translation_verbose.py
│  │        │  │  ├─ audio_model.py
│  │        │  │  ├─ audio_response_format.py
│  │        │  │  ├─ auto_file_chunking_strategy_param.py
│  │        │  │  ├─ batch.py
│  │        │  │  ├─ batch_create_params.py
│  │        │  │  ├─ batch_error.py
│  │        │  │  ├─ batch_list_params.py
│  │        │  │  ├─ batch_request_counts.py
│  │        │  │  ├─ beta
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ assistant.py
│  │        │  │  │  ├─ assistant_create_params.py
│  │        │  │  │  ├─ assistant_deleted.py
│  │        │  │  │  ├─ assistant_list_params.py
│  │        │  │  │  ├─ assistant_response_format_option.py
│  │        │  │  │  ├─ assistant_response_format_option_param.py
│  │        │  │  │  ├─ assistant_stream_event.py
│  │        │  │  │  ├─ assistant_tool.py
│  │        │  │  │  ├─ assistant_tool_choice.py
│  │        │  │  │  ├─ assistant_tool_choice_function.py
│  │        │  │  │  ├─ assistant_tool_choice_function_param.py
│  │        │  │  │  ├─ assistant_tool_choice_option.py
│  │        │  │  │  ├─ assistant_tool_choice_option_param.py
│  │        │  │  │  ├─ assistant_tool_choice_param.py
│  │        │  │  │  ├─ assistant_tool_param.py
│  │        │  │  │  ├─ assistant_update_params.py
│  │        │  │  │  ├─ chat
│  │        │  │  │  │  └─ __init__.py
│  │        │  │  │  ├─ code_interpreter_tool.py
│  │        │  │  │  ├─ code_interpreter_tool_param.py
│  │        │  │  │  ├─ file_search_tool.py
│  │        │  │  │  ├─ file_search_tool_param.py
│  │        │  │  │  ├─ function_tool.py
│  │        │  │  │  ├─ function_tool_param.py
│  │        │  │  │  ├─ realtime
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ conversation_created_event.py
│  │        │  │  │  │  ├─ conversation_item.py
│  │        │  │  │  │  ├─ conversation_item_content.py
│  │        │  │  │  │  ├─ conversation_item_content_param.py
│  │        │  │  │  │  ├─ conversation_item_create_event.py
│  │        │  │  │  │  ├─ conversation_item_create_event_param.py
│  │        │  │  │  │  ├─ conversation_item_created_event.py
│  │        │  │  │  │  ├─ conversation_item_delete_event.py
│  │        │  │  │  │  ├─ conversation_item_delete_event_param.py
│  │        │  │  │  │  ├─ conversation_item_deleted_event.py
│  │        │  │  │  │  ├─ conversation_item_input_audio_transcription_completed_event.py
│  │        │  │  │  │  ├─ conversation_item_input_audio_transcription_delta_event.py
│  │        │  │  │  │  ├─ conversation_item_input_audio_transcription_failed_event.py
│  │        │  │  │  │  ├─ conversation_item_param.py
│  │        │  │  │  │  ├─ conversation_item_retrieve_event.py
│  │        │  │  │  │  ├─ conversation_item_retrieve_event_param.py
│  │        │  │  │  │  ├─ conversation_item_truncate_event.py
│  │        │  │  │  │  ├─ conversation_item_truncate_event_param.py
│  │        │  │  │  │  ├─ conversation_item_truncated_event.py
│  │        │  │  │  │  ├─ conversation_item_with_reference.py
│  │        │  │  │  │  ├─ conversation_item_with_reference_param.py
│  │        │  │  │  │  ├─ error_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_append_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_append_event_param.py
│  │        │  │  │  │  ├─ input_audio_buffer_clear_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_clear_event_param.py
│  │        │  │  │  │  ├─ input_audio_buffer_cleared_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_commit_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_commit_event_param.py
│  │        │  │  │  │  ├─ input_audio_buffer_committed_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_speech_started_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_speech_stopped_event.py
│  │        │  │  │  │  ├─ rate_limits_updated_event.py
│  │        │  │  │  │  ├─ realtime_client_event.py
│  │        │  │  │  │  ├─ realtime_client_event_param.py
│  │        │  │  │  │  ├─ realtime_connect_params.py
│  │        │  │  │  │  ├─ realtime_response.py
│  │        │  │  │  │  ├─ realtime_response_status.py
│  │        │  │  │  │  ├─ realtime_response_usage.py
│  │        │  │  │  │  ├─ realtime_server_event.py
│  │        │  │  │  │  ├─ response_audio_delta_event.py
│  │        │  │  │  │  ├─ response_audio_done_event.py
│  │        │  │  │  │  ├─ response_audio_transcript_delta_event.py
│  │        │  │  │  │  ├─ response_audio_transcript_done_event.py
│  │        │  │  │  │  ├─ response_cancel_event.py
│  │        │  │  │  │  ├─ response_cancel_event_param.py
│  │        │  │  │  │  ├─ response_content_part_added_event.py
│  │        │  │  │  │  ├─ response_content_part_done_event.py
│  │        │  │  │  │  ├─ response_create_event.py
│  │        │  │  │  │  ├─ response_create_event_param.py
│  │        │  │  │  │  ├─ response_created_event.py
│  │        │  │  │  │  ├─ response_done_event.py
│  │        │  │  │  │  ├─ response_function_call_arguments_delta_event.py
│  │        │  │  │  │  ├─ response_function_call_arguments_done_event.py
│  │        │  │  │  │  ├─ response_output_item_added_event.py
│  │        │  │  │  │  ├─ response_output_item_done_event.py
│  │        │  │  │  │  ├─ response_text_delta_event.py
│  │        │  │  │  │  ├─ response_text_done_event.py
│  │        │  │  │  │  ├─ session.py
│  │        │  │  │  │  ├─ session_create_params.py
│  │        │  │  │  │  ├─ session_create_response.py
│  │        │  │  │  │  ├─ session_created_event.py
│  │        │  │  │  │  ├─ session_update_event.py
│  │        │  │  │  │  ├─ session_update_event_param.py
│  │        │  │  │  │  ├─ session_updated_event.py
│  │        │  │  │  │  ├─ transcription_session.py
│  │        │  │  │  │  ├─ transcription_session_create_params.py
│  │        │  │  │  │  ├─ transcription_session_update.py
│  │        │  │  │  │  ├─ transcription_session_update_param.py
│  │        │  │  │  │  └─ transcription_session_updated_event.py
│  │        │  │  │  ├─ thread.py
│  │        │  │  │  ├─ thread_create_and_run_params.py
│  │        │  │  │  ├─ thread_create_params.py
│  │        │  │  │  ├─ thread_deleted.py
│  │        │  │  │  ├─ thread_update_params.py
│  │        │  │  │  └─ threads
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ annotation.py
│  │        │  │  │     ├─ annotation_delta.py
│  │        │  │  │     ├─ file_citation_annotation.py
│  │        │  │  │     ├─ file_citation_delta_annotation.py
│  │        │  │  │     ├─ file_path_annotation.py
│  │        │  │  │     ├─ file_path_delta_annotation.py
│  │        │  │  │     ├─ image_file.py
│  │        │  │  │     ├─ image_file_content_block.py
│  │        │  │  │     ├─ image_file_content_block_param.py
│  │        │  │  │     ├─ image_file_delta.py
│  │        │  │  │     ├─ image_file_delta_block.py
│  │        │  │  │     ├─ image_file_param.py
│  │        │  │  │     ├─ image_url.py
│  │        │  │  │     ├─ image_url_content_block.py
│  │        │  │  │     ├─ image_url_content_block_param.py
│  │        │  │  │     ├─ image_url_delta.py
│  │        │  │  │     ├─ image_url_delta_block.py
│  │        │  │  │     ├─ image_url_param.py
│  │        │  │  │     ├─ message.py
│  │        │  │  │     ├─ message_content.py
│  │        │  │  │     ├─ message_content_delta.py
│  │        │  │  │     ├─ message_content_part_param.py
│  │        │  │  │     ├─ message_create_params.py
│  │        │  │  │     ├─ message_deleted.py
│  │        │  │  │     ├─ message_delta.py
│  │        │  │  │     ├─ message_delta_event.py
│  │        │  │  │     ├─ message_list_params.py
│  │        │  │  │     ├─ message_update_params.py
│  │        │  │  │     ├─ refusal_content_block.py
│  │        │  │  │     ├─ refusal_delta_block.py
│  │        │  │  │     ├─ required_action_function_tool_call.py
│  │        │  │  │     ├─ run.py
│  │        │  │  │     ├─ run_create_params.py
│  │        │  │  │     ├─ run_list_params.py
│  │        │  │  │     ├─ run_status.py
│  │        │  │  │     ├─ run_submit_tool_outputs_params.py
│  │        │  │  │     ├─ run_update_params.py
│  │        │  │  │     ├─ runs
│  │        │  │  │     │  ├─ __init__.py
│  │        │  │  │     │  ├─ code_interpreter_logs.py
│  │        │  │  │     │  ├─ code_interpreter_output_image.py
│  │        │  │  │     │  ├─ code_interpreter_tool_call.py
│  │        │  │  │     │  ├─ code_interpreter_tool_call_delta.py
│  │        │  │  │     │  ├─ file_search_tool_call.py
│  │        │  │  │     │  ├─ file_search_tool_call_delta.py
│  │        │  │  │     │  ├─ function_tool_call.py
│  │        │  │  │     │  ├─ function_tool_call_delta.py
│  │        │  │  │     │  ├─ message_creation_step_details.py
│  │        │  │  │     │  ├─ run_step.py
│  │        │  │  │     │  ├─ run_step_delta.py
│  │        │  │  │     │  ├─ run_step_delta_event.py
│  │        │  │  │     │  ├─ run_step_delta_message_delta.py
│  │        │  │  │     │  ├─ run_step_include.py
│  │        │  │  │     │  ├─ step_list_params.py
│  │        │  │  │     │  ├─ step_retrieve_params.py
│  │        │  │  │     │  ├─ tool_call.py
│  │        │  │  │     │  ├─ tool_call_delta.py
│  │        │  │  │     │  ├─ tool_call_delta_object.py
│  │        │  │  │     │  └─ tool_calls_step_details.py
│  │        │  │  │     ├─ text.py
│  │        │  │  │     ├─ text_content_block.py
│  │        │  │  │     ├─ text_content_block_param.py
│  │        │  │  │     ├─ text_delta.py
│  │        │  │  │     └─ text_delta_block.py
│  │        │  │  ├─ chat
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ chat_completion.py
│  │        │  │  │  ├─ chat_completion_assistant_message_param.py
│  │        │  │  │  ├─ chat_completion_audio.py
│  │        │  │  │  ├─ chat_completion_audio_param.py
│  │        │  │  │  ├─ chat_completion_chunk.py
│  │        │  │  │  ├─ chat_completion_content_part_image_param.py
│  │        │  │  │  ├─ chat_completion_content_part_input_audio_param.py
│  │        │  │  │  ├─ chat_completion_content_part_param.py
│  │        │  │  │  ├─ chat_completion_content_part_refusal_param.py
│  │        │  │  │  ├─ chat_completion_content_part_text_param.py
│  │        │  │  │  ├─ chat_completion_deleted.py
│  │        │  │  │  ├─ chat_completion_developer_message_param.py
│  │        │  │  │  ├─ chat_completion_function_call_option_param.py
│  │        │  │  │  ├─ chat_completion_function_message_param.py
│  │        │  │  │  ├─ chat_completion_message.py
│  │        │  │  │  ├─ chat_completion_message_param.py
│  │        │  │  │  ├─ chat_completion_message_tool_call.py
│  │        │  │  │  ├─ chat_completion_message_tool_call_param.py
│  │        │  │  │  ├─ chat_completion_modality.py
│  │        │  │  │  ├─ chat_completion_named_tool_choice_param.py
│  │        │  │  │  ├─ chat_completion_prediction_content_param.py
│  │        │  │  │  ├─ chat_completion_reasoning_effort.py
│  │        │  │  │  ├─ chat_completion_role.py
│  │        │  │  │  ├─ chat_completion_store_message.py
│  │        │  │  │  ├─ chat_completion_stream_options_param.py
│  │        │  │  │  ├─ chat_completion_system_message_param.py
│  │        │  │  │  ├─ chat_completion_token_logprob.py
│  │        │  │  │  ├─ chat_completion_tool_choice_option_param.py
│  │        │  │  │  ├─ chat_completion_tool_message_param.py
│  │        │  │  │  ├─ chat_completion_tool_param.py
│  │        │  │  │  ├─ chat_completion_user_message_param.py
│  │        │  │  │  ├─ completion_create_params.py
│  │        │  │  │  ├─ completion_list_params.py
│  │        │  │  │  ├─ completion_update_params.py
│  │        │  │  │  ├─ completions
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ message_list_params.py
│  │        │  │  │  ├─ parsed_chat_completion.py
│  │        │  │  │  └─ parsed_function_tool_call.py
│  │        │  │  ├─ chat_model.py
│  │        │  │  ├─ completion.py
│  │        │  │  ├─ completion_choice.py
│  │        │  │  ├─ completion_create_params.py
│  │        │  │  ├─ completion_usage.py
│  │        │  │  ├─ container_create_params.py
│  │        │  │  ├─ container_create_response.py
│  │        │  │  ├─ container_list_params.py
│  │        │  │  ├─ container_list_response.py
│  │        │  │  ├─ container_retrieve_response.py
│  │        │  │  ├─ containers
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ file_create_params.py
│  │        │  │  │  ├─ file_create_response.py
│  │        │  │  │  ├─ file_list_params.py
│  │        │  │  │  ├─ file_list_response.py
│  │        │  │  │  ├─ file_retrieve_response.py
│  │        │  │  │  └─ files
│  │        │  │  │     └─ __init__.py
│  │        │  │  ├─ create_embedding_response.py
│  │        │  │  ├─ embedding.py
│  │        │  │  ├─ embedding_create_params.py
│  │        │  │  ├─ embedding_model.py
│  │        │  │  ├─ eval_create_params.py
│  │        │  │  ├─ eval_create_response.py
│  │        │  │  ├─ eval_custom_data_source_config.py
│  │        │  │  ├─ eval_delete_response.py
│  │        │  │  ├─ eval_list_params.py
│  │        │  │  ├─ eval_list_response.py
│  │        │  │  ├─ eval_retrieve_response.py
│  │        │  │  ├─ eval_stored_completions_data_source_config.py
│  │        │  │  ├─ eval_update_params.py
│  │        │  │  ├─ eval_update_response.py
│  │        │  │  ├─ evals
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ create_eval_completions_run_data_source.py
│  │        │  │  │  ├─ create_eval_completions_run_data_source_param.py
│  │        │  │  │  ├─ create_eval_jsonl_run_data_source.py
│  │        │  │  │  ├─ create_eval_jsonl_run_data_source_param.py
│  │        │  │  │  ├─ eval_api_error.py
│  │        │  │  │  ├─ run_cancel_response.py
│  │        │  │  │  ├─ run_create_params.py
│  │        │  │  │  ├─ run_create_response.py
│  │        │  │  │  ├─ run_delete_response.py
│  │        │  │  │  ├─ run_list_params.py
│  │        │  │  │  ├─ run_list_response.py
│  │        │  │  │  ├─ run_retrieve_response.py
│  │        │  │  │  └─ runs
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ output_item_list_params.py
│  │        │  │  │     ├─ output_item_list_response.py
│  │        │  │  │     └─ output_item_retrieve_response.py
│  │        │  │  ├─ file_chunking_strategy.py
│  │        │  │  ├─ file_chunking_strategy_param.py
│  │        │  │  ├─ file_content.py
│  │        │  │  ├─ file_create_params.py
│  │        │  │  ├─ file_deleted.py
│  │        │  │  ├─ file_list_params.py
│  │        │  │  ├─ file_object.py
│  │        │  │  ├─ file_purpose.py
│  │        │  │  ├─ fine_tuning
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ alpha
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ grader_run_params.py
│  │        │  │  │  │  ├─ grader_run_response.py
│  │        │  │  │  │  ├─ grader_validate_params.py
│  │        │  │  │  │  └─ grader_validate_response.py
│  │        │  │  │  ├─ checkpoints
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ permission_create_params.py
│  │        │  │  │  │  ├─ permission_create_response.py
│  │        │  │  │  │  ├─ permission_delete_response.py
│  │        │  │  │  │  ├─ permission_retrieve_params.py
│  │        │  │  │  │  └─ permission_retrieve_response.py
│  │        │  │  │  ├─ dpo_hyperparameters.py
│  │        │  │  │  ├─ dpo_hyperparameters_param.py
│  │        │  │  │  ├─ dpo_method.py
│  │        │  │  │  ├─ dpo_method_param.py
│  │        │  │  │  ├─ fine_tuning_job.py
│  │        │  │  │  ├─ fine_tuning_job_event.py
│  │        │  │  │  ├─ fine_tuning_job_integration.py
│  │        │  │  │  ├─ fine_tuning_job_wandb_integration.py
│  │        │  │  │  ├─ fine_tuning_job_wandb_integration_object.py
│  │        │  │  │  ├─ job_create_params.py
│  │        │  │  │  ├─ job_list_events_params.py
│  │        │  │  │  ├─ job_list_params.py
│  │        │  │  │  ├─ jobs
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ checkpoint_list_params.py
│  │        │  │  │  │  └─ fine_tuning_job_checkpoint.py
│  │        │  │  │  ├─ reinforcement_hyperparameters.py
│  │        │  │  │  ├─ reinforcement_hyperparameters_param.py
│  │        │  │  │  ├─ reinforcement_method.py
│  │        │  │  │  ├─ reinforcement_method_param.py
│  │        │  │  │  ├─ supervised_hyperparameters.py
│  │        │  │  │  ├─ supervised_hyperparameters_param.py
│  │        │  │  │  ├─ supervised_method.py
│  │        │  │  │  └─ supervised_method_param.py
│  │        │  │  ├─ graders
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ label_model_grader.py
│  │        │  │  │  ├─ label_model_grader_param.py
│  │        │  │  │  ├─ multi_grader.py
│  │        │  │  │  ├─ multi_grader_param.py
│  │        │  │  │  ├─ python_grader.py
│  │        │  │  │  ├─ python_grader_param.py
│  │        │  │  │  ├─ score_model_grader.py
│  │        │  │  │  ├─ score_model_grader_param.py
│  │        │  │  │  ├─ string_check_grader.py
│  │        │  │  │  ├─ string_check_grader_param.py
│  │        │  │  │  ├─ text_similarity_grader.py
│  │        │  │  │  └─ text_similarity_grader_param.py
│  │        │  │  ├─ image.py
│  │        │  │  ├─ image_create_variation_params.py
│  │        │  │  ├─ image_edit_params.py
│  │        │  │  ├─ image_generate_params.py
│  │        │  │  ├─ image_model.py
│  │        │  │  ├─ images_response.py
│  │        │  │  ├─ model.py
│  │        │  │  ├─ model_deleted.py
│  │        │  │  ├─ moderation.py
│  │        │  │  ├─ moderation_create_params.py
│  │        │  │  ├─ moderation_create_response.py
│  │        │  │  ├─ moderation_image_url_input_param.py
│  │        │  │  ├─ moderation_model.py
│  │        │  │  ├─ moderation_multi_modal_input_param.py
│  │        │  │  ├─ moderation_text_input_param.py
│  │        │  │  ├─ other_file_chunking_strategy_object.py
│  │        │  │  ├─ responses
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ computer_tool.py
│  │        │  │  │  ├─ computer_tool_param.py
│  │        │  │  │  ├─ easy_input_message.py
│  │        │  │  │  ├─ easy_input_message_param.py
│  │        │  │  │  ├─ file_search_tool.py
│  │        │  │  │  ├─ file_search_tool_param.py
│  │        │  │  │  ├─ function_tool.py
│  │        │  │  │  ├─ function_tool_param.py
│  │        │  │  │  ├─ input_item_list_params.py
│  │        │  │  │  ├─ parsed_response.py
│  │        │  │  │  ├─ response.py
│  │        │  │  │  ├─ response_audio_delta_event.py
│  │        │  │  │  ├─ response_audio_done_event.py
│  │        │  │  │  ├─ response_audio_transcript_delta_event.py
│  │        │  │  │  ├─ response_audio_transcript_done_event.py
│  │        │  │  │  ├─ response_code_interpreter_call_code_delta_event.py
│  │        │  │  │  ├─ response_code_interpreter_call_code_done_event.py
│  │        │  │  │  ├─ response_code_interpreter_call_completed_event.py
│  │        │  │  │  ├─ response_code_interpreter_call_in_progress_event.py
│  │        │  │  │  ├─ response_code_interpreter_call_interpreting_event.py
│  │        │  │  │  ├─ response_code_interpreter_tool_call.py
│  │        │  │  │  ├─ response_code_interpreter_tool_call_param.py
│  │        │  │  │  ├─ response_completed_event.py
│  │        │  │  │  ├─ response_computer_tool_call.py
│  │        │  │  │  ├─ response_computer_tool_call_output_item.py
│  │        │  │  │  ├─ response_computer_tool_call_output_screenshot.py
│  │        │  │  │  ├─ response_computer_tool_call_output_screenshot_param.py
│  │        │  │  │  ├─ response_computer_tool_call_param.py
│  │        │  │  │  ├─ response_content_part_added_event.py
│  │        │  │  │  ├─ response_content_part_done_event.py
│  │        │  │  │  ├─ response_create_params.py
│  │        │  │  │  ├─ response_created_event.py
│  │        │  │  │  ├─ response_error.py
│  │        │  │  │  ├─ response_error_event.py
│  │        │  │  │  ├─ response_failed_event.py
│  │        │  │  │  ├─ response_file_search_call_completed_event.py
│  │        │  │  │  ├─ response_file_search_call_in_progress_event.py
│  │        │  │  │  ├─ response_file_search_call_searching_event.py
│  │        │  │  │  ├─ response_file_search_tool_call.py
│  │        │  │  │  ├─ response_file_search_tool_call_param.py
│  │        │  │  │  ├─ response_format_text_config.py
│  │        │  │  │  ├─ response_format_text_config_param.py
│  │        │  │  │  ├─ response_format_text_json_schema_config.py
│  │        │  │  │  ├─ response_format_text_json_schema_config_param.py
│  │        │  │  │  ├─ response_function_call_arguments_delta_event.py
│  │        │  │  │  ├─ response_function_call_arguments_done_event.py
│  │        │  │  │  ├─ response_function_tool_call.py
│  │        │  │  │  ├─ response_function_tool_call_item.py
│  │        │  │  │  ├─ response_function_tool_call_output_item.py
│  │        │  │  │  ├─ response_function_tool_call_param.py
│  │        │  │  │  ├─ response_function_web_search.py
│  │        │  │  │  ├─ response_function_web_search_param.py
│  │        │  │  │  ├─ response_image_gen_call_completed_event.py
│  │        │  │  │  ├─ response_image_gen_call_generating_event.py
│  │        │  │  │  ├─ response_image_gen_call_in_progress_event.py
│  │        │  │  │  ├─ response_image_gen_call_partial_image_event.py
│  │        │  │  │  ├─ response_in_progress_event.py
│  │        │  │  │  ├─ response_includable.py
│  │        │  │  │  ├─ response_incomplete_event.py
│  │        │  │  │  ├─ response_input_content.py
│  │        │  │  │  ├─ response_input_content_param.py
│  │        │  │  │  ├─ response_input_file.py
│  │        │  │  │  ├─ response_input_file_param.py
│  │        │  │  │  ├─ response_input_image.py
│  │        │  │  │  ├─ response_input_image_param.py
│  │        │  │  │  ├─ response_input_item_param.py
│  │        │  │  │  ├─ response_input_message_content_list.py
│  │        │  │  │  ├─ response_input_message_content_list_param.py
│  │        │  │  │  ├─ response_input_message_item.py
│  │        │  │  │  ├─ response_input_param.py
│  │        │  │  │  ├─ response_input_text.py
│  │        │  │  │  ├─ response_input_text_param.py
│  │        │  │  │  ├─ response_item.py
│  │        │  │  │  ├─ response_item_list.py
│  │        │  │  │  ├─ response_mcp_call_arguments_delta_event.py
│  │        │  │  │  ├─ response_mcp_call_arguments_done_event.py
│  │        │  │  │  ├─ response_mcp_call_completed_event.py
│  │        │  │  │  ├─ response_mcp_call_failed_event.py
│  │        │  │  │  ├─ response_mcp_call_in_progress_event.py
│  │        │  │  │  ├─ response_mcp_list_tools_completed_event.py
│  │        │  │  │  ├─ response_mcp_list_tools_failed_event.py
│  │        │  │  │  ├─ response_mcp_list_tools_in_progress_event.py
│  │        │  │  │  ├─ response_output_item.py
│  │        │  │  │  ├─ response_output_item_added_event.py
│  │        │  │  │  ├─ response_output_item_done_event.py
│  │        │  │  │  ├─ response_output_message.py
│  │        │  │  │  ├─ response_output_message_param.py
│  │        │  │  │  ├─ response_output_refusal.py
│  │        │  │  │  ├─ response_output_refusal_param.py
│  │        │  │  │  ├─ response_output_text.py
│  │        │  │  │  ├─ response_output_text_annotation_added_event.py
│  │        │  │  │  ├─ response_output_text_param.py
│  │        │  │  │  ├─ response_queued_event.py
│  │        │  │  │  ├─ response_reasoning_delta_event.py
│  │        │  │  │  ├─ response_reasoning_done_event.py
│  │        │  │  │  ├─ response_reasoning_item.py
│  │        │  │  │  ├─ response_reasoning_item_param.py
│  │        │  │  │  ├─ response_reasoning_summary_delta_event.py
│  │        │  │  │  ├─ response_reasoning_summary_done_event.py
│  │        │  │  │  ├─ response_reasoning_summary_part_added_event.py
│  │        │  │  │  ├─ response_reasoning_summary_part_done_event.py
│  │        │  │  │  ├─ response_reasoning_summary_text_delta_event.py
│  │        │  │  │  ├─ response_reasoning_summary_text_done_event.py
│  │        │  │  │  ├─ response_refusal_delta_event.py
│  │        │  │  │  ├─ response_refusal_done_event.py
│  │        │  │  │  ├─ response_retrieve_params.py
│  │        │  │  │  ├─ response_status.py
│  │        │  │  │  ├─ response_stream_event.py
│  │        │  │  │  ├─ response_text_config.py
│  │        │  │  │  ├─ response_text_config_param.py
│  │        │  │  │  ├─ response_text_delta_event.py
│  │        │  │  │  ├─ response_text_done_event.py
│  │        │  │  │  ├─ response_usage.py
│  │        │  │  │  ├─ response_web_search_call_completed_event.py
│  │        │  │  │  ├─ response_web_search_call_in_progress_event.py
│  │        │  │  │  ├─ response_web_search_call_searching_event.py
│  │        │  │  │  ├─ tool.py
│  │        │  │  │  ├─ tool_choice_function.py
│  │        │  │  │  ├─ tool_choice_function_param.py
│  │        │  │  │  ├─ tool_choice_options.py
│  │        │  │  │  ├─ tool_choice_types.py
│  │        │  │  │  ├─ tool_choice_types_param.py
│  │        │  │  │  ├─ tool_param.py
│  │        │  │  │  ├─ web_search_tool.py
│  │        │  │  │  └─ web_search_tool_param.py
│  │        │  │  ├─ shared
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ all_models.py
│  │        │  │  │  ├─ chat_model.py
│  │        │  │  │  ├─ comparison_filter.py
│  │        │  │  │  ├─ compound_filter.py
│  │        │  │  │  ├─ error_object.py
│  │        │  │  │  ├─ function_definition.py
│  │        │  │  │  ├─ function_parameters.py
│  │        │  │  │  ├─ metadata.py
│  │        │  │  │  ├─ reasoning.py
│  │        │  │  │  ├─ reasoning_effort.py
│  │        │  │  │  ├─ response_format_json_object.py
│  │        │  │  │  ├─ response_format_json_schema.py
│  │        │  │  │  ├─ response_format_text.py
│  │        │  │  │  └─ responses_model.py
│  │        │  │  ├─ shared_params
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ chat_model.py
│  │        │  │  │  ├─ comparison_filter.py
│  │        │  │  │  ├─ compound_filter.py
│  │        │  │  │  ├─ function_definition.py
│  │        │  │  │  ├─ function_parameters.py
│  │        │  │  │  ├─ metadata.py
│  │        │  │  │  ├─ reasoning.py
│  │        │  │  │  ├─ reasoning_effort.py
│  │        │  │  │  ├─ response_format_json_object.py
│  │        │  │  │  ├─ response_format_json_schema.py
│  │        │  │  │  ├─ response_format_text.py
│  │        │  │  │  └─ responses_model.py
│  │        │  │  ├─ static_file_chunking_strategy.py
│  │        │  │  ├─ static_file_chunking_strategy_object.py
│  │        │  │  ├─ static_file_chunking_strategy_object_param.py
│  │        │  │  ├─ static_file_chunking_strategy_param.py
│  │        │  │  ├─ upload.py
│  │        │  │  ├─ upload_complete_params.py
│  │        │  │  ├─ upload_create_params.py
│  │        │  │  ├─ uploads
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ part_create_params.py
│  │        │  │  │  └─ upload_part.py
│  │        │  │  ├─ vector_store.py
│  │        │  │  ├─ vector_store_create_params.py
│  │        │  │  ├─ vector_store_deleted.py
│  │        │  │  ├─ vector_store_list_params.py
│  │        │  │  ├─ vector_store_search_params.py
│  │        │  │  ├─ vector_store_search_response.py
│  │        │  │  ├─ vector_store_update_params.py
│  │        │  │  ├─ vector_stores
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ file_batch_create_params.py
│  │        │  │  │  ├─ file_batch_list_files_params.py
│  │        │  │  │  ├─ file_content_response.py
│  │        │  │  │  ├─ file_create_params.py
│  │        │  │  │  ├─ file_list_params.py
│  │        │  │  │  ├─ file_update_params.py
│  │        │  │  │  ├─ vector_store_file.py
│  │        │  │  │  ├─ vector_store_file_batch.py
│  │        │  │  │  └─ vector_store_file_deleted.py
│  │        │  │  └─ websocket_connection_options.py
│  │        │  └─ version.py
│  │        ├─ openai-1.82.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ pip
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ __pip-runner__.py
│  │        │  ├─ _internal
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ build_env.py
│  │        │  │  ├─ cache.py
│  │        │  │  ├─ cli
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ autocompletion.py
│  │        │  │  │  ├─ base_command.py
│  │        │  │  │  ├─ cmdoptions.py
│  │        │  │  │  ├─ command_context.py
│  │        │  │  │  ├─ main.py
│  │        │  │  │  ├─ main_parser.py
│  │        │  │  │  ├─ parser.py
│  │        │  │  │  ├─ progress_bars.py
│  │        │  │  │  ├─ req_command.py
│  │        │  │  │  ├─ spinners.py
│  │        │  │  │  └─ status_codes.py
│  │        │  │  ├─ commands
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ cache.py
│  │        │  │  │  ├─ check.py
│  │        │  │  │  ├─ completion.py
│  │        │  │  │  ├─ configuration.py
│  │        │  │  │  ├─ debug.py
│  │        │  │  │  ├─ download.py
│  │        │  │  │  ├─ freeze.py
│  │        │  │  │  ├─ hash.py
│  │        │  │  │  ├─ help.py
│  │        │  │  │  ├─ index.py
│  │        │  │  │  ├─ inspect.py
│  │        │  │  │  ├─ install.py
│  │        │  │  │  ├─ list.py
│  │        │  │  │  ├─ search.py
│  │        │  │  │  ├─ show.py
│  │        │  │  │  ├─ uninstall.py
│  │        │  │  │  └─ wheel.py
│  │        │  │  ├─ configuration.py
│  │        │  │  ├─ distributions
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ installed.py
│  │        │  │  │  ├─ sdist.py
│  │        │  │  │  └─ wheel.py
│  │        │  │  ├─ exceptions.py
│  │        │  │  ├─ index
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ collector.py
│  │        │  │  │  ├─ package_finder.py
│  │        │  │  │  └─ sources.py
│  │        │  │  ├─ locations
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _distutils.py
│  │        │  │  │  ├─ _sysconfig.py
│  │        │  │  │  └─ base.py
│  │        │  │  ├─ main.py
│  │        │  │  ├─ metadata
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _json.py
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ importlib
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ _compat.py
│  │        │  │  │  │  ├─ _dists.py
│  │        │  │  │  │  └─ _envs.py
│  │        │  │  │  └─ pkg_resources.py
│  │        │  │  ├─ models
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ candidate.py
│  │        │  │  │  ├─ direct_url.py
│  │        │  │  │  ├─ format_control.py
│  │        │  │  │  ├─ index.py
│  │        │  │  │  ├─ installation_report.py
│  │        │  │  │  ├─ link.py
│  │        │  │  │  ├─ scheme.py
│  │        │  │  │  ├─ search_scope.py
│  │        │  │  │  ├─ selection_prefs.py
│  │        │  │  │  ├─ target_python.py
│  │        │  │  │  └─ wheel.py
│  │        │  │  ├─ network
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ auth.py
│  │        │  │  │  ├─ cache.py
│  │        │  │  │  ├─ download.py
│  │        │  │  │  ├─ lazy_wheel.py
│  │        │  │  │  ├─ session.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  └─ xmlrpc.py
│  │        │  │  ├─ operations
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ build
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ build_tracker.py
│  │        │  │  │  │  ├─ metadata.py
│  │        │  │  │  │  ├─ metadata_editable.py
│  │        │  │  │  │  ├─ metadata_legacy.py
│  │        │  │  │  │  ├─ wheel.py
│  │        │  │  │  │  ├─ wheel_editable.py
│  │        │  │  │  │  └─ wheel_legacy.py
│  │        │  │  │  ├─ check.py
│  │        │  │  │  ├─ freeze.py
│  │        │  │  │  ├─ install
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ editable_legacy.py
│  │        │  │  │  │  ├─ legacy.py
│  │        │  │  │  │  └─ wheel.py
│  │        │  │  │  └─ prepare.py
│  │        │  │  ├─ pyproject.py
│  │        │  │  ├─ req
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ constructors.py
│  │        │  │  │  ├─ req_file.py
│  │        │  │  │  ├─ req_install.py
│  │        │  │  │  ├─ req_set.py
│  │        │  │  │  └─ req_uninstall.py
│  │        │  │  ├─ resolution
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ legacy
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ resolver.py
│  │        │  │  │  └─ resolvelib
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ base.py
│  │        │  │  │     ├─ candidates.py
│  │        │  │  │     ├─ factory.py
│  │        │  │  │     ├─ found_candidates.py
│  │        │  │  │     ├─ provider.py
│  │        │  │  │     ├─ reporter.py
│  │        │  │  │     ├─ requirements.py
│  │        │  │  │     └─ resolver.py
│  │        │  │  ├─ self_outdated_check.py
│  │        │  │  ├─ utils
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _log.py
│  │        │  │  │  ├─ appdirs.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ compatibility_tags.py
│  │        │  │  │  ├─ datetime.py
│  │        │  │  │  ├─ deprecation.py
│  │        │  │  │  ├─ direct_url_helpers.py
│  │        │  │  │  ├─ distutils_args.py
│  │        │  │  │  ├─ egg_link.py
│  │        │  │  │  ├─ encoding.py
│  │        │  │  │  ├─ entrypoints.py
│  │        │  │  │  ├─ filesystem.py
│  │        │  │  │  ├─ filetypes.py
│  │        │  │  │  ├─ glibc.py
│  │        │  │  │  ├─ hashes.py
│  │        │  │  │  ├─ inject_securetransport.py
│  │        │  │  │  ├─ logging.py
│  │        │  │  │  ├─ misc.py
│  │        │  │  │  ├─ models.py
│  │        │  │  │  ├─ packaging.py
│  │        │  │  │  ├─ setuptools_build.py
│  │        │  │  │  ├─ subprocess.py
│  │        │  │  │  ├─ temp_dir.py
│  │        │  │  │  ├─ unpacking.py
│  │        │  │  │  ├─ urls.py
│  │        │  │  │  ├─ virtualenv.py
│  │        │  │  │  └─ wheel.py
│  │        │  │  ├─ vcs
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ bazaar.py
│  │        │  │  │  ├─ git.py
│  │        │  │  │  ├─ mercurial.py
│  │        │  │  │  ├─ subversion.py
│  │        │  │  │  └─ versioncontrol.py
│  │        │  │  └─ wheel_builder.py
│  │        │  ├─ _vendor
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ cachecontrol
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _cmd.py
│  │        │  │  │  ├─ adapter.py
│  │        │  │  │  ├─ cache.py
│  │        │  │  │  ├─ caches
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ file_cache.py
│  │        │  │  │  │  └─ redis_cache.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ controller.py
│  │        │  │  │  ├─ filewrapper.py
│  │        │  │  │  ├─ heuristics.py
│  │        │  │  │  ├─ serialize.py
│  │        │  │  │  └─ wrapper.py
│  │        │  │  ├─ certifi
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  ├─ cacert.pem
│  │        │  │  │  └─ core.py
│  │        │  │  ├─ chardet
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ big5freq.py
│  │        │  │  │  ├─ big5prober.py
│  │        │  │  │  ├─ chardistribution.py
│  │        │  │  │  ├─ charsetgroupprober.py
│  │        │  │  │  ├─ charsetprober.py
│  │        │  │  │  ├─ cli
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ chardetect.py
│  │        │  │  │  ├─ codingstatemachine.py
│  │        │  │  │  ├─ codingstatemachinedict.py
│  │        │  │  │  ├─ cp949prober.py
│  │        │  │  │  ├─ enums.py
│  │        │  │  │  ├─ escprober.py
│  │        │  │  │  ├─ escsm.py
│  │        │  │  │  ├─ eucjpprober.py
│  │        │  │  │  ├─ euckrfreq.py
│  │        │  │  │  ├─ euckrprober.py
│  │        │  │  │  ├─ euctwfreq.py
│  │        │  │  │  ├─ euctwprober.py
│  │        │  │  │  ├─ gb2312freq.py
│  │        │  │  │  ├─ gb2312prober.py
│  │        │  │  │  ├─ hebrewprober.py
│  │        │  │  │  ├─ jisfreq.py
│  │        │  │  │  ├─ johabfreq.py
│  │        │  │  │  ├─ johabprober.py
│  │        │  │  │  ├─ jpcntx.py
│  │        │  │  │  ├─ langbulgarianmodel.py
│  │        │  │  │  ├─ langgreekmodel.py
│  │        │  │  │  ├─ langhebrewmodel.py
│  │        │  │  │  ├─ langhungarianmodel.py
│  │        │  │  │  ├─ langrussianmodel.py
│  │        │  │  │  ├─ langthaimodel.py
│  │        │  │  │  ├─ langturkishmodel.py
│  │        │  │  │  ├─ latin1prober.py
│  │        │  │  │  ├─ macromanprober.py
│  │        │  │  │  ├─ mbcharsetprober.py
│  │        │  │  │  ├─ mbcsgroupprober.py
│  │        │  │  │  ├─ mbcssm.py
│  │        │  │  │  ├─ metadata
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ languages.py
│  │        │  │  │  ├─ resultdict.py
│  │        │  │  │  ├─ sbcharsetprober.py
│  │        │  │  │  ├─ sbcsgroupprober.py
│  │        │  │  │  ├─ sjisprober.py
│  │        │  │  │  ├─ universaldetector.py
│  │        │  │  │  ├─ utf1632prober.py
│  │        │  │  │  ├─ utf8prober.py
│  │        │  │  │  └─ version.py
│  │        │  │  ├─ colorama
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ ansi.py
│  │        │  │  │  ├─ ansitowin32.py
│  │        │  │  │  ├─ initialise.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ ansi_test.py
│  │        │  │  │  │  ├─ ansitowin32_test.py
│  │        │  │  │  │  ├─ initialise_test.py
│  │        │  │  │  │  ├─ isatty_test.py
│  │        │  │  │  │  ├─ utils.py
│  │        │  │  │  │  └─ winterm_test.py
│  │        │  │  │  ├─ win32.py
│  │        │  │  │  └─ winterm.py
│  │        │  │  ├─ distlib
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ database.py
│  │        │  │  │  ├─ index.py
│  │        │  │  │  ├─ locators.py
│  │        │  │  │  ├─ manifest.py
│  │        │  │  │  ├─ markers.py
│  │        │  │  │  ├─ metadata.py
│  │        │  │  │  ├─ resources.py
│  │        │  │  │  ├─ scripts.py
│  │        │  │  │  ├─ t32.exe
│  │        │  │  │  ├─ t64-arm.exe
│  │        │  │  │  ├─ t64.exe
│  │        │  │  │  ├─ util.py
│  │        │  │  │  ├─ version.py
│  │        │  │  │  ├─ w32.exe
│  │        │  │  │  ├─ w64-arm.exe
│  │        │  │  │  ├─ w64.exe
│  │        │  │  │  └─ wheel.py
│  │        │  │  ├─ distro
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  └─ distro.py
│  │        │  │  ├─ idna
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ codec.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ core.py
│  │        │  │  │  ├─ idnadata.py
│  │        │  │  │  ├─ intranges.py
│  │        │  │  │  ├─ package_data.py
│  │        │  │  │  └─ uts46data.py
│  │        │  │  ├─ msgpack
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ exceptions.py
│  │        │  │  │  ├─ ext.py
│  │        │  │  │  └─ fallback.py
│  │        │  │  ├─ packaging
│  │        │  │  │  ├─ __about__.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _manylinux.py
│  │        │  │  │  ├─ _musllinux.py
│  │        │  │  │  ├─ _structures.py
│  │        │  │  │  ├─ markers.py
│  │        │  │  │  ├─ requirements.py
│  │        │  │  │  ├─ specifiers.py
│  │        │  │  │  ├─ tags.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  └─ version.py
│  │        │  │  ├─ pkg_resources
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ py31compat.py
│  │        │  │  ├─ platformdirs
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  ├─ android.py
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ macos.py
│  │        │  │  │  ├─ unix.py
│  │        │  │  │  ├─ version.py
│  │        │  │  │  └─ windows.py
│  │        │  │  ├─ pygments
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  ├─ cmdline.py
│  │        │  │  │  ├─ console.py
│  │        │  │  │  ├─ filter.py
│  │        │  │  │  ├─ filters
│  │        │  │  │  │  └─ __init__.py
│  │        │  │  │  ├─ formatter.py
│  │        │  │  │  ├─ formatters
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ _mapping.py
│  │        │  │  │  │  ├─ bbcode.py
│  │        │  │  │  │  ├─ groff.py
│  │        │  │  │  │  ├─ html.py
│  │        │  │  │  │  ├─ img.py
│  │        │  │  │  │  ├─ irc.py
│  │        │  │  │  │  ├─ latex.py
│  │        │  │  │  │  ├─ other.py
│  │        │  │  │  │  ├─ pangomarkup.py
│  │        │  │  │  │  ├─ rtf.py
│  │        │  │  │  │  ├─ svg.py
│  │        │  │  │  │  ├─ terminal.py
│  │        │  │  │  │  └─ terminal256.py
│  │        │  │  │  ├─ lexer.py
│  │        │  │  │  ├─ lexers
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ _mapping.py
│  │        │  │  │  │  └─ python.py
│  │        │  │  │  ├─ modeline.py
│  │        │  │  │  ├─ plugin.py
│  │        │  │  │  ├─ regexopt.py
│  │        │  │  │  ├─ scanner.py
│  │        │  │  │  ├─ sphinxext.py
│  │        │  │  │  ├─ style.py
│  │        │  │  │  ├─ styles
│  │        │  │  │  │  └─ __init__.py
│  │        │  │  │  ├─ token.py
│  │        │  │  │  ├─ unistring.py
│  │        │  │  │  └─ util.py
│  │        │  │  ├─ pyparsing
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ actions.py
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ core.py
│  │        │  │  │  ├─ diagram
│  │        │  │  │  │  └─ __init__.py
│  │        │  │  │  ├─ exceptions.py
│  │        │  │  │  ├─ helpers.py
│  │        │  │  │  ├─ results.py
│  │        │  │  │  ├─ testing.py
│  │        │  │  │  ├─ unicode.py
│  │        │  │  │  └─ util.py
│  │        │  │  ├─ pyproject_hooks
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _compat.py
│  │        │  │  │  ├─ _impl.py
│  │        │  │  │  └─ _in_process
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     └─ _in_process.py
│  │        │  │  ├─ requests
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __version__.py
│  │        │  │  │  ├─ _internal_utils.py
│  │        │  │  │  ├─ adapters.py
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ auth.py
│  │        │  │  │  ├─ certs.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ cookies.py
│  │        │  │  │  ├─ exceptions.py
│  │        │  │  │  ├─ help.py
│  │        │  │  │  ├─ hooks.py
│  │        │  │  │  ├─ models.py
│  │        │  │  │  ├─ packages.py
│  │        │  │  │  ├─ sessions.py
│  │        │  │  │  ├─ status_codes.py
│  │        │  │  │  ├─ structures.py
│  │        │  │  │  └─ utils.py
│  │        │  │  ├─ resolvelib
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ compat
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ collections_abc.py
│  │        │  │  │  ├─ providers.py
│  │        │  │  │  ├─ reporters.py
│  │        │  │  │  ├─ resolvers.py
│  │        │  │  │  └─ structs.py
│  │        │  │  ├─ rich
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  ├─ _cell_widths.py
│  │        │  │  │  ├─ _emoji_codes.py
│  │        │  │  │  ├─ _emoji_replace.py
│  │        │  │  │  ├─ _export_format.py
│  │        │  │  │  ├─ _extension.py
│  │        │  │  │  ├─ _inspect.py
│  │        │  │  │  ├─ _log_render.py
│  │        │  │  │  ├─ _loop.py
│  │        │  │  │  ├─ _null_file.py
│  │        │  │  │  ├─ _palettes.py
│  │        │  │  │  ├─ _pick.py
│  │        │  │  │  ├─ _ratio.py
│  │        │  │  │  ├─ _spinners.py
│  │        │  │  │  ├─ _stack.py
│  │        │  │  │  ├─ _timer.py
│  │        │  │  │  ├─ _win32_console.py
│  │        │  │  │  ├─ _windows.py
│  │        │  │  │  ├─ _windows_renderer.py
│  │        │  │  │  ├─ _wrap.py
│  │        │  │  │  ├─ abc.py
│  │        │  │  │  ├─ align.py
│  │        │  │  │  ├─ ansi.py
│  │        │  │  │  ├─ bar.py
│  │        │  │  │  ├─ box.py
│  │        │  │  │  ├─ cells.py
│  │        │  │  │  ├─ color.py
│  │        │  │  │  ├─ color_triplet.py
│  │        │  │  │  ├─ columns.py
│  │        │  │  │  ├─ console.py
│  │        │  │  │  ├─ constrain.py
│  │        │  │  │  ├─ containers.py
│  │        │  │  │  ├─ control.py
│  │        │  │  │  ├─ default_styles.py
│  │        │  │  │  ├─ diagnose.py
│  │        │  │  │  ├─ emoji.py
│  │        │  │  │  ├─ errors.py
│  │        │  │  │  ├─ file_proxy.py
│  │        │  │  │  ├─ filesize.py
│  │        │  │  │  ├─ highlighter.py
│  │        │  │  │  ├─ json.py
│  │        │  │  │  ├─ jupyter.py
│  │        │  │  │  ├─ layout.py
│  │        │  │  │  ├─ live.py
│  │        │  │  │  ├─ live_render.py
│  │        │  │  │  ├─ logging.py
│  │        │  │  │  ├─ markup.py
│  │        │  │  │  ├─ measure.py
│  │        │  │  │  ├─ padding.py
│  │        │  │  │  ├─ pager.py
│  │        │  │  │  ├─ palette.py
│  │        │  │  │  ├─ panel.py
│  │        │  │  │  ├─ pretty.py
│  │        │  │  │  ├─ progress.py
│  │        │  │  │  ├─ progress_bar.py
│  │        │  │  │  ├─ prompt.py
│  │        │  │  │  ├─ protocol.py
│  │        │  │  │  ├─ region.py
│  │        │  │  │  ├─ repr.py
│  │        │  │  │  ├─ rule.py
│  │        │  │  │  ├─ scope.py
│  │        │  │  │  ├─ screen.py
│  │        │  │  │  ├─ segment.py
│  │        │  │  │  ├─ spinner.py
│  │        │  │  │  ├─ status.py
│  │        │  │  │  ├─ style.py
│  │        │  │  │  ├─ styled.py
│  │        │  │  │  ├─ syntax.py
│  │        │  │  │  ├─ table.py
│  │        │  │  │  ├─ terminal_theme.py
│  │        │  │  │  ├─ text.py
│  │        │  │  │  ├─ theme.py
│  │        │  │  │  ├─ themes.py
│  │        │  │  │  ├─ traceback.py
│  │        │  │  │  └─ tree.py
│  │        │  │  ├─ six.py
│  │        │  │  ├─ tenacity
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _asyncio.py
│  │        │  │  │  ├─ _utils.py
│  │        │  │  │  ├─ after.py
│  │        │  │  │  ├─ before.py
│  │        │  │  │  ├─ before_sleep.py
│  │        │  │  │  ├─ nap.py
│  │        │  │  │  ├─ retry.py
│  │        │  │  │  ├─ stop.py
│  │        │  │  │  ├─ tornadoweb.py
│  │        │  │  │  └─ wait.py
│  │        │  │  ├─ tomli
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _parser.py
│  │        │  │  │  ├─ _re.py
│  │        │  │  │  └─ _types.py
│  │        │  │  ├─ typing_extensions.py
│  │        │  │  ├─ urllib3
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _collections.py
│  │        │  │  │  ├─ _version.py
│  │        │  │  │  ├─ connection.py
│  │        │  │  │  ├─ connectionpool.py
│  │        │  │  │  ├─ contrib
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ _appengine_environ.py
│  │        │  │  │  │  ├─ _securetransport
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  ├─ bindings.py
│  │        │  │  │  │  │  └─ low_level.py
│  │        │  │  │  │  ├─ appengine.py
│  │        │  │  │  │  ├─ ntlmpool.py
│  │        │  │  │  │  ├─ pyopenssl.py
│  │        │  │  │  │  ├─ securetransport.py
│  │        │  │  │  │  └─ socks.py
│  │        │  │  │  ├─ exceptions.py
│  │        │  │  │  ├─ fields.py
│  │        │  │  │  ├─ filepost.py
│  │        │  │  │  ├─ packages
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ backports
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ makefile.py
│  │        │  │  │  │  └─ six.py
│  │        │  │  │  ├─ poolmanager.py
│  │        │  │  │  ├─ request.py
│  │        │  │  │  ├─ response.py
│  │        │  │  │  └─ util
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ connection.py
│  │        │  │  │     ├─ proxy.py
│  │        │  │  │     ├─ queue.py
│  │        │  │  │     ├─ request.py
│  │        │  │  │     ├─ response.py
│  │        │  │  │     ├─ retry.py
│  │        │  │  │     ├─ ssl_.py
│  │        │  │  │     ├─ ssl_match_hostname.py
│  │        │  │  │     ├─ ssltransport.py
│  │        │  │  │     ├─ timeout.py
│  │        │  │  │     ├─ url.py
│  │        │  │  │     └─ wait.py
│  │        │  │  ├─ vendor.txt
│  │        │  │  └─ webencodings
│  │        │  │     ├─ __init__.py
│  │        │  │     ├─ labels.py
│  │        │  │     ├─ mklabels.py
│  │        │  │     ├─ tests.py
│  │        │  │     └─ x_user_defined.py
│  │        │  └─ py.typed
│  │        ├─ pip-23.0.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        ├─ pkg_resources
│  │        │  ├─ __init__.py
│  │        │  ├─ _vendor
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ appdirs.py
│  │        │  │  ├─ packaging
│  │        │  │  │  ├─ __about__.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _compat.py
│  │        │  │  │  ├─ _structures.py
│  │        │  │  │  ├─ _typing.py
│  │        │  │  │  ├─ markers.py
│  │        │  │  │  ├─ requirements.py
│  │        │  │  │  ├─ specifiers.py
│  │        │  │  │  ├─ tags.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  └─ version.py
│  │        │  │  └─ pyparsing.py
│  │        │  ├─ extern
│  │        │  │  └─ __init__.py
│  │        │  └─ tests
│  │        │     └─ data
│  │        │        └─ my-test-package-source
│  │        │           └─ setup.py
│  │        ├─ pydantic
│  │        │  ├─ __init__.py
│  │        │  ├─ _internal
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _config.py
│  │        │  │  ├─ _core_metadata.py
│  │        │  │  ├─ _core_utils.py
│  │        │  │  ├─ _dataclasses.py
│  │        │  │  ├─ _decorators.py
│  │        │  │  ├─ _decorators_v1.py
│  │        │  │  ├─ _discriminated_union.py
│  │        │  │  ├─ _docs_extraction.py
│  │        │  │  ├─ _fields.py
│  │        │  │  ├─ _forward_ref.py
│  │        │  │  ├─ _generate_schema.py
│  │        │  │  ├─ _generics.py
│  │        │  │  ├─ _git.py
│  │        │  │  ├─ _import_utils.py
│  │        │  │  ├─ _internal_dataclass.py
│  │        │  │  ├─ _known_annotated_metadata.py
│  │        │  │  ├─ _mock_val_ser.py
│  │        │  │  ├─ _model_construction.py
│  │        │  │  ├─ _namespace_utils.py
│  │        │  │  ├─ _repr.py
│  │        │  │  ├─ _schema_gather.py
│  │        │  │  ├─ _schema_generation_shared.py
│  │        │  │  ├─ _serializers.py
│  │        │  │  ├─ _signature.py
│  │        │  │  ├─ _typing_extra.py
│  │        │  │  ├─ _utils.py
│  │        │  │  ├─ _validate_call.py
│  │        │  │  └─ _validators.py
│  │        │  ├─ _migration.py
│  │        │  ├─ alias_generators.py
│  │        │  ├─ aliases.py
│  │        │  ├─ annotated_handlers.py
│  │        │  ├─ class_validators.py
│  │        │  ├─ color.py
│  │        │  ├─ config.py
│  │        │  ├─ dataclasses.py
│  │        │  ├─ datetime_parse.py
│  │        │  ├─ decorator.py
│  │        │  ├─ deprecated
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ class_validators.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ copy_internals.py
│  │        │  │  ├─ decorator.py
│  │        │  │  ├─ json.py
│  │        │  │  ├─ parse.py
│  │        │  │  └─ tools.py
│  │        │  ├─ env_settings.py
│  │        │  ├─ error_wrappers.py
│  │        │  ├─ errors.py
│  │        │  ├─ experimental
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ arguments_schema.py
│  │        │  │  └─ pipeline.py
│  │        │  ├─ fields.py
│  │        │  ├─ functional_serializers.py
│  │        │  ├─ functional_validators.py
│  │        │  ├─ generics.py
│  │        │  ├─ json.py
│  │        │  ├─ json_schema.py
│  │        │  ├─ main.py
│  │        │  ├─ mypy.py
│  │        │  ├─ networks.py
│  │        │  ├─ parse.py
│  │        │  ├─ plugin
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _loader.py
│  │        │  │  └─ _schema_validator.py
│  │        │  ├─ py.typed
│  │        │  ├─ root_model.py
│  │        │  ├─ schema.py
│  │        │  ├─ tools.py
│  │        │  ├─ type_adapter.py
│  │        │  ├─ types.py
│  │        │  ├─ typing.py
│  │        │  ├─ utils.py
│  │        │  ├─ v1
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _hypothesis_plugin.py
│  │        │  │  ├─ annotated_types.py
│  │        │  │  ├─ class_validators.py
│  │        │  │  ├─ color.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ dataclasses.py
│  │        │  │  ├─ datetime_parse.py
│  │        │  │  ├─ decorator.py
│  │        │  │  ├─ env_settings.py
│  │        │  │  ├─ error_wrappers.py
│  │        │  │  ├─ errors.py
│  │        │  │  ├─ fields.py
│  │        │  │  ├─ generics.py
│  │        │  │  ├─ json.py
│  │        │  │  ├─ main.py
│  │        │  │  ├─ mypy.py
│  │        │  │  ├─ networks.py
│  │        │  │  ├─ parse.py
│  │        │  │  ├─ py.typed
│  │        │  │  ├─ schema.py
│  │        │  │  ├─ tools.py
│  │        │  │  ├─ types.py
│  │        │  │  ├─ typing.py
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ validators.py
│  │        │  │  └─ version.py
│  │        │  ├─ validate_call_decorator.py
│  │        │  ├─ validators.py
│  │        │  ├─ version.py
│  │        │  └─ warnings.py
│  │        ├─ pydantic-2.11.5.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ pydantic_core
│  │        │  ├─ __init__.py
│  │        │  ├─ _pydantic_core.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ _pydantic_core.pyi
│  │        │  ├─ core_schema.py
│  │        │  └─ py.typed
│  │        ├─ pydantic_core-2.33.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ pymongo
│  │        │  ├─ __init__.py
│  │        │  ├─ _asyncio_lock.py
│  │        │  ├─ _asyncio_task.py
│  │        │  ├─ _azure_helpers.py
│  │        │  ├─ _client_bulk_shared.py
│  │        │  ├─ _cmessage.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ _cmessagemodule.c
│  │        │  ├─ _csot.py
│  │        │  ├─ _gcp_helpers.py
│  │        │  ├─ _version.py
│  │        │  ├─ asynchronous
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ aggregation.py
│  │        │  │  ├─ auth.py
│  │        │  │  ├─ auth_aws.py
│  │        │  │  ├─ auth_oidc.py
│  │        │  │  ├─ bulk.py
│  │        │  │  ├─ change_stream.py
│  │        │  │  ├─ client_bulk.py
│  │        │  │  ├─ client_session.py
│  │        │  │  ├─ collection.py
│  │        │  │  ├─ command_cursor.py
│  │        │  │  ├─ cursor.py
│  │        │  │  ├─ database.py
│  │        │  │  ├─ encryption.py
│  │        │  │  ├─ helpers.py
│  │        │  │  ├─ mongo_client.py
│  │        │  │  ├─ monitor.py
│  │        │  │  ├─ network.py
│  │        │  │  ├─ pool.py
│  │        │  │  ├─ server.py
│  │        │  │  ├─ settings.py
│  │        │  │  ├─ srv_resolver.py
│  │        │  │  ├─ topology.py
│  │        │  │  └─ uri_parser.py
│  │        │  ├─ auth.py
│  │        │  ├─ auth_oidc.py
│  │        │  ├─ auth_oidc_shared.py
│  │        │  ├─ auth_shared.py
│  │        │  ├─ bulk_shared.py
│  │        │  ├─ change_stream.py
│  │        │  ├─ client_options.py
│  │        │  ├─ client_session.py
│  │        │  ├─ collation.py
│  │        │  ├─ collection.py
│  │        │  ├─ command_cursor.py
│  │        │  ├─ common.py
│  │        │  ├─ compression_support.py
│  │        │  ├─ cursor.py
│  │        │  ├─ cursor_shared.py
│  │        │  ├─ daemon.py
│  │        │  ├─ database.py
│  │        │  ├─ database_shared.py
│  │        │  ├─ driver_info.py
│  │        │  ├─ encryption.py
│  │        │  ├─ encryption_options.py
│  │        │  ├─ errors.py
│  │        │  ├─ event_loggers.py
│  │        │  ├─ hello.py
│  │        │  ├─ helpers_shared.py
│  │        │  ├─ lock.py
│  │        │  ├─ logger.py
│  │        │  ├─ max_staleness_selectors.py
│  │        │  ├─ message.py
│  │        │  ├─ mongo_client.py
│  │        │  ├─ monitoring.py
│  │        │  ├─ network_layer.py
│  │        │  ├─ ocsp_cache.py
│  │        │  ├─ ocsp_support.py
│  │        │  ├─ operations.py
│  │        │  ├─ periodic_executor.py
│  │        │  ├─ pool.py
│  │        │  ├─ pool_options.py
│  │        │  ├─ pool_shared.py
│  │        │  ├─ py.typed
│  │        │  ├─ pyopenssl_context.py
│  │        │  ├─ read_concern.py
│  │        │  ├─ read_preferences.py
│  │        │  ├─ response.py
│  │        │  ├─ results.py
│  │        │  ├─ saslprep.py
│  │        │  ├─ server_api.py
│  │        │  ├─ server_description.py
│  │        │  ├─ server_selectors.py
│  │        │  ├─ server_type.py
│  │        │  ├─ socket_checker.py
│  │        │  ├─ ssl_context.py
│  │        │  ├─ ssl_support.py
│  │        │  ├─ synchronous
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ aggregation.py
│  │        │  │  ├─ auth.py
│  │        │  │  ├─ auth_aws.py
│  │        │  │  ├─ auth_oidc.py
│  │        │  │  ├─ bulk.py
│  │        │  │  ├─ change_stream.py
│  │        │  │  ├─ client_bulk.py
│  │        │  │  ├─ client_session.py
│  │        │  │  ├─ collection.py
│  │        │  │  ├─ command_cursor.py
│  │        │  │  ├─ cursor.py
│  │        │  │  ├─ database.py
│  │        │  │  ├─ encryption.py
│  │        │  │  ├─ helpers.py
│  │        │  │  ├─ mongo_client.py
│  │        │  │  ├─ monitor.py
│  │        │  │  ├─ network.py
│  │        │  │  ├─ pool.py
│  │        │  │  ├─ server.py
│  │        │  │  ├─ settings.py
│  │        │  │  ├─ srv_resolver.py
│  │        │  │  ├─ topology.py
│  │        │  │  └─ uri_parser.py
│  │        │  ├─ topology_description.py
│  │        │  ├─ typings.py
│  │        │  ├─ uri_parser.py
│  │        │  ├─ uri_parser_shared.py
│  │        │  └─ write_concern.py
│  │        ├─ pymongo-4.13.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ python_dotenv-1.1.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  └─ top_level.txt
│  │        ├─ python_multipart
│  │        │  ├─ __init__.py
│  │        │  ├─ decoders.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ multipart.py
│  │        │  └─ py.typed
│  │        ├─ python_multipart-0.0.20.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE.txt
│  │        ├─ requests
│  │        │  ├─ __init__.py
│  │        │  ├─ __version__.py
│  │        │  ├─ _internal_utils.py
│  │        │  ├─ adapters.py
│  │        │  ├─ api.py
│  │        │  ├─ auth.py
│  │        │  ├─ certs.py
│  │        │  ├─ compat.py
│  │        │  ├─ cookies.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ help.py
│  │        │  ├─ hooks.py
│  │        │  ├─ models.py
│  │        │  ├─ packages.py
│  │        │  ├─ sessions.py
│  │        │  ├─ status_codes.py
│  │        │  ├─ structures.py
│  │        │  └─ utils.py
│  │        ├─ requests-2.32.3.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ top_level.txt
│  │        ├─ setuptools
│  │        │  ├─ __init__.py
│  │        │  ├─ _deprecation_warning.py
│  │        │  ├─ _distutils
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _msvccompiler.py
│  │        │  │  ├─ archive_util.py
│  │        │  │  ├─ bcppcompiler.py
│  │        │  │  ├─ ccompiler.py
│  │        │  │  ├─ cmd.py
│  │        │  │  ├─ command
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ bdist.py
│  │        │  │  │  ├─ bdist_dumb.py
│  │        │  │  │  ├─ bdist_msi.py
│  │        │  │  │  ├─ bdist_rpm.py
│  │        │  │  │  ├─ bdist_wininst.py
│  │        │  │  │  ├─ build.py
│  │        │  │  │  ├─ build_clib.py
│  │        │  │  │  ├─ build_ext.py
│  │        │  │  │  ├─ build_py.py
│  │        │  │  │  ├─ build_scripts.py
│  │        │  │  │  ├─ check.py
│  │        │  │  │  ├─ clean.py
│  │        │  │  │  ├─ config.py
│  │        │  │  │  ├─ install.py
│  │        │  │  │  ├─ install_data.py
│  │        │  │  │  ├─ install_egg_info.py
│  │        │  │  │  ├─ install_headers.py
│  │        │  │  │  ├─ install_lib.py
│  │        │  │  │  ├─ install_scripts.py
│  │        │  │  │  ├─ py37compat.py
│  │        │  │  │  ├─ register.py
│  │        │  │  │  ├─ sdist.py
│  │        │  │  │  └─ upload.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ core.py
│  │        │  │  ├─ cygwinccompiler.py
│  │        │  │  ├─ debug.py
│  │        │  │  ├─ dep_util.py
│  │        │  │  ├─ dir_util.py
│  │        │  │  ├─ dist.py
│  │        │  │  ├─ errors.py
│  │        │  │  ├─ extension.py
│  │        │  │  ├─ fancy_getopt.py
│  │        │  │  ├─ file_util.py
│  │        │  │  ├─ filelist.py
│  │        │  │  ├─ log.py
│  │        │  │  ├─ msvc9compiler.py
│  │        │  │  ├─ msvccompiler.py
│  │        │  │  ├─ py35compat.py
│  │        │  │  ├─ py38compat.py
│  │        │  │  ├─ spawn.py
│  │        │  │  ├─ sysconfig.py
│  │        │  │  ├─ text_file.py
│  │        │  │  ├─ unixccompiler.py
│  │        │  │  ├─ util.py
│  │        │  │  ├─ version.py
│  │        │  │  └─ versionpredicate.py
│  │        │  ├─ _imp.py
│  │        │  ├─ _vendor
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ more_itertools
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ more.py
│  │        │  │  │  └─ recipes.py
│  │        │  │  ├─ ordered_set.py
│  │        │  │  ├─ packaging
│  │        │  │  │  ├─ __about__.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _compat.py
│  │        │  │  │  ├─ _structures.py
│  │        │  │  │  ├─ _typing.py
│  │        │  │  │  ├─ markers.py
│  │        │  │  │  ├─ requirements.py
│  │        │  │  │  ├─ specifiers.py
│  │        │  │  │  ├─ tags.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  └─ version.py
│  │        │  │  └─ pyparsing.py
│  │        │  ├─ archive_util.py
│  │        │  ├─ build_meta.py
│  │        │  ├─ cli-32.exe
│  │        │  ├─ cli-64.exe
│  │        │  ├─ cli.exe
│  │        │  ├─ command
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ alias.py
│  │        │  │  ├─ bdist_egg.py
│  │        │  │  ├─ bdist_rpm.py
│  │        │  │  ├─ build_clib.py
│  │        │  │  ├─ build_ext.py
│  │        │  │  ├─ build_py.py
│  │        │  │  ├─ develop.py
│  │        │  │  ├─ dist_info.py
│  │        │  │  ├─ easy_install.py
│  │        │  │  ├─ egg_info.py
│  │        │  │  ├─ install.py
│  │        │  │  ├─ install_egg_info.py
│  │        │  │  ├─ install_lib.py
│  │        │  │  ├─ install_scripts.py
│  │        │  │  ├─ launcher manifest.xml
│  │        │  │  ├─ py36compat.py
│  │        │  │  ├─ register.py
│  │        │  │  ├─ rotate.py
│  │        │  │  ├─ saveopts.py
│  │        │  │  ├─ sdist.py
│  │        │  │  ├─ setopt.py
│  │        │  │  ├─ test.py
│  │        │  │  ├─ upload.py
│  │        │  │  └─ upload_docs.py
│  │        │  ├─ config.py
│  │        │  ├─ dep_util.py
│  │        │  ├─ depends.py
│  │        │  ├─ dist.py
│  │        │  ├─ errors.py
│  │        │  ├─ extension.py
│  │        │  ├─ extern
│  │        │  │  └─ __init__.py
│  │        │  ├─ glob.py
│  │        │  ├─ gui-32.exe
│  │        │  ├─ gui-64.exe
│  │        │  ├─ gui.exe
│  │        │  ├─ installer.py
│  │        │  ├─ launch.py
│  │        │  ├─ monkey.py
│  │        │  ├─ msvc.py
│  │        │  ├─ namespaces.py
│  │        │  ├─ package_index.py
│  │        │  ├─ py34compat.py
│  │        │  ├─ sandbox.py
│  │        │  ├─ script (dev).tmpl
│  │        │  ├─ script.tmpl
│  │        │  ├─ unicode_utils.py
│  │        │  ├─ version.py
│  │        │  ├─ wheel.py
│  │        │  └─ windows_support.py
│  │        ├─ setuptools-58.1.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        ├─ sniffio
│  │        │  ├─ __init__.py
│  │        │  ├─ _impl.py
│  │        │  ├─ _tests
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ test_sniffio.py
│  │        │  ├─ _version.py
│  │        │  └─ py.typed
│  │        ├─ sniffio-1.3.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ LICENSE.APACHE2
│  │        │  ├─ LICENSE.MIT
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ top_level.txt
│  │        ├─ starlette
│  │        │  ├─ __init__.py
│  │        │  ├─ _exception_handler.py
│  │        │  ├─ _utils.py
│  │        │  ├─ applications.py
│  │        │  ├─ authentication.py
│  │        │  ├─ background.py
│  │        │  ├─ concurrency.py
│  │        │  ├─ config.py
│  │        │  ├─ convertors.py
│  │        │  ├─ datastructures.py
│  │        │  ├─ endpoints.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ formparsers.py
│  │        │  ├─ middleware
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ authentication.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ cors.py
│  │        │  │  ├─ errors.py
│  │        │  │  ├─ exceptions.py
│  │        │  │  ├─ gzip.py
│  │        │  │  ├─ httpsredirect.py
│  │        │  │  ├─ sessions.py
│  │        │  │  ├─ trustedhost.py
│  │        │  │  └─ wsgi.py
│  │        │  ├─ py.typed
│  │        │  ├─ requests.py
│  │        │  ├─ responses.py
│  │        │  ├─ routing.py
│  │        │  ├─ schemas.py
│  │        │  ├─ staticfiles.py
│  │        │  ├─ status.py
│  │        │  ├─ templating.py
│  │        │  ├─ testclient.py
│  │        │  ├─ types.py
│  │        │  └─ websockets.py
│  │        ├─ starlette-0.46.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE.md
│  │        ├─ tqdm
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ _dist_ver.py
│  │        │  ├─ _main.py
│  │        │  ├─ _monitor.py
│  │        │  ├─ _tqdm.py
│  │        │  ├─ _tqdm_gui.py
│  │        │  ├─ _tqdm_notebook.py
│  │        │  ├─ _tqdm_pandas.py
│  │        │  ├─ _utils.py
│  │        │  ├─ asyncio.py
│  │        │  ├─ auto.py
│  │        │  ├─ autonotebook.py
│  │        │  ├─ cli.py
│  │        │  ├─ completion.sh
│  │        │  ├─ contrib
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ bells.py
│  │        │  │  ├─ concurrent.py
│  │        │  │  ├─ discord.py
│  │        │  │  ├─ itertools.py
│  │        │  │  ├─ logging.py
│  │        │  │  ├─ slack.py
│  │        │  │  ├─ telegram.py
│  │        │  │  └─ utils_worker.py
│  │        │  ├─ dask.py
│  │        │  ├─ gui.py
│  │        │  ├─ keras.py
│  │        │  ├─ notebook.py
│  │        │  ├─ rich.py
│  │        │  ├─ std.py
│  │        │  ├─ tk.py
│  │        │  ├─ tqdm.1
│  │        │  ├─ utils.py
│  │        │  └─ version.py
│  │        ├─ tqdm-4.67.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENCE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        ├─ typing_extensions-4.13.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ typing_extensions.py
│  │        ├─ typing_inspection
│  │        │  ├─ __init__.py
│  │        │  ├─ introspection.py
│  │        │  ├─ py.typed
│  │        │  ├─ typing_objects.py
│  │        │  └─ typing_objects.pyi
│  │        ├─ typing_inspection-0.4.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ urllib3
│  │        │  ├─ __init__.py
│  │        │  ├─ _base_connection.py
│  │        │  ├─ _collections.py
│  │        │  ├─ _request_methods.py
│  │        │  ├─ _version.py
│  │        │  ├─ connection.py
│  │        │  ├─ connectionpool.py
│  │        │  ├─ contrib
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ emscripten
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ connection.py
│  │        │  │  │  ├─ emscripten_fetch_worker.js
│  │        │  │  │  ├─ fetch.py
│  │        │  │  │  ├─ request.py
│  │        │  │  │  └─ response.py
│  │        │  │  ├─ pyopenssl.py
│  │        │  │  └─ socks.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ fields.py
│  │        │  ├─ filepost.py
│  │        │  ├─ http2
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ connection.py
│  │        │  │  └─ probe.py
│  │        │  ├─ poolmanager.py
│  │        │  ├─ py.typed
│  │        │  ├─ response.py
│  │        │  └─ util
│  │        │     ├─ __init__.py
│  │        │     ├─ connection.py
│  │        │     ├─ proxy.py
│  │        │     ├─ request.py
│  │        │     ├─ response.py
│  │        │     ├─ retry.py
│  │        │     ├─ ssl_.py
│  │        │     ├─ ssl_match_hostname.py
│  │        │     ├─ ssltransport.py
│  │        │     ├─ timeout.py
│  │        │     ├─ url.py
│  │        │     ├─ util.py
│  │        │     └─ wait.py
│  │        ├─ urllib3-2.4.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE.txt
│  │        ├─ uvicorn
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ _subprocess.py
│  │        │  ├─ _types.py
│  │        │  ├─ config.py
│  │        │  ├─ importer.py
│  │        │  ├─ lifespan
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ off.py
│  │        │  │  └─ on.py
│  │        │  ├─ logging.py
│  │        │  ├─ loops
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ asyncio.py
│  │        │  │  ├─ auto.py
│  │        │  │  └─ uvloop.py
│  │        │  ├─ main.py
│  │        │  ├─ middleware
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ asgi2.py
│  │        │  │  ├─ message_logger.py
│  │        │  │  ├─ proxy_headers.py
│  │        │  │  └─ wsgi.py
│  │        │  ├─ protocols
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ http
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ auto.py
│  │        │  │  │  ├─ flow_control.py
│  │        │  │  │  ├─ h11_impl.py
│  │        │  │  │  └─ httptools_impl.py
│  │        │  │  ├─ utils.py
│  │        │  │  └─ websockets
│  │        │  │     ├─ __init__.py
│  │        │  │     ├─ auto.py
│  │        │  │     ├─ websockets_impl.py
│  │        │  │     └─ wsproto_impl.py
│  │        │  ├─ py.typed
│  │        │  ├─ server.py
│  │        │  ├─ supervisors
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ basereload.py
│  │        │  │  ├─ multiprocess.py
│  │        │  │  ├─ statreload.py
│  │        │  │  └─ watchfilesreload.py
│  │        │  └─ workers.py
│  │        ├─ uvicorn-0.34.3.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ licenses
│  │        │     └─ LICENSE.md
│  │        ├─ uvloop
│  │        │  ├─ __init__.py
│  │        │  ├─ _noop.py
│  │        │  ├─ _testbase.py
│  │        │  ├─ _version.py
│  │        │  ├─ cbhandles.pxd
│  │        │  ├─ cbhandles.pyx
│  │        │  ├─ dns.pyx
│  │        │  ├─ errors.pyx
│  │        │  ├─ handles
│  │        │  │  ├─ async_.pxd
│  │        │  │  ├─ async_.pyx
│  │        │  │  ├─ basetransport.pxd
│  │        │  │  ├─ basetransport.pyx
│  │        │  │  ├─ check.pxd
│  │        │  │  ├─ check.pyx
│  │        │  │  ├─ fsevent.pxd
│  │        │  │  ├─ fsevent.pyx
│  │        │  │  ├─ handle.pxd
│  │        │  │  ├─ handle.pyx
│  │        │  │  ├─ idle.pxd
│  │        │  │  ├─ idle.pyx
│  │        │  │  ├─ pipe.pxd
│  │        │  │  ├─ pipe.pyx
│  │        │  │  ├─ poll.pxd
│  │        │  │  ├─ poll.pyx
│  │        │  │  ├─ process.pxd
│  │        │  │  ├─ process.pyx
│  │        │  │  ├─ stream.pxd
│  │        │  │  ├─ stream.pyx
│  │        │  │  ├─ streamserver.pxd
│  │        │  │  ├─ streamserver.pyx
│  │        │  │  ├─ tcp.pxd
│  │        │  │  ├─ tcp.pyx
│  │        │  │  ├─ timer.pxd
│  │        │  │  ├─ timer.pyx
│  │        │  │  ├─ udp.pxd
│  │        │  │  └─ udp.pyx
│  │        │  ├─ includes
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ consts.pxi
│  │        │  │  ├─ debug.pxd
│  │        │  │  ├─ flowcontrol.pxd
│  │        │  │  ├─ python.pxd
│  │        │  │  ├─ stdlib.pxi
│  │        │  │  ├─ system.pxd
│  │        │  │  └─ uv.pxd
│  │        │  ├─ loop.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ loop.pxd
│  │        │  ├─ loop.pyi
│  │        │  ├─ loop.pyx
│  │        │  ├─ lru.pyx
│  │        │  ├─ pseudosock.pyx
│  │        │  ├─ py.typed
│  │        │  ├─ request.pxd
│  │        │  ├─ request.pyx
│  │        │  ├─ server.pxd
│  │        │  ├─ server.pyx
│  │        │  ├─ sslproto.pxd
│  │        │  └─ sslproto.pyx
│  │        ├─ uvloop-0.21.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE-APACHE
│  │        │  ├─ LICENSE-MIT
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ top_level.txt
│  │        ├─ watchfiles
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ _rust_notify.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ _rust_notify.pyi
│  │        │  ├─ cli.py
│  │        │  ├─ filters.py
│  │        │  ├─ main.py
│  │        │  ├─ py.typed
│  │        │  ├─ run.py
│  │        │  └─ version.py
│  │        ├─ watchfiles-1.0.5.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ websockets
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ asyncio
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ async_timeout.py
│  │        │  │  ├─ client.py
│  │        │  │  ├─ compatibility.py
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ messages.py
│  │        │  │  ├─ router.py
│  │        │  │  └─ server.py
│  │        │  ├─ auth.py
│  │        │  ├─ cli.py
│  │        │  ├─ client.py
│  │        │  ├─ connection.py
│  │        │  ├─ datastructures.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ extensions
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ base.py
│  │        │  │  └─ permessage_deflate.py
│  │        │  ├─ frames.py
│  │        │  ├─ headers.py
│  │        │  ├─ http.py
│  │        │  ├─ http11.py
│  │        │  ├─ imports.py
│  │        │  ├─ legacy
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ auth.py
│  │        │  │  ├─ client.py
│  │        │  │  ├─ exceptions.py
│  │        │  │  ├─ framing.py
│  │        │  │  ├─ handshake.py
│  │        │  │  ├─ http.py
│  │        │  │  ├─ protocol.py
│  │        │  │  └─ server.py
│  │        │  ├─ protocol.py
│  │        │  ├─ py.typed
│  │        │  ├─ server.py
│  │        │  ├─ speedups.c
│  │        │  ├─ speedups.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ speedups.pyi
│  │        │  ├─ streams.py
│  │        │  ├─ sync
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ client.py
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ messages.py
│  │        │  │  ├─ router.py
│  │        │  │  ├─ server.py
│  │        │  │  └─ utils.py
│  │        │  ├─ typing.py
│  │        │  ├─ uri.py
│  │        │  ├─ utils.py
│  │        │  └─ version.py
│  │        ├─ websockets-15.0.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        └─ yaml
│  │           ├─ __init__.py
│  │           ├─ _yaml.cpython-39-x86_64-linux-gnu.so
│  │           ├─ composer.py
│  │           ├─ constructor.py
│  │           ├─ cyaml.py
│  │           ├─ dumper.py
│  │           ├─ emitter.py
│  │           ├─ error.py
│  │           ├─ events.py
│  │           ├─ loader.py
│  │           ├─ nodes.py
│  │           ├─ parser.py
│  │           ├─ reader.py
│  │           ├─ representer.py
│  │           ├─ resolver.py
│  │           ├─ scanner.py
│  │           ├─ serializer.py
│  │           └─ tokens.py
│  ├─ lib64
│  │  └─ python3.9
│  │     └─ site-packages
│  │        ├─ PyYAML-6.0.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ top_level.txt
│  │        ├─ _distutils_hack
│  │        │  ├─ __init__.py
│  │        │  └─ override.py
│  │        ├─ _yaml
│  │        │  └─ __init__.py
│  │        ├─ aiofiles
│  │        │  ├─ __init__.py
│  │        │  ├─ base.py
│  │        │  ├─ os.py
│  │        │  ├─ ospath.py
│  │        │  ├─ tempfile
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ temptypes.py
│  │        │  └─ threadpool
│  │        │     ├─ __init__.py
│  │        │     ├─ binary.py
│  │        │     ├─ text.py
│  │        │     └─ utils.py
│  │        ├─ aiofiles-24.1.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     ├─ LICENSE
│  │        │     └─ NOTICE
│  │        ├─ annotated_types
│  │        │  ├─ __init__.py
│  │        │  ├─ py.typed
│  │        │  └─ test_cases.py
│  │        ├─ annotated_types-0.7.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ anyio
│  │        │  ├─ __init__.py
│  │        │  ├─ _backends
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _asyncio.py
│  │        │  │  └─ _trio.py
│  │        │  ├─ _core
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _asyncio_selector_thread.py
│  │        │  │  ├─ _eventloop.py
│  │        │  │  ├─ _exceptions.py
│  │        │  │  ├─ _fileio.py
│  │        │  │  ├─ _resources.py
│  │        │  │  ├─ _signals.py
│  │        │  │  ├─ _sockets.py
│  │        │  │  ├─ _streams.py
│  │        │  │  ├─ _subprocesses.py
│  │        │  │  ├─ _synchronization.py
│  │        │  │  ├─ _tasks.py
│  │        │  │  ├─ _tempfile.py
│  │        │  │  ├─ _testing.py
│  │        │  │  └─ _typedattr.py
│  │        │  ├─ abc
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _eventloop.py
│  │        │  │  ├─ _resources.py
│  │        │  │  ├─ _sockets.py
│  │        │  │  ├─ _streams.py
│  │        │  │  ├─ _subprocesses.py
│  │        │  │  ├─ _tasks.py
│  │        │  │  └─ _testing.py
│  │        │  ├─ from_thread.py
│  │        │  ├─ lowlevel.py
│  │        │  ├─ py.typed
│  │        │  ├─ pytest_plugin.py
│  │        │  ├─ streams
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ buffered.py
│  │        │  │  ├─ file.py
│  │        │  │  ├─ memory.py
│  │        │  │  ├─ stapled.py
│  │        │  │  ├─ text.py
│  │        │  │  └─ tls.py
│  │        │  ├─ to_interpreter.py
│  │        │  ├─ to_process.py
│  │        │  └─ to_thread.py
│  │        ├─ anyio-4.9.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        ├─ bson
│  │        │  ├─ __init__.py
│  │        │  ├─ _cbson.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ _cbsonmodule.c
│  │        │  ├─ _cbsonmodule.h
│  │        │  ├─ _helpers.py
│  │        │  ├─ binary.py
│  │        │  ├─ bson-endian.h
│  │        │  ├─ buffer.c
│  │        │  ├─ buffer.h
│  │        │  ├─ code.py
│  │        │  ├─ codec_options.py
│  │        │  ├─ datetime_ms.py
│  │        │  ├─ dbref.py
│  │        │  ├─ decimal128.py
│  │        │  ├─ errors.py
│  │        │  ├─ int64.py
│  │        │  ├─ json_util.py
│  │        │  ├─ max_key.py
│  │        │  ├─ min_key.py
│  │        │  ├─ objectid.py
│  │        │  ├─ py.typed
│  │        │  ├─ raw_bson.py
│  │        │  ├─ regex.py
│  │        │  ├─ son.py
│  │        │  ├─ time64.c
│  │        │  ├─ time64.h
│  │        │  ├─ time64_config.h
│  │        │  ├─ time64_limits.h
│  │        │  ├─ timestamp.py
│  │        │  ├─ typings.py
│  │        │  └─ tz_util.py
│  │        ├─ certifi
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ cacert.pem
│  │        │  ├─ core.py
│  │        │  └─ py.typed
│  │        ├─ certifi-2025.4.26.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  └─ top_level.txt
│  │        ├─ charset_normalizer
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ api.py
│  │        │  ├─ cd.py
│  │        │  ├─ cli
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ __main__.py
│  │        │  ├─ constant.py
│  │        │  ├─ legacy.py
│  │        │  ├─ md.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ md.py
│  │        │  ├─ md__mypyc.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ models.py
│  │        │  ├─ py.typed
│  │        │  ├─ utils.py
│  │        │  └─ version.py
│  │        ├─ charset_normalizer-3.4.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  └─ top_level.txt
│  │        ├─ click
│  │        │  ├─ __init__.py
│  │        │  ├─ _compat.py
│  │        │  ├─ _termui_impl.py
│  │        │  ├─ _textwrap.py
│  │        │  ├─ _winconsole.py
│  │        │  ├─ core.py
│  │        │  ├─ decorators.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ formatting.py
│  │        │  ├─ globals.py
│  │        │  ├─ parser.py
│  │        │  ├─ py.typed
│  │        │  ├─ shell_completion.py
│  │        │  ├─ termui.py
│  │        │  ├─ testing.py
│  │        │  ├─ types.py
│  │        │  └─ utils.py
│  │        ├─ click-8.1.8.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ distro
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ distro.py
│  │        │  └─ py.typed
│  │        ├─ distro-1.9.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        ├─ distutils-precedence.pth
│  │        ├─ dns
│  │        │  ├─ __init__.py
│  │        │  ├─ _asyncbackend.py
│  │        │  ├─ _asyncio_backend.py
│  │        │  ├─ _ddr.py
│  │        │  ├─ _features.py
│  │        │  ├─ _immutable_ctx.py
│  │        │  ├─ _trio_backend.py
│  │        │  ├─ asyncbackend.py
│  │        │  ├─ asyncquery.py
│  │        │  ├─ asyncresolver.py
│  │        │  ├─ dnssec.py
│  │        │  ├─ dnssecalgs
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ cryptography.py
│  │        │  │  ├─ dsa.py
│  │        │  │  ├─ ecdsa.py
│  │        │  │  ├─ eddsa.py
│  │        │  │  └─ rsa.py
│  │        │  ├─ dnssectypes.py
│  │        │  ├─ e164.py
│  │        │  ├─ edns.py
│  │        │  ├─ entropy.py
│  │        │  ├─ enum.py
│  │        │  ├─ exception.py
│  │        │  ├─ flags.py
│  │        │  ├─ grange.py
│  │        │  ├─ immutable.py
│  │        │  ├─ inet.py
│  │        │  ├─ ipv4.py
│  │        │  ├─ ipv6.py
│  │        │  ├─ message.py
│  │        │  ├─ name.py
│  │        │  ├─ namedict.py
│  │        │  ├─ nameserver.py
│  │        │  ├─ node.py
│  │        │  ├─ opcode.py
│  │        │  ├─ py.typed
│  │        │  ├─ query.py
│  │        │  ├─ quic
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _asyncio.py
│  │        │  │  ├─ _common.py
│  │        │  │  ├─ _sync.py
│  │        │  │  └─ _trio.py
│  │        │  ├─ rcode.py
│  │        │  ├─ rdata.py
│  │        │  ├─ rdataclass.py
│  │        │  ├─ rdataset.py
│  │        │  ├─ rdatatype.py
│  │        │  ├─ rdtypes
│  │        │  │  ├─ ANY
│  │        │  │  │  ├─ AFSDB.py
│  │        │  │  │  ├─ AMTRELAY.py
│  │        │  │  │  ├─ AVC.py
│  │        │  │  │  ├─ CAA.py
│  │        │  │  │  ├─ CDNSKEY.py
│  │        │  │  │  ├─ CDS.py
│  │        │  │  │  ├─ CERT.py
│  │        │  │  │  ├─ CNAME.py
│  │        │  │  │  ├─ CSYNC.py
│  │        │  │  │  ├─ DLV.py
│  │        │  │  │  ├─ DNAME.py
│  │        │  │  │  ├─ DNSKEY.py
│  │        │  │  │  ├─ DS.py
│  │        │  │  │  ├─ EUI48.py
│  │        │  │  │  ├─ EUI64.py
│  │        │  │  │  ├─ GPOS.py
│  │        │  │  │  ├─ HINFO.py
│  │        │  │  │  ├─ HIP.py
│  │        │  │  │  ├─ ISDN.py
│  │        │  │  │  ├─ L32.py
│  │        │  │  │  ├─ L64.py
│  │        │  │  │  ├─ LOC.py
│  │        │  │  │  ├─ LP.py
│  │        │  │  │  ├─ MX.py
│  │        │  │  │  ├─ NID.py
│  │        │  │  │  ├─ NINFO.py
│  │        │  │  │  ├─ NS.py
│  │        │  │  │  ├─ NSEC.py
│  │        │  │  │  ├─ NSEC3.py
│  │        │  │  │  ├─ NSEC3PARAM.py
│  │        │  │  │  ├─ OPENPGPKEY.py
│  │        │  │  │  ├─ OPT.py
│  │        │  │  │  ├─ PTR.py
│  │        │  │  │  ├─ RESINFO.py
│  │        │  │  │  ├─ RP.py
│  │        │  │  │  ├─ RRSIG.py
│  │        │  │  │  ├─ RT.py
│  │        │  │  │  ├─ SMIMEA.py
│  │        │  │  │  ├─ SOA.py
│  │        │  │  │  ├─ SPF.py
│  │        │  │  │  ├─ SSHFP.py
│  │        │  │  │  ├─ TKEY.py
│  │        │  │  │  ├─ TLSA.py
│  │        │  │  │  ├─ TSIG.py
│  │        │  │  │  ├─ TXT.py
│  │        │  │  │  ├─ URI.py
│  │        │  │  │  ├─ WALLET.py
│  │        │  │  │  ├─ X25.py
│  │        │  │  │  ├─ ZONEMD.py
│  │        │  │  │  └─ __init__.py
│  │        │  │  ├─ CH
│  │        │  │  │  ├─ A.py
│  │        │  │  │  └─ __init__.py
│  │        │  │  ├─ IN
│  │        │  │  │  ├─ A.py
│  │        │  │  │  ├─ AAAA.py
│  │        │  │  │  ├─ APL.py
│  │        │  │  │  ├─ DHCID.py
│  │        │  │  │  ├─ HTTPS.py
│  │        │  │  │  ├─ IPSECKEY.py
│  │        │  │  │  ├─ KX.py
│  │        │  │  │  ├─ NAPTR.py
│  │        │  │  │  ├─ NSAP.py
│  │        │  │  │  ├─ NSAP_PTR.py
│  │        │  │  │  ├─ PX.py
│  │        │  │  │  ├─ SRV.py
│  │        │  │  │  ├─ SVCB.py
│  │        │  │  │  ├─ WKS.py
│  │        │  │  │  └─ __init__.py
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ dnskeybase.py
│  │        │  │  ├─ dsbase.py
│  │        │  │  ├─ euibase.py
│  │        │  │  ├─ mxbase.py
│  │        │  │  ├─ nsbase.py
│  │        │  │  ├─ svcbbase.py
│  │        │  │  ├─ tlsabase.py
│  │        │  │  ├─ txtbase.py
│  │        │  │  └─ util.py
│  │        │  ├─ renderer.py
│  │        │  ├─ resolver.py
│  │        │  ├─ reversename.py
│  │        │  ├─ rrset.py
│  │        │  ├─ serial.py
│  │        │  ├─ set.py
│  │        │  ├─ tokenizer.py
│  │        │  ├─ transaction.py
│  │        │  ├─ tsig.py
│  │        │  ├─ tsigkeyring.py
│  │        │  ├─ ttl.py
│  │        │  ├─ update.py
│  │        │  ├─ version.py
│  │        │  ├─ versioned.py
│  │        │  ├─ win32util.py
│  │        │  ├─ wire.py
│  │        │  ├─ xfr.py
│  │        │  ├─ zone.py
│  │        │  ├─ zonefile.py
│  │        │  └─ zonetypes.py
│  │        ├─ dnspython-2.7.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ docker
│  │        │  ├─ __init__.py
│  │        │  ├─ _version.py
│  │        │  ├─ api
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ build.py
│  │        │  │  ├─ client.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ container.py
│  │        │  │  ├─ daemon.py
│  │        │  │  ├─ exec_api.py
│  │        │  │  ├─ image.py
│  │        │  │  ├─ network.py
│  │        │  │  ├─ plugin.py
│  │        │  │  ├─ secret.py
│  │        │  │  ├─ service.py
│  │        │  │  ├─ swarm.py
│  │        │  │  └─ volume.py
│  │        │  ├─ auth.py
│  │        │  ├─ client.py
│  │        │  ├─ constants.py
│  │        │  ├─ context
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ api.py
│  │        │  │  ├─ config.py
│  │        │  │  └─ context.py
│  │        │  ├─ credentials
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ constants.py
│  │        │  │  ├─ errors.py
│  │        │  │  ├─ store.py
│  │        │  │  └─ utils.py
│  │        │  ├─ errors.py
│  │        │  ├─ models
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ configs.py
│  │        │  │  ├─ containers.py
│  │        │  │  ├─ images.py
│  │        │  │  ├─ networks.py
│  │        │  │  ├─ nodes.py
│  │        │  │  ├─ plugins.py
│  │        │  │  ├─ resource.py
│  │        │  │  ├─ secrets.py
│  │        │  │  ├─ services.py
│  │        │  │  ├─ swarm.py
│  │        │  │  └─ volumes.py
│  │        │  ├─ tls.py
│  │        │  ├─ transport
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ basehttpadapter.py
│  │        │  │  ├─ npipeconn.py
│  │        │  │  ├─ npipesocket.py
│  │        │  │  ├─ sshconn.py
│  │        │  │  └─ unixconn.py
│  │        │  ├─ types
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ containers.py
│  │        │  │  ├─ daemon.py
│  │        │  │  ├─ healthcheck.py
│  │        │  │  ├─ networks.py
│  │        │  │  ├─ services.py
│  │        │  │  └─ swarm.py
│  │        │  ├─ utils
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ build.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ decorators.py
│  │        │  │  ├─ fnmatch.py
│  │        │  │  ├─ json_stream.py
│  │        │  │  ├─ ports.py
│  │        │  │  ├─ proxy.py
│  │        │  │  ├─ socket.py
│  │        │  │  └─ utils.py
│  │        │  └─ version.py
│  │        ├─ docker-7.1.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ dotenv
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ cli.py
│  │        │  ├─ ipython.py
│  │        │  ├─ main.py
│  │        │  ├─ parser.py
│  │        │  ├─ py.typed
│  │        │  ├─ variables.py
│  │        │  └─ version.py
│  │        ├─ exceptiongroup
│  │        │  ├─ __init__.py
│  │        │  ├─ _catch.py
│  │        │  ├─ _exceptions.py
│  │        │  ├─ _formatting.py
│  │        │  ├─ _suppress.py
│  │        │  ├─ _version.py
│  │        │  └─ py.typed
│  │        ├─ exceptiongroup-1.3.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ fastapi
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ _compat.py
│  │        │  ├─ applications.py
│  │        │  ├─ background.py
│  │        │  ├─ cli.py
│  │        │  ├─ concurrency.py
│  │        │  ├─ datastructures.py
│  │        │  ├─ dependencies
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ models.py
│  │        │  │  └─ utils.py
│  │        │  ├─ encoders.py
│  │        │  ├─ exception_handlers.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ logger.py
│  │        │  ├─ middleware
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ cors.py
│  │        │  │  ├─ gzip.py
│  │        │  │  ├─ httpsredirect.py
│  │        │  │  ├─ trustedhost.py
│  │        │  │  └─ wsgi.py
│  │        │  ├─ openapi
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ constants.py
│  │        │  │  ├─ docs.py
│  │        │  │  ├─ models.py
│  │        │  │  └─ utils.py
│  │        │  ├─ param_functions.py
│  │        │  ├─ params.py
│  │        │  ├─ py.typed
│  │        │  ├─ requests.py
│  │        │  ├─ responses.py
│  │        │  ├─ routing.py
│  │        │  ├─ security
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ api_key.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ http.py
│  │        │  │  ├─ oauth2.py
│  │        │  │  ├─ open_id_connect_url.py
│  │        │  │  └─ utils.py
│  │        │  ├─ staticfiles.py
│  │        │  ├─ templating.py
│  │        │  ├─ testclient.py
│  │        │  ├─ types.py
│  │        │  ├─ utils.py
│  │        │  └─ websockets.py
│  │        ├─ fastapi-0.115.12.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ gridfs
│  │        │  ├─ __init__.py
│  │        │  ├─ asynchronous
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ grid_file.py
│  │        │  ├─ errors.py
│  │        │  ├─ grid_file.py
│  │        │  ├─ grid_file_shared.py
│  │        │  ├─ py.typed
│  │        │  └─ synchronous
│  │        │     ├─ __init__.py
│  │        │     └─ grid_file.py
│  │        ├─ h11
│  │        │  ├─ __init__.py
│  │        │  ├─ _abnf.py
│  │        │  ├─ _connection.py
│  │        │  ├─ _events.py
│  │        │  ├─ _headers.py
│  │        │  ├─ _readers.py
│  │        │  ├─ _receivebuffer.py
│  │        │  ├─ _state.py
│  │        │  ├─ _util.py
│  │        │  ├─ _version.py
│  │        │  ├─ _writers.py
│  │        │  └─ py.typed
│  │        ├─ h11-0.16.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE.txt
│  │        │  └─ top_level.txt
│  │        ├─ httpcore
│  │        │  ├─ __init__.py
│  │        │  ├─ _api.py
│  │        │  ├─ _async
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ connection_pool.py
│  │        │  │  ├─ http11.py
│  │        │  │  ├─ http2.py
│  │        │  │  ├─ http_proxy.py
│  │        │  │  ├─ interfaces.py
│  │        │  │  └─ socks_proxy.py
│  │        │  ├─ _backends
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ anyio.py
│  │        │  │  ├─ auto.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ mock.py
│  │        │  │  ├─ sync.py
│  │        │  │  └─ trio.py
│  │        │  ├─ _exceptions.py
│  │        │  ├─ _models.py
│  │        │  ├─ _ssl.py
│  │        │  ├─ _sync
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ connection_pool.py
│  │        │  │  ├─ http11.py
│  │        │  │  ├─ http2.py
│  │        │  │  ├─ http_proxy.py
│  │        │  │  ├─ interfaces.py
│  │        │  │  └─ socks_proxy.py
│  │        │  ├─ _synchronization.py
│  │        │  ├─ _trace.py
│  │        │  ├─ _utils.py
│  │        │  └─ py.typed
│  │        ├─ httpcore-1.0.9.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE.md
│  │        ├─ httptools
│  │        │  ├─ __init__.py
│  │        │  ├─ _version.py
│  │        │  └─ parser
│  │        │     ├─ __init__.py
│  │        │     ├─ cparser.pxd
│  │        │     ├─ errors.py
│  │        │     ├─ parser.cpython-39-x86_64-linux-gnu.so
│  │        │     ├─ parser.pyx
│  │        │     ├─ python.pxd
│  │        │     ├─ url_cparser.pxd
│  │        │     ├─ url_parser.cpython-39-x86_64-linux-gnu.so
│  │        │     └─ url_parser.pyx
│  │        ├─ httptools-0.6.4.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ top_level.txt
│  │        ├─ httpx
│  │        │  ├─ __init__.py
│  │        │  ├─ __version__.py
│  │        │  ├─ _api.py
│  │        │  ├─ _auth.py
│  │        │  ├─ _client.py
│  │        │  ├─ _config.py
│  │        │  ├─ _content.py
│  │        │  ├─ _decoders.py
│  │        │  ├─ _exceptions.py
│  │        │  ├─ _main.py
│  │        │  ├─ _models.py
│  │        │  ├─ _multipart.py
│  │        │  ├─ _status_codes.py
│  │        │  ├─ _transports
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ asgi.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ default.py
│  │        │  │  ├─ mock.py
│  │        │  │  └─ wsgi.py
│  │        │  ├─ _types.py
│  │        │  ├─ _urlparse.py
│  │        │  ├─ _urls.py
│  │        │  ├─ _utils.py
│  │        │  └─ py.typed
│  │        ├─ httpx-0.28.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ licenses
│  │        │     └─ LICENSE.md
│  │        ├─ idna
│  │        │  ├─ __init__.py
│  │        │  ├─ codec.py
│  │        │  ├─ compat.py
│  │        │  ├─ core.py
│  │        │  ├─ idnadata.py
│  │        │  ├─ intranges.py
│  │        │  ├─ package_data.py
│  │        │  ├─ py.typed
│  │        │  └─ uts46data.py
│  │        ├─ idna-3.10.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.md
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ jiter
│  │        │  ├─ __init__.py
│  │        │  ├─ __init__.pyi
│  │        │  ├─ jiter.cpython-39-x86_64-linux-gnu.so
│  │        │  └─ py.typed
│  │        ├─ jiter-0.10.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  └─ WHEEL
│  │        ├─ motor
│  │        │  ├─ __init__.py
│  │        │  ├─ _version.py
│  │        │  ├─ aiohttp
│  │        │  │  └─ __init__.py
│  │        │  ├─ core.py
│  │        │  ├─ core.pyi
│  │        │  ├─ docstrings.py
│  │        │  ├─ frameworks
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ asyncio
│  │        │  │  │  └─ __init__.py
│  │        │  │  └─ tornado
│  │        │  │     └─ __init__.py
│  │        │  ├─ metaprogramming.py
│  │        │  ├─ motor_asyncio.py
│  │        │  ├─ motor_asyncio.pyi
│  │        │  ├─ motor_common.py
│  │        │  ├─ motor_gridfs.py
│  │        │  ├─ motor_gridfs.pyi
│  │        │  ├─ motor_tornado.py
│  │        │  ├─ motor_tornado.pyi
│  │        │  ├─ py.typed
│  │        │  └─ web.py
│  │        ├─ motor-3.7.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ multipart
│  │        │  ├─ __init__.py
│  │        │  ├─ decoders.py
│  │        │  ├─ exceptions.py
│  │        │  └─ multipart.py
│  │        ├─ openai
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ _base_client.py
│  │        │  ├─ _client.py
│  │        │  ├─ _compat.py
│  │        │  ├─ _constants.py
│  │        │  ├─ _exceptions.py
│  │        │  ├─ _extras
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _common.py
│  │        │  │  ├─ numpy_proxy.py
│  │        │  │  ├─ pandas_proxy.py
│  │        │  │  └─ sounddevice_proxy.py
│  │        │  ├─ _files.py
│  │        │  ├─ _legacy_response.py
│  │        │  ├─ _models.py
│  │        │  ├─ _module_client.py
│  │        │  ├─ _qs.py
│  │        │  ├─ _resource.py
│  │        │  ├─ _response.py
│  │        │  ├─ _streaming.py
│  │        │  ├─ _types.py
│  │        │  ├─ _utils
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _logs.py
│  │        │  │  ├─ _proxy.py
│  │        │  │  ├─ _reflection.py
│  │        │  │  ├─ _resources_proxy.py
│  │        │  │  ├─ _streams.py
│  │        │  │  ├─ _sync.py
│  │        │  │  ├─ _transform.py
│  │        │  │  ├─ _typing.py
│  │        │  │  └─ _utils.py
│  │        │  ├─ _version.py
│  │        │  ├─ cli
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _api
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _main.py
│  │        │  │  │  ├─ audio.py
│  │        │  │  │  ├─ chat
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ completions.py
│  │        │  │  │  ├─ completions.py
│  │        │  │  │  ├─ files.py
│  │        │  │  │  ├─ image.py
│  │        │  │  │  └─ models.py
│  │        │  │  ├─ _cli.py
│  │        │  │  ├─ _errors.py
│  │        │  │  ├─ _models.py
│  │        │  │  ├─ _progress.py
│  │        │  │  ├─ _tools
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _main.py
│  │        │  │  │  ├─ fine_tunes.py
│  │        │  │  │  └─ migrate.py
│  │        │  │  └─ _utils.py
│  │        │  ├─ helpers
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ local_audio_player.py
│  │        │  │  └─ microphone.py
│  │        │  ├─ lib
│  │        │  │  ├─ .keep
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _old_api.py
│  │        │  │  ├─ _parsing
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _completions.py
│  │        │  │  │  └─ _responses.py
│  │        │  │  ├─ _pydantic.py
│  │        │  │  ├─ _tools.py
│  │        │  │  ├─ _validators.py
│  │        │  │  ├─ azure.py
│  │        │  │  └─ streaming
│  │        │  │     ├─ __init__.py
│  │        │  │     ├─ _assistants.py
│  │        │  │     ├─ _deltas.py
│  │        │  │     ├─ chat
│  │        │  │     │  ├─ __init__.py
│  │        │  │     │  ├─ _completions.py
│  │        │  │     │  ├─ _events.py
│  │        │  │     │  └─ _types.py
│  │        │  │     └─ responses
│  │        │  │        ├─ __init__.py
│  │        │  │        ├─ _events.py
│  │        │  │        ├─ _responses.py
│  │        │  │        └─ _types.py
│  │        │  ├─ pagination.py
│  │        │  ├─ py.typed
│  │        │  ├─ resources
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ audio
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ audio.py
│  │        │  │  │  ├─ speech.py
│  │        │  │  │  ├─ transcriptions.py
│  │        │  │  │  └─ translations.py
│  │        │  │  ├─ batches.py
│  │        │  │  ├─ beta
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ assistants.py
│  │        │  │  │  ├─ beta.py
│  │        │  │  │  ├─ chat
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ chat.py
│  │        │  │  │  │  └─ completions.py
│  │        │  │  │  ├─ realtime
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ realtime.py
│  │        │  │  │  │  ├─ sessions.py
│  │        │  │  │  │  └─ transcription_sessions.py
│  │        │  │  │  └─ threads
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ messages.py
│  │        │  │  │     ├─ runs
│  │        │  │  │     │  ├─ __init__.py
│  │        │  │  │     │  ├─ runs.py
│  │        │  │  │     │  └─ steps.py
│  │        │  │  │     └─ threads.py
│  │        │  │  ├─ chat
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ chat.py
│  │        │  │  │  └─ completions
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ completions.py
│  │        │  │  │     └─ messages.py
│  │        │  │  ├─ completions.py
│  │        │  │  ├─ containers
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ containers.py
│  │        │  │  │  └─ files
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ content.py
│  │        │  │  │     └─ files.py
│  │        │  │  ├─ embeddings.py
│  │        │  │  ├─ evals
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ evals.py
│  │        │  │  │  └─ runs
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ output_items.py
│  │        │  │  │     └─ runs.py
│  │        │  │  ├─ files.py
│  │        │  │  ├─ fine_tuning
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ alpha
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ alpha.py
│  │        │  │  │  │  └─ graders.py
│  │        │  │  │  ├─ checkpoints
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ checkpoints.py
│  │        │  │  │  │  └─ permissions.py
│  │        │  │  │  ├─ fine_tuning.py
│  │        │  │  │  └─ jobs
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ checkpoints.py
│  │        │  │  │     └─ jobs.py
│  │        │  │  ├─ images.py
│  │        │  │  ├─ models.py
│  │        │  │  ├─ moderations.py
│  │        │  │  ├─ responses
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ input_items.py
│  │        │  │  │  └─ responses.py
│  │        │  │  ├─ uploads
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ parts.py
│  │        │  │  │  └─ uploads.py
│  │        │  │  └─ vector_stores
│  │        │  │     ├─ __init__.py
│  │        │  │     ├─ file_batches.py
│  │        │  │     ├─ files.py
│  │        │  │     └─ vector_stores.py
│  │        │  ├─ types
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ audio
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ speech_create_params.py
│  │        │  │  │  ├─ speech_model.py
│  │        │  │  │  ├─ transcription.py
│  │        │  │  │  ├─ transcription_create_params.py
│  │        │  │  │  ├─ transcription_create_response.py
│  │        │  │  │  ├─ transcription_include.py
│  │        │  │  │  ├─ transcription_segment.py
│  │        │  │  │  ├─ transcription_stream_event.py
│  │        │  │  │  ├─ transcription_text_delta_event.py
│  │        │  │  │  ├─ transcription_text_done_event.py
│  │        │  │  │  ├─ transcription_verbose.py
│  │        │  │  │  ├─ transcription_word.py
│  │        │  │  │  ├─ translation.py
│  │        │  │  │  ├─ translation_create_params.py
│  │        │  │  │  ├─ translation_create_response.py
│  │        │  │  │  └─ translation_verbose.py
│  │        │  │  ├─ audio_model.py
│  │        │  │  ├─ audio_response_format.py
│  │        │  │  ├─ auto_file_chunking_strategy_param.py
│  │        │  │  ├─ batch.py
│  │        │  │  ├─ batch_create_params.py
│  │        │  │  ├─ batch_error.py
│  │        │  │  ├─ batch_list_params.py
│  │        │  │  ├─ batch_request_counts.py
│  │        │  │  ├─ beta
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ assistant.py
│  │        │  │  │  ├─ assistant_create_params.py
│  │        │  │  │  ├─ assistant_deleted.py
│  │        │  │  │  ├─ assistant_list_params.py
│  │        │  │  │  ├─ assistant_response_format_option.py
│  │        │  │  │  ├─ assistant_response_format_option_param.py
│  │        │  │  │  ├─ assistant_stream_event.py
│  │        │  │  │  ├─ assistant_tool.py
│  │        │  │  │  ├─ assistant_tool_choice.py
│  │        │  │  │  ├─ assistant_tool_choice_function.py
│  │        │  │  │  ├─ assistant_tool_choice_function_param.py
│  │        │  │  │  ├─ assistant_tool_choice_option.py
│  │        │  │  │  ├─ assistant_tool_choice_option_param.py
│  │        │  │  │  ├─ assistant_tool_choice_param.py
│  │        │  │  │  ├─ assistant_tool_param.py
│  │        │  │  │  ├─ assistant_update_params.py
│  │        │  │  │  ├─ chat
│  │        │  │  │  │  └─ __init__.py
│  │        │  │  │  ├─ code_interpreter_tool.py
│  │        │  │  │  ├─ code_interpreter_tool_param.py
│  │        │  │  │  ├─ file_search_tool.py
│  │        │  │  │  ├─ file_search_tool_param.py
│  │        │  │  │  ├─ function_tool.py
│  │        │  │  │  ├─ function_tool_param.py
│  │        │  │  │  ├─ realtime
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ conversation_created_event.py
│  │        │  │  │  │  ├─ conversation_item.py
│  │        │  │  │  │  ├─ conversation_item_content.py
│  │        │  │  │  │  ├─ conversation_item_content_param.py
│  │        │  │  │  │  ├─ conversation_item_create_event.py
│  │        │  │  │  │  ├─ conversation_item_create_event_param.py
│  │        │  │  │  │  ├─ conversation_item_created_event.py
│  │        │  │  │  │  ├─ conversation_item_delete_event.py
│  │        │  │  │  │  ├─ conversation_item_delete_event_param.py
│  │        │  │  │  │  ├─ conversation_item_deleted_event.py
│  │        │  │  │  │  ├─ conversation_item_input_audio_transcription_completed_event.py
│  │        │  │  │  │  ├─ conversation_item_input_audio_transcription_delta_event.py
│  │        │  │  │  │  ├─ conversation_item_input_audio_transcription_failed_event.py
│  │        │  │  │  │  ├─ conversation_item_param.py
│  │        │  │  │  │  ├─ conversation_item_retrieve_event.py
│  │        │  │  │  │  ├─ conversation_item_retrieve_event_param.py
│  │        │  │  │  │  ├─ conversation_item_truncate_event.py
│  │        │  │  │  │  ├─ conversation_item_truncate_event_param.py
│  │        │  │  │  │  ├─ conversation_item_truncated_event.py
│  │        │  │  │  │  ├─ conversation_item_with_reference.py
│  │        │  │  │  │  ├─ conversation_item_with_reference_param.py
│  │        │  │  │  │  ├─ error_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_append_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_append_event_param.py
│  │        │  │  │  │  ├─ input_audio_buffer_clear_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_clear_event_param.py
│  │        │  │  │  │  ├─ input_audio_buffer_cleared_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_commit_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_commit_event_param.py
│  │        │  │  │  │  ├─ input_audio_buffer_committed_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_speech_started_event.py
│  │        │  │  │  │  ├─ input_audio_buffer_speech_stopped_event.py
│  │        │  │  │  │  ├─ rate_limits_updated_event.py
│  │        │  │  │  │  ├─ realtime_client_event.py
│  │        │  │  │  │  ├─ realtime_client_event_param.py
│  │        │  │  │  │  ├─ realtime_connect_params.py
│  │        │  │  │  │  ├─ realtime_response.py
│  │        │  │  │  │  ├─ realtime_response_status.py
│  │        │  │  │  │  ├─ realtime_response_usage.py
│  │        │  │  │  │  ├─ realtime_server_event.py
│  │        │  │  │  │  ├─ response_audio_delta_event.py
│  │        │  │  │  │  ├─ response_audio_done_event.py
│  │        │  │  │  │  ├─ response_audio_transcript_delta_event.py
│  │        │  │  │  │  ├─ response_audio_transcript_done_event.py
│  │        │  │  │  │  ├─ response_cancel_event.py
│  │        │  │  │  │  ├─ response_cancel_event_param.py
│  │        │  │  │  │  ├─ response_content_part_added_event.py
│  │        │  │  │  │  ├─ response_content_part_done_event.py
│  │        │  │  │  │  ├─ response_create_event.py
│  │        │  │  │  │  ├─ response_create_event_param.py
│  │        │  │  │  │  ├─ response_created_event.py
│  │        │  │  │  │  ├─ response_done_event.py
│  │        │  │  │  │  ├─ response_function_call_arguments_delta_event.py
│  │        │  │  │  │  ├─ response_function_call_arguments_done_event.py
│  │        │  │  │  │  ├─ response_output_item_added_event.py
│  │        │  │  │  │  ├─ response_output_item_done_event.py
│  │        │  │  │  │  ├─ response_text_delta_event.py
│  │        │  │  │  │  ├─ response_text_done_event.py
│  │        │  │  │  │  ├─ session.py
│  │        │  │  │  │  ├─ session_create_params.py
│  │        │  │  │  │  ├─ session_create_response.py
│  │        │  │  │  │  ├─ session_created_event.py
│  │        │  │  │  │  ├─ session_update_event.py
│  │        │  │  │  │  ├─ session_update_event_param.py
│  │        │  │  │  │  ├─ session_updated_event.py
│  │        │  │  │  │  ├─ transcription_session.py
│  │        │  │  │  │  ├─ transcription_session_create_params.py
│  │        │  │  │  │  ├─ transcription_session_update.py
│  │        │  │  │  │  ├─ transcription_session_update_param.py
│  │        │  │  │  │  └─ transcription_session_updated_event.py
│  │        │  │  │  ├─ thread.py
│  │        │  │  │  ├─ thread_create_and_run_params.py
│  │        │  │  │  ├─ thread_create_params.py
│  │        │  │  │  ├─ thread_deleted.py
│  │        │  │  │  ├─ thread_update_params.py
│  │        │  │  │  └─ threads
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ annotation.py
│  │        │  │  │     ├─ annotation_delta.py
│  │        │  │  │     ├─ file_citation_annotation.py
│  │        │  │  │     ├─ file_citation_delta_annotation.py
│  │        │  │  │     ├─ file_path_annotation.py
│  │        │  │  │     ├─ file_path_delta_annotation.py
│  │        │  │  │     ├─ image_file.py
│  │        │  │  │     ├─ image_file_content_block.py
│  │        │  │  │     ├─ image_file_content_block_param.py
│  │        │  │  │     ├─ image_file_delta.py
│  │        │  │  │     ├─ image_file_delta_block.py
│  │        │  │  │     ├─ image_file_param.py
│  │        │  │  │     ├─ image_url.py
│  │        │  │  │     ├─ image_url_content_block.py
│  │        │  │  │     ├─ image_url_content_block_param.py
│  │        │  │  │     ├─ image_url_delta.py
│  │        │  │  │     ├─ image_url_delta_block.py
│  │        │  │  │     ├─ image_url_param.py
│  │        │  │  │     ├─ message.py
│  │        │  │  │     ├─ message_content.py
│  │        │  │  │     ├─ message_content_delta.py
│  │        │  │  │     ├─ message_content_part_param.py
│  │        │  │  │     ├─ message_create_params.py
│  │        │  │  │     ├─ message_deleted.py
│  │        │  │  │     ├─ message_delta.py
│  │        │  │  │     ├─ message_delta_event.py
│  │        │  │  │     ├─ message_list_params.py
│  │        │  │  │     ├─ message_update_params.py
│  │        │  │  │     ├─ refusal_content_block.py
│  │        │  │  │     ├─ refusal_delta_block.py
│  │        │  │  │     ├─ required_action_function_tool_call.py
│  │        │  │  │     ├─ run.py
│  │        │  │  │     ├─ run_create_params.py
│  │        │  │  │     ├─ run_list_params.py
│  │        │  │  │     ├─ run_status.py
│  │        │  │  │     ├─ run_submit_tool_outputs_params.py
│  │        │  │  │     ├─ run_update_params.py
│  │        │  │  │     ├─ runs
│  │        │  │  │     │  ├─ __init__.py
│  │        │  │  │     │  ├─ code_interpreter_logs.py
│  │        │  │  │     │  ├─ code_interpreter_output_image.py
│  │        │  │  │     │  ├─ code_interpreter_tool_call.py
│  │        │  │  │     │  ├─ code_interpreter_tool_call_delta.py
│  │        │  │  │     │  ├─ file_search_tool_call.py
│  │        │  │  │     │  ├─ file_search_tool_call_delta.py
│  │        │  │  │     │  ├─ function_tool_call.py
│  │        │  │  │     │  ├─ function_tool_call_delta.py
│  │        │  │  │     │  ├─ message_creation_step_details.py
│  │        │  │  │     │  ├─ run_step.py
│  │        │  │  │     │  ├─ run_step_delta.py
│  │        │  │  │     │  ├─ run_step_delta_event.py
│  │        │  │  │     │  ├─ run_step_delta_message_delta.py
│  │        │  │  │     │  ├─ run_step_include.py
│  │        │  │  │     │  ├─ step_list_params.py
│  │        │  │  │     │  ├─ step_retrieve_params.py
│  │        │  │  │     │  ├─ tool_call.py
│  │        │  │  │     │  ├─ tool_call_delta.py
│  │        │  │  │     │  ├─ tool_call_delta_object.py
│  │        │  │  │     │  └─ tool_calls_step_details.py
│  │        │  │  │     ├─ text.py
│  │        │  │  │     ├─ text_content_block.py
│  │        │  │  │     ├─ text_content_block_param.py
│  │        │  │  │     ├─ text_delta.py
│  │        │  │  │     └─ text_delta_block.py
│  │        │  │  ├─ chat
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ chat_completion.py
│  │        │  │  │  ├─ chat_completion_assistant_message_param.py
│  │        │  │  │  ├─ chat_completion_audio.py
│  │        │  │  │  ├─ chat_completion_audio_param.py
│  │        │  │  │  ├─ chat_completion_chunk.py
│  │        │  │  │  ├─ chat_completion_content_part_image_param.py
│  │        │  │  │  ├─ chat_completion_content_part_input_audio_param.py
│  │        │  │  │  ├─ chat_completion_content_part_param.py
│  │        │  │  │  ├─ chat_completion_content_part_refusal_param.py
│  │        │  │  │  ├─ chat_completion_content_part_text_param.py
│  │        │  │  │  ├─ chat_completion_deleted.py
│  │        │  │  │  ├─ chat_completion_developer_message_param.py
│  │        │  │  │  ├─ chat_completion_function_call_option_param.py
│  │        │  │  │  ├─ chat_completion_function_message_param.py
│  │        │  │  │  ├─ chat_completion_message.py
│  │        │  │  │  ├─ chat_completion_message_param.py
│  │        │  │  │  ├─ chat_completion_message_tool_call.py
│  │        │  │  │  ├─ chat_completion_message_tool_call_param.py
│  │        │  │  │  ├─ chat_completion_modality.py
│  │        │  │  │  ├─ chat_completion_named_tool_choice_param.py
│  │        │  │  │  ├─ chat_completion_prediction_content_param.py
│  │        │  │  │  ├─ chat_completion_reasoning_effort.py
│  │        │  │  │  ├─ chat_completion_role.py
│  │        │  │  │  ├─ chat_completion_store_message.py
│  │        │  │  │  ├─ chat_completion_stream_options_param.py
│  │        │  │  │  ├─ chat_completion_system_message_param.py
│  │        │  │  │  ├─ chat_completion_token_logprob.py
│  │        │  │  │  ├─ chat_completion_tool_choice_option_param.py
│  │        │  │  │  ├─ chat_completion_tool_message_param.py
│  │        │  │  │  ├─ chat_completion_tool_param.py
│  │        │  │  │  ├─ chat_completion_user_message_param.py
│  │        │  │  │  ├─ completion_create_params.py
│  │        │  │  │  ├─ completion_list_params.py
│  │        │  │  │  ├─ completion_update_params.py
│  │        │  │  │  ├─ completions
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ message_list_params.py
│  │        │  │  │  ├─ parsed_chat_completion.py
│  │        │  │  │  └─ parsed_function_tool_call.py
│  │        │  │  ├─ chat_model.py
│  │        │  │  ├─ completion.py
│  │        │  │  ├─ completion_choice.py
│  │        │  │  ├─ completion_create_params.py
│  │        │  │  ├─ completion_usage.py
│  │        │  │  ├─ container_create_params.py
│  │        │  │  ├─ container_create_response.py
│  │        │  │  ├─ container_list_params.py
│  │        │  │  ├─ container_list_response.py
│  │        │  │  ├─ container_retrieve_response.py
│  │        │  │  ├─ containers
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ file_create_params.py
│  │        │  │  │  ├─ file_create_response.py
│  │        │  │  │  ├─ file_list_params.py
│  │        │  │  │  ├─ file_list_response.py
│  │        │  │  │  ├─ file_retrieve_response.py
│  │        │  │  │  └─ files
│  │        │  │  │     └─ __init__.py
│  │        │  │  ├─ create_embedding_response.py
│  │        │  │  ├─ embedding.py
│  │        │  │  ├─ embedding_create_params.py
│  │        │  │  ├─ embedding_model.py
│  │        │  │  ├─ eval_create_params.py
│  │        │  │  ├─ eval_create_response.py
│  │        │  │  ├─ eval_custom_data_source_config.py
│  │        │  │  ├─ eval_delete_response.py
│  │        │  │  ├─ eval_list_params.py
│  │        │  │  ├─ eval_list_response.py
│  │        │  │  ├─ eval_retrieve_response.py
│  │        │  │  ├─ eval_stored_completions_data_source_config.py
│  │        │  │  ├─ eval_update_params.py
│  │        │  │  ├─ eval_update_response.py
│  │        │  │  ├─ evals
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ create_eval_completions_run_data_source.py
│  │        │  │  │  ├─ create_eval_completions_run_data_source_param.py
│  │        │  │  │  ├─ create_eval_jsonl_run_data_source.py
│  │        │  │  │  ├─ create_eval_jsonl_run_data_source_param.py
│  │        │  │  │  ├─ eval_api_error.py
│  │        │  │  │  ├─ run_cancel_response.py
│  │        │  │  │  ├─ run_create_params.py
│  │        │  │  │  ├─ run_create_response.py
│  │        │  │  │  ├─ run_delete_response.py
│  │        │  │  │  ├─ run_list_params.py
│  │        │  │  │  ├─ run_list_response.py
│  │        │  │  │  ├─ run_retrieve_response.py
│  │        │  │  │  └─ runs
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ output_item_list_params.py
│  │        │  │  │     ├─ output_item_list_response.py
│  │        │  │  │     └─ output_item_retrieve_response.py
│  │        │  │  ├─ file_chunking_strategy.py
│  │        │  │  ├─ file_chunking_strategy_param.py
│  │        │  │  ├─ file_content.py
│  │        │  │  ├─ file_create_params.py
│  │        │  │  ├─ file_deleted.py
│  │        │  │  ├─ file_list_params.py
│  │        │  │  ├─ file_object.py
│  │        │  │  ├─ file_purpose.py
│  │        │  │  ├─ fine_tuning
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ alpha
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ grader_run_params.py
│  │        │  │  │  │  ├─ grader_run_response.py
│  │        │  │  │  │  ├─ grader_validate_params.py
│  │        │  │  │  │  └─ grader_validate_response.py
│  │        │  │  │  ├─ checkpoints
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ permission_create_params.py
│  │        │  │  │  │  ├─ permission_create_response.py
│  │        │  │  │  │  ├─ permission_delete_response.py
│  │        │  │  │  │  ├─ permission_retrieve_params.py
│  │        │  │  │  │  └─ permission_retrieve_response.py
│  │        │  │  │  ├─ dpo_hyperparameters.py
│  │        │  │  │  ├─ dpo_hyperparameters_param.py
│  │        │  │  │  ├─ dpo_method.py
│  │        │  │  │  ├─ dpo_method_param.py
│  │        │  │  │  ├─ fine_tuning_job.py
│  │        │  │  │  ├─ fine_tuning_job_event.py
│  │        │  │  │  ├─ fine_tuning_job_integration.py
│  │        │  │  │  ├─ fine_tuning_job_wandb_integration.py
│  │        │  │  │  ├─ fine_tuning_job_wandb_integration_object.py
│  │        │  │  │  ├─ job_create_params.py
│  │        │  │  │  ├─ job_list_events_params.py
│  │        │  │  │  ├─ job_list_params.py
│  │        │  │  │  ├─ jobs
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ checkpoint_list_params.py
│  │        │  │  │  │  └─ fine_tuning_job_checkpoint.py
│  │        │  │  │  ├─ reinforcement_hyperparameters.py
│  │        │  │  │  ├─ reinforcement_hyperparameters_param.py
│  │        │  │  │  ├─ reinforcement_method.py
│  │        │  │  │  ├─ reinforcement_method_param.py
│  │        │  │  │  ├─ supervised_hyperparameters.py
│  │        │  │  │  ├─ supervised_hyperparameters_param.py
│  │        │  │  │  ├─ supervised_method.py
│  │        │  │  │  └─ supervised_method_param.py
│  │        │  │  ├─ graders
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ label_model_grader.py
│  │        │  │  │  ├─ label_model_grader_param.py
│  │        │  │  │  ├─ multi_grader.py
│  │        │  │  │  ├─ multi_grader_param.py
│  │        │  │  │  ├─ python_grader.py
│  │        │  │  │  ├─ python_grader_param.py
│  │        │  │  │  ├─ score_model_grader.py
│  │        │  │  │  ├─ score_model_grader_param.py
│  │        │  │  │  ├─ string_check_grader.py
│  │        │  │  │  ├─ string_check_grader_param.py
│  │        │  │  │  ├─ text_similarity_grader.py
│  │        │  │  │  └─ text_similarity_grader_param.py
│  │        │  │  ├─ image.py
│  │        │  │  ├─ image_create_variation_params.py
│  │        │  │  ├─ image_edit_params.py
│  │        │  │  ├─ image_generate_params.py
│  │        │  │  ├─ image_model.py
│  │        │  │  ├─ images_response.py
│  │        │  │  ├─ model.py
│  │        │  │  ├─ model_deleted.py
│  │        │  │  ├─ moderation.py
│  │        │  │  ├─ moderation_create_params.py
│  │        │  │  ├─ moderation_create_response.py
│  │        │  │  ├─ moderation_image_url_input_param.py
│  │        │  │  ├─ moderation_model.py
│  │        │  │  ├─ moderation_multi_modal_input_param.py
│  │        │  │  ├─ moderation_text_input_param.py
│  │        │  │  ├─ other_file_chunking_strategy_object.py
│  │        │  │  ├─ responses
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ computer_tool.py
│  │        │  │  │  ├─ computer_tool_param.py
│  │        │  │  │  ├─ easy_input_message.py
│  │        │  │  │  ├─ easy_input_message_param.py
│  │        │  │  │  ├─ file_search_tool.py
│  │        │  │  │  ├─ file_search_tool_param.py
│  │        │  │  │  ├─ function_tool.py
│  │        │  │  │  ├─ function_tool_param.py
│  │        │  │  │  ├─ input_item_list_params.py
│  │        │  │  │  ├─ parsed_response.py
│  │        │  │  │  ├─ response.py
│  │        │  │  │  ├─ response_audio_delta_event.py
│  │        │  │  │  ├─ response_audio_done_event.py
│  │        │  │  │  ├─ response_audio_transcript_delta_event.py
│  │        │  │  │  ├─ response_audio_transcript_done_event.py
│  │        │  │  │  ├─ response_code_interpreter_call_code_delta_event.py
│  │        │  │  │  ├─ response_code_interpreter_call_code_done_event.py
│  │        │  │  │  ├─ response_code_interpreter_call_completed_event.py
│  │        │  │  │  ├─ response_code_interpreter_call_in_progress_event.py
│  │        │  │  │  ├─ response_code_interpreter_call_interpreting_event.py
│  │        │  │  │  ├─ response_code_interpreter_tool_call.py
│  │        │  │  │  ├─ response_code_interpreter_tool_call_param.py
│  │        │  │  │  ├─ response_completed_event.py
│  │        │  │  │  ├─ response_computer_tool_call.py
│  │        │  │  │  ├─ response_computer_tool_call_output_item.py
│  │        │  │  │  ├─ response_computer_tool_call_output_screenshot.py
│  │        │  │  │  ├─ response_computer_tool_call_output_screenshot_param.py
│  │        │  │  │  ├─ response_computer_tool_call_param.py
│  │        │  │  │  ├─ response_content_part_added_event.py
│  │        │  │  │  ├─ response_content_part_done_event.py
│  │        │  │  │  ├─ response_create_params.py
│  │        │  │  │  ├─ response_created_event.py
│  │        │  │  │  ├─ response_error.py
│  │        │  │  │  ├─ response_error_event.py
│  │        │  │  │  ├─ response_failed_event.py
│  │        │  │  │  ├─ response_file_search_call_completed_event.py
│  │        │  │  │  ├─ response_file_search_call_in_progress_event.py
│  │        │  │  │  ├─ response_file_search_call_searching_event.py
│  │        │  │  │  ├─ response_file_search_tool_call.py
│  │        │  │  │  ├─ response_file_search_tool_call_param.py
│  │        │  │  │  ├─ response_format_text_config.py
│  │        │  │  │  ├─ response_format_text_config_param.py
│  │        │  │  │  ├─ response_format_text_json_schema_config.py
│  │        │  │  │  ├─ response_format_text_json_schema_config_param.py
│  │        │  │  │  ├─ response_function_call_arguments_delta_event.py
│  │        │  │  │  ├─ response_function_call_arguments_done_event.py
│  │        │  │  │  ├─ response_function_tool_call.py
│  │        │  │  │  ├─ response_function_tool_call_item.py
│  │        │  │  │  ├─ response_function_tool_call_output_item.py
│  │        │  │  │  ├─ response_function_tool_call_param.py
│  │        │  │  │  ├─ response_function_web_search.py
│  │        │  │  │  ├─ response_function_web_search_param.py
│  │        │  │  │  ├─ response_image_gen_call_completed_event.py
│  │        │  │  │  ├─ response_image_gen_call_generating_event.py
│  │        │  │  │  ├─ response_image_gen_call_in_progress_event.py
│  │        │  │  │  ├─ response_image_gen_call_partial_image_event.py
│  │        │  │  │  ├─ response_in_progress_event.py
│  │        │  │  │  ├─ response_includable.py
│  │        │  │  │  ├─ response_incomplete_event.py
│  │        │  │  │  ├─ response_input_content.py
│  │        │  │  │  ├─ response_input_content_param.py
│  │        │  │  │  ├─ response_input_file.py
│  │        │  │  │  ├─ response_input_file_param.py
│  │        │  │  │  ├─ response_input_image.py
│  │        │  │  │  ├─ response_input_image_param.py
│  │        │  │  │  ├─ response_input_item_param.py
│  │        │  │  │  ├─ response_input_message_content_list.py
│  │        │  │  │  ├─ response_input_message_content_list_param.py
│  │        │  │  │  ├─ response_input_message_item.py
│  │        │  │  │  ├─ response_input_param.py
│  │        │  │  │  ├─ response_input_text.py
│  │        │  │  │  ├─ response_input_text_param.py
│  │        │  │  │  ├─ response_item.py
│  │        │  │  │  ├─ response_item_list.py
│  │        │  │  │  ├─ response_mcp_call_arguments_delta_event.py
│  │        │  │  │  ├─ response_mcp_call_arguments_done_event.py
│  │        │  │  │  ├─ response_mcp_call_completed_event.py
│  │        │  │  │  ├─ response_mcp_call_failed_event.py
│  │        │  │  │  ├─ response_mcp_call_in_progress_event.py
│  │        │  │  │  ├─ response_mcp_list_tools_completed_event.py
│  │        │  │  │  ├─ response_mcp_list_tools_failed_event.py
│  │        │  │  │  ├─ response_mcp_list_tools_in_progress_event.py
│  │        │  │  │  ├─ response_output_item.py
│  │        │  │  │  ├─ response_output_item_added_event.py
│  │        │  │  │  ├─ response_output_item_done_event.py
│  │        │  │  │  ├─ response_output_message.py
│  │        │  │  │  ├─ response_output_message_param.py
│  │        │  │  │  ├─ response_output_refusal.py
│  │        │  │  │  ├─ response_output_refusal_param.py
│  │        │  │  │  ├─ response_output_text.py
│  │        │  │  │  ├─ response_output_text_annotation_added_event.py
│  │        │  │  │  ├─ response_output_text_param.py
│  │        │  │  │  ├─ response_queued_event.py
│  │        │  │  │  ├─ response_reasoning_delta_event.py
│  │        │  │  │  ├─ response_reasoning_done_event.py
│  │        │  │  │  ├─ response_reasoning_item.py
│  │        │  │  │  ├─ response_reasoning_item_param.py
│  │        │  │  │  ├─ response_reasoning_summary_delta_event.py
│  │        │  │  │  ├─ response_reasoning_summary_done_event.py
│  │        │  │  │  ├─ response_reasoning_summary_part_added_event.py
│  │        │  │  │  ├─ response_reasoning_summary_part_done_event.py
│  │        │  │  │  ├─ response_reasoning_summary_text_delta_event.py
│  │        │  │  │  ├─ response_reasoning_summary_text_done_event.py
│  │        │  │  │  ├─ response_refusal_delta_event.py
│  │        │  │  │  ├─ response_refusal_done_event.py
│  │        │  │  │  ├─ response_retrieve_params.py
│  │        │  │  │  ├─ response_status.py
│  │        │  │  │  ├─ response_stream_event.py
│  │        │  │  │  ├─ response_text_config.py
│  │        │  │  │  ├─ response_text_config_param.py
│  │        │  │  │  ├─ response_text_delta_event.py
│  │        │  │  │  ├─ response_text_done_event.py
│  │        │  │  │  ├─ response_usage.py
│  │        │  │  │  ├─ response_web_search_call_completed_event.py
│  │        │  │  │  ├─ response_web_search_call_in_progress_event.py
│  │        │  │  │  ├─ response_web_search_call_searching_event.py
│  │        │  │  │  ├─ tool.py
│  │        │  │  │  ├─ tool_choice_function.py
│  │        │  │  │  ├─ tool_choice_function_param.py
│  │        │  │  │  ├─ tool_choice_options.py
│  │        │  │  │  ├─ tool_choice_types.py
│  │        │  │  │  ├─ tool_choice_types_param.py
│  │        │  │  │  ├─ tool_param.py
│  │        │  │  │  ├─ web_search_tool.py
│  │        │  │  │  └─ web_search_tool_param.py
│  │        │  │  ├─ shared
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ all_models.py
│  │        │  │  │  ├─ chat_model.py
│  │        │  │  │  ├─ comparison_filter.py
│  │        │  │  │  ├─ compound_filter.py
│  │        │  │  │  ├─ error_object.py
│  │        │  │  │  ├─ function_definition.py
│  │        │  │  │  ├─ function_parameters.py
│  │        │  │  │  ├─ metadata.py
│  │        │  │  │  ├─ reasoning.py
│  │        │  │  │  ├─ reasoning_effort.py
│  │        │  │  │  ├─ response_format_json_object.py
│  │        │  │  │  ├─ response_format_json_schema.py
│  │        │  │  │  ├─ response_format_text.py
│  │        │  │  │  └─ responses_model.py
│  │        │  │  ├─ shared_params
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ chat_model.py
│  │        │  │  │  ├─ comparison_filter.py
│  │        │  │  │  ├─ compound_filter.py
│  │        │  │  │  ├─ function_definition.py
│  │        │  │  │  ├─ function_parameters.py
│  │        │  │  │  ├─ metadata.py
│  │        │  │  │  ├─ reasoning.py
│  │        │  │  │  ├─ reasoning_effort.py
│  │        │  │  │  ├─ response_format_json_object.py
│  │        │  │  │  ├─ response_format_json_schema.py
│  │        │  │  │  ├─ response_format_text.py
│  │        │  │  │  └─ responses_model.py
│  │        │  │  ├─ static_file_chunking_strategy.py
│  │        │  │  ├─ static_file_chunking_strategy_object.py
│  │        │  │  ├─ static_file_chunking_strategy_object_param.py
│  │        │  │  ├─ static_file_chunking_strategy_param.py
│  │        │  │  ├─ upload.py
│  │        │  │  ├─ upload_complete_params.py
│  │        │  │  ├─ upload_create_params.py
│  │        │  │  ├─ uploads
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ part_create_params.py
│  │        │  │  │  └─ upload_part.py
│  │        │  │  ├─ vector_store.py
│  │        │  │  ├─ vector_store_create_params.py
│  │        │  │  ├─ vector_store_deleted.py
│  │        │  │  ├─ vector_store_list_params.py
│  │        │  │  ├─ vector_store_search_params.py
│  │        │  │  ├─ vector_store_search_response.py
│  │        │  │  ├─ vector_store_update_params.py
│  │        │  │  ├─ vector_stores
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ file_batch_create_params.py
│  │        │  │  │  ├─ file_batch_list_files_params.py
│  │        │  │  │  ├─ file_content_response.py
│  │        │  │  │  ├─ file_create_params.py
│  │        │  │  │  ├─ file_list_params.py
│  │        │  │  │  ├─ file_update_params.py
│  │        │  │  │  ├─ vector_store_file.py
│  │        │  │  │  ├─ vector_store_file_batch.py
│  │        │  │  │  └─ vector_store_file_deleted.py
│  │        │  │  └─ websocket_connection_options.py
│  │        │  └─ version.py
│  │        ├─ openai-1.82.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ pip
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ __pip-runner__.py
│  │        │  ├─ _internal
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ build_env.py
│  │        │  │  ├─ cache.py
│  │        │  │  ├─ cli
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ autocompletion.py
│  │        │  │  │  ├─ base_command.py
│  │        │  │  │  ├─ cmdoptions.py
│  │        │  │  │  ├─ command_context.py
│  │        │  │  │  ├─ main.py
│  │        │  │  │  ├─ main_parser.py
│  │        │  │  │  ├─ parser.py
│  │        │  │  │  ├─ progress_bars.py
│  │        │  │  │  ├─ req_command.py
│  │        │  │  │  ├─ spinners.py
│  │        │  │  │  └─ status_codes.py
│  │        │  │  ├─ commands
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ cache.py
│  │        │  │  │  ├─ check.py
│  │        │  │  │  ├─ completion.py
│  │        │  │  │  ├─ configuration.py
│  │        │  │  │  ├─ debug.py
│  │        │  │  │  ├─ download.py
│  │        │  │  │  ├─ freeze.py
│  │        │  │  │  ├─ hash.py
│  │        │  │  │  ├─ help.py
│  │        │  │  │  ├─ index.py
│  │        │  │  │  ├─ inspect.py
│  │        │  │  │  ├─ install.py
│  │        │  │  │  ├─ list.py
│  │        │  │  │  ├─ search.py
│  │        │  │  │  ├─ show.py
│  │        │  │  │  ├─ uninstall.py
│  │        │  │  │  └─ wheel.py
│  │        │  │  ├─ configuration.py
│  │        │  │  ├─ distributions
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ installed.py
│  │        │  │  │  ├─ sdist.py
│  │        │  │  │  └─ wheel.py
│  │        │  │  ├─ exceptions.py
│  │        │  │  ├─ index
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ collector.py
│  │        │  │  │  ├─ package_finder.py
│  │        │  │  │  └─ sources.py
│  │        │  │  ├─ locations
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _distutils.py
│  │        │  │  │  ├─ _sysconfig.py
│  │        │  │  │  └─ base.py
│  │        │  │  ├─ main.py
│  │        │  │  ├─ metadata
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _json.py
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ importlib
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ _compat.py
│  │        │  │  │  │  ├─ _dists.py
│  │        │  │  │  │  └─ _envs.py
│  │        │  │  │  └─ pkg_resources.py
│  │        │  │  ├─ models
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ candidate.py
│  │        │  │  │  ├─ direct_url.py
│  │        │  │  │  ├─ format_control.py
│  │        │  │  │  ├─ index.py
│  │        │  │  │  ├─ installation_report.py
│  │        │  │  │  ├─ link.py
│  │        │  │  │  ├─ scheme.py
│  │        │  │  │  ├─ search_scope.py
│  │        │  │  │  ├─ selection_prefs.py
│  │        │  │  │  ├─ target_python.py
│  │        │  │  │  └─ wheel.py
│  │        │  │  ├─ network
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ auth.py
│  │        │  │  │  ├─ cache.py
│  │        │  │  │  ├─ download.py
│  │        │  │  │  ├─ lazy_wheel.py
│  │        │  │  │  ├─ session.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  └─ xmlrpc.py
│  │        │  │  ├─ operations
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ build
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ build_tracker.py
│  │        │  │  │  │  ├─ metadata.py
│  │        │  │  │  │  ├─ metadata_editable.py
│  │        │  │  │  │  ├─ metadata_legacy.py
│  │        │  │  │  │  ├─ wheel.py
│  │        │  │  │  │  ├─ wheel_editable.py
│  │        │  │  │  │  └─ wheel_legacy.py
│  │        │  │  │  ├─ check.py
│  │        │  │  │  ├─ freeze.py
│  │        │  │  │  ├─ install
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ editable_legacy.py
│  │        │  │  │  │  ├─ legacy.py
│  │        │  │  │  │  └─ wheel.py
│  │        │  │  │  └─ prepare.py
│  │        │  │  ├─ pyproject.py
│  │        │  │  ├─ req
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ constructors.py
│  │        │  │  │  ├─ req_file.py
│  │        │  │  │  ├─ req_install.py
│  │        │  │  │  ├─ req_set.py
│  │        │  │  │  └─ req_uninstall.py
│  │        │  │  ├─ resolution
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ base.py
│  │        │  │  │  ├─ legacy
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ resolver.py
│  │        │  │  │  └─ resolvelib
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ base.py
│  │        │  │  │     ├─ candidates.py
│  │        │  │  │     ├─ factory.py
│  │        │  │  │     ├─ found_candidates.py
│  │        │  │  │     ├─ provider.py
│  │        │  │  │     ├─ reporter.py
│  │        │  │  │     ├─ requirements.py
│  │        │  │  │     └─ resolver.py
│  │        │  │  ├─ self_outdated_check.py
│  │        │  │  ├─ utils
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _log.py
│  │        │  │  │  ├─ appdirs.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ compatibility_tags.py
│  │        │  │  │  ├─ datetime.py
│  │        │  │  │  ├─ deprecation.py
│  │        │  │  │  ├─ direct_url_helpers.py
│  │        │  │  │  ├─ distutils_args.py
│  │        │  │  │  ├─ egg_link.py
│  │        │  │  │  ├─ encoding.py
│  │        │  │  │  ├─ entrypoints.py
│  │        │  │  │  ├─ filesystem.py
│  │        │  │  │  ├─ filetypes.py
│  │        │  │  │  ├─ glibc.py
│  │        │  │  │  ├─ hashes.py
│  │        │  │  │  ├─ inject_securetransport.py
│  │        │  │  │  ├─ logging.py
│  │        │  │  │  ├─ misc.py
│  │        │  │  │  ├─ models.py
│  │        │  │  │  ├─ packaging.py
│  │        │  │  │  ├─ setuptools_build.py
│  │        │  │  │  ├─ subprocess.py
│  │        │  │  │  ├─ temp_dir.py
│  │        │  │  │  ├─ unpacking.py
│  │        │  │  │  ├─ urls.py
│  │        │  │  │  ├─ virtualenv.py
│  │        │  │  │  └─ wheel.py
│  │        │  │  ├─ vcs
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ bazaar.py
│  │        │  │  │  ├─ git.py
│  │        │  │  │  ├─ mercurial.py
│  │        │  │  │  ├─ subversion.py
│  │        │  │  │  └─ versioncontrol.py
│  │        │  │  └─ wheel_builder.py
│  │        │  ├─ _vendor
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ cachecontrol
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _cmd.py
│  │        │  │  │  ├─ adapter.py
│  │        │  │  │  ├─ cache.py
│  │        │  │  │  ├─ caches
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ file_cache.py
│  │        │  │  │  │  └─ redis_cache.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ controller.py
│  │        │  │  │  ├─ filewrapper.py
│  │        │  │  │  ├─ heuristics.py
│  │        │  │  │  ├─ serialize.py
│  │        │  │  │  └─ wrapper.py
│  │        │  │  ├─ certifi
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  ├─ cacert.pem
│  │        │  │  │  └─ core.py
│  │        │  │  ├─ chardet
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ big5freq.py
│  │        │  │  │  ├─ big5prober.py
│  │        │  │  │  ├─ chardistribution.py
│  │        │  │  │  ├─ charsetgroupprober.py
│  │        │  │  │  ├─ charsetprober.py
│  │        │  │  │  ├─ cli
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ chardetect.py
│  │        │  │  │  ├─ codingstatemachine.py
│  │        │  │  │  ├─ codingstatemachinedict.py
│  │        │  │  │  ├─ cp949prober.py
│  │        │  │  │  ├─ enums.py
│  │        │  │  │  ├─ escprober.py
│  │        │  │  │  ├─ escsm.py
│  │        │  │  │  ├─ eucjpprober.py
│  │        │  │  │  ├─ euckrfreq.py
│  │        │  │  │  ├─ euckrprober.py
│  │        │  │  │  ├─ euctwfreq.py
│  │        │  │  │  ├─ euctwprober.py
│  │        │  │  │  ├─ gb2312freq.py
│  │        │  │  │  ├─ gb2312prober.py
│  │        │  │  │  ├─ hebrewprober.py
│  │        │  │  │  ├─ jisfreq.py
│  │        │  │  │  ├─ johabfreq.py
│  │        │  │  │  ├─ johabprober.py
│  │        │  │  │  ├─ jpcntx.py
│  │        │  │  │  ├─ langbulgarianmodel.py
│  │        │  │  │  ├─ langgreekmodel.py
│  │        │  │  │  ├─ langhebrewmodel.py
│  │        │  │  │  ├─ langhungarianmodel.py
│  │        │  │  │  ├─ langrussianmodel.py
│  │        │  │  │  ├─ langthaimodel.py
│  │        │  │  │  ├─ langturkishmodel.py
│  │        │  │  │  ├─ latin1prober.py
│  │        │  │  │  ├─ macromanprober.py
│  │        │  │  │  ├─ mbcharsetprober.py
│  │        │  │  │  ├─ mbcsgroupprober.py
│  │        │  │  │  ├─ mbcssm.py
│  │        │  │  │  ├─ metadata
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ languages.py
│  │        │  │  │  ├─ resultdict.py
│  │        │  │  │  ├─ sbcharsetprober.py
│  │        │  │  │  ├─ sbcsgroupprober.py
│  │        │  │  │  ├─ sjisprober.py
│  │        │  │  │  ├─ universaldetector.py
│  │        │  │  │  ├─ utf1632prober.py
│  │        │  │  │  ├─ utf8prober.py
│  │        │  │  │  └─ version.py
│  │        │  │  ├─ colorama
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ ansi.py
│  │        │  │  │  ├─ ansitowin32.py
│  │        │  │  │  ├─ initialise.py
│  │        │  │  │  ├─ tests
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ ansi_test.py
│  │        │  │  │  │  ├─ ansitowin32_test.py
│  │        │  │  │  │  ├─ initialise_test.py
│  │        │  │  │  │  ├─ isatty_test.py
│  │        │  │  │  │  ├─ utils.py
│  │        │  │  │  │  └─ winterm_test.py
│  │        │  │  │  ├─ win32.py
│  │        │  │  │  └─ winterm.py
│  │        │  │  ├─ distlib
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ database.py
│  │        │  │  │  ├─ index.py
│  │        │  │  │  ├─ locators.py
│  │        │  │  │  ├─ manifest.py
│  │        │  │  │  ├─ markers.py
│  │        │  │  │  ├─ metadata.py
│  │        │  │  │  ├─ resources.py
│  │        │  │  │  ├─ scripts.py
│  │        │  │  │  ├─ t32.exe
│  │        │  │  │  ├─ t64-arm.exe
│  │        │  │  │  ├─ t64.exe
│  │        │  │  │  ├─ util.py
│  │        │  │  │  ├─ version.py
│  │        │  │  │  ├─ w32.exe
│  │        │  │  │  ├─ w64-arm.exe
│  │        │  │  │  ├─ w64.exe
│  │        │  │  │  └─ wheel.py
│  │        │  │  ├─ distro
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  └─ distro.py
│  │        │  │  ├─ idna
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ codec.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ core.py
│  │        │  │  │  ├─ idnadata.py
│  │        │  │  │  ├─ intranges.py
│  │        │  │  │  ├─ package_data.py
│  │        │  │  │  └─ uts46data.py
│  │        │  │  ├─ msgpack
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ exceptions.py
│  │        │  │  │  ├─ ext.py
│  │        │  │  │  └─ fallback.py
│  │        │  │  ├─ packaging
│  │        │  │  │  ├─ __about__.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _manylinux.py
│  │        │  │  │  ├─ _musllinux.py
│  │        │  │  │  ├─ _structures.py
│  │        │  │  │  ├─ markers.py
│  │        │  │  │  ├─ requirements.py
│  │        │  │  │  ├─ specifiers.py
│  │        │  │  │  ├─ tags.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  └─ version.py
│  │        │  │  ├─ pkg_resources
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  └─ py31compat.py
│  │        │  │  ├─ platformdirs
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  ├─ android.py
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ macos.py
│  │        │  │  │  ├─ unix.py
│  │        │  │  │  ├─ version.py
│  │        │  │  │  └─ windows.py
│  │        │  │  ├─ pygments
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  ├─ cmdline.py
│  │        │  │  │  ├─ console.py
│  │        │  │  │  ├─ filter.py
│  │        │  │  │  ├─ filters
│  │        │  │  │  │  └─ __init__.py
│  │        │  │  │  ├─ formatter.py
│  │        │  │  │  ├─ formatters
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ _mapping.py
│  │        │  │  │  │  ├─ bbcode.py
│  │        │  │  │  │  ├─ groff.py
│  │        │  │  │  │  ├─ html.py
│  │        │  │  │  │  ├─ img.py
│  │        │  │  │  │  ├─ irc.py
│  │        │  │  │  │  ├─ latex.py
│  │        │  │  │  │  ├─ other.py
│  │        │  │  │  │  ├─ pangomarkup.py
│  │        │  │  │  │  ├─ rtf.py
│  │        │  │  │  │  ├─ svg.py
│  │        │  │  │  │  ├─ terminal.py
│  │        │  │  │  │  └─ terminal256.py
│  │        │  │  │  ├─ lexer.py
│  │        │  │  │  ├─ lexers
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ _mapping.py
│  │        │  │  │  │  └─ python.py
│  │        │  │  │  ├─ modeline.py
│  │        │  │  │  ├─ plugin.py
│  │        │  │  │  ├─ regexopt.py
│  │        │  │  │  ├─ scanner.py
│  │        │  │  │  ├─ sphinxext.py
│  │        │  │  │  ├─ style.py
│  │        │  │  │  ├─ styles
│  │        │  │  │  │  └─ __init__.py
│  │        │  │  │  ├─ token.py
│  │        │  │  │  ├─ unistring.py
│  │        │  │  │  └─ util.py
│  │        │  │  ├─ pyparsing
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ actions.py
│  │        │  │  │  ├─ common.py
│  │        │  │  │  ├─ core.py
│  │        │  │  │  ├─ diagram
│  │        │  │  │  │  └─ __init__.py
│  │        │  │  │  ├─ exceptions.py
│  │        │  │  │  ├─ helpers.py
│  │        │  │  │  ├─ results.py
│  │        │  │  │  ├─ testing.py
│  │        │  │  │  ├─ unicode.py
│  │        │  │  │  └─ util.py
│  │        │  │  ├─ pyproject_hooks
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _compat.py
│  │        │  │  │  ├─ _impl.py
│  │        │  │  │  └─ _in_process
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     └─ _in_process.py
│  │        │  │  ├─ requests
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __version__.py
│  │        │  │  │  ├─ _internal_utils.py
│  │        │  │  │  ├─ adapters.py
│  │        │  │  │  ├─ api.py
│  │        │  │  │  ├─ auth.py
│  │        │  │  │  ├─ certs.py
│  │        │  │  │  ├─ compat.py
│  │        │  │  │  ├─ cookies.py
│  │        │  │  │  ├─ exceptions.py
│  │        │  │  │  ├─ help.py
│  │        │  │  │  ├─ hooks.py
│  │        │  │  │  ├─ models.py
│  │        │  │  │  ├─ packages.py
│  │        │  │  │  ├─ sessions.py
│  │        │  │  │  ├─ status_codes.py
│  │        │  │  │  ├─ structures.py
│  │        │  │  │  └─ utils.py
│  │        │  │  ├─ resolvelib
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ compat
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  └─ collections_abc.py
│  │        │  │  │  ├─ providers.py
│  │        │  │  │  ├─ reporters.py
│  │        │  │  │  ├─ resolvers.py
│  │        │  │  │  └─ structs.py
│  │        │  │  ├─ rich
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ __main__.py
│  │        │  │  │  ├─ _cell_widths.py
│  │        │  │  │  ├─ _emoji_codes.py
│  │        │  │  │  ├─ _emoji_replace.py
│  │        │  │  │  ├─ _export_format.py
│  │        │  │  │  ├─ _extension.py
│  │        │  │  │  ├─ _inspect.py
│  │        │  │  │  ├─ _log_render.py
│  │        │  │  │  ├─ _loop.py
│  │        │  │  │  ├─ _null_file.py
│  │        │  │  │  ├─ _palettes.py
│  │        │  │  │  ├─ _pick.py
│  │        │  │  │  ├─ _ratio.py
│  │        │  │  │  ├─ _spinners.py
│  │        │  │  │  ├─ _stack.py
│  │        │  │  │  ├─ _timer.py
│  │        │  │  │  ├─ _win32_console.py
│  │        │  │  │  ├─ _windows.py
│  │        │  │  │  ├─ _windows_renderer.py
│  │        │  │  │  ├─ _wrap.py
│  │        │  │  │  ├─ abc.py
│  │        │  │  │  ├─ align.py
│  │        │  │  │  ├─ ansi.py
│  │        │  │  │  ├─ bar.py
│  │        │  │  │  ├─ box.py
│  │        │  │  │  ├─ cells.py
│  │        │  │  │  ├─ color.py
│  │        │  │  │  ├─ color_triplet.py
│  │        │  │  │  ├─ columns.py
│  │        │  │  │  ├─ console.py
│  │        │  │  │  ├─ constrain.py
│  │        │  │  │  ├─ containers.py
│  │        │  │  │  ├─ control.py
│  │        │  │  │  ├─ default_styles.py
│  │        │  │  │  ├─ diagnose.py
│  │        │  │  │  ├─ emoji.py
│  │        │  │  │  ├─ errors.py
│  │        │  │  │  ├─ file_proxy.py
│  │        │  │  │  ├─ filesize.py
│  │        │  │  │  ├─ highlighter.py
│  │        │  │  │  ├─ json.py
│  │        │  │  │  ├─ jupyter.py
│  │        │  │  │  ├─ layout.py
│  │        │  │  │  ├─ live.py
│  │        │  │  │  ├─ live_render.py
│  │        │  │  │  ├─ logging.py
│  │        │  │  │  ├─ markup.py
│  │        │  │  │  ├─ measure.py
│  │        │  │  │  ├─ padding.py
│  │        │  │  │  ├─ pager.py
│  │        │  │  │  ├─ palette.py
│  │        │  │  │  ├─ panel.py
│  │        │  │  │  ├─ pretty.py
│  │        │  │  │  ├─ progress.py
│  │        │  │  │  ├─ progress_bar.py
│  │        │  │  │  ├─ prompt.py
│  │        │  │  │  ├─ protocol.py
│  │        │  │  │  ├─ region.py
│  │        │  │  │  ├─ repr.py
│  │        │  │  │  ├─ rule.py
│  │        │  │  │  ├─ scope.py
│  │        │  │  │  ├─ screen.py
│  │        │  │  │  ├─ segment.py
│  │        │  │  │  ├─ spinner.py
│  │        │  │  │  ├─ status.py
│  │        │  │  │  ├─ style.py
│  │        │  │  │  ├─ styled.py
│  │        │  │  │  ├─ syntax.py
│  │        │  │  │  ├─ table.py
│  │        │  │  │  ├─ terminal_theme.py
│  │        │  │  │  ├─ text.py
│  │        │  │  │  ├─ theme.py
│  │        │  │  │  ├─ themes.py
│  │        │  │  │  ├─ traceback.py
│  │        │  │  │  └─ tree.py
│  │        │  │  ├─ six.py
│  │        │  │  ├─ tenacity
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _asyncio.py
│  │        │  │  │  ├─ _utils.py
│  │        │  │  │  ├─ after.py
│  │        │  │  │  ├─ before.py
│  │        │  │  │  ├─ before_sleep.py
│  │        │  │  │  ├─ nap.py
│  │        │  │  │  ├─ retry.py
│  │        │  │  │  ├─ stop.py
│  │        │  │  │  ├─ tornadoweb.py
│  │        │  │  │  └─ wait.py
│  │        │  │  ├─ tomli
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _parser.py
│  │        │  │  │  ├─ _re.py
│  │        │  │  │  └─ _types.py
│  │        │  │  ├─ typing_extensions.py
│  │        │  │  ├─ urllib3
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _collections.py
│  │        │  │  │  ├─ _version.py
│  │        │  │  │  ├─ connection.py
│  │        │  │  │  ├─ connectionpool.py
│  │        │  │  │  ├─ contrib
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ _appengine_environ.py
│  │        │  │  │  │  ├─ _securetransport
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  ├─ bindings.py
│  │        │  │  │  │  │  └─ low_level.py
│  │        │  │  │  │  ├─ appengine.py
│  │        │  │  │  │  ├─ ntlmpool.py
│  │        │  │  │  │  ├─ pyopenssl.py
│  │        │  │  │  │  ├─ securetransport.py
│  │        │  │  │  │  └─ socks.py
│  │        │  │  │  ├─ exceptions.py
│  │        │  │  │  ├─ fields.py
│  │        │  │  │  ├─ filepost.py
│  │        │  │  │  ├─ packages
│  │        │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  ├─ backports
│  │        │  │  │  │  │  ├─ __init__.py
│  │        │  │  │  │  │  └─ makefile.py
│  │        │  │  │  │  └─ six.py
│  │        │  │  │  ├─ poolmanager.py
│  │        │  │  │  ├─ request.py
│  │        │  │  │  ├─ response.py
│  │        │  │  │  └─ util
│  │        │  │  │     ├─ __init__.py
│  │        │  │  │     ├─ connection.py
│  │        │  │  │     ├─ proxy.py
│  │        │  │  │     ├─ queue.py
│  │        │  │  │     ├─ request.py
│  │        │  │  │     ├─ response.py
│  │        │  │  │     ├─ retry.py
│  │        │  │  │     ├─ ssl_.py
│  │        │  │  │     ├─ ssl_match_hostname.py
│  │        │  │  │     ├─ ssltransport.py
│  │        │  │  │     ├─ timeout.py
│  │        │  │  │     ├─ url.py
│  │        │  │  │     └─ wait.py
│  │        │  │  ├─ vendor.txt
│  │        │  │  └─ webencodings
│  │        │  │     ├─ __init__.py
│  │        │  │     ├─ labels.py
│  │        │  │     ├─ mklabels.py
│  │        │  │     ├─ tests.py
│  │        │  │     └─ x_user_defined.py
│  │        │  └─ py.typed
│  │        ├─ pip-23.0.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE.txt
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        ├─ pkg_resources
│  │        │  ├─ __init__.py
│  │        │  ├─ _vendor
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ appdirs.py
│  │        │  │  ├─ packaging
│  │        │  │  │  ├─ __about__.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _compat.py
│  │        │  │  │  ├─ _structures.py
│  │        │  │  │  ├─ _typing.py
│  │        │  │  │  ├─ markers.py
│  │        │  │  │  ├─ requirements.py
│  │        │  │  │  ├─ specifiers.py
│  │        │  │  │  ├─ tags.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  └─ version.py
│  │        │  │  └─ pyparsing.py
│  │        │  ├─ extern
│  │        │  │  └─ __init__.py
│  │        │  └─ tests
│  │        │     └─ data
│  │        │        └─ my-test-package-source
│  │        │           └─ setup.py
│  │        ├─ pydantic
│  │        │  ├─ __init__.py
│  │        │  ├─ _internal
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _config.py
│  │        │  │  ├─ _core_metadata.py
│  │        │  │  ├─ _core_utils.py
│  │        │  │  ├─ _dataclasses.py
│  │        │  │  ├─ _decorators.py
│  │        │  │  ├─ _decorators_v1.py
│  │        │  │  ├─ _discriminated_union.py
│  │        │  │  ├─ _docs_extraction.py
│  │        │  │  ├─ _fields.py
│  │        │  │  ├─ _forward_ref.py
│  │        │  │  ├─ _generate_schema.py
│  │        │  │  ├─ _generics.py
│  │        │  │  ├─ _git.py
│  │        │  │  ├─ _import_utils.py
│  │        │  │  ├─ _internal_dataclass.py
│  │        │  │  ├─ _known_annotated_metadata.py
│  │        │  │  ├─ _mock_val_ser.py
│  │        │  │  ├─ _model_construction.py
│  │        │  │  ├─ _namespace_utils.py
│  │        │  │  ├─ _repr.py
│  │        │  │  ├─ _schema_gather.py
│  │        │  │  ├─ _schema_generation_shared.py
│  │        │  │  ├─ _serializers.py
│  │        │  │  ├─ _signature.py
│  │        │  │  ├─ _typing_extra.py
│  │        │  │  ├─ _utils.py
│  │        │  │  ├─ _validate_call.py
│  │        │  │  └─ _validators.py
│  │        │  ├─ _migration.py
│  │        │  ├─ alias_generators.py
│  │        │  ├─ aliases.py
│  │        │  ├─ annotated_handlers.py
│  │        │  ├─ class_validators.py
│  │        │  ├─ color.py
│  │        │  ├─ config.py
│  │        │  ├─ dataclasses.py
│  │        │  ├─ datetime_parse.py
│  │        │  ├─ decorator.py
│  │        │  ├─ deprecated
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ class_validators.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ copy_internals.py
│  │        │  │  ├─ decorator.py
│  │        │  │  ├─ json.py
│  │        │  │  ├─ parse.py
│  │        │  │  └─ tools.py
│  │        │  ├─ env_settings.py
│  │        │  ├─ error_wrappers.py
│  │        │  ├─ errors.py
│  │        │  ├─ experimental
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ arguments_schema.py
│  │        │  │  └─ pipeline.py
│  │        │  ├─ fields.py
│  │        │  ├─ functional_serializers.py
│  │        │  ├─ functional_validators.py
│  │        │  ├─ generics.py
│  │        │  ├─ json.py
│  │        │  ├─ json_schema.py
│  │        │  ├─ main.py
│  │        │  ├─ mypy.py
│  │        │  ├─ networks.py
│  │        │  ├─ parse.py
│  │        │  ├─ plugin
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _loader.py
│  │        │  │  └─ _schema_validator.py
│  │        │  ├─ py.typed
│  │        │  ├─ root_model.py
│  │        │  ├─ schema.py
│  │        │  ├─ tools.py
│  │        │  ├─ type_adapter.py
│  │        │  ├─ types.py
│  │        │  ├─ typing.py
│  │        │  ├─ utils.py
│  │        │  ├─ v1
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _hypothesis_plugin.py
│  │        │  │  ├─ annotated_types.py
│  │        │  │  ├─ class_validators.py
│  │        │  │  ├─ color.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ dataclasses.py
│  │        │  │  ├─ datetime_parse.py
│  │        │  │  ├─ decorator.py
│  │        │  │  ├─ env_settings.py
│  │        │  │  ├─ error_wrappers.py
│  │        │  │  ├─ errors.py
│  │        │  │  ├─ fields.py
│  │        │  │  ├─ generics.py
│  │        │  │  ├─ json.py
│  │        │  │  ├─ main.py
│  │        │  │  ├─ mypy.py
│  │        │  │  ├─ networks.py
│  │        │  │  ├─ parse.py
│  │        │  │  ├─ py.typed
│  │        │  │  ├─ schema.py
│  │        │  │  ├─ tools.py
│  │        │  │  ├─ types.py
│  │        │  │  ├─ typing.py
│  │        │  │  ├─ utils.py
│  │        │  │  ├─ validators.py
│  │        │  │  └─ version.py
│  │        │  ├─ validate_call_decorator.py
│  │        │  ├─ validators.py
│  │        │  ├─ version.py
│  │        │  └─ warnings.py
│  │        ├─ pydantic-2.11.5.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ pydantic_core
│  │        │  ├─ __init__.py
│  │        │  ├─ _pydantic_core.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ _pydantic_core.pyi
│  │        │  ├─ core_schema.py
│  │        │  └─ py.typed
│  │        ├─ pydantic_core-2.33.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ pymongo
│  │        │  ├─ __init__.py
│  │        │  ├─ _asyncio_lock.py
│  │        │  ├─ _asyncio_task.py
│  │        │  ├─ _azure_helpers.py
│  │        │  ├─ _client_bulk_shared.py
│  │        │  ├─ _cmessage.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ _cmessagemodule.c
│  │        │  ├─ _csot.py
│  │        │  ├─ _gcp_helpers.py
│  │        │  ├─ _version.py
│  │        │  ├─ asynchronous
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ aggregation.py
│  │        │  │  ├─ auth.py
│  │        │  │  ├─ auth_aws.py
│  │        │  │  ├─ auth_oidc.py
│  │        │  │  ├─ bulk.py
│  │        │  │  ├─ change_stream.py
│  │        │  │  ├─ client_bulk.py
│  │        │  │  ├─ client_session.py
│  │        │  │  ├─ collection.py
│  │        │  │  ├─ command_cursor.py
│  │        │  │  ├─ cursor.py
│  │        │  │  ├─ database.py
│  │        │  │  ├─ encryption.py
│  │        │  │  ├─ helpers.py
│  │        │  │  ├─ mongo_client.py
│  │        │  │  ├─ monitor.py
│  │        │  │  ├─ network.py
│  │        │  │  ├─ pool.py
│  │        │  │  ├─ server.py
│  │        │  │  ├─ settings.py
│  │        │  │  ├─ srv_resolver.py
│  │        │  │  ├─ topology.py
│  │        │  │  └─ uri_parser.py
│  │        │  ├─ auth.py
│  │        │  ├─ auth_oidc.py
│  │        │  ├─ auth_oidc_shared.py
│  │        │  ├─ auth_shared.py
│  │        │  ├─ bulk_shared.py
│  │        │  ├─ change_stream.py
│  │        │  ├─ client_options.py
│  │        │  ├─ client_session.py
│  │        │  ├─ collation.py
│  │        │  ├─ collection.py
│  │        │  ├─ command_cursor.py
│  │        │  ├─ common.py
│  │        │  ├─ compression_support.py
│  │        │  ├─ cursor.py
│  │        │  ├─ cursor_shared.py
│  │        │  ├─ daemon.py
│  │        │  ├─ database.py
│  │        │  ├─ database_shared.py
│  │        │  ├─ driver_info.py
│  │        │  ├─ encryption.py
│  │        │  ├─ encryption_options.py
│  │        │  ├─ errors.py
│  │        │  ├─ event_loggers.py
│  │        │  ├─ hello.py
│  │        │  ├─ helpers_shared.py
│  │        │  ├─ lock.py
│  │        │  ├─ logger.py
│  │        │  ├─ max_staleness_selectors.py
│  │        │  ├─ message.py
│  │        │  ├─ mongo_client.py
│  │        │  ├─ monitoring.py
│  │        │  ├─ network_layer.py
│  │        │  ├─ ocsp_cache.py
│  │        │  ├─ ocsp_support.py
│  │        │  ├─ operations.py
│  │        │  ├─ periodic_executor.py
│  │        │  ├─ pool.py
│  │        │  ├─ pool_options.py
│  │        │  ├─ pool_shared.py
│  │        │  ├─ py.typed
│  │        │  ├─ pyopenssl_context.py
│  │        │  ├─ read_concern.py
│  │        │  ├─ read_preferences.py
│  │        │  ├─ response.py
│  │        │  ├─ results.py
│  │        │  ├─ saslprep.py
│  │        │  ├─ server_api.py
│  │        │  ├─ server_description.py
│  │        │  ├─ server_selectors.py
│  │        │  ├─ server_type.py
│  │        │  ├─ socket_checker.py
│  │        │  ├─ ssl_context.py
│  │        │  ├─ ssl_support.py
│  │        │  ├─ synchronous
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ aggregation.py
│  │        │  │  ├─ auth.py
│  │        │  │  ├─ auth_aws.py
│  │        │  │  ├─ auth_oidc.py
│  │        │  │  ├─ bulk.py
│  │        │  │  ├─ change_stream.py
│  │        │  │  ├─ client_bulk.py
│  │        │  │  ├─ client_session.py
│  │        │  │  ├─ collection.py
│  │        │  │  ├─ command_cursor.py
│  │        │  │  ├─ cursor.py
│  │        │  │  ├─ database.py
│  │        │  │  ├─ encryption.py
│  │        │  │  ├─ helpers.py
│  │        │  │  ├─ mongo_client.py
│  │        │  │  ├─ monitor.py
│  │        │  │  ├─ network.py
│  │        │  │  ├─ pool.py
│  │        │  │  ├─ server.py
│  │        │  │  ├─ settings.py
│  │        │  │  ├─ srv_resolver.py
│  │        │  │  ├─ topology.py
│  │        │  │  └─ uri_parser.py
│  │        │  ├─ topology_description.py
│  │        │  ├─ typings.py
│  │        │  ├─ uri_parser.py
│  │        │  ├─ uri_parser_shared.py
│  │        │  └─ write_concern.py
│  │        ├─ pymongo-4.13.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ python_dotenv-1.1.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  ├─ licenses
│  │        │  │  └─ LICENSE
│  │        │  └─ top_level.txt
│  │        ├─ python_multipart
│  │        │  ├─ __init__.py
│  │        │  ├─ decoders.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ multipart.py
│  │        │  └─ py.typed
│  │        ├─ python_multipart-0.0.20.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE.txt
│  │        ├─ requests
│  │        │  ├─ __init__.py
│  │        │  ├─ __version__.py
│  │        │  ├─ _internal_utils.py
│  │        │  ├─ adapters.py
│  │        │  ├─ api.py
│  │        │  ├─ auth.py
│  │        │  ├─ certs.py
│  │        │  ├─ compat.py
│  │        │  ├─ cookies.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ help.py
│  │        │  ├─ hooks.py
│  │        │  ├─ models.py
│  │        │  ├─ packages.py
│  │        │  ├─ sessions.py
│  │        │  ├─ status_codes.py
│  │        │  ├─ structures.py
│  │        │  └─ utils.py
│  │        ├─ requests-2.32.3.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ top_level.txt
│  │        ├─ setuptools
│  │        │  ├─ __init__.py
│  │        │  ├─ _deprecation_warning.py
│  │        │  ├─ _distutils
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ _msvccompiler.py
│  │        │  │  ├─ archive_util.py
│  │        │  │  ├─ bcppcompiler.py
│  │        │  │  ├─ ccompiler.py
│  │        │  │  ├─ cmd.py
│  │        │  │  ├─ command
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ bdist.py
│  │        │  │  │  ├─ bdist_dumb.py
│  │        │  │  │  ├─ bdist_msi.py
│  │        │  │  │  ├─ bdist_rpm.py
│  │        │  │  │  ├─ bdist_wininst.py
│  │        │  │  │  ├─ build.py
│  │        │  │  │  ├─ build_clib.py
│  │        │  │  │  ├─ build_ext.py
│  │        │  │  │  ├─ build_py.py
│  │        │  │  │  ├─ build_scripts.py
│  │        │  │  │  ├─ check.py
│  │        │  │  │  ├─ clean.py
│  │        │  │  │  ├─ config.py
│  │        │  │  │  ├─ install.py
│  │        │  │  │  ├─ install_data.py
│  │        │  │  │  ├─ install_egg_info.py
│  │        │  │  │  ├─ install_headers.py
│  │        │  │  │  ├─ install_lib.py
│  │        │  │  │  ├─ install_scripts.py
│  │        │  │  │  ├─ py37compat.py
│  │        │  │  │  ├─ register.py
│  │        │  │  │  ├─ sdist.py
│  │        │  │  │  └─ upload.py
│  │        │  │  ├─ config.py
│  │        │  │  ├─ core.py
│  │        │  │  ├─ cygwinccompiler.py
│  │        │  │  ├─ debug.py
│  │        │  │  ├─ dep_util.py
│  │        │  │  ├─ dir_util.py
│  │        │  │  ├─ dist.py
│  │        │  │  ├─ errors.py
│  │        │  │  ├─ extension.py
│  │        │  │  ├─ fancy_getopt.py
│  │        │  │  ├─ file_util.py
│  │        │  │  ├─ filelist.py
│  │        │  │  ├─ log.py
│  │        │  │  ├─ msvc9compiler.py
│  │        │  │  ├─ msvccompiler.py
│  │        │  │  ├─ py35compat.py
│  │        │  │  ├─ py38compat.py
│  │        │  │  ├─ spawn.py
│  │        │  │  ├─ sysconfig.py
│  │        │  │  ├─ text_file.py
│  │        │  │  ├─ unixccompiler.py
│  │        │  │  ├─ util.py
│  │        │  │  ├─ version.py
│  │        │  │  └─ versionpredicate.py
│  │        │  ├─ _imp.py
│  │        │  ├─ _vendor
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ more_itertools
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ more.py
│  │        │  │  │  └─ recipes.py
│  │        │  │  ├─ ordered_set.py
│  │        │  │  ├─ packaging
│  │        │  │  │  ├─ __about__.py
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ _compat.py
│  │        │  │  │  ├─ _structures.py
│  │        │  │  │  ├─ _typing.py
│  │        │  │  │  ├─ markers.py
│  │        │  │  │  ├─ requirements.py
│  │        │  │  │  ├─ specifiers.py
│  │        │  │  │  ├─ tags.py
│  │        │  │  │  ├─ utils.py
│  │        │  │  │  └─ version.py
│  │        │  │  └─ pyparsing.py
│  │        │  ├─ archive_util.py
│  │        │  ├─ build_meta.py
│  │        │  ├─ cli-32.exe
│  │        │  ├─ cli-64.exe
│  │        │  ├─ cli.exe
│  │        │  ├─ command
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ alias.py
│  │        │  │  ├─ bdist_egg.py
│  │        │  │  ├─ bdist_rpm.py
│  │        │  │  ├─ build_clib.py
│  │        │  │  ├─ build_ext.py
│  │        │  │  ├─ build_py.py
│  │        │  │  ├─ develop.py
│  │        │  │  ├─ dist_info.py
│  │        │  │  ├─ easy_install.py
│  │        │  │  ├─ egg_info.py
│  │        │  │  ├─ install.py
│  │        │  │  ├─ install_egg_info.py
│  │        │  │  ├─ install_lib.py
│  │        │  │  ├─ install_scripts.py
│  │        │  │  ├─ launcher manifest.xml
│  │        │  │  ├─ py36compat.py
│  │        │  │  ├─ register.py
│  │        │  │  ├─ rotate.py
│  │        │  │  ├─ saveopts.py
│  │        │  │  ├─ sdist.py
│  │        │  │  ├─ setopt.py
│  │        │  │  ├─ test.py
│  │        │  │  ├─ upload.py
│  │        │  │  └─ upload_docs.py
│  │        │  ├─ config.py
│  │        │  ├─ dep_util.py
│  │        │  ├─ depends.py
│  │        │  ├─ dist.py
│  │        │  ├─ errors.py
│  │        │  ├─ extension.py
│  │        │  ├─ extern
│  │        │  │  └─ __init__.py
│  │        │  ├─ glob.py
│  │        │  ├─ gui-32.exe
│  │        │  ├─ gui-64.exe
│  │        │  ├─ gui.exe
│  │        │  ├─ installer.py
│  │        │  ├─ launch.py
│  │        │  ├─ monkey.py
│  │        │  ├─ msvc.py
│  │        │  ├─ namespaces.py
│  │        │  ├─ package_index.py
│  │        │  ├─ py34compat.py
│  │        │  ├─ sandbox.py
│  │        │  ├─ script (dev).tmpl
│  │        │  ├─ script.tmpl
│  │        │  ├─ unicode_utils.py
│  │        │  ├─ version.py
│  │        │  ├─ wheel.py
│  │        │  └─ windows_support.py
│  │        ├─ setuptools-58.1.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        ├─ sniffio
│  │        │  ├─ __init__.py
│  │        │  ├─ _impl.py
│  │        │  ├─ _tests
│  │        │  │  ├─ __init__.py
│  │        │  │  └─ test_sniffio.py
│  │        │  ├─ _version.py
│  │        │  └─ py.typed
│  │        ├─ sniffio-1.3.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ LICENSE.APACHE2
│  │        │  ├─ LICENSE.MIT
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ top_level.txt
│  │        ├─ starlette
│  │        │  ├─ __init__.py
│  │        │  ├─ _exception_handler.py
│  │        │  ├─ _utils.py
│  │        │  ├─ applications.py
│  │        │  ├─ authentication.py
│  │        │  ├─ background.py
│  │        │  ├─ concurrency.py
│  │        │  ├─ config.py
│  │        │  ├─ convertors.py
│  │        │  ├─ datastructures.py
│  │        │  ├─ endpoints.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ formparsers.py
│  │        │  ├─ middleware
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ authentication.py
│  │        │  │  ├─ base.py
│  │        │  │  ├─ cors.py
│  │        │  │  ├─ errors.py
│  │        │  │  ├─ exceptions.py
│  │        │  │  ├─ gzip.py
│  │        │  │  ├─ httpsredirect.py
│  │        │  │  ├─ sessions.py
│  │        │  │  ├─ trustedhost.py
│  │        │  │  └─ wsgi.py
│  │        │  ├─ py.typed
│  │        │  ├─ requests.py
│  │        │  ├─ responses.py
│  │        │  ├─ routing.py
│  │        │  ├─ schemas.py
│  │        │  ├─ staticfiles.py
│  │        │  ├─ status.py
│  │        │  ├─ templating.py
│  │        │  ├─ testclient.py
│  │        │  ├─ types.py
│  │        │  └─ websockets.py
│  │        ├─ starlette-0.46.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE.md
│  │        ├─ tqdm
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ _dist_ver.py
│  │        │  ├─ _main.py
│  │        │  ├─ _monitor.py
│  │        │  ├─ _tqdm.py
│  │        │  ├─ _tqdm_gui.py
│  │        │  ├─ _tqdm_notebook.py
│  │        │  ├─ _tqdm_pandas.py
│  │        │  ├─ _utils.py
│  │        │  ├─ asyncio.py
│  │        │  ├─ auto.py
│  │        │  ├─ autonotebook.py
│  │        │  ├─ cli.py
│  │        │  ├─ completion.sh
│  │        │  ├─ contrib
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ bells.py
│  │        │  │  ├─ concurrent.py
│  │        │  │  ├─ discord.py
│  │        │  │  ├─ itertools.py
│  │        │  │  ├─ logging.py
│  │        │  │  ├─ slack.py
│  │        │  │  ├─ telegram.py
│  │        │  │  └─ utils_worker.py
│  │        │  ├─ dask.py
│  │        │  ├─ gui.py
│  │        │  ├─ keras.py
│  │        │  ├─ notebook.py
│  │        │  ├─ rich.py
│  │        │  ├─ std.py
│  │        │  ├─ tk.py
│  │        │  ├─ tqdm.1
│  │        │  ├─ utils.py
│  │        │  └─ version.py
│  │        ├─ tqdm-4.67.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENCE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        ├─ typing_extensions-4.13.2.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ typing_extensions.py
│  │        ├─ typing_inspection
│  │        │  ├─ __init__.py
│  │        │  ├─ introspection.py
│  │        │  ├─ py.typed
│  │        │  ├─ typing_objects.py
│  │        │  └─ typing_objects.pyi
│  │        ├─ typing_inspection-0.4.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ urllib3
│  │        │  ├─ __init__.py
│  │        │  ├─ _base_connection.py
│  │        │  ├─ _collections.py
│  │        │  ├─ _request_methods.py
│  │        │  ├─ _version.py
│  │        │  ├─ connection.py
│  │        │  ├─ connectionpool.py
│  │        │  ├─ contrib
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ emscripten
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ connection.py
│  │        │  │  │  ├─ emscripten_fetch_worker.js
│  │        │  │  │  ├─ fetch.py
│  │        │  │  │  ├─ request.py
│  │        │  │  │  └─ response.py
│  │        │  │  ├─ pyopenssl.py
│  │        │  │  └─ socks.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ fields.py
│  │        │  ├─ filepost.py
│  │        │  ├─ http2
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ connection.py
│  │        │  │  └─ probe.py
│  │        │  ├─ poolmanager.py
│  │        │  ├─ py.typed
│  │        │  ├─ response.py
│  │        │  └─ util
│  │        │     ├─ __init__.py
│  │        │     ├─ connection.py
│  │        │     ├─ proxy.py
│  │        │     ├─ request.py
│  │        │     ├─ response.py
│  │        │     ├─ retry.py
│  │        │     ├─ ssl_.py
│  │        │     ├─ ssl_match_hostname.py
│  │        │     ├─ ssltransport.py
│  │        │     ├─ timeout.py
│  │        │     ├─ url.py
│  │        │     ├─ util.py
│  │        │     └─ wait.py
│  │        ├─ urllib3-2.4.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ licenses
│  │        │     └─ LICENSE.txt
│  │        ├─ uvicorn
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ _subprocess.py
│  │        │  ├─ _types.py
│  │        │  ├─ config.py
│  │        │  ├─ importer.py
│  │        │  ├─ lifespan
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ off.py
│  │        │  │  └─ on.py
│  │        │  ├─ logging.py
│  │        │  ├─ loops
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ asyncio.py
│  │        │  │  ├─ auto.py
│  │        │  │  └─ uvloop.py
│  │        │  ├─ main.py
│  │        │  ├─ middleware
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ asgi2.py
│  │        │  │  ├─ message_logger.py
│  │        │  │  ├─ proxy_headers.py
│  │        │  │  └─ wsgi.py
│  │        │  ├─ protocols
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ http
│  │        │  │  │  ├─ __init__.py
│  │        │  │  │  ├─ auto.py
│  │        │  │  │  ├─ flow_control.py
│  │        │  │  │  ├─ h11_impl.py
│  │        │  │  │  └─ httptools_impl.py
│  │        │  │  ├─ utils.py
│  │        │  │  └─ websockets
│  │        │  │     ├─ __init__.py
│  │        │  │     ├─ auto.py
│  │        │  │     ├─ websockets_impl.py
│  │        │  │     └─ wsproto_impl.py
│  │        │  ├─ py.typed
│  │        │  ├─ server.py
│  │        │  ├─ supervisors
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ basereload.py
│  │        │  │  ├─ multiprocess.py
│  │        │  │  ├─ statreload.py
│  │        │  │  └─ watchfilesreload.py
│  │        │  └─ workers.py
│  │        ├─ uvicorn-0.34.3.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ REQUESTED
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ licenses
│  │        │     └─ LICENSE.md
│  │        ├─ uvloop
│  │        │  ├─ __init__.py
│  │        │  ├─ _noop.py
│  │        │  ├─ _testbase.py
│  │        │  ├─ _version.py
│  │        │  ├─ cbhandles.pxd
│  │        │  ├─ cbhandles.pyx
│  │        │  ├─ dns.pyx
│  │        │  ├─ errors.pyx
│  │        │  ├─ handles
│  │        │  │  ├─ async_.pxd
│  │        │  │  ├─ async_.pyx
│  │        │  │  ├─ basetransport.pxd
│  │        │  │  ├─ basetransport.pyx
│  │        │  │  ├─ check.pxd
│  │        │  │  ├─ check.pyx
│  │        │  │  ├─ fsevent.pxd
│  │        │  │  ├─ fsevent.pyx
│  │        │  │  ├─ handle.pxd
│  │        │  │  ├─ handle.pyx
│  │        │  │  ├─ idle.pxd
│  │        │  │  ├─ idle.pyx
│  │        │  │  ├─ pipe.pxd
│  │        │  │  ├─ pipe.pyx
│  │        │  │  ├─ poll.pxd
│  │        │  │  ├─ poll.pyx
│  │        │  │  ├─ process.pxd
│  │        │  │  ├─ process.pyx
│  │        │  │  ├─ stream.pxd
│  │        │  │  ├─ stream.pyx
│  │        │  │  ├─ streamserver.pxd
│  │        │  │  ├─ streamserver.pyx
│  │        │  │  ├─ tcp.pxd
│  │        │  │  ├─ tcp.pyx
│  │        │  │  ├─ timer.pxd
│  │        │  │  ├─ timer.pyx
│  │        │  │  ├─ udp.pxd
│  │        │  │  └─ udp.pyx
│  │        │  ├─ includes
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ consts.pxi
│  │        │  │  ├─ debug.pxd
│  │        │  │  ├─ flowcontrol.pxd
│  │        │  │  ├─ python.pxd
│  │        │  │  ├─ stdlib.pxi
│  │        │  │  ├─ system.pxd
│  │        │  │  └─ uv.pxd
│  │        │  ├─ loop.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ loop.pxd
│  │        │  ├─ loop.pyi
│  │        │  ├─ loop.pyx
│  │        │  ├─ lru.pyx
│  │        │  ├─ pseudosock.pyx
│  │        │  ├─ py.typed
│  │        │  ├─ request.pxd
│  │        │  ├─ request.pyx
│  │        │  ├─ server.pxd
│  │        │  ├─ server.pyx
│  │        │  ├─ sslproto.pxd
│  │        │  └─ sslproto.pyx
│  │        ├─ uvloop-0.21.0.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE-APACHE
│  │        │  ├─ LICENSE-MIT
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  └─ top_level.txt
│  │        ├─ watchfiles
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ _rust_notify.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ _rust_notify.pyi
│  │        │  ├─ cli.py
│  │        │  ├─ filters.py
│  │        │  ├─ main.py
│  │        │  ├─ py.typed
│  │        │  ├─ run.py
│  │        │  └─ version.py
│  │        ├─ watchfiles-1.0.5.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ licenses
│  │        │     └─ LICENSE
│  │        ├─ websockets
│  │        │  ├─ __init__.py
│  │        │  ├─ __main__.py
│  │        │  ├─ asyncio
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ async_timeout.py
│  │        │  │  ├─ client.py
│  │        │  │  ├─ compatibility.py
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ messages.py
│  │        │  │  ├─ router.py
│  │        │  │  └─ server.py
│  │        │  ├─ auth.py
│  │        │  ├─ cli.py
│  │        │  ├─ client.py
│  │        │  ├─ connection.py
│  │        │  ├─ datastructures.py
│  │        │  ├─ exceptions.py
│  │        │  ├─ extensions
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ base.py
│  │        │  │  └─ permessage_deflate.py
│  │        │  ├─ frames.py
│  │        │  ├─ headers.py
│  │        │  ├─ http.py
│  │        │  ├─ http11.py
│  │        │  ├─ imports.py
│  │        │  ├─ legacy
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ auth.py
│  │        │  │  ├─ client.py
│  │        │  │  ├─ exceptions.py
│  │        │  │  ├─ framing.py
│  │        │  │  ├─ handshake.py
│  │        │  │  ├─ http.py
│  │        │  │  ├─ protocol.py
│  │        │  │  └─ server.py
│  │        │  ├─ protocol.py
│  │        │  ├─ py.typed
│  │        │  ├─ server.py
│  │        │  ├─ speedups.c
│  │        │  ├─ speedups.cpython-39-x86_64-linux-gnu.so
│  │        │  ├─ speedups.pyi
│  │        │  ├─ streams.py
│  │        │  ├─ sync
│  │        │  │  ├─ __init__.py
│  │        │  │  ├─ client.py
│  │        │  │  ├─ connection.py
│  │        │  │  ├─ messages.py
│  │        │  │  ├─ router.py
│  │        │  │  ├─ server.py
│  │        │  │  └─ utils.py
│  │        │  ├─ typing.py
│  │        │  ├─ uri.py
│  │        │  ├─ utils.py
│  │        │  └─ version.py
│  │        ├─ websockets-15.0.1.dist-info
│  │        │  ├─ INSTALLER
│  │        │  ├─ LICENSE
│  │        │  ├─ METADATA
│  │        │  ├─ RECORD
│  │        │  ├─ WHEEL
│  │        │  ├─ entry_points.txt
│  │        │  └─ top_level.txt
│  │        └─ yaml
│  │           ├─ __init__.py
│  │           ├─ _yaml.cpython-39-x86_64-linux-gnu.so
│  │           ├─ composer.py
│  │           ├─ constructor.py
│  │           ├─ cyaml.py
│  │           ├─ dumper.py
│  │           ├─ emitter.py
│  │           ├─ error.py
│  │           ├─ events.py
│  │           ├─ loader.py
│  │           ├─ nodes.py
│  │           ├─ parser.py
│  │           ├─ reader.py
│  │           ├─ representer.py
│  │           ├─ resolver.py
│  │           ├─ scanner.py
│  │           ├─ serializer.py
│  │           └─ tokens.py
│  └─ pyvenv.cfg
├─ Dockerfile
├─ README.md
├─ docker-compose.yml
├─ docker_bridge.py
├─ frames
├─ input
├─ main.py
├─ models
│  └─ models.py
├─ requirements.txt
└─ routers
   ├─ __init__.py
   └─ endpoints.py

```