from prometheus_client import start_http_server, Counter, Gauge, Histogram
import random
import time

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency'
)

ACTIVE_USERS = Gauge(
    'active_users',
    'Number of active users'
)

def simulate_traffic():
    while True:
        REQUEST_COUNT.labels(method='GET', status='200').inc(random.randint(1, 5))
        REQUEST_COUNT.labels(method='POST', status='200').inc(random.randint(0, 2))
        REQUEST_COUNT.labels(method='GET', status='404').inc(random.randint(0, 1))

        with REQUEST_LATENCY.time():
            time.sleep(random.uniform(0.1, 0.5))

        ACTIVE_USERS.set(random.randint(10, 100))

        time.sleep(1)

if __name__ == '__main__':
    start_http_server(8080)
    print("Metrics server started on port 8080")
    simulate_traffic()
