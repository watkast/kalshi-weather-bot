# Range-Scalp Bot

*Updated Sun Nov 15 01:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60138 | 52458 | 7680 (107) | 1 | $-16369.20 | -4.3% |
| **+10¢** | 44935 | 35934 | 9001 (143) | 0 | $-15460.58 | -5.5% |
| **+15¢** | 37650 | 27944 | 9706 (181) | 0 | $-14102.54 | -6.0% |
| **+20¢** | 33549 | 23366 | 10183 (233) | 0 | $-12435.14 | -5.9% |
| **+10¢ (15¢ stop)** | 73224 | 73081 | 143 (82) | 0 | $-26954.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 01:21 | +5 | XRP | DOWN | 0.69 | 0.85 | 1.37 |
| 11-15 01:21 | +10 | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 11-15 01:21 | +10 stop | BTC | DOWN | 0.57 | 0.87 | 2.74 |
| 11-15 01:21 | +10 stop | HYPE | DOWN | 0.68 | 0.90 | 1.97 |
| 11-15 01:21 | +10 stop | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 11-15 01:21 | +10 stop | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 11-15 01:21 | +10 stop | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 11-15 01:21 | +10 stop | DOGE | UP | 0.54 | 0.35 | -2.19 |
| 11-15 01:20 | +10 stop | ETH | UP | 0.58 | 0.30 | -3.13 |
| 11-15 01:20 | +10 stop | SOL | UP | 0.57 | 0.42 | -1.86 |
| 11-15 01:19 | +10 stop | XRP | UP | 0.56 | 0.41 | -1.85 |
| 11-15 01:19 | +10 stop | BNB | UP | 0.63 | 0.47 | -1.95 |
| 11-15 01:19 | +10 stop | DOGE | UP | 0.70 | 0.55 | -1.83 |
| 11-15 01:19 | +10 stop | BTC | UP | 0.61 | 0.42 | -2.25 |
| 11-15 01:19 | +10 stop | HYPE | UP | 0.62 | 0.46 | -1.95 |
| 11-15 01:19 | +10 stop | NEAR | UP | 0.65 | 0.46 | -2.24 |
| 11-15 01:19 | +5 | SOL | UP | 0.60 | open |  |
| 11-15 01:17 | +5 | DOGE | DOWN | 0.58 | 0.63 | 0.15 |
| 11-15 01:17 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 11-15 01:16 | +10 stop | XRP | DOWN | 0.59 | 0.39 | -2.34 |
| 11-15 01:16 | +20 | XRP | DOWN | 0.59 | 0.85 | 2.34 |
| 11-15 01:16 | +15 | XRP | DOWN | 0.60 | 0.85 | 2.24 |
| 11-15 01:16 | +10 | XRP | DOWN | 0.58 | 0.70 | 0.87 |
| 11-15 01:16 | +5 | XRP | DOWN | 0.58 | 0.63 | 0.15 |
| 11-15 01:16 | +10 stop | SOL | DOWN | 0.55 | 0.38 | -2.05 |
| 11-15 01:16 | +20 | SOL | DOWN | 0.55 | 0.77 | 1.89 |
| 11-15 01:16 | +15 | SOL | DOWN | 0.55 | 0.70 | 1.17 |
| 11-15 01:16 | +10 | SOL | DOWN | 0.55 | 0.65 | 0.66 |
| 11-15 01:16 | +5 | SOL | DOWN | 0.56 | 0.61 | 0.15 |
| 11-15 01:16 | +10 stop | BNB | DOWN | 0.61 | 0.41 | -2.34 |
| 11-15 01:16 | +20 | BNB | DOWN | 0.61 | 0.88 | 2.45 |
| 11-15 01:16 | +15 | BNB | DOWN | 0.61 | 0.88 | 2.45 |
| 11-15 01:16 | +10 | BNB | DOWN | 0.61 | 0.88 | 2.45 |
| 11-15 01:16 | +5 | BNB | DOWN | 0.61 | 0.88 | 2.45 |
| 11-15 01:16 | +10 stop | ETH | DOWN | 0.58 | 0.33 | -2.84 |
| 11-15 01:16 | +20 | ETH | DOWN | 0.58 | 0.82 | 2.11 |
| 11-15 01:16 | +15 | ETH | DOWN | 0.59 | 0.82 | 2.02 |
| 11-15 01:16 | +10 | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 11-15 01:16 | +5 | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 11-15 01:16 | +10 stop | DOGE | DOWN | 0.58 | 0.30 | -3.13 |
