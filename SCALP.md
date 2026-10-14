# Range-Scalp Bot

*Updated Wed Oct 14 17:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16252 | 14073 | 2179 (28) | 0 | $-5178.84 | -5.1% |
| **+10¢** | 12291 | 9768 | 2523 (40) | 0 | $-4770.92 | -6.2% |
| **+15¢** | 10329 | 7622 | 2707 (59) | 0 | $-4274.01 | -6.6% |
| **+20¢** | 9189 | 6350 | 2839 (76) | 1 | $-3786.76 | -6.6% |
| **+10¢ (15¢ stop)** | 20028 | 19978 | 50 (29) | 0 | $-7738.07 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 17:05 | +10 stop | DOGE | DOWN | 0.55 | 0.76 | 1.79 |
| 10-14 17:05 | +20 | DOGE | DOWN | 0.55 | 0.76 | 1.79 |
| 10-14 17:05 | +15 | DOGE | DOWN | 0.55 | 0.76 | 1.79 |
| 10-14 17:05 | +10 | DOGE | DOWN | 0.55 | 0.76 | 1.79 |
| 10-14 17:05 | +5 | DOGE | DOWN | 0.55 | 0.62 | 0.35 |
| 10-14 17:01 | +10 stop | BTC | UP | 0.66 | 0.79 | 1.02 |
| 10-14 17:01 | +20 | BTC | UP | 0.66 | open |  |
| 10-14 17:01 | +15 | BTC | UP | 0.66 | 0.81 | 1.23 |
| 10-14 17:01 | +10 | BTC | UP | 0.66 | 0.79 | 1.02 |
| 10-14 17:01 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 10-14 16:59 | +10 stop | SOL | DOWN | 0.15 | 0.55 | 3.73 |
| 10-14 16:57 | +10 stop | ZEC | DOWN | 0.71 | 0.46 | -2.83 |
| 10-14 16:57 | +10 stop | ETH | DOWN | 0.58 | 0.24 | -3.71 |
| 10-14 16:57 | +5 | ETH | DOWN | 0.57 | yes | -5.88 |
| 10-14 16:56 | +10 stop | DOGE | DOWN | 0.57 | 0.41 | -1.95 |
| 10-14 16:55 | +10 stop | HYPE | DOWN | 0.70 | 0.47 | -2.63 |
| 10-14 16:54 | +10 stop | ZEC | DOWN | 0.58 | 0.69 | 0.77 |
| 10-14 16:54 | +10 stop | NEAR | UP | 0.62 | 0.36 | -2.94 |
| 10-14 16:54 | +10 | NEAR | UP | 0.62 | no | -6.37 |
| 10-14 16:54 | +5 | NEAR | UP | 0.62 | no | -6.37 |
| 10-14 16:54 | +10 stop | ETH | DOWN | 0.69 | 0.91 | 1.95 |
| 10-14 16:54 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-14 16:53 | +10 stop | BNB | UP | 0.52 | 0.30 | -2.53 |
| 10-14 16:53 | +10 | BNB | UP | 0.52 | 0.72 | 1.67 |
| 10-14 16:53 | +5 | BNB | UP | 0.52 | 0.57 | 0.14 |
| 10-14 16:53 | +10 stop | DOGE | UP | 0.70 | 0.48 | -2.53 |
| 10-14 16:53 | +10 | DOGE | UP | 0.70 | 0.97 | 2.55 |
| 10-14 16:53 | +5 | DOGE | UP | 0.70 | 0.76 | 0.32 |
| 10-14 16:52 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-14 16:51 | +10 stop | HYPE | UP | 0.59 | 0.39 | -2.34 |
| 10-14 16:51 | +10 stop | BTC | DOWN | 0.70 | 0.50 | -2.33 |
| 10-14 16:51 | +10 | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 10-14 16:51 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-14 16:50 | +10 stop | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 10-14 16:48 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 10-14 16:48 | +10 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 10-14 16:48 | +5 | XRP | DOWN | 0.69 | 0.76 | 0.42 |
| 10-14 16:48 | +10 stop | SOL | UP | 0.62 | 0.43 | -2.25 |
| 10-14 16:47 | +10 stop | ETH | DOWN | 0.59 | 0.42 | -2.10 |
| 10-14 16:47 | +10 stop | NEAR | UP | 0.53 | 0.66 | 0.93 |
