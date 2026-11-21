# Range-Scalp Bot

*Updated Sat Nov 21 13:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67387 | 58810 | 8577 (134) | 1 | $-18075.67 | -4.3% |
| **+10¢** | 50331 | 40312 | 10019 (175) | 1 | $-16768.10 | -5.3% |
| **+15¢** | 42217 | 31414 | 10803 (225) | 1 | $-15023.05 | -5.7% |
| **+20¢** | 37578 | 26226 | 11352 (283) | 2 | $-13335.62 | -5.7% |
| **+10¢ (15¢ stop)** | 82043 | 81872 | 171 (105) | 1 | $-30110.64 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 13:54 | +10 stop | DOGE | UP | 0.64 | open |  |
| 11-21 13:53 | +5 | ZEC | UP | 0.64 | 0.80 | 1.31 |
| 11-21 13:53 | +10 stop | ZEC | UP | 0.62 | 0.80 | 1.51 |
| 11-21 13:50 | +10 stop | ZEC | DOWN | 0.63 | 0.48 | -1.85 |
| 11-21 13:49 | +10 stop | BNB | UP | 0.69 | 0.80 | 0.83 |
| 11-21 13:49 | +10 | BNB | UP | 0.69 | 0.80 | 0.83 |
| 11-21 13:49 | +5 | BNB | UP | 0.69 | 0.74 | 0.21 |
| 11-21 13:49 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-21 13:47 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 11-21 13:47 | +10 stop | XRP | UP | 0.69 | 0.79 | 0.73 |
| 11-21 13:47 | +20 | XRP | UP | 0.69 | 0.91 | 1.99 |
| 11-21 13:47 | +15 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 11-21 13:47 | +10 | XRP | UP | 0.69 | 0.79 | 0.73 |
| 11-21 13:47 | +5 | XRP | UP | 0.69 | 0.78 | 0.62 |
| 11-21 13:47 | +10 stop | BNB | UP | 0.61 | 0.72 | 0.78 |
| 11-21 13:47 | +20 | BNB | UP | 0.60 | 0.80 | 1.71 |
| 11-21 13:47 | +15 | BNB | UP | 0.60 | 0.80 | 1.71 |
| 11-21 13:47 | +10 | BNB | UP | 0.60 | 0.72 | 0.88 |
| 11-21 13:47 | +5 | BNB | UP | 0.60 | 0.72 | 0.88 |
| 11-21 13:47 | +10 stop | ETH | UP | 0.65 | 0.78 | 1.01 |
| 11-21 13:47 | +20 | ETH | UP | 0.65 | open |  |
| 11-21 13:47 | +15 | ETH | UP | 0.65 | 0.82 | 1.43 |
| 11-21 13:47 | +10 | ETH | UP | 0.65 | 0.78 | 1.01 |
| 11-21 13:47 | +5 | ETH | UP | 0.65 | 0.70 | 0.19 |
| 11-21 13:47 | +10 stop | NEAR | UP | 0.67 | 0.77 | 0.71 |
| 11-21 13:47 | +10 | NEAR | UP | 0.68 | 0.82 | 1.13 |
| 11-21 13:47 | +5 | NEAR | UP | 0.68 | 0.74 | 0.30 |
| 11-21 13:47 | +10 stop | DOGE | DOWN | 0.55 | 0.34 | -2.44 |
| 11-21 13:47 | +20 | DOGE | DOWN | 0.55 | open |  |
| 11-21 13:47 | +15 | DOGE | DOWN | 0.55 | open |  |
| 11-21 13:47 | +10 | DOGE | DOWN | 0.55 | open |  |
| 11-21 13:47 | +5 | DOGE | DOWN | 0.55 | open |  |
| 11-21 13:46 | +10 stop | ZEC | UP | 0.56 | 0.41 | -1.85 |
| 11-21 13:46 | +20 | ZEC | UP | 0.56 | 0.80 | 2.10 |
| 11-21 13:46 | +15 | ZEC | UP | 0.55 | 0.80 | 2.18 |
| 11-21 13:46 | +10 | ZEC | UP | 0.55 | 0.66 | 0.76 |
| 11-21 13:46 | +5 | ZEC | UP | 0.55 | 0.61 | 0.21 |
| 11-21 13:46 | +10 stop | BTC | UP | 0.59 | 0.70 | 0.78 |
| 11-21 13:46 | +20 | BTC | UP | 0.58 | 0.81 | 2.01 |
| 11-21 13:46 | +15 | BTC | UP | 0.58 | 0.76 | 1.49 |
