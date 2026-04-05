num = int(input())

for i in range(num):
    
    sh, sm, eh, em = map(int, input().split())
    start_time = (sh * 60) + sm
    end_time = (eh * 60) + em
    duration = end_time - start_time
    duration_hours = duration_in_minutes // 60
    duration_minutes = duration_in_minutes % 60
    print(duration_hours, duration_minutes)
