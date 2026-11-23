# Range-Scalp Bot

*Updated Mon Nov 23 11:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69874 | 60973 | 8901 (146) | 1 | $-18803.10 | -4.3% |
| **+10¢** | 52137 | 41735 | 10402 (189) | 1 | $-17511.92 | -5.3% |
| **+15¢** | 43690 | 32485 | 11205 (245) | 1 | $-15635.13 | -5.7% |
| **+20¢** | 38904 | 27113 | 11791 (310) | 3 | $-13998.46 | -5.7% |
| **+10¢ (15¢ stop)** | 85095 | 84905 | 190 (118) | 1 | $-31260.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 11:20 | +5 | BNB | UP | 0.68 | open |  |
| 11-23 11:20 | +10 stop | BNB | UP | 0.62 | open |  |
| 11-23 11:20 | +10 | BNB | UP | 0.62 | open |  |
| 11-23 11:20 | +5 | BNB | UP | 0.64 | 0.69 | 0.18 |
| 11-23 11:19 | +10 stop | XRP | UP | 0.69 | 0.80 | 0.83 |
| 11-23 11:19 | +10 | XRP | UP | 0.69 | 0.80 | 0.83 |
| 11-23 11:19 | +5 | XRP | UP | 0.69 | 0.75 | 0.31 |
| 11-23 11:19 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-23 11:19 | +10 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-23 11:19 | +5 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-23 11:18 | +10 stop | NEAR | UP | 0.59 | 0.74 | 1.19 |
| 11-23 11:18 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-23 11:18 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-23 11:18 | +10 stop | SOL | DOWN | 0.48 | 0.31 | -2.03 |
| 11-23 11:17 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-23 11:17 | +20 | HYPE | DOWN | 0.67 | 0.87 | 1.80 |
| 11-23 11:17 | +15 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-23 11:17 | +10 | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-23 11:17 | +5 | HYPE | DOWN | 0.65 | 0.74 | 0.60 |
| 11-23 11:17 | +10 stop | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-23 11:17 | +20 | ZEC | DOWN | 0.60 | 0.81 | 1.82 |
| 11-23 11:17 | +15 | ZEC | DOWN | 0.60 | 0.75 | 1.19 |
| 11-23 11:17 | +10 | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-23 11:17 | +5 | ZEC | DOWN | 0.60 | 0.69 | 0.58 |
| 11-23 11:16 | +10 stop | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-23 11:16 | +20 | XRP | UP | 0.60 | 0.80 | 1.71 |
| 11-23 11:16 | +15 | XRP | UP | 0.60 | 0.75 | 1.19 |
| 11-23 11:16 | +10 | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-23 11:16 | +5 | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-23 11:16 | +10 stop | NEAR | UP | 0.64 | 0.46 | -2.15 |
| 11-23 11:16 | +20 | NEAR | UP | 0.64 | open |  |
| 11-23 11:16 | +15 | NEAR | UP | 0.64 | 0.80 | 1.31 |
| 11-23 11:16 | +10 | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 11-23 11:16 | +5 | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 11-23 11:16 | +10 stop | DOGE | UP | 0.68 | 0.82 | 1.13 |
| 11-23 11:16 | +20 | DOGE | UP | 0.68 | 0.88 | 1.76 |
| 11-23 11:16 | +15 | DOGE | UP | 0.68 | 0.86 | 1.55 |
| 11-23 11:16 | +10 | DOGE | UP | 0.69 | 0.82 | 1.04 |
| 11-23 11:16 | +5 | DOGE | UP | 0.69 | 0.74 | 0.21 |
| 11-23 11:16 | +10 stop | BTC | UP | 0.62 | 0.76 | 1.10 |
