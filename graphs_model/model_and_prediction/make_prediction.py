import pickle

model = pickle.load(open('cyber_model.pkl', 'rb'))

motive = int(input("Motive: 1 for Protest, -1 for Financial or 0 for undetermined: "))
actor_location = int(input("Actor Location: 1 for Russia, -1 for China or 0 for Other: "))
actor = int(input("Actor: 1 [rootkit, killnet or Moses Staff], -1 [BlueNorff, Lockbit Royal] or 0 for undetermined: "))
victim = int(input("Victim Type: 1 for Healthcare, -1 for Finance or 0 for Other: "))
result = model.predict([[motive, actor_location, actor, victim, 1, -1, 1, 1, 0]])
print(result[0])

if result[0] == 0:
    print("Mixed")
elif result[0] == 1:
    print("Exploitative")
else:
    print("Disruptive")