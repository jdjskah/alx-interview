def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x < 1:
        return None

    def sieve_of_eratosthenes(n):
        """Generate a list of prime numbers up to n using Sieve of Eratosthenes."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    def count_primes(primes, n):
        """Count the number of primes up to n."""
        return sum(primes[:n + 1])

    # Precompute primes up to the maximum value in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_counts = [count_primes(primes, i) for i in range(max_n + 1)]

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

