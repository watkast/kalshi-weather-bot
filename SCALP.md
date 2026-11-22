# Range-Scalp Bot

*Updated Sun Nov 22 11:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68526 | 59790 | 8736 (142) | 4 | $-18460.15 | -4.3% |
| **+10¢** | 51172 | 40967 | 10205 (186) | 4 | $-17132.85 | -5.3% |
| **+15¢** | 42888 | 31890 | 10998 (237) | 4 | $-15361.80 | -5.7% |
| **+20¢** | 38183 | 26626 | 11557 (295) | 4 | $-13684.45 | -5.7% |
| **+10¢ (15¢ stop)** | 83477 | 83292 | 185 (116) | 0 | $-30722.71 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 11:10 | +10 stop | DOGE | DOWN | 0.63 | 0.47 | -1.95 |
| 11-22 11:10 | +5 | DOGE | DOWN | 0.63 | open |  |
| 11-22 11:09 | +10 stop | BTC | UP | 0.56 | 0.71 | 1.17 |
| 11-22 11:08 | +10 stop | DOGE | UP | 0.59 | 0.37 | -2.54 |
| 11-22 11:08 | +5 | ZEC | DOWN | 0.67 | open |  |
| 11-22 11:07 | +10 stop | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-22 11:06 | +10 stop | NEAR | UP | 0.71 | 0.54 | -2.03 |
| 11-22 11:06 | +20 | NEAR | UP | 0.71 | 0.91 | 1.80 |
| 11-22 11:06 | +15 | NEAR | UP | 0.71 | 0.86 | 1.26 |
| 11-22 11:06 | +10 | NEAR | UP | 0.71 | 0.86 | 1.26 |
| 11-22 11:06 | +5 | NEAR | UP | 0.71 | 0.86 | 1.26 |
| 11-22 11:06 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-22 11:05 | +5 | ZEC | DOWN | 0.56 | 0.61 | 0.15 |
| 11-22 11:04 | +10 stop | BTC | UP | 0.52 | 0.74 | 1.88 |
| 11-22 11:04 | +10 stop | BNB | DOWN | 0.56 | 0.25 | -3.42 |
| 11-22 11:04 | +15 | ETH | UP | 0.66 | 0.82 | 1.35 |
| 11-22 11:04 | +10 | XRP | UP | 0.60 | 0.73 | 0.99 |
| 11-22 11:03 | +10 | ETH | UP | 0.64 | 0.79 | 1.21 |
| 11-22 11:03 | +10 stop | DOGE | UP | 0.65 | 0.49 | -1.94 |
| 11-22 11:03 | +5 | XRP | UP | 0.66 | 0.73 | 0.40 |
| 11-22 11:03 | +10 stop | ETH | UP | 0.68 | 0.79 | 0.82 |
| 11-22 11:03 | +5 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 11-22 11:03 | +5 | ZEC | DOWN | 0.67 | 0.77 | 0.70 |
| 11-22 11:03 | +10 stop | HYPE | UP | 0.64 | 0.74 | 0.70 |
| 11-22 11:03 | +20 | HYPE | UP | 0.64 | 0.85 | 1.85 |
| 11-22 11:03 | +15 | HYPE | UP | 0.64 | 0.80 | 1.32 |
| 11-22 11:03 | +10 | HYPE | UP | 0.64 | 0.74 | 0.70 |
| 11-22 11:03 | +5 | HYPE | UP | 0.64 | 0.72 | 0.49 |
| 11-22 11:03 | +10 stop | XRP | DOWN | 0.44 | 0.25 | -2.22 |
| 11-22 11:03 | +5 | BNB | DOWN | 0.66 | open |  |
| 11-22 11:02 | +10 stop | DOGE | DOWN | 0.54 | 0.32 | -2.54 |
| 11-22 11:02 | +20 | DOGE | DOWN | 0.54 | open |  |
| 11-22 11:02 | +15 | DOGE | DOWN | 0.55 | open |  |
| 11-22 11:02 | +10 | DOGE | DOWN | 0.55 | open |  |
| 11-22 11:02 | +5 | DOGE | DOWN | 0.55 | 0.62 | 0.35 |
| 11-22 11:02 | +10 stop | ETH | UP | 0.47 | 0.59 | 0.85 |
| 11-22 11:02 | +20 | ETH | UP | 0.51 | 0.71 | 1.67 |
| 11-22 11:02 | +15 | ETH | UP | 0.54 | 0.69 | 1.17 |
| 11-22 11:02 | +10 | ETH | UP | 0.54 | 0.64 | 0.65 |
| 11-22 11:02 | +5 | ETH | UP | 0.54 | 0.59 | 0.15 |
