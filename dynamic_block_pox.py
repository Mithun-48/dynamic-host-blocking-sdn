from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

packet_count = {}
THRESHOLD = 10

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet.parsed:
        return

    ip_packet = packet.find('ipv4')

    if ip_packet:
        src_ip = ip_packet.srcip

        # Count packets
        packet_count[src_ip] = packet_count.get(src_ip, 0) + 1
        log.info(f"{src_ip} -> Count: {packet_count[src_ip]}")

        # Block only h3 (10.0.0.3)
        if str(src_ip) == "10.0.0.3" and packet_count[src_ip] > THRESHOLD:
            log.warning(f"🚫 Blocking {src_ip}")

            msg = of.ofp_flow_mod()
            msg.match.dl_type = 0x0800
            msg.match.nw_src = src_ip
            msg.priority = 100
            event.connection.send(msg)
            return

    # Normal forwarding
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    log.info("🔥 Dynamic Blocking Controller Started")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

