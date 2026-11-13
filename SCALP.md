# Range-Scalp Bot

*Updated Fri Nov 13 21:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58697 | 51221 | 7476 (105) | 0 | $-15807.86 | -4.3% |
| **+10¢** | 43845 | 35101 | 8744 (139) | 0 | $-14776.79 | -5.4% |
| **+15¢** | 36746 | 27327 | 9419 (174) | 1 | $-13353.18 | -5.8% |
| **+20¢** | 32736 | 22847 | 9889 (225) | 1 | $-11742.98 | -5.7% |
| **+10¢ (15¢ stop)** | 71465 | 71331 | 134 (82) | 0 | $-26310.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 21:42 | +10 stop | XRP | UP | 0.53 | 0.29 | -2.73 |
| 11-13 21:42 | +20 | XRP | UP | 0.53 | open |  |
| 11-13 21:42 | +15 | XRP | UP | 0.53 | open |  |
| 11-13 21:42 | +5 | XRP | UP | 0.54 | 0.59 | 0.15 |
| 11-13 21:40 | +10 stop | XRP | UP | 0.56 | 0.39 | -2.05 |
| 11-13 21:39 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 11-13 21:38 | +10 stop | XRP | UP | 0.66 | 0.51 | -1.84 |
| 11-13 21:37 | +10 stop | SOL | DOWN | 0.61 | 0.75 | 1.11 |
| 11-13 21:37 | +15 | SOL | DOWN | 0.59 | 0.75 | 1.29 |
| 11-13 21:37 | +10 | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 11-13 21:37 | +5 | SOL | DOWN | 0.57 | 0.65 | 0.46 |
| 11-13 21:36 | +10 stop | XRP | DOWN | 0.69 | 0.52 | -2.03 |
| 11-13 21:36 | +10 | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-13 21:34 | +5 | XRP | UP | 0.68 | 0.81 | 1.03 |
| 11-13 21:34 | +10 stop | ETH | DOWN | 0.68 | 0.87 | 1.66 |
| 11-13 21:34 | +10 | ETH | DOWN | 0.68 | 0.87 | 1.66 |
| 11-13 21:34 | +15 | HYPE | DOWN | 0.71 | 0.94 | 2.13 |
| 11-13 21:34 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-13 21:34 | +5 | HYPE | DOWN | 0.71 | 0.77 | 0.32 |
| 11-13 21:34 | +10 stop | XRP | UP | 0.64 | 0.33 | -3.43 |
| 11-13 21:34 | +10 stop | SOL | UP | 0.51 | 0.30 | -2.43 |
| 11-13 21:34 | +5 | DOGE | DOWN | 0.71 | 0.80 | 0.63 |
| 11-13 21:34 | +5 | BTC | DOWN | 0.61 | 0.68 | 0.37 |
| 11-13 21:32 | +10 stop | XRP | DOWN | 0.60 | 0.41 | -2.24 |
| 11-13 21:32 | +5 | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 11-13 21:32 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-13 21:32 | +20 | DOGE | DOWN | 0.70 | 0.96 | 2.39 |
| 11-13 21:32 | +15 | DOGE | DOWN | 0.70 | 0.96 | 2.39 |
| 11-13 21:32 | +10 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-13 21:32 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-13 21:32 | +10 stop | SOL | DOWN | 0.62 | 0.43 | -2.25 |
| 11-13 21:32 | +20 | SOL | DOWN | 0.62 | 0.85 | 2.04 |
| 11-13 21:32 | +15 | SOL | DOWN | 0.62 | 0.79 | 1.41 |
| 11-13 21:32 | +10 | SOL | DOWN | 0.62 | 0.79 | 1.41 |
| 11-13 21:32 | +5 | SOL | DOWN | 0.61 | 0.69 | 0.48 |
| 11-13 21:31 | +10 stop | XRP | UP | 0.56 | 0.40 | -1.94 |
| 11-13 21:31 | +20 | XRP | UP | 0.56 | 0.81 | 2.22 |
| 11-13 21:31 | +15 | XRP | UP | 0.57 | 0.81 | 2.14 |
| 11-13 21:31 | +10 | XRP | UP | 0.56 | 0.67 | 0.77 |
| 11-13 21:31 | +5 | XRP | UP | 0.56 | 0.64 | 0.46 |
