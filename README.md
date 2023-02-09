# My Personal Site

## Local Setup

```bash
./setup.sh
echo sabar_me > .python-version
./run.sh
```

### Docker

```bash
docker build . -t sabar_me
docker run -p 5000:5000 -d sabar_me
```
