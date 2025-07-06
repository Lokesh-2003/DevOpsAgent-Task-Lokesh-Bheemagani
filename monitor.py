from prometheus_api_client import PrometheusConnect
import datetime

prom = PrometheusConnect(url="http://13.203.210.83:9100", disable_ssl=True)


def check_cpu_spike(threshold=80.0):
    query = '100 - (avg by(instance)(irate(node_cpu_seconds_total{mode="idle"}[2m])) * 100)'
    result = prom.custom_query(query)
    if result:
        value = float(result[0]['value'][1])
        if value > threshold:
            return True, value
    return False, 0.0
