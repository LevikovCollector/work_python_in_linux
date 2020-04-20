import argparse
import  work_with_linux as wwl

parser = argparse.ArgumentParser(argument_default=None)
parser.add_argument('-ch_net_port', action='store_true', default=False)
parser.add_argument('-default_r', action='store_true', default=False)
parser.add_argument('-pr_info', action='store_true', default=False)
parser.add_argument('-all_proc', action='store_true', default=False)
parser.add_argument('-st_apache', action='store_true', default=False)
parser.add_argument('-net_port_st', action='store_true', default=False)
parser.add_argument('-p_ver', action='store', default=None)
parser.add_argument('-f_in_d', action='store', default=None)
parser.add_argument('-where', action='store_true', default=False)
parser.add_argument('-core', action='store_true', default=False)
parser.add_argument('-info', action='store_true', default=False)
parser.add_argument('-net_int', action='store_true', default=False)
args = parser.parse_args()

if args.ch_net_port:
    wwl.check_internet_port()
if args.default_r:
    wwl.default_route()
if args.pr_info:
    wwl.processor_info()
if args.all_proc:
    wwl.all_process()
if args.st_apache:
    wwl.apache_service_status()
if args.net_port_st:
    wwl.internet_ports_status()
if args.p_ver is not None:
    wwl.pack_version(args.p_ver)
if args.f_in_d is not None:
    wwl.files_in_dir(args.f_in_d)
if args.where:
    wwl.where_i_am()
if args.core:
    wwl.linux_core()
if args.info:
    wwl.linux_info()
if args.net_int:
    wwl.net_interface()