import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
