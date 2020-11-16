import nmap3
from constants import COMMON_MAIL_PORTS,MAIL_PROTOCOLS

NO_NMAP_INSTALLED = False

try:    
    nmap = nmap3.Nmap()
except:
    NO_NMAP_INSTALLED = True
    print("No Nmap Installed -> Please Install the Nmap engine to Enable this functionality")

def scan_mail_server_standard_ports(hostnames):

    """
       Given a List of Hostnames this function will use Nmap to Scan the Server and return the found standard ports  
    """

    if not NO_NMAP_INSTALLED:
            hostnames_with_ports = []
            print("Beginning Scans with Nmap")
            for hostname in hostnames:
                print(f"\t Scanning Host {hostname}")
                scan_results = nmap.nmap_version_detection(hostname,arg="-sV -Pn")
                open_ports_services = []
                for scan_result in scan_results:
                    if int(scan_result.get("port")) in COMMON_MAIL_PORTS or scan_result.get("service").get("name") in MAIL_PROTOCOLS:
                        open_ports_services.append({"port":int(scan_result.get("port")),"protocol":scan_result.get("service").get("name")})
                hostnames_with_ports.append({"hostname":hostname,"open_mail_ports":open_ports_services})    
            return hostnames_with_ports    
    else: 
        print("NMAP is not Installed")
        return {}

