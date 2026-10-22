# Range-Scalp Bot

*Updated Thu Oct 22 15:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28896 | 25169 | 3727 (39) | 2 | $-8382.46 | -4.6% |
| **+10¢** | 21689 | 17381 | 4308 (55) | 5 | $-7452.30 | -5.5% |
| **+15¢** | 18156 | 13523 | 4633 (78) | 4 | $-6672.80 | -5.9% |
| **+20¢** | 16068 | 11210 | 4858 (100) | 3 | $-6016.07 | -6.0% |
| **+10¢ (15¢ stop)** | 35459 | 35400 | 59 (32) | 0 | $-13297.46 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 15:18 | +10 stop | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-22 15:18 | +20 | DOGE | UP | 0.66 | 0.86 | 1.75 |
| 10-22 15:17 | +10 stop | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 10-22 15:17 | +5 | HYPE | UP | 0.67 | 0.76 | 0.61 |
| 10-22 15:16 | +10 stop | XRP | DOWN | 0.58 | 0.41 | -2.05 |
| 10-22 15:16 | +20 | XRP | DOWN | 0.57 | open |  |
| 10-22 15:16 | +15 | XRP | DOWN | 0.57 | open |  |
| 10-22 15:16 | +10 | XRP | DOWN | 0.56 | open |  |
| 10-22 15:16 | +5 | XRP | DOWN | 0.55 | 0.62 | 0.35 |
| 10-22 15:16 | +10 stop | BNB | DOWN | 0.55 | 0.40 | -1.85 |
| 10-22 15:16 | +20 | BNB | DOWN | 0.55 | open |  |
| 10-22 15:16 | +15 | BNB | DOWN | 0.55 | open |  |
| 10-22 15:16 | +10 | BNB | DOWN | 0.55 | open |  |
| 10-22 15:16 | +5 | BNB | DOWN | 0.55 | 0.62 | 0.35 |
| 10-22 15:16 | +10 stop | ETH | DOWN | 0.56 | 0.35 | -2.44 |
| 10-22 15:16 | +10 | ETH | DOWN | 0.56 | open |  |
| 10-22 15:16 | +5 | ETH | DOWN | 0.56 | open |  |
| 10-22 15:16 | +10 stop | HYPE | DOWN | 0.60 | 0.41 | -2.24 |
| 10-22 15:16 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-22 15:16 | +15 | HYPE | DOWN | 0.62 | open |  |
| 10-22 15:16 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-22 15:16 | +5 | HYPE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-22 15:16 | +15 | DOGE | DOWN | 0.71 | open |  |
| 10-22 15:16 | +10 | DOGE | DOWN | 0.71 | open |  |
| 10-22 15:16 | +5 | DOGE | DOWN | 0.70 | open |  |
| 10-22 15:16 | +10 stop | BTC | UP | 0.53 | 0.70 | 1.37 |
| 10-22 15:16 | +20 | BTC | UP | 0.53 | 0.78 | 2.19 |
| 10-22 15:16 | +15 | BTC | UP | 0.53 | 0.70 | 1.37 |
| 10-22 15:16 | +10 | BTC | UP | 0.53 | 0.70 | 1.37 |
| 10-22 15:16 | +5 | BTC | UP | 0.54 | 0.70 | 1.27 |
| 10-22 15:16 | +10 stop | ZEC | UP | 0.54 | 0.64 | 0.65 |
| 10-22 15:16 | +20 | ZEC | UP | 0.55 | 0.77 | 1.87 |
| 10-22 15:16 | +15 | ZEC | UP | 0.55 | 0.71 | 1.24 |
| 10-22 15:16 | +10 | ZEC | UP | 0.55 | 0.71 | 1.24 |
| 10-22 15:16 | +5 | ZEC | UP | 0.55 | 0.64 | 0.55 |
| 10-22 15:16 | +10 stop | ETH | UP | 0.49 | 0.60 | 0.75 |
| 10-22 15:16 | +20 | ETH | UP | 0.49 | 0.70 | 1.77 |
| 10-22 15:16 | +15 | ETH | UP | 0.50 | 0.70 | 1.67 |
| 10-22 15:16 | +10 | ETH | UP | 0.50 | 0.60 | 0.65 |
| 10-22 15:16 | +5 | ETH | UP | 0.50 | 0.60 | 0.65 |
