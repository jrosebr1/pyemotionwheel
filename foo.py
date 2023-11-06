from pyemotionwheel import EmotionWheel

emo_wheel = EmotionWheel()

# path from node back to root
for emotion in emo_wheel.tertiary_emotions():
    for node in emotion.path[::-1]:
        #print(node)
        pass
    break

for emotion in emo_wheel.secondary_emotions():
    children = [str(c) for c in emotion.children]
    print("{} => {}" .format(emotion, ", ".join(children)))
    break
