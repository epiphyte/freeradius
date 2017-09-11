"""User with inheritance."""
import __config__
normal = __config__.Assignment()
normal.macs = ["001122334455"]
normal.password = "3657463861.3307820909|2702706688.2267165039|1859720229.986357834|1188223676.2354860831|965936788.1948144843|2913848686.1316052557|2466498395.95102647|3306101127.2402892941|4047649161.784657166|1948413968.2150633169|1855885807.2490076162|3131970261.3648664069|2050236555.3631678687|2289570300.6319459|3138096756.463515019|2636475272.2763257482"
normal.vlan = "dev"
normal.attrs = ["test=test"]
normal.port_bypass = ["001122221100"]
normal.wildcard = ["abc"]

admin = __config__.Assignment()
admin.inherits = normal
admin.vlan = "prod"
