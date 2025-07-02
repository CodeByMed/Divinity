'''
from datetime import datetime
import psutil
import socket

def collect_system_info():
    """Collects system information such as CPU, memory, and disk usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    system_info = {
        'timestamp': datetime.now().isoformat(),
        'cpu_usage': cpu_usage,
        'memory_usage': memory_info.percent,
        'disk_usage': disk_info.percent,
        'total_memory': memory_info.total,
        'available_memory': memory_info.available,
        'total_disk': disk_info.total,
        'available_disk': disk_info.free
    }
    
    return system_info

def collect_network_info():
    """Collects network information such as IP address and active connections."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    connections = psutil.net_connections(kind='inet')

    network_info = {
        'hostname': hostname,
        'ip_address': ip_address,
        'active_connections': len(connections)
    }
    
    return network_info

def gather_data():
    """Gathers both system and network information."""
    system_info = collect_system_info()
    network_info = collect_network_info()
    
    return {
        'system_info': system_info,
        'network_info': network_info
    }
'''