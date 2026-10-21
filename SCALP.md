# Range-Scalp Bot

*Updated Wed Oct 21 14:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27303 | 23778 | 3525 (39) | 5 | $-7927.14 | -4.6% |
| **+10¢** | 20522 | 16449 | 4073 (55) | 6 | $-7006.14 | -5.4% |
| **+15¢** | 17184 | 12801 | 4383 (78) | 6 | $-6259.80 | -5.8% |
| **+20¢** | 15210 | 10616 | 4594 (98) | 6 | $-5623.11 | -5.9% |
| **+10¢ (15¢ stop)** | 33513 | 33454 | 59 (32) | 0 | $-12437.63 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 14:27 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-21 14:27 | +5 | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-21 14:26 | +5 | ZEC | UP | 0.71 | 0.80 | 0.63 |
| 10-21 14:25 | +10 stop | HYPE | DOWN | 0.55 | 0.25 | -3.32 |
| 10-21 14:25 | +10 | HYPE | DOWN | 0.57 | 0.69 | 0.87 |
| 10-21 14:25 | +10 stop | ZEC | DOWN | 0.52 | 0.17 | -3.78 |
| 10-21 14:25 | +20 | ZEC | DOWN | 0.52 | 0.99 | 4.53 |
| 10-21 14:25 | +15 | ZEC | DOWN | 0.52 | 0.99 | 4.53 |
| 10-21 14:25 | +10 | ZEC | DOWN | 0.52 | 0.62 | 0.65 |
| 10-21 14:25 | +5 | ZEC | DOWN | 0.52 | 0.59 | 0.35 |
| 10-21 14:25 | +10 stop | HYPE | UP | 0.64 | 0.39 | -2.84 |
| 10-21 14:25 | +5 | HYPE | UP | 0.63 | 0.70 | 0.38 |
| 10-21 14:24 | +10 stop | NEAR | UP | 0.65 | 0.84 | 1.64 |
| 10-21 14:24 | +10 | NEAR | UP | 0.65 | 0.84 | 1.64 |
| 10-21 14:24 | +5 | NEAR | UP | 0.69 | 0.84 | 1.25 |
| 10-21 14:23 | +10 stop | HYPE | DOWN | 0.48 | 0.32 | -1.94 |
| 10-21 14:23 | +15 | HYPE | DOWN | 0.48 | 0.69 | 1.77 |
| 10-21 14:23 | +10 | HYPE | DOWN | 0.48 | 0.60 | 0.85 |
| 10-21 14:23 | +5 | HYPE | DOWN | 0.48 | 0.57 | 0.54 |
| 10-21 14:23 | +10 stop | NEAR | DOWN | 0.50 | 0.63 | 0.95 |
| 10-21 14:23 | +20 | NEAR | DOWN | 0.50 | 0.80 | 2.70 |
| 10-21 14:23 | +15 | NEAR | DOWN | 0.52 | 0.80 | 2.50 |
| 10-21 14:23 | +10 | NEAR | DOWN | 0.52 | 0.63 | 0.75 |
| 10-21 14:23 | +5 | NEAR | DOWN | 0.52 | 0.63 | 0.75 |
| 10-21 14:23 | +10 stop | BNB | UP | 0.71 | 0.81 | 0.74 |
| 10-21 14:22 | +10 stop | ETH | UP | 0.65 | 0.79 | 1.12 |
| 10-21 14:22 | +10 stop | DOGE | DOWN | 0.64 | 0.47 | -2.05 |
| 10-21 14:22 | +20 | DOGE | DOWN | 0.64 | open |  |
| 10-21 14:22 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-21 14:22 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-21 14:22 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-21 14:21 | +10 stop | XRP | DOWN | 0.49 | 0.32 | -2.04 |
| 10-21 14:21 | +10 stop | SOL | DOWN | 0.65 | 0.41 | -2.73 |
| 10-21 14:20 | +10 stop | BNB | DOWN | 0.70 | 0.53 | -2.07 |
| 10-21 14:18 | +10 stop | ETH | DOWN | 0.67 | 0.45 | -2.54 |
| 10-21 14:18 | +20 | ETH | DOWN | 0.67 | open |  |
| 10-21 14:18 | +15 | ETH | DOWN | 0.67 | open |  |
| 10-21 14:18 | +10 | ETH | DOWN | 0.67 | open |  |
| 10-21 14:18 | +5 | ETH | DOWN | 0.67 | open |  |
| 10-21 14:17 | +15 | DOGE | DOWN | 0.70 | open |  |
