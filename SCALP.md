# Range-Scalp Bot

*Updated Sat Oct 24 04:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31431 | 27391 | 4040 (40) | 4 | $-9074.12 | -4.6% |
| **+10¢** | 23509 | 18844 | 4665 (58) | 7 | $-8057.34 | -5.4% |
| **+15¢** | 19679 | 14667 | 5012 (81) | 8 | $-7181.10 | -5.8% |
| **+20¢** | 17433 | 12184 | 5249 (103) | 8 | $-6398.02 | -5.8% |
| **+10¢ (15¢ stop)** | 38586 | 38527 | 59 (32) | 0 | $-14742.48 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 04:24 | +5 | ETH | UP | 0.62 | 0.77 | 1.20 |
| 10-24 04:24 | +10 stop | XRP | DOWN | 0.71 | 0.50 | -2.43 |
| 10-24 04:24 | +15 | XRP | DOWN | 0.71 | open |  |
| 10-24 04:24 | +10 | XRP | DOWN | 0.71 | open |  |
| 10-24 04:24 | +5 | XRP | DOWN | 0.71 | open |  |
| 10-24 04:24 | +10 stop | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 10-24 04:24 | +5 | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 10-24 04:23 | +10 stop | NEAR | UP | 0.65 | 0.78 | 1.01 |
| 10-24 04:23 | +5 | NEAR | UP | 0.65 | 0.71 | 0.29 |
| 10-24 04:23 | +10 stop | HYPE | DOWN | 0.61 | 0.43 | -2.15 |
| 10-24 04:23 | +5 | ETH | DOWN | 0.50 | 0.56 | 0.24 |
| 10-24 04:22 | +10 stop | ETH | DOWN | 0.52 | 0.22 | -3.31 |
| 10-24 04:22 | +5 | ETH | DOWN | 0.52 | 0.60 | 0.45 |
| 10-24 04:22 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-24 04:22 | +5 | DOGE | DOWN | 0.50 | 0.63 | 0.95 |
| 10-24 04:22 | +10 stop | ZEC | DOWN | 0.49 | 0.29 | -2.33 |
| 10-24 04:22 | +10 stop | SOL | DOWN | 0.46 | 0.25 | -2.42 |
| 10-24 04:21 | +10 stop | DOGE | DOWN | 0.64 | 0.45 | -2.25 |
| 10-24 04:21 | +10 stop | NEAR | DOWN | 0.64 | 0.49 | -1.85 |
| 10-24 04:21 | +10 stop | SOL | UP | 0.48 | 0.63 | 1.15 |
| 10-24 04:21 | +10 stop | HYPE | DOWN | 0.69 | 0.54 | -1.83 |
| 10-24 04:20 | +10 stop | ZEC | UP | 0.65 | 0.46 | -2.24 |
| 10-24 04:20 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
| 10-24 04:20 | +10 stop | ETH | UP | 0.51 | 0.30 | -2.43 |
| 10-24 04:20 | +10 stop | DOGE | UP | 0.64 | 0.34 | -3.33 |
| 10-24 04:20 | +10 stop | XRP | UP | 0.54 | 0.30 | -2.73 |
| 10-24 04:20 | +10 stop | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 10-24 04:19 | +10 stop | NEAR | UP | 0.57 | 0.67 | 0.66 |
| 10-24 04:19 | +10 stop | SOL | UP | 0.58 | 0.74 | 1.28 |
| 10-24 04:19 | +10 stop | ZEC | UP | 0.55 | 0.66 | 0.76 |
| 10-24 04:18 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.37 |
| 10-24 04:17 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-24 04:17 | +5 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-24 04:17 | +10 stop | SOL | DOWN | 0.60 | 0.43 | -2.03 |
| 10-24 04:17 | +20 | SOL | DOWN | 0.60 | open |  |
| 10-24 04:17 | +15 | SOL | DOWN | 0.60 | open |  |
| 10-24 04:17 | +10 | SOL | DOWN | 0.60 | open |  |
| 10-24 04:17 | +5 | SOL | DOWN | 0.60 | open |  |
| 10-24 04:16 | +10 stop | BTC | DOWN | 0.56 | 0.74 | 1.48 |
| 10-24 04:16 | +20 | BTC | DOWN | 0.56 | 0.78 | 1.89 |
