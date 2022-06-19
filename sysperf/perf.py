import json
import time
import psutil
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def getHomePage():
    return render_template('home.html')


@app.route('/sysinfo', methods=['GET'])
def getSysInfo():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    uptime = psutil.boot_time()
    disk = psutil.disk_usage('/')
    cpu_count = psutil.cpu_count()
    infos=[]
    infos.append(["Uptime (Hrs)", uptime/(1000*60*60)])
    infos.append(["CPU (Cores)", cpu_count])
    infos.append(["Total Memory (GB)", mem.total/(1024*1024*1024)])
    infos.append(["SWAP Memory (GB)", swap.total/(1024*1024*1024)])
    infos.append(["Disk (GB)", str(disk.total//(1024*1024*1024))+" ( "+str(disk.percent)+"% Used)"])
    return json.dumps(infos)


@app.route('/cpu', methods=['GET'])
def getCpu():
    s = time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime())
    perc = psutil.cpu_percent(interval=1)
    data = [s, perc]
    return json.dumps(data)


@app.route('/mem', methods=['GET'])
def getMem():
    s = time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime())
    mem = psutil.virtual_memory()
    data = [s, mem.percent]
    return json.dumps(data)


@app.route('/swap', methods=['GET'])
def getSwap():
    s = time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime())
    swap = psutil.swap_memory()
    data = [s, swap.percent]
    return json.dumps(data)


@app.route('/network', methods=['GET'])
def getNetwork():
    s = time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime())
    network = psutil.net_io_counters()
    data = [s, network.bytes_sent//(1024*1024),network.bytes_recv//(1024*1024)]
    return json.dumps(data)


@app.route('/disk', methods=['GET'])
def getDisk():
    s = time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime())
    disk = psutil.disk_io_counters()
    data = [s, disk.read_bytes//(1024*1024),disk.write_bytes//(1024*1024)]
    return json.dumps(data)


if __name__ == '__main__':
    app.run(port=4000, debug=True)
