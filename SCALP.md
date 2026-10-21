# Range-Scalp Bot

*Updated Wed Oct 21 10:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27034 | 23539 | 3495 (39) | 3 | $-7869.13 | -4.6% |
| **+10¢** | 20340 | 16303 | 4037 (55) | 4 | $-6947.88 | -5.4% |
| **+15¢** | 17028 | 12682 | 4346 (78) | 4 | $-6228.68 | -5.8% |
| **+20¢** | 15077 | 10522 | 4555 (97) | 4 | $-5592.05 | -5.9% |
| **+10¢ (15¢ stop)** | 33176 | 33117 | 59 (32) | 0 | $-12274.55 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 10:12 | +10 stop | XRP | DOWN | 0.49 | 0.59 | 0.65 |
| 10-21 10:11 | +10 stop | HYPE | UP | 0.49 | 0.59 | 0.65 |
| 10-21 10:11 | +15 | HYPE | UP | 0.49 | open |  |
| 10-21 10:11 | +10 | HYPE | UP | 0.50 | open |  |
| 10-21 10:11 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-21 10:11 | +10 stop | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-21 10:09 | +10 stop | HYPE | UP | 0.70 | 0.85 | 1.22 |
| 10-21 10:08 | +10 stop | HYPE | DOWN | 0.59 | 0.43 | -1.95 |
| 10-21 10:08 | +10 stop | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-21 10:07 | +10 stop | HYPE | DOWN | 0.52 | 0.64 | 0.85 |
| 10-21 10:06 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.42 |
| 10-21 10:05 | +10 stop | BTC | DOWN | 0.59 | 0.73 | 1.09 |
| 10-21 10:05 | +10 stop | HYPE | UP | 0.54 | 0.30 | -2.73 |
| 10-21 10:05 | +15 | HYPE | UP | 0.54 | 0.73 | 1.58 |
| 10-21 10:05 | +10 | HYPE | UP | 0.54 | 0.73 | 1.58 |
| 10-21 10:05 | +5 | HYPE | UP | 0.54 | 0.59 | 0.15 |
| 10-21 10:05 | +10 stop | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 10-21 10:05 | +20 | DOGE | DOWN | 0.71 | 0.91 | 1.82 |
| 10-21 10:05 | +15 | DOGE | DOWN | 0.71 | 0.91 | 1.78 |
| 10-21 10:05 | +10 | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 10-21 10:05 | +5 | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 10-21 10:04 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-21 10:04 | +10 stop | XRP | UP | 0.62 | 0.31 | -3.42 |
| 10-21 10:04 | +10 stop | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 10-21 10:04 | +15 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 10-21 10:04 | +10 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 10-21 10:04 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 10-21 10:03 | +10 stop | XRP | DOWN | 0.65 | 0.43 | -2.54 |
| 10-21 10:02 | +10 stop | BTC | DOWN | 0.58 | 0.71 | 0.97 |
| 10-21 10:02 | +10 stop | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-21 10:02 | +20 | ZEC | DOWN | 0.70 | 0.92 | 1.95 |
| 10-21 10:02 | +15 | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-21 10:02 | +10 | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-21 10:02 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-21 10:02 | +10 stop | ETH | DOWN | 0.63 | 0.77 | 1.10 |
| 10-21 10:02 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 10-21 10:02 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-21 10:02 | +20 | DOGE | DOWN | 0.55 | 0.78 | 1.99 |
| 10-21 10:02 | +15 | DOGE | DOWN | 0.55 | 0.72 | 1.37 |
| 10-21 10:02 | +10 | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
