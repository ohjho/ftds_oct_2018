chapter_counts = { noun:[] for noun in [*people,*places] }

for chapter in chapters:
    counts = count_words(chapter)
    for noun in chapter_counts.keys():
        chapter_counts[noun].append(counts.get(noun,0))