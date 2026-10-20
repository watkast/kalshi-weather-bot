# Range-Scalp Bot

*Updated Tue Oct 20 11:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25589 | 22282 | 3307 (31) | 0 | $-7489.10 | -4.6% |
| **+10¢** | 19256 | 15437 | 3819 (46) | 0 | $-6625.40 | -5.5% |
| **+15¢** | 16116 | 12003 | 4113 (70) | 0 | $-5949.10 | -5.9% |
| **+20¢** | 14254 | 9950 | 4304 (88) | 0 | $-5306.38 | -5.9% |
| **+10¢ (15¢ stop)** | 31401 | 31348 | 53 (30) | 0 | $-11594.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 11:45 | +10 stop | BNB | DOWN | 0.69 | 0.82 | 1.04 |
| 10-20 11:45 | +20 | BNB | DOWN | 0.69 | 0.89 | 1.78 |
| 10-20 11:45 | +15 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 10-20 11:45 | +10 | BNB | DOWN | 0.69 | 0.82 | 1.04 |
| 10-20 11:45 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.42 |
| 10-20 11:45 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-20 11:45 | +20 | ZEC | DOWN | 0.70 | 0.93 | 2.10 |
| 10-20 11:45 | +15 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 10-20 11:45 | +10 | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-20 11:45 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
| 10-20 11:45 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 10-20 11:45 | +20 | XRP | DOWN | 0.69 | 0.90 | 1.90 |
| 10-20 11:45 | +15 | XRP | DOWN | 0.69 | 0.87 | 1.57 |
| 10-20 11:45 | +10 | XRP | DOWN | 0.67 | 0.81 | 1.13 |
| 10-20 11:45 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 10-20 11:37 | +10 stop | BTC | DOWN | 0.49 | 0.34 | -1.84 |
| 10-20 11:37 | +10 stop | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-20 11:37 | +5 | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-20 11:37 | +10 stop | HYPE | DOWN | 0.60 | 0.39 | -2.44 |
| 10-20 11:36 | +10 stop | BNB | UP | 0.60 | 0.83 | 2.03 |
| 10-20 11:36 | +5 | BNB | UP | 0.59 | 0.65 | 0.27 |
| 10-20 11:36 | +10 stop | XRP | UP | 0.49 | 0.60 | 0.75 |
| 10-20 11:36 | +10 stop | HYPE | UP | 0.61 | 0.45 | -1.95 |
| 10-20 11:34 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.28 |
| 10-20 11:34 | +10 stop | BNB | UP | 0.53 | 0.64 | 0.75 |
| 10-20 11:34 | +10 stop | DOGE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-20 11:34 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.25 |
| 10-20 11:33 | +10 stop | BNB | DOWN | 0.45 | 0.58 | 0.94 |
| 10-20 11:33 | +10 stop | ETH | DOWN | 0.63 | 0.79 | 1.31 |
| 10-20 11:33 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-20 11:33 | +5 | DOGE | UP | 0.47 | 0.61 | 1.02 |
| 10-20 11:32 | +5 | BNB | UP | 0.55 | 0.64 | 0.55 |
| 10-20 11:32 | +10 stop | HYPE | DOWN | 0.65 | 0.47 | -2.14 |
| 10-20 11:32 | +20 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 10-20 11:32 | +15 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 10-20 11:32 | +10 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 10-20 11:32 | +5 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 10-20 11:32 | +5 | NEAR | UP | 0.65 | 0.79 | 1.12 |
| 10-20 11:31 | +10 stop | ETH | UP | 0.69 | 0.53 | -1.93 |
| 10-20 11:31 | +20 | ETH | UP | 0.69 | 0.90 | 1.89 |
