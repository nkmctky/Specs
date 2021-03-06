{
  "name": "shell-vc707-riffa2-ap_fifo128-tcl",
  "type": "shell",
  "version": "0.1.1",
  "summary": "A hCODE shell based on RIFFA2.2.1 (VC707_Gen2x8If128) PCIe module.",
  "description": "RIFFA is original developed in http://riffa.ucsd.edu/. The hCODE version is developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "http://riffa.ucsd.edu/",
  "driver" : "riffa",
  "license": "MIT",
  "authors": {
    "Takuya Nakamichi": "nakamichi@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/nkmctky/shell-vc707-riffa2-ap_fifo128-tcl.git",
    "tag": "0.1.1"
  },
  "hardware": {
    "board": "vc707",
    "device": "xc7vx485tffg1761-2"
  },
  "interface": {
    "host": {
      "ap_fifo": {
        "data_width": 128 
       }
    }
  },
  "compatible_shell": {
    "shell-vc707-xillybus-ap_fifo128": "Shell driver not compatible."
  }
}
