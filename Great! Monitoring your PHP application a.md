Great! Monitoring your PHP application and the Ubuntu server is key to ensure performance, availability, and quick issue detection. Here's a straightforward guide on how to set this up:

---

### 1. **Monitor the Ubuntu Server**

You want to monitor system metrics like CPU, memory, disk, network, and processes.

#### Tools to consider:

* **Prometheus + Node Exporter + Grafana**
  Prometheus scrapes metrics, Node Exporter collects Linux system metrics, and Grafana visualizes them.
* **Netdata**
  Easy to install and provides real-time monitoring with a beautiful web dashboard.
* **Nagios / Zabbix**
  More traditional monitoring solutions with alerting and extensive plugin support.

---

### 2. **Monitor the PHP Application**

Focus on metrics like response time, error rates, throughput, and resource usage.

#### Options:

* **Application Performance Monitoring (APM) tools** like:

  * **New Relic**
  * **Datadog**
  * **Elastic APM**
  * **AppDynamics**

These tools provide deep insights into your PHP app performance.

* **PHP built-in tools**:

  * **Xdebug** (for profiling in dev)
  * **Blackfire.io** (profiling and performance)
* **Custom logs + Monitoring**:

  * Ensure PHP errors are logged (`error_log`).
  * Use a log shipper (e.g., Filebeat) to send logs to ELK stack or Graylog.

---

### Step-by-step Basic Setup Example

#### Install Netdata (Server + App monitoring)

```bash
bash <(curl -Ss https://my-netdata.io/kickstart.sh)
```

* After install, access dashboard: `http://your-server-ip:19999`
* It shows CPU, memory, disk, network, processes, and even some app metrics.

---

#### Setup PHP Error Logging

1. Edit `php.ini` (location varies, e.g., `/etc/php/7.4/fpm/php.ini` or `/etc/php/7.4/apache2/php.ini`):

```ini
log_errors = On
error_log = /var/log/php_errors.log
```

2. Restart PHP service (e.g., `sudo systemctl restart php7.4-fpm` or `apache2`).

3. Monitor this log regularly or forward to a log management tool.

---

#### Install Node Exporter + Prometheus + Grafana (for advanced monitoring)

* **Node Exporter** collects server metrics.
* **Prometheus** collects & stores metrics.
* **Grafana** visualizes.

There are many tutorials on this, but here’s a quick start:

```bash
# Node Exporter install
wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz
tar xvfz node_exporter-1.6.1.linux-amd64.tar.gz
sudo cp node_exporter-1.6.1.linux-amd64/node_exporter /usr/local/bin/
sudo useradd -rs /bin/false node_exporter

# Create systemd service for node_exporter
sudo tee /etc/systemd/system/node_exporter.service <<EOF
[Unit]
Description=Node Exporter
After=network.target

[Service]
User=node_exporter
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=default.target
EOF

sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl enable node_exporter
```

Then set up Prometheus to scrape from node\_exporter and configure Grafana dashboards.

---

### Summary Recommendations

| Task                      | Tool / Method                                          |
| ------------------------- | ------------------------------------------------------ |
| Server metrics monitoring | Netdata or Prometheus + Node Exporter + Grafana        |
| PHP app performance       | New Relic / Datadog / Elastic APM / Custom logging     |
| Log aggregation           | ELK Stack (Elasticsearch, Logstash, Kibana) or Graylog |
| Alerting                  | Prometheus Alertmanager, or built-in alerts in APM     |

---



Absolutely! Here's a **complete deployment plan** to set up **Prometheus and Grafana** on your **Ubuntu server** for monitoring your **Laravel PHP application and system metrics**:

---

## 🚀 Deployment Plan: Prometheus + Grafana on Ubuntu

### 🔧 Step 1: Install Prometheus

Prometheus collects metrics from your Laravel app and system.

```bash
# Download Prometheus
wget https://github.com/prometheus/prometheus/releases/download/v2.47.0/prometheus-2.47.0.linux-amd64.tar.gz
tar xvfz prometheus-2.47.0.linux-amd64.tar.gz
cd prometheus-2.47.0.linux-amd64

# Move binaries
sudo cp prometheus /usr/local/bin/
sudo cp promtool /usr/local/bin/
```

Create a config file `prometheus.yml`:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'laravel-app'
    static_configs:
      - targets: ['localhost:9000']  # Laravel metrics endpoint

  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']  # Node Exporter for system metrics
```

---

### 📊 Step 2: Install Grafana

Grafana visualizes Prometheus data.

```bash
# Add Grafana repo
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

