# Range-Scalp Bot

*Updated Wed Oct 07 01:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5744 | 4971 | 773 (9) | 0 | $-1815.33 | -5.0% |
| **+10¢** | 4381 | 3472 | 909 (16) | 0 | $-1724.21 | -6.3% |
| **+15¢** | 3676 | 2712 | 964 (20) | 0 | $-1518.73 | -6.6% |
| **+20¢** | 3284 | 2280 | 1004 (27) | 0 | $-1261.07 | -6.1% |
| **+10¢ (15¢ stop)** | 6996 | 6981 | 15 (9) | 0 | $-2514.14 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 01:10 | +10 stop | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 10-07 01:10 | +10 stop | ZEC | DOWN | 0.70 | 0.88 | 1.54 |
| 10-07 01:10 | +10 | ZEC | DOWN | 0.70 | 0.88 | 1.54 |
| 10-07 01:10 | +5 | ZEC | DOWN | 0.70 | 0.79 | 0.61 |
| 10-07 01:10 | +10 stop | DOGE | DOWN | 0.60 | 0.78 | 1.50 |
| 10-07 01:10 | +10 | DOGE | DOWN | 0.60 | 0.78 | 1.50 |
| 10-07 01:10 | +5 | DOGE | DOWN | 0.60 | 0.68 | 0.47 |
| 10-07 01:08 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.92 |
| 10-07 01:08 | +20 | DOGE | DOWN | 0.65 | 0.93 | 2.55 |
| 10-07 01:08 | +15 | DOGE | DOWN | 0.65 | 0.93 | 2.55 |
| 10-07 01:08 | +10 | DOGE | DOWN | 0.65 | 0.77 | 0.92 |
| 10-07 01:08 | +5 | DOGE | DOWN | 0.65 | 0.77 | 0.92 |
| 10-07 01:08 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-07 01:05 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-07 01:05 | +10 stop | ZEC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-07 01:05 | +20 | ZEC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-07 01:05 | +15 | ZEC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-07 01:05 | +10 | ZEC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-07 01:05 | +5 | ZEC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-07 01:05 | +10 stop | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-07 01:05 | +15 | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-07 01:05 | +10 | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-07 01:05 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-07 01:05 | +10 stop | BNB | DOWN | 0.60 | 0.39 | -2.44 |
| 10-07 01:05 | +20 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-07 01:05 | +15 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-07 01:05 | +10 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-07 01:05 | +5 | BNB | DOWN | 0.60 | 0.65 | 0.17 |
| 10-07 01:04 | +10 stop | HYPE | UP | 0.69 | 0.53 | -1.93 |
| 10-07 01:02 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-07 01:02 | +10 stop | HYPE | DOWN | 0.68 | 0.49 | -2.28 |
| 10-07 01:02 | +20 | HYPE | DOWN | 0.68 | 0.90 | 1.95 |
| 10-07 01:02 | +15 | HYPE | DOWN | 0.68 | 0.85 | 1.41 |
| 10-07 01:02 | +10 | HYPE | DOWN | 0.68 | 0.82 | 1.09 |
| 10-07 01:02 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.26 |
| 10-07 01:01 | +10 stop | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-07 01:01 | +20 | DOGE | DOWN | 0.60 | 0.85 | 2.24 |
| 10-07 01:01 | +15 | DOGE | DOWN | 0.60 | 0.75 | 1.23 |
| 10-07 01:01 | +10 | DOGE | DOWN | 0.60 | 0.73 | 1.02 |
| 10-07 01:01 | +5 | DOGE | DOWN | 0.59 | 0.67 | 0.45 |
