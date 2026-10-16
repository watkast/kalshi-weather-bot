# Range-Scalp Bot

*Updated Fri Oct 16 05:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18706 | 16242 | 2464 (28) | 0 | $-5732.66 | -4.9% |
| **+10¢** | 14098 | 11251 | 2847 (40) | 1 | $-5172.11 | -5.8% |
| **+15¢** | 11823 | 8759 | 3064 (59) | 1 | $-4679.25 | -6.3% |
| **+20¢** | 10502 | 7295 | 3207 (78) | 1 | $-4104.82 | -6.2% |
| **+10¢ (15¢ stop)** | 23045 | 22995 | 50 (29) | 0 | $-8918.25 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 05:25 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-16 05:25 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-16 05:25 | +5 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-16 05:25 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-16 05:25 | +5 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-16 05:24 | +10 stop | DOGE | DOWN | 0.53 | 0.65 | 0.86 |
| 10-16 05:24 | +10 | DOGE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-16 05:24 | +5 | DOGE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-16 05:23 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-16 05:23 | +10 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-16 05:23 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.56 |
| 10-16 05:23 | +10 stop | BNB | DOWN | 0.70 | 0.84 | 1.15 |
| 10-16 05:23 | +10 | BNB | DOWN | 0.70 | 0.84 | 1.15 |
| 10-16 05:23 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.32 |
| 10-16 05:23 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-16 05:23 | +15 | DOGE | DOWN | 0.56 | 0.72 | 1.27 |
| 10-16 05:23 | +10 | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-16 05:23 | +5 | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-16 05:22 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.19 |
| 10-16 05:19 | +10 stop | XRP | DOWN | 0.65 | 0.50 | -1.84 |
| 10-16 05:19 | +20 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 10-16 05:19 | +15 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 10-16 05:19 | +10 | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 10-16 05:19 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 10-16 05:19 | +10 stop | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 10-16 05:19 | +20 | ZEC | DOWN | 0.65 | 0.88 | 2.06 |
| 10-16 05:19 | +15 | ZEC | DOWN | 0.65 | 0.84 | 1.64 |
| 10-16 05:19 | +10 | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 10-16 05:19 | +5 | ZEC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-16 05:19 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-16 05:19 | +20 | SOL | DOWN | 0.69 | 0.90 | 1.91 |
| 10-16 05:19 | +15 | SOL | DOWN | 0.69 | 0.85 | 1.36 |
| 10-16 05:19 | +10 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-16 05:19 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 10-16 05:19 | +5 | HYPE | DOWN | 0.61 | 0.74 | 1.01 |
| 10-16 05:19 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-16 05:19 | +20 | DOGE | DOWN | 0.71 | 0.93 | 1.95 |
| 10-16 05:19 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-16 05:19 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-16 05:19 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
