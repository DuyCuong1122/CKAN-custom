# Huong Dan Setup CKAN Local Tu Clone Source Den Khi Su Dung Duoc Tren Web

Tai lieu nay mo ta cac buoc thuc te cho repo hien tai, tu luc clone source code den khi co the dang nhap va thao tac duoc tren giao dien web local.

## 1. Yeu Cau Moi Truong

Can cai san:

- `git`
- `docker`
- `docker compose`

Kiem tra nhanh:

```bash
git --version
docker --version
docker compose version
```

## 2. Clone Source Code

```bash
git clone <repo-url>
cd ckan
```

Neu da co source san thi chi can vao dung thu muc goc:

```bash
cd /duong-dan-toi/ckan
```

## 3. Khoi Dong Cac Service Phu Tro

Repo nay dung `docker compose` trong thu muc `test-infrastructure` de chay:

- PostgreSQL
- Redis
- Solr
- container `ckan`

Chay:

```bash
cd test-infrastructure
docker compose up -d
```

Kiem tra container:

```bash
docker compose ps
```

## 4. Luu Y Quan Trong Ve Container CKAN

Trong repo nay, service `ckan` trong `test-infrastructure/docker-compose.yml` khong tu dong chay web server. No dang duoc cau hinh giu container song bang lenh:

```bash
tail -f /etc/debian_version
```

Vi vay, sau khi `docker compose up -d`, ban phai tu chay CKAN web server ben trong container.

## 5. Cai Dat Python Package Trong Container

Lan dau chay source moi clone, nen cai package cua repo vao container:

```bash
docker compose exec ckan bash -lc 'cd /usr/src && pip install -e .'
```

Neu can them package phuc vu dev/test:

```bash
docker compose exec ckan bash -lc 'cd /usr/src && pip install -r dev-requirements.txt'
```

## 6. Cau Hinh Dang Duoc Dung

Moi truong local hien tai dang dung file:

```text
test-core-ci.ini
```

Mot so gia tri quan trong:

- `ckan.site_url = http://localhost:5000`
- `ckan.plugins = dataset_quality`
- Postgres, Redis, Solr tro vao cac service docker noi bo

## 7. Khoi Tao Database Neu Can

Neu la moi truong moi hoan toan, hay chay:

```bash
docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini db init'
```

Neu repo/DB da tung duoc khoi tao truoc do, lenh nay co the khong can chay lai.

## 8. Chay CKAN Web Server

Chay web server trong container `ckan`:

```bash
docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini run -H 0.0.0.0 -p 5000'
```

Giai thich:

- CKAN chay trong container o port `5000`
- Docker map ra may host thanh `5000`
- Vi vay URL local dung de truy cap la:

```text
http://localhost:5000
```

## 9. Tao Tai Khoan Dang Nhap

Neu chua co user admin, tao user:

```bash
docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini user add admin email=admin@example.com password=pass1234 fullname="Admin User"'
```

Cap quyen sysadmin:

```bash
docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini sysadmin add admin'
```

## 10. Truy Cap Giao Dien Web

Mo trinh duyet:

```text
http://localhost:5000
```

Dang nhap tai:

```text
http://localhost:5000/user/login
```

Thong tin mac dinh neu dung lenh tao o tren:

- Username: `admin`
- Password: `pass1234`

## 11. Kiem Tra Da Thao Tac Duoc Tren Web Chua

Sau khi dang nhap thanh cong, co the kiem tra nhanh:

1. Vao trang danh sach dataset:

```text
http://localhost:5000/dataset
```

2. Thu tao dataset moi bang nut `Add Dataset`

3. Neu plugin `dataset_quality` dang bat, kiem tra them:

```text
http://localhost:5000/dataset/quality-report
```

## 12. Cac Lenh Thuong Dung

Dung va xoa toan bo container:

```bash
cd test-infrastructure
docker compose down
```

Khoi dong lai:

```bash
cd test-infrastructure
docker compose up -d
```

Xem log service:

```bash
cd test-infrastructure
docker compose logs -f ckan
docker compose logs -f ckan-postgres
docker compose logs -f ckan-solr
docker compose logs -f ckan-redis
```

Vao shell trong container:

```bash
cd test-infrastructure
docker compose exec ckan bash
```

## 13. Loi Thuong Gap

### 1. Mo `localhost:5000` khong len

Nguyen nhan thuong gap:

- chua chay `docker compose up -d`
- chua chay web server CKAN trong container
- service Postgres / Solr / Redis chua san sang

Kiem tra:

```bash
cd test-infrastructure
docker compose ps
docker compose logs -f
```

### 2. Dang nhap xong bi redirect sai domain

Can dam bao trong `test-core-ci.ini` co:

```ini
ckan.site_url = http://localhost:5000
```

### 3. Da tao user nhung khong dang nhap duoc

Thu tao lai user va cap lai quyen sysadmin:

```bash
docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini user add admin email=admin@example.com password=pass1234 fullname="Admin User"'
docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini sysadmin add admin'
```

### 4. Sua code xong ma web khong thay doi

Hay restart lai process CKAN dang chay trong container.

Neu dang chay bang lenh:

```bash
ckan -c test-core-ci.ini run -H 0.0.0.0 -p 5000
```

thi dung no va chay lai.

## 14. Quy Trinh Nhanh Nhat

Neu muon di tu clone den web nhanh nhat, co the dung checklist sau:

```bash
git clone <repo-url>
cd ckan/test-infrastructure
docker compose up -d
docker compose exec ckan bash -lc 'cd /usr/src && pip install -e .'
docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini db init'
docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini user add admin email=admin@example.com password=pass1234 fullname="Admin User"'
docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini sysadmin add admin'
docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini run -H 0.0.0.0 -p 5000'
```

Sau do mo:

```text
http://localhost:5000
```

## 15. Ghi Chu Cho Repo Nay

- Port truy cap web tren may local la `5000`
- `test-infrastructure/docker-compose.yml` chi giu container `ckan` song, khong tu dong start web
- File config local dang dung la `test-core-ci.ini`
- Plugin hien dang bat trong local config la `dataset_quality`
