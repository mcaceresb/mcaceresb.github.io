""" Build index from directory listing

make_index.py </path/to/directory> [--header <header text>]
"""

from datetime import datetime
import argparse
import os

INDEX_TEMPLATE = r"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<HTML>
  <HEAD>
    <TITLE>Index of /{0}</TITLE>
    <style type="text/css">
    <!--
    .name, .mtime {{ text-align: left; }}
    .size {{ text-align: right; }}
    td {{ text-overflow: ellipsis; white-space: nowrap; overflow: hidden; }}
    table {{ border-collapse: collapse; }}
    tr th {{ border-bottom: 2px groove; }}
    //-->
    </style>
  </HEAD>
  <BODY>
    <H1>Index of /{0}</H1>
<TABLE width="100%"><THEAD><TR>
<TH class="name"><A HREF="?N=D">Name</A></TH><TH class="mtime"><A HREF="?M=D">Last modified</A></TH><TH class="size"><A HREF="?S=D">Size</A></TH>
</TR></THEAD>
<TBODY>
{1}
</TBODY></TABLE><HR>
  </BODY>
</HTML>
"""

EXCLUDED = ['index.html']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--header")
    args = parser.parse_args()
    fnames   = [fname for fname in sorted(os.listdir(args.directory)) if fname not in EXCLUDED]
    # header   = (args.header if args.header else os.path.basename(args.directory))
    template = '<TR><TD class="name"><A HREF="{0}">{0}</A></TD><TD class="mtime">{1}</TD><TD class="size">{2:.1f}KiB</TD></TR>'
    table    = []
    for f in fnames:
        lastTime = datetime.fromtimestamp(os.path.getmtime(os.path.join(args.directory, f))).strftime('%Y-%m-%d %H:%M:%S')
        fileSize = os.path.getsize(os.path.join(args.directory, f)) / 1024.0
        table += [template.format(f, lastTime, fileSize)]

    with open(os.path.join(args.directory, "index.html"), "w+") as outFile:
        outFile.write(INDEX_TEMPLATE.format(args.directory, os.linesep.join(table)))


if __name__ == '__main__':
    main()
