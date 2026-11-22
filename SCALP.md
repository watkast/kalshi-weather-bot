# Range-Scalp Bot

*Updated Sun Nov 22 04:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68233 | 59544 | 8689 (138) | 0 | $-18347.19 | -4.3% |
| **+10¢** | 50946 | 40797 | 10149 (181) | 1 | $-17018.36 | -5.3% |
| **+15¢** | 42705 | 31764 | 10941 (231) | 2 | $-15270.37 | -5.7% |
| **+20¢** | 38017 | 26517 | 11500 (289) | 2 | $-13608.70 | -5.7% |
| **+10¢ (15¢ stop)** | 83085 | 82906 | 179 (111) | 0 | $-30498.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 04:07 | +10 stop | XRP | UP | 0.66 | 0.76 | 0.71 |
| 11-22 04:05 | +10 stop | NEAR | UP | 0.62 | 0.76 | 1.05 |
| 11-22 04:05 | +20 | NEAR | UP | 0.62 | open |  |
| 11-22 04:05 | +15 | NEAR | UP | 0.62 | open |  |
| 11-22 04:05 | +10 | NEAR | UP | 0.63 | 0.76 | 1.00 |
| 11-22 04:05 | +5 | NEAR | UP | 0.64 | 0.72 | 0.50 |
| 11-22 04:05 | +10 stop | XRP | UP | 0.71 | 0.52 | -2.23 |
| 11-22 04:05 | +20 | XRP | UP | 0.71 | open |  |
| 11-22 04:05 | +15 | XRP | UP | 0.71 | open |  |
| 11-22 04:05 | +10 | XRP | UP | 0.71 | open |  |
| 11-22 04:05 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |
| 11-22 03:54 | +10 stop | ETH | UP | 0.65 | 0.77 | 0.91 |
| 11-22 03:54 | +10 stop | ETH | DOWN | 0.38 | 0.56 | 1.45 |
| 11-22 03:54 | +10 stop | BNB | UP | 0.60 | 0.70 | 0.68 |
| 11-22 03:53 | +10 stop | ETH | UP | 0.59 | 0.43 | -1.95 |
| 11-22 03:53 | +10 stop | NEAR | UP | 0.68 | 0.82 | 1.13 |
| 11-22 03:53 | +5 | NEAR | UP | 0.68 | 0.74 | 0.30 |
| 11-22 03:52 | +10 stop | HYPE | UP | 0.64 | 0.81 | 1.42 |
| 11-22 03:51 | +5 | ETH | DOWN | 0.63 | yes | -6.47 |
| 11-22 03:51 | +10 stop | NEAR | DOWN | 0.51 | 0.62 | 0.75 |
| 11-22 03:51 | +10 stop | BNB | DOWN | 0.60 | 0.31 | -3.22 |
| 11-22 03:51 | +5 | BNB | DOWN | 0.60 | yes | -6.17 |
| 11-22 03:51 | +10 stop | DOGE | UP | 0.61 | 0.84 | 2.03 |
| 11-22 03:51 | +10 stop | HYPE | DOWN | 0.64 | 0.49 | -1.85 |
| 11-22 03:51 | +20 | HYPE | DOWN | 0.64 | yes | -6.57 |
| 11-22 03:51 | +15 | HYPE | DOWN | 0.64 | yes | -6.57 |
| 11-22 03:51 | +10 | HYPE | DOWN | 0.64 | yes | -6.57 |
| 11-22 03:51 | +5 | HYPE | DOWN | 0.64 | yes | -6.57 |
| 11-22 03:51 | +10 stop | SOL | UP | 0.51 | 0.80 | 2.60 |
| 11-22 03:51 | +10 | SOL | UP | 0.51 | 0.80 | 2.60 |
| 11-22 03:51 | +5 | SOL | UP | 0.51 | 0.57 | 0.24 |
| 11-22 03:50 | +10 stop | BNB | DOWN | 0.51 | 0.62 | 0.73 |
| 11-22 03:50 | +20 | BNB | DOWN | 0.52 | yes | -5.38 |
| 11-22 03:50 | +15 | BNB | DOWN | 0.53 | yes | -5.48 |
| 11-22 03:50 | +10 | BNB | DOWN | 0.53 | yes | -5.48 |
| 11-22 03:50 | +5 | BNB | DOWN | 0.52 | 0.62 | 0.65 |
| 11-22 03:50 | +10 stop | ETH | DOWN | 0.57 | 0.41 | -1.95 |
| 11-22 03:50 | +20 | ETH | DOWN | 0.57 | yes | -5.88 |
| 11-22 03:50 | +15 | ETH | DOWN | 0.56 | yes | -5.78 |
| 11-22 03:50 | +10 | ETH | DOWN | 0.57 | yes | -5.88 |
