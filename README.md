# Python Dependencies Audit

Offline check of simple `requirements.txt` entries for exact `==` version pins. Python 3.9+, standard library only.

```sh
python depsaudit.py requirements.txt
python -m unittest discover -s tests -v
```

The tool prints line numbers and categories without printing requirement contents, which can contain credentials. Exit status is 0 when all supported entries are exact pins, 1 for unpinned or unsupported lines, 2 for input errors. It does not install packages, access a registry, check hashes, resolve transitive dependencies, or identify vulnerabilities. Includes, options, direct URLs, editable installs, and multiline requirements must be reviewed manually. An exact version alone does not guarantee reproducibility or safety. The tool is not a complete PEP 508 parser.

## 中文

本工具离线检查简单的 Python requirements 文件，提示没有使用精确版本或无法识别的行。输出不包含依赖行的原始内容；它不会联网、安装软件或进行漏洞扫描。版本固定不代表安全，也不能保证完整的可复现构建。
