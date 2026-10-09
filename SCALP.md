# Range-Scalp Bot

*Updated Fri Oct 09 19:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9406 | 8120 | 1286 (17) | 2 | $-3171.60 | -5.3% |
| **+10¢** | 7099 | 5590 | 1509 (29) | 3 | $-3104.04 | -6.9% |
| **+15¢** | 5979 | 4392 | 1587 (42) | 4 | $-2554.60 | -6.8% |
| **+20¢** | 5322 | 3673 | 1649 (53) | 4 | $-2141.48 | -6.4% |
| **+10¢ (15¢ stop)** | 11521 | 11489 | 32 (20) | 0 | $-4438.85 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 19:36 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-09 19:35 | +5 | ETH | DOWN | 0.70 | 0.79 | 0.63 |
| 10-09 19:35 | +10 | BNB | UP | 0.52 | open |  |
| 10-09 19:35 | +10 stop | XRP | DOWN | 0.61 | 0.73 | 0.89 |
| 10-09 19:35 | +10 stop | BTC | UP | 0.59 | 0.43 | -1.95 |
| 10-09 19:35 | +10 stop | BNB | UP | 0.59 | 0.38 | -2.43 |
| 10-09 19:35 | +10 stop | ZEC | DOWN | 0.62 | 0.76 | 1.05 |
| 10-09 19:35 | +10 | ZEC | DOWN | 0.62 | 0.76 | 1.05 |
| 10-09 19:35 | +5 | ZEC | DOWN | 0.62 | 0.71 | 0.53 |
| 10-09 19:34 | +10 stop | SOL | DOWN | 0.53 | 0.73 | 1.68 |
| 10-09 19:34 | +10 | SOL | DOWN | 0.53 | 0.73 | 1.68 |
| 10-09 19:34 | +5 | SOL | DOWN | 0.53 | 0.59 | 0.25 |
| 10-09 19:34 | +5 | ETH | DOWN | 0.56 | 0.64 | 0.45 |
| 10-09 19:34 | +10 stop | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 10-09 19:34 | +10 | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 10-09 19:34 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-09 19:33 | +10 stop | BTC | DOWN | 0.59 | 0.43 | -1.95 |
| 10-09 19:33 | +10 stop | XRP | DOWN | 0.70 | 0.54 | -1.89 |
| 10-09 19:33 | +15 | XRP | DOWN | 0.70 | open |  |
| 10-09 19:33 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.77 |
| 10-09 19:33 | +10 stop | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 10-09 19:33 | +20 | ETH | DOWN | 0.62 | 0.83 | 1.83 |
| 10-09 19:33 | +15 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 10-09 19:33 | +10 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 10-09 19:33 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 10-09 19:33 | +10 stop | BNB | DOWN | 0.67 | 0.49 | -2.09 |
| 10-09 19:33 | +5 | BNB | DOWN | 0.67 | 0.74 | 0.45 |
| 10-09 19:33 | +5 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-09 19:32 | +5 | BNB | DOWN | 0.59 | 0.68 | 0.57 |
| 10-09 19:32 | +10 stop | XRP | DOWN | 0.52 | 0.68 | 1.26 |
| 10-09 19:32 | +10 | XRP | DOWN | 0.52 | 0.68 | 1.26 |
| 10-09 19:32 | +5 | XRP | DOWN | 0.52 | 0.57 | 0.14 |
| 10-09 19:32 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.81 |
| 10-09 19:32 | +20 | HYPE | DOWN | 0.63 | 0.83 | 1.75 |
| 10-09 19:32 | +15 | HYPE | DOWN | 0.63 | 0.83 | 1.75 |
| 10-09 19:32 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.81 |
| 10-09 19:32 | +5 | HYPE | DOWN | 0.63 | 0.74 | 0.81 |
| 10-09 19:32 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.70 |
| 10-09 19:32 | +20 | SOL | DOWN | 0.64 | open |  |
| 10-09 19:32 | +15 | SOL | DOWN | 0.64 | 0.79 | 1.22 |
