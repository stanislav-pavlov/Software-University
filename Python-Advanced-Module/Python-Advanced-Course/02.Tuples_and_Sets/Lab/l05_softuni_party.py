N = int(input())
reservations_made = set()
guests_arrived = set()
VIP_absentees = set()
regular_absentees = set()

for _ in range(N):
    reservation_code = input()
    reservations_made.add(reservation_code)

attending = input()
while attending != "END":
    guests_arrived.add(attending)
    attending = input()

absentees = reservations_made - guests_arrived
for guest in absentees:
    if guest[0].isdigit():
        VIP_absentees.add(guest)
    else:
        regular_absentees.add(guest)

print(len(absentees))
for reservation in sorted(VIP_absentees):
    print(reservation)
for reservation in sorted(regular_absentees):
    print(reservation)