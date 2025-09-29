Great — since the children are **5 and 3 years old**, here’s a **specific guide** to apply for **minor passports** for both of them in India.

---

## 🧒 Minor Passport Application – For Age 5 & 3

### ✅ **Type of Application**

* **Age**: 5 and 3 years
* **Application Type**: **Fresh Passport**
* **Validity**: Passport will be valid for **5 years or till the child turns 18**, whichever comes first.
* **Police Verification**: Usually **not required** if:

  * **Both parents have valid passports**
  * Names and details match exactly

---

## 📝 Step-by-Step Process

### 1. **Register and Login**

* Go to [https://www.passportindia.gov.in](https://www.passportindia.gov.in)
* Register using one parent’s details (if not already done)
* Login to the account

---

### 2. **Fill Application Form**

* Choose **Apply for Fresh Passport**
* Select **Minor** as applicant type
* Fill in all details for each child separately
* Save and submit

---

### 3. **Pay the Fee & Book Appointment**

#### 💰 **Fee Details (Normal Scheme)**

| Age      | Pages    | Validity           | Fee              |
| -------- | -------- | ------------------ | ---------------- |
| Below 15 | 36 pages | 5 years / until 18 | ₹1,000 per child |

* Pay online via Net Banking, Debit/Credit Card, UPI, etc.
* Book an appointment at your nearest **Passport Seva Kendra (PSK)** or **Post Office PSK (POPSK)**

---

### 📄 **Documents Required (per child)**

> 🔹 Bring **originals + self-attested photocopies** (by either parent)

#### 1. **Date of Birth Proof** (any one)

* **Birth Certificate** (preferred)

#### 2. **Address Proof** (in parents' name, any one)

* Aadhaar Card
* Voter ID
* Electricity/Water bill
* Rent agreement (if applicable)

#### 3. **Parent(s) Passport Copy**

* If both parents have valid passports:

  * Submit **copies of front and back pages**
  * Originals must be shown at appointment

#### 4. **Annexure ‘D’ (Mandatory)**

* Declaration by parents affirming:

  * Relationship
  * Consent
  * Legal responsibility
* Download from here:
  👉 [Annexure D (PDF)](https://www.passportindia.gov.in/AppOnlineProject/pdf/AnnexureD.pdf)
* Print, fill, and **sign by both parents**

#### 5. **Photographs**

* Not needed if being taken at the PSK
* But carry **one passport-sized photo** (4.5 x 3.5 cm, white background), **especially for 3-year-old** (may be required)

---

### 🧾 On Appointment Day

* **Both parents and the child** must be present.
* Bring all **original documents** + **Annexure D**
* At PSK/POPSK:

  * Biometrics and photo will be taken
  * Documents verified

---

### 📬 After the Visit

* If no police verification is needed, passport is usually dispatched in **3–10 working days**
* Track status using your **Application Reference Number (ARN)**

---

### ✅ Checklist Summary for Each Child:

| Document                                       | Mandatory?               |
| ---------------------------------------------- | ------------------------ |
| Birth Certificate                              | ✅                        |
| Annexure D (signed by both parents)            | ✅                        |
| Aadhaar Card of parents                        | ✅                        |
| Passport copies of both parents (if available) | ✅                        |
| 1 Passport-size photo (4.5 x 3.5 cm)           | Optional but recommended |
| Originals of all documents                     | ✅                        |


Nhsrc#321n

#
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

This gives you a total count of block-level I/O ops (reads + writes). Run this query twice over a period (e.g. 60 seconds apart), then calculate the difference to get IOPS.
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

## 🔹 5. **Check Per-Segment Disk IOPS (via OS)**

Use `iostat` or `sar`:

```bash
iostat -dx 1
```

You’ll see IOPS per device under the `tps` column (transactions per second = IOPS).
Look at the tps column: transactions per second = IOPS

Or sum r/s (read per sec) and w/s (write per sec)
This gives you real-time disk-level IOPS per device.

---

## 📌 Tips

* IOPS includes both reads and writes.
* If you're using SSD-backed storage, IOPS matters a lot for performance.
* Consider using monitoring tools like:

  * **Grafana + Prometheus**
  * **Datadog**
  * **Percona Monitoring and Management (PMM)**
  * **Azure Monitor / Google Cloud Monitoring** for cloud DBs


