// app/api/metrics/route.ts
import {NextResponse} from "next/server";
import {Registry, collectDefaultMetrics, Counter, Histogram} from "prom-client";

// Initialize the Prometheus Registry
const registry = new Registry();

// Collect default system metrics like memory, CPU usage, and garbage collection
collectDefaultMetrics({register: registry});

// HTTP request count metric
const httpRequestCount = new Counter({
  name: "http_requests_total",
  help: "Total number of HTTP requests made",
  labelNames: ["method", "status"],
});

// HTTP request duration histogram
const httpRequestDuration = new Histogram({
  name: "http_request_duration_seconds",
  help: "Histogram of HTTP request durations in seconds",
  labelNames: ["method", "status"],
  buckets: [0.1, 0.3, 0.5, 1, 2, 5], // Specify the buckets for request durations
});

// Add metrics to registry
registry.registerMetric(httpRequestCount);
registry.registerMetric(httpRequestDuration);

// Track request durations and counts for each incoming request
export async function GET() {
  // You can increment and record metrics on every request in your app
  httpRequestCount.inc({method: "GET", status: "200"});

  // Record the request duration
  const end = httpRequestDuration.startTimer();
  end({method: "GET", status: "200"});

  // Return the metrics in Prometheus format
  return NextResponse.json(await registry.metrics(), {
    headers: {"Content-Type": registry.contentType},
  });
}
