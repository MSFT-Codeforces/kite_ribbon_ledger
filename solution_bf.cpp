#include <iostream>
#include <cstdint>

using namespace std;

static long long solveOneCase(long long n, long long c, long long d, long long p) {
    // If n is odd, 2A + 4B can never equal n.
    if (n % 2 != 0) {
        return -1;
    }

    long long best = -1;

    // Enumerate all possible B that are multiples of d.
    // B can be at most n/4 because each QuadTail uses 4 ribbons.
    long long maxB = n / 4;

    for (long long b = 0; b <= maxB; b += d) {
        // Compute A from 2A + 4B = n  =>  A = (n - 4B) / 2
        __int128 rem = (__int128)n - (__int128)4 * (__int128)b;
        if (rem < 0) {
            continue;
        }
        if (rem % 2 != 0) {
            continue;
        }

        long long a = (long long)(rem / 2);

        // A must be a multiple of c. B is already a multiple of d by construction.
        if (a % c != 0) {
            continue;
        }

        // Check (A + B) divisible by p.
        __int128 total = (__int128)a + (__int128)b;
        if (total % p != 0) {
            continue;
        }

        long long totalLl = (long long)total; // Safe: total <= n/2.
        if (best == -1 || totalLl < best) {
            best = totalLl;
        }
    }

    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        long long n, c, d, p;
        cin >> n >> c >> d >> p;
        cout << solveOneCase(n, c, d, p) << "\n";
    }

    return 0;
}