# Install Grafana
sudo apt-get update
sudo apt-get install grafana

# Start Grafana
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

Access Grafana at `http://your-server-ip:3000` (default login: `admin/admin`).

---

### 📈 Step 3: Expose Laravel Metrics

Use [`romanzipp/laravel-prometheus`](https://github.com/romanzipp/Laravel-Prometheus) to expose metrics:

```bash
composer require romanzipp/laravel-prometheus
```

- Add service provider and facade
- Create `/metrics` route
- Prometheus scrapes this endpoint

---

### 🖥️ Step 4: Monitor Server Metrics

Install **Node Exporter**:

```bash
wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz
tar xvfz node_exporter-1.6.1.linux-amd64.tar.gz
cd node_exporter-1.6.1.linux-amd64
./node_exporter
```

Add `localhost:9100` to Prometheus targets.

---

### 📊 Step 5: Create Dashboards in Grafana

- Add Prometheus as a data source (`http://localhost:9090`)
- Import dashboards (e.g., [Grafana dashboard ID 3662](https://grafana.com/grafana/dashboards/3662/) for Node Exporter)
- Build custom panels for:
  - Laravel response time, error rate, DB queries
  - CPU, memory, disk, network usage

---

### 🔔 Step 6: Set Up Alerts

Use **Grafana alert rules** or **Prometheus Alertmanager** to notify via:
- Email
- Slack
- Webhooks

---

### 🧠 Helpful Guides

- [NeevCloud’s Ubuntu setup guide](https://docs.neevcloud.com/neevcloud-guide/neevcloud-knowledgebase/set-up-grafana/install-grafana-and-prometheus-on-ubuntu-22.04)
- [DevOpsOfWorld’s full tutorial](https://devopsofworld.com/setting-up-grafana-with-prometheus-on-ubuntu-a-comprehensive-guide)

---

To check **database IOPS (Input/Output Operations Per Second)**, you need to monitor how many read and write operations your database is performing. The method depends on the type of database and environment you're using (e.g., AWS RDS, on-premises MySQL, PostgreSQL, SQL Server, etc.).

Here’s how to check IOPS in different scenarios:

---

## 🔹 1. **For AWS RDS / Aurora**

You can use **Amazon CloudWatch** to check IOPS:

### Steps:

1. Go to **AWS Console** → **CloudWatch**.
2. Navigate to **Metrics** → **RDS**.
3. Select your DB instance.
4. Check:

   * `ReadIOPS`
   * `WriteIOPS`

You can set a time range and view graphs or download the data.

---

## 🔹 2. **For MySQL / MariaDB (On-Prem or EC2)**

Use the `SHOW GLOBAL STATUS` command to calculate IOPS manually.

### Command:

```sql
SHOW GLOBAL STATUS LIKE 'Innodb_%ops';
```

Or more specifically:

```sql
SHOW GLOBAL STATUS WHERE Variable_name IN ('Innodb_data_reads', 'Innodb_data_writes');
```

To get IOPS:

1. Run the command twice, e.g., with a 60-second gap.
2. Subtract the first value from the second.
3. Divide by 60 to get IOPS.

Alternatively, use tools:

* `iostat -dx 1` (Linux tool)
* `mysqladmin extended-status`

---

## 🔹 3. **For PostgreSQL**

You can query the statistics views:

```sql
SELECT sum(blks_read + blks_written) AS total_iops
FROM pg_stat_database;
```

To get current IOPS:

1. Query the value now.
2. Wait for a minute.
3. Query again.
4. Subtract and divide by the time interval.

Also, monitor disk-level stats via `iostat`.

---

## 🔹 4. **For SQL Server**

Use Performance Monitor (PerfMon) or SQL DMV queries:

```sql
SELECT 
  [ReadIOPS] = SUM(num_of_reads),
  [WriteIOPS] = SUM(num_of_writes)
FROM sys.dm_io_virtual_file_stats(NULL, NULL);
```

Again, run this periodically and compute the difference over time.

---

## 🔹 5. **Linux Disk IOPS (General)**

Use `iostat` or `sar`:

```bash
iostat -dx 1
```

You’ll see IOPS per device under the `tps` column (transactions per second = IOPS).

---

## 📌 Tips

* IOPS includes both reads and writes.
* If you're using SSD-backed storage, IOPS matters a lot for performance.
* Consider using monitoring tools like:

  * **Grafana + Prometheus**
  * **Datadog**
  * **Percona Monitoring and Management (PMM)**
  * **Azure Monitor / Google Cloud Monitoring** for cloud DBs

---

