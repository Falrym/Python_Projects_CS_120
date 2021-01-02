def get_time(start_time, current_time):
    minutes = 2
    time_allowed = minutes * 60
    if current_time >= start_time + time_allowed:
        print("""
        SORRY, OUT OF TIME
        GAME OVER
        YOU LOSE""")
        os._exit(0)
    else:
        seconds_left = int(time_allowed -  (time.time() - start_time))
        minutes = seconds_left // 60
        seconds = seconds_left % 60
        print(f"Time remaining: {minutes:02}:{seconds:02}")