for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0: print('У вас нет новых сообщений')
    elif 11 < messages_count < 19:
        print('У вас', messages_count, 'новых сообщений')
    elif remainder == 1 and messages_count != 11 :
        print('У вас', messages_count, 'новое сообщение')
    elif 1 < remainder < 5 :
         print('У вас', messages_count, 'новых сообщения')
    else:
        print('У вас', messages_count, 'новых сообщений')