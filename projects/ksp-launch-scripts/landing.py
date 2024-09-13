import krpc
import time
conn = krpc.connect(name='Sub-orbital flight')
vessel = conn.space_center.active_vessel

## Preparing for launch
vessel.auto_pilot.target_pitch_and_heading(90,90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
time.sleep(1)

#Liftoff
print("Launch in ...")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Liftoff")

vessel.control.activate_next_stage()

mean_altitude = conn.get_call(getattr, vessel.flight(), 'mean_altitude')
expr = conn.krpc.Expression.greater_than(
    conn.krpc.Expression.call(mean_altitude),
    conn.krpc.Expression.constant_double(300))
event = conn.krpc.add_event(expr)

with event.condition:
    event.wait()

vessel.control.throttle = 0.0

mean_altitude = conn.get_call(getattr, vessel.flight(), 'mean_altitude')
expr = conn.krpc.Expression.less_than(
    conn.krpc.Expression.call(mean_altitude),
    conn.krpc.Expression.constant_double(275))
event = conn.krpc.add_event(expr)

with event.condition:
    event.wait()
    
vessel.control.throttle = 100.0

mean_altitude = conn.get_call(getattr, vessel.flight(), 'mean_altitude')
expr = conn.krpc.Expression.less_than(
    conn.krpc.Expression.call(mean_altitude),
    conn.krpc.Expression.constant_double(60))
event = conn.krpc.add_event(expr)

with event.condition:
    event.wait()
    
vessel.control.throttle = 0.0