# Range-Scalp Bot

*Updated Fri Nov 20 14:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66254 | 57816 | 8438 (128) | 3 | $-17855.08 | -4.3% |
| **+10¢** | 49475 | 39608 | 9867 (170) | 4 | $-16634.91 | -5.3% |
| **+15¢** | 41489 | 30848 | 10641 (217) | 4 | $-14987.86 | -5.8% |
| **+20¢** | 36938 | 25762 | 11176 (273) | 4 | $-13297.68 | -5.7% |
| **+10¢ (15¢ stop)** | 80710 | 80544 | 166 (100) | 1 | $-29839.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 14:30 | +5 | BTC | DOWN | 0.65 | open |  |
| 11-20 14:30 | +10 stop | BTC | DOWN | 0.60 | open |  |
| 11-20 14:30 | +20 | BTC | DOWN | 0.60 | open |  |
| 11-20 14:30 | +15 | BTC | DOWN | 0.60 | open |  |
| 11-20 14:30 | +10 | BTC | DOWN | 0.60 | open |  |
| 11-20 14:30 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 11-20 14:26 | +10 stop | XRP | UP | 0.54 | 0.69 | 1.17 |
| 11-20 14:23 | +10 | XRP | DOWN | 0.64 | yes | -6.57 |
| 11-20 14:22 | +5 | HYPE | UP | 0.58 | 0.71 | 0.97 |
| 11-20 14:22 | +5 | DOGE | UP | 0.62 | 0.70 | 0.48 |
| 11-20 14:22 | +10 | DOGE | UP | 0.63 | 0.79 | 1.31 |
| 11-20 14:22 | +10 stop | BTC | UP | 0.66 | 0.78 | 0.91 |
| 11-20 14:22 | +5 | SOL | UP | 0.63 | 0.68 | 0.17 |
| 11-20 14:22 | +5 | DOGE | UP | 0.64 | 0.69 | 0.18 |
| 11-20 14:21 | +10 stop | SOL | UP | 0.58 | 0.68 | 0.67 |
| 11-20 14:21 | +10 stop | BNB | UP | 0.70 | 0.81 | 0.84 |
| 11-20 14:20 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 11-20 14:20 | +10 stop | HYPE | UP | 0.64 | 0.83 | 1.63 |
| 11-20 14:20 | +10 stop | BTC | UP | 0.57 | 0.71 | 1.07 |
| 11-20 14:20 | +10 stop | DOGE | UP | 0.60 | 0.70 | 0.68 |
| 11-20 14:19 | +10 stop | SOL | UP | 0.65 | 0.50 | -1.84 |
| 11-20 14:19 | +10 stop | HYPE | UP | 0.51 | 0.63 | 0.84 |
| 11-20 14:18 | +5 | XRP | DOWN | 0.59 | yes | -6.07 |
| 11-20 14:18 | +10 stop | BNB | DOWN | 0.62 | 0.47 | -1.85 |
| 11-20 14:18 | +20 | BNB | DOWN | 0.62 | open |  |
| 11-20 14:18 | +15 | BNB | DOWN | 0.62 | open |  |
| 11-20 14:18 | +10 | BNB | DOWN | 0.62 | open |  |
| 11-20 14:18 | +5 | BNB | DOWN | 0.62 | open |  |
| 11-20 14:18 | +10 stop | ZEC | UP | 0.57 | 0.69 | 0.87 |
| 11-20 14:18 | +20 | ZEC | UP | 0.57 | 0.78 | 1.79 |
| 11-20 14:18 | +15 | ZEC | UP | 0.57 | 0.76 | 1.59 |
| 11-20 14:18 | +10 | ZEC | UP | 0.57 | 0.69 | 0.87 |
| 11-20 14:18 | +5 | ZEC | UP | 0.56 | 0.63 | 0.35 |
| 11-20 14:18 | +10 stop | DOGE | UP | 0.58 | 0.43 | -1.86 |
| 11-20 14:18 | +20 | DOGE | UP | 0.58 | 0.79 | 1.80 |
| 11-20 14:18 | +15 | DOGE | UP | 0.58 | 0.79 | 1.80 |
| 11-20 14:18 | +10 | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 11-20 14:18 | +5 | DOGE | UP | 0.58 | 0.64 | 0.25 |
| 11-20 14:17 | +10 stop | SOL | UP | 0.66 | 0.50 | -1.94 |
| 11-20 14:16 | +10 stop | HYPE | UP | 0.63 | 0.47 | -1.95 |
