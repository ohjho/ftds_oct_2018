window_len = 30
avg = [ returns[i:i+window_len].mean() for i in range(len(returns) - window_len)]