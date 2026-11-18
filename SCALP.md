# Range-Scalp Bot

*Updated Wed Nov 18 16:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64202 | 55988 | 8214 (124) | 1 | $-17574.88 | -4.3% |
| **+10¢** | 47947 | 38335 | 9612 (165) | 1 | $-16480.48 | -5.5% |
| **+15¢** | 40198 | 29837 | 10361 (210) | 0 | $-14942.57 | -5.9% |
| **+20¢** | 35794 | 24919 | 10875 (265) | 0 | $-13248.06 | -5.9% |
| **+10¢ (15¢ stop)** | 78102 | 77938 | 164 (98) | 0 | $-28745.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 16:11 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 11-18 16:10 | +5 | NEAR | UP | 0.65 | open |  |
| 11-18 16:10 | +5 | SOL | DOWN | 0.58 | 0.67 | 0.56 |
| 11-18 16:09 | +10 stop | XRP | DOWN | 0.49 | 0.70 | 1.77 |
| 11-18 16:09 | +15 | XRP | DOWN | 0.49 | 0.70 | 1.77 |
| 11-18 16:09 | +10 | XRP | DOWN | 0.49 | 0.70 | 1.77 |
| 11-18 16:09 | +5 | XRP | DOWN | 0.49 | 0.55 | 0.24 |
| 11-18 16:09 | +10 stop | DOGE | DOWN | 0.66 | 0.49 | -2.04 |
| 11-18 16:09 | +10 stop | ZEC | DOWN | 0.68 | 0.24 | -4.69 |
| 11-18 16:09 | +15 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-18 16:09 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-18 16:09 | +5 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-18 16:09 | +10 stop | NEAR | UP | 0.53 | 0.32 | -2.48 |
| 11-18 16:09 | +10 | NEAR | UP | 0.53 | open |  |
| 11-18 16:09 | +5 | NEAR | UP | 0.53 | 0.61 | 0.41 |
| 11-18 16:09 | +10 stop | HYPE | UP | 0.59 | 0.23 | -3.90 |
| 11-18 16:08 | +10 stop | SOL | DOWN | 0.64 | 0.83 | 1.63 |
| 11-18 16:08 | +15 | SOL | DOWN | 0.64 | 0.83 | 1.63 |
| 11-18 16:08 | +10 | SOL | DOWN | 0.64 | 0.83 | 1.63 |
| 11-18 16:08 | +5 | SOL | DOWN | 0.64 | 0.70 | 0.28 |
| 11-18 16:08 | +10 stop | NEAR | DOWN | 0.54 | 0.29 | -2.87 |
| 11-18 16:07 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-18 16:07 | +10 stop | HYPE | UP | 0.51 | 0.73 | 1.88 |
| 11-18 16:06 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-18 16:06 | +10 stop | NEAR | UP | 0.61 | 0.43 | -2.19 |
| 11-18 16:06 | +5 | NEAR | UP | 0.63 | 0.69 | 0.28 |
| 11-18 16:06 | +10 stop | ZEC | UP | 0.49 | 0.32 | -2.04 |
| 11-18 16:06 | +5 | XRP | DOWN | 0.54 | 0.59 | 0.15 |
| 11-18 16:05 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 11-18 16:05 | +20 | SOL | DOWN | 0.69 | 0.98 | 2.74 |
| 11-18 16:05 | +15 | SOL | DOWN | 0.69 | 0.87 | 1.57 |
| 11-18 16:05 | +10 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 11-18 16:05 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.62 |
| 11-18 16:05 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-18 16:05 | +10 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-18 16:05 | +5 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-18 16:04 | +5 | XRP | DOWN | 0.62 | 0.67 | 0.17 |
| 11-18 16:04 | +5 | HYPE | DOWN | 0.60 | 0.75 | 1.19 |
| 11-18 16:04 | +5 | DOGE | DOWN | 0.70 | 0.87 | 1.51 |
| 11-18 16:04 | +10 stop | XRP | DOWN | 0.58 | 0.71 | 0.97 |
