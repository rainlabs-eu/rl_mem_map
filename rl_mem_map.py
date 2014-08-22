#!/usr/bin/python
import bloat
import optparse
import sys
import subprocess
import os
import zipfile
import webbrowser


def call_nm(nm, source):
    '''
    :rtype: string
    '''
    nm_result = subprocess.Popen([nm, '-C', '-S', '-l', source], stdout=subprocess.PIPE, shell=True)
    (nm_output, _) = nm_result.communicate()
    nm_result.wait()
    return nm_output


def get_nm_output_as_file(nm, source):
    '''
    :rtype: file
    '''
    f_nm = open("tmp_nm.out", 'w')
    string_result = call_nm(nm, source)
    f_nm.write(string_result)
    f_nm.close()
    f_nm = open("tmp_nm.out", 'r')
    return f_nm


def make_output_files(str_json, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    bloat_json_path = os.path.join(output_directory, 'bloat.json')
    output_json = open(bloat_json_path, 'w')
    output_json.write(str_json)
    path_to_script_directory = os.path.dirname(os.path.realpath(__file__))
    path_to_zip = os.path.join(path_to_script_directory, 'bloat.zip')
    with zipfile.ZipFile(path_to_zip, 'r') as z:
        z.extractall(output_directory)


def check_args(parser, args):
    if len(args) != 2:
        parser.print_usage()
        sys.exit(1)

if __name__ == "__main__":
    usage = """%prog path/to/smth.exe path/to/output/directory [options]\n or \n
    %prog path/to/nm.out path/to/output/directory -n [options]
    \n\n nm output passed with -nm should from running a command
    like the following (note, can take a long time -- 30 minutes):
      nm -C -S -l /path/to/binary > nm.out"""
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('--strip-prefix', metavar='PATH', action='store',
                      help='strip PATH prefix from paths; e.g. /path/to/src/root')
    parser.add_option('--filter', action='store',
                      help='include only symbols/files matching FILTER')
    parser.add_option('--c++filt', action='store', metavar='PATH', dest='cppfilt',
                      default='c++filt', help="Path to c++filt, used to demangle "
                      "symbols that weren't handled by nm. Set to an invalid path "
                      "to disable.")
    parser.add_option('--nm-prefix', action='store', metavar='STRING', dest='nmprefix',
                  default='', help="Prefix to append while calling nm"
                  "eg: --nm-prefix=avs. results in calling avs.nm while processing file")
    parser.add_option('-n', action="store_true", dest="nm_input", default=False,
                      help="Use this if you want to pass nm output")
    parser.add_option('-b', action="store_true", dest="open_in_web_browser", default=False,
                      help="Use this if you want to open resulting file in web browser")
    opts, args = parser.parse_args()

    check_args(parser, args)
    if opts.nm_input:
        nm_out = args[0]
        nmfile = open(nm_out, 'r')
    else:
        nmfile = get_nm_output_as_file(opts.nmprefix + "nm", args[0])

    try:
        res = subprocess.check_output([opts.cppfilt, 'main'])
        if res.strip() != 'main':
            print >>sys.stderr, ("%s failed demangling, "
                                 "output won't be demangled." % opts.cppfilt)
            opts.cppfilt = None
    except:
        print >>sys.stderr, ("Could not find c++filt at %s, "
                             "output won't be demangled." % opts.cppfilt)
        opts.cppfilt = None
    bloat_json = bloat.dump_nm(nmfile, strip_prefix=opts.strip_prefix, cppfilt=opts.cppfilt)
    output_directory = args[1]
    make_output_files(bloat_json, output_directory)
    if opts.nm_input:
        os.remove("tmp_nm.out")
    if opts.open_in_web_browser:
        index_html_path = os.path.join(os.getcwd(), output_directory, "index.html")
        webbrowser.open()
