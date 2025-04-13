import angr
import claripy

binary_path = '/home/kali/reveng/SimpleCrackme'
proj = angr.Project(binary_path, auto_load_libs=False)

key_len = 8

license_key = claripy.BVS("license_key", key_len * 8)

newline = claripy.BVV(b'\n')
input_data = claripy.Concat(license_key, newline)

state = proj.factory.full_init_state(stdin=input_data)

for i in range(key_len):
    c = license_key.get_byte(i)
    state.solver.add(c >= ord('A'))
    state.solver.add(c <= ord('Z'))

simgr = proj.factory.simgr(state)

def is_successful(state):
    return b"Access granted" in state.posix.dumps(1)

simgr.explore(find=is_successful)

if simgr.found:
    found = simgr.found[0]
    key = found.solver.eval(license_key, cast_to=bytes)
    print("✅ Valid License Key:", key.decode())
else:
    print("❌ No valid license key found.")